import json
from GeneticPumpOptimizer import GeneticPumpOptimizer
import requests
import os
from flask import Flask, render_template, send_file, url_for, render_template_string, request
import os

app = Flask(__name__)
pumps = {}

@app.route("/")                 #Homepage
def index():
    global pumps
    pumps = get_all_pumps()     # Get all the available pumps as a dictionary
    pumps_table = render_template("pump_table.html", pumps=pumps)     # Render the HTML template with the available pumps

    return render_template("vpm.html", pumps_table=pumps_table)


@app.route("/get-image")
def get_image():
    target_vpm = request.args.get("targetVPM", default=None, type=float) #get the sent VPM to find matching image
    filename = f"pump_{target_vpm}.png"
    currentDirectory = os.path.dirname(os.path.abspath(__file__))
    image_directory_name = "Images"
    image_file_path = os.path.join(currentDirectory, image_directory_name, filename)

    if os.path.exists(image_file_path):
        return send_file(image_file_path, mimetype="image/png")
    else:
        return "No image found for the given target VPM, 3D model has not been generated yet."

@app.route("/order-page")                                           #Page to place order
def order_page():
    pump_name = request.args.get("pump_name", default=None)
    return render_template("order.html", pump_name=pump_name)

@app.route("/confirmed-order",  methods=["POST"])   
def confirmed_order():                                              #Order confirmation page
    username = request.form["username"]
    email = request.form["email"]
    pump_amount = request.form["pump_amount"]
    pump_name = request.form.get("pump_name", default=None)

    if not check_username_exists(username):
        # If the username does not exist, insert the customer data into the ontology    
        insert_customer_data(username, email)
    
    order_number = insert_order_data(pump_name, pump_amount, username)     # Insert the order data into the ontology, returns the order number
    orders = get_orders(username)
    return render_template('order_confirmed.html', order_number=order_number, orders=orders, username=username)     

@app.route("/create-pump", methods=["POST"])
def calculate():                                                    #Page where pump is either created or an existing pump is shown
    target_vpm = float(request.form["targetVPM"])
    global pumps
 
    # Check if pump already exists
    if pump_exists(target_vpm):
        pump_name = get_pump(target_vpm)
        pump_details = get_pump_details(target_vpm)

        results =  render_template(
        'pump_data.html',
        target_vpm=target_vpm,
        pump_data=pump_details,
        pump_name=pump_name,
        pump_exists=True)

    # If pump does not exist, optimize the parameters with the Genetic Algorithm
    else:
        optimizer = GeneticPumpOptimizer(target_vpm)
        best_pump = optimizer.run()
        thickness = 10.0
        radius = best_pump.radius
        teethDiameter = best_pump.teethDiameter
        depth = best_pump.depth
        calculated_vpm = best_pump.vpm()
        angleSpeed = best_pump.angleSpeed
        numberOfTeeth = best_pump.numberOfTeeth()
        best_pump_data = {
            "targetVpm": target_vpm,
            "radius": radius,
            "teethDiameter": teethDiameter,
            "depth": depth,
            "angleSpeed": best_pump.angleSpeed,
            "caseThickness": thickness,
            "x": 0,
            "y": 0
        }

        currentDirectory = os.path.dirname(os.path.abspath(__file__))
        inputJsonPath = os.path.join(currentDirectory, "Pump_parameters.json")   # Path to the JSON file
        with open(inputJsonPath, "w") as file:                                   # Write the best pump parameters to the JSON file for use in NX
            json.dump(best_pump_data, file)
        
        # Run all update functions
        insert_data(target_vpm, depth, thickness, radius, teethDiameter, angleSpeed, numberOfTeeth)
        pumps = get_all_pumps()   # Update the pumps dictionary   
        pump_name = get_pump(target_vpm) 
        pump_details = get_pump_details(target_vpm)

        results =  render_template(
        'pump_data.html',
        target_vpm=target_vpm,
        pump_data=pump_details,
        pumps=pumps,
        pump_name=pump_name,
        pump_exists=False,
        calculated_vpm= round(calculated_vpm, 4))

    return results 

def get_pump_details(target_vpm):
    # Query to get details of the Pump with the given targetVPM in a dictionary
    sparql_query = f"""
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    SELECT DISTINCT ?pump ?targetVPM ?gearRadius ?teethDiameter ?depth ?thickness ?angleSpeed ?numberOfTeeth
    WHERE {{
        ?pump a A3:Pump ;
            A3:targetVPM "{target_vpm}"^^xsd:decimal ;
            A3:angleSpeed ?angleSpeed ;
            A3:hasLowerCase ?lowerCase ;
            A3:hasGear ?gear .

        ?lowerCase A3:thickness ?thickness .

        ?gear A3:gearRadius ?gearRadius ;
            A3:teethDiameter ?teethDiameter ;
            A3:depth ?depth ;
            A3:numberOfTeeth ?numberOfTeeth . 
    }}

    """
    url = "http://localhost:3030/A3/query"
    PARAMS = {"query": sparql_query}
    response = requests.get(url, PARAMS)
    if response.status_code == 200:
        data = response.json()
        bindings = data["results"]["bindings"] 
        if len(bindings) > 0:
            result = {}
            for key, value in bindings[0].items():
                if key == "pump": 
                    result[key] = value["value"].split("#")[1]
                else:
                    if key in ["gearRadius", "teethDiameter", "depth"]:
                        result[key] = round(float(value["value"]) * 1000, 2)        #Convert to mm
                    elif key == "angleSpeed":
                        result[key] = round(float(value["value"]), 2)
                    else:
                        result[key] = float(value["value"])
            return result 
        else:
            return None
    else:
        raise Exception(f"Failed with status code: {response.status_code}. Message: {response.text}")

def get_all_pumps():
    # Query to get all pumps in a dictionary
    sparql_query = """
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    SELECT DISTINCT ?pump ?targetVPM ?gearRadius ?teethDiameter ?depth ?thickness ?angleSpeed ?numberOfTeeth
    WHERE {
        ?pump a A3:Pump ;
            A3:targetVPM ?targetVPM ;
            A3:angleSpeed ?angleSpeed ;
            A3:hasLowerCase ?lowerCase ;
            A3:hasGear ?gear .

        ?lowerCase A3:thickness ?thickness .

        ?gear A3:gearRadius ?gearRadius ;
            A3:teethDiameter ?teethDiameter ;
            A3:depth ?depth ;
            A3:numberOfTeeth ?numberOfTeeth . 
    }
    ORDER BY (?targetVPM)
    """
    url = "http://localhost:3030/A3/query"
    PARAMS = {"query": sparql_query}
    response = requests.get(url, PARAMS)
    if response.status_code == 200:
        data = response.json()
        bindings = data["results"]["bindings"]
        pumps = {}
        for binding in bindings:
            pump_name = binding["pump"]["value"].split("#")[1]
            pumps[pump_name] = {
                "targetVPM": float(binding["targetVPM"]["value"]),
                "gearRadius": round(float(binding["gearRadius"]["value"]) * 1000, 2),                   #Convert to mm
                "teethDiameter": round(float(binding["teethDiameter"]["value"]) * 1000, 2),             #Convert to mm
                "depth": round(float(binding["depth"]["value"]) * 1000, 2),                             #Convert to mm      
                "thickness": float(binding["thickness"]["value"]),
                "angleSpeed": round(float(binding["angleSpeed"]["value"]), 2),
                "numberOfTeeth": int(binding["numberOfTeeth"]["value"])
            }
        return pumps
    else:
        raise Exception(f"Failed with status code: {response.status_code}. Message: {response.text}")

def insert_data(target_vpm, depth, thickness, gear_radius, tooth_radius, angleSpeed, numberOfTeeth): 
        # Query to insert the data of the optimized pump into the ontology 
        count = get_pump_count()
        sparql_query = f"""
        PREFIX A3: <http://www.kbe.com/pump.owl#>
        INSERT {{
                A3:pump_{count} a A3:Pump;
                        A3:targetVPM {target_vpm};
                        A3:angleSpeed {angleSpeed};
                        A3:hasGear [ a A3:PumpGear;
                                                    A3:depth {depth};
                                                    A3:gearRadius {gear_radius};
                                                    A3:teethDiameter {tooth_radius};
                                                    A3:numberOfTeeth {numberOfTeeth};
                                                    A3:offset true
                                                ],
                                            [ a A3:PumpGear;
                                                    A3:depth {depth};
                                                    A3:gearRadius {gear_radius};
                                                    A3:teethDiameter {tooth_radius};
                                                    A3:numberOfTeeth {numberOfTeeth};
                                                    A3:offset false
                                                ];
                        A3:hasUpperCase [ a A3:UpperCase;
                                                            A3:depth {depth};
                                                            A3:thickness {thickness};
                                                            A3:gearRadius {gear_radius};
                                                            A3:teethDiameter {tooth_radius}
                                                        ];
                        A3:hasLowerCase [ a A3:LowerCase;
                                                            A3:depth {depth};
                                                            A3:thickness {thickness};
                                                            A3:gearRadius {gear_radius};
                                                            A3:teethDiameter {tooth_radius}
                                                        ]
        }}
        WHERE {{
        }}
        """
        insert_sparql_data(sparql_query)

def insert_sparql_data(sparql_query):
    # Function to insert data into the ontology
    url = "http://localhost:3030/A3/update"
    
    PARAMS = {"update": sparql_query}

    response = requests.post(url, PARAMS)

    if response.status_code == 200:
        return "Update successful!"
    else:
        return f"Failed with status code: {response.status_code}. Message: {response.text}"

def get_pump_count():
    # SPARQL Query to get the number of pumps in the ontology
    sparql_query = """
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    SELECT (COUNT(?pump) AS ?count)
    WHERE {
        ?pump a A3:Pump.
    }
    """
    url = "http://localhost:3030/A3/query"
    PARAMS = {"query": sparql_query}
    response = requests.get(url, PARAMS)
    data = response.json()
    count = int(data["results"]["bindings"][0]["count"]["value"])
    return count + 1

def pump_exists(target_vpm):
    # SPARQL Query to check if a Pump with the given targetVPM exists
    sparql_query = f"""
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    ASK {{
        ?pump a A3:Pump ;
              A3:targetVPM "{target_vpm}"^^xsd:decimal.
    }}
    """
    url = "http://localhost:3030/A3/query"
    PARAMS = {"query": sparql_query}
    response = requests.get(url, PARAMS)
    if response.status_code == 200:
        data = response.json()
        return data["boolean"]  # This will be True if the Pump exists, False otherwise
    else:
        raise Exception(f"Failed with status code: {response.status_code}. Message: {response.text}")
    
def get_pump(target_vpm):
    # Query to get the Pump with the given targetVPM
    sparql_query = f"""
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    SELECT ?pump
    WHERE {{
        ?pump a A3:Pump ;
              A3:targetVPM "{target_vpm}"^^xsd:decimal.
    }}
    """
    url = "http://localhost:3030/A3/query"
    PARAMS = {"query": sparql_query}
    response = requests.get(url, PARAMS)
    if response.status_code == 200:
        data = response.json()
        bindings = data["results"]["bindings"] 
        if len(bindings) > 0:
            return bindings[0]["pump"]["value"].split("#")[1]
        else:
            return None
    else:
        raise Exception(f"Failed with status code: {response.status_code}. Message: {response.text}")

def get_order_count():
    # SPARQL Query to get the number of orders in the ontology
    sparql_query = """
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    SELECT (COUNT(?order) AS ?count)
    WHERE {
        ?order a A3:Order.
    }
    """
    url = "http://localhost:3030/A3/query"
    PARAMS = {"query": sparql_query}
    response = requests.get(url, PARAMS)
    data = response.json()
    count = int(data["results"]["bindings"][0]["count"]["value"])
    return count + 1

def insert_order_data(pump_name, order_quantity, customer_username):
    # SPARQL Query to insert the order data into the ontology
    count = get_order_count()
    order_number = f"order_{count}"
    sparql_query = f"""
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    INSERT {{
        A3:{order_number} a A3:Order;
            A3:hasProduct A3:{pump_name};
            A3:hasCustomer A3:{customer_username};
            A3:orderQuantity {order_quantity}
    }}
    WHERE {{
    }}
    """
    insert_sparql_data(sparql_query)
    return order_number

def insert_customer_data(customer_username, customer_email):
    # SPARQL Query to insert the customer data into the ontology
    count = get_customer_count()
    sparql_query = f"""
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    INSERT {{
            A3:customer_{count} a A3:Customer;
                    A3:userName "{customer_username}";
                    A3:mail "{customer_email}"
    }}
    WHERE {{
    }}
    """
    insert_sparql_data(sparql_query)

def get_customer_count():
    # SPARQL Query to get the number of customers in the ontology
    sparql_query = """
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    SELECT (COUNT(?customer) AS ?count)
    WHERE {
        ?customer a A3:Customer.
    }
    """
    url = "http://localhost:3030/A3/query"
    PARAMS = {"query": sparql_query}
    response = requests.get(url, PARAMS)
    data = response.json()
    count = int(data["results"]["bindings"][0]["count"]["value"])
    return count + 1

def get_orders(customer_username):
    # Query to get all orders of the given customer in a dictionary
    sparql_query = f"""
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    SELECT ?order ?pump ?quantity
    WHERE {{
        ?order a A3:Order ;
              A3:hasCustomer A3:{customer_username} ;
              A3:hasProduct ?pump ;
              A3:orderQuantity ?quantity .
    }}
    ORDER BY (?order)
    """
    url = "http://localhost:3030/A3/query"
    PARAMS = {"query": sparql_query}
    response = requests.get(url, PARAMS)
    if response.status_code == 200:
        data = response.json()
        bindings = data["results"]["bindings"]
        orders = []
        for binding in bindings:
            orders.append({
                "order": binding["order"]["value"].split("#")[1],
                "pump": binding["pump"]["value"].split("#")[1],
                "quantity": int(binding["quantity"]["value"])
            })
        return orders
    else:
        raise Exception(f"Failed with status code: {response.status_code}. Message: {response.text}")

def check_username_exists(customer_username):
    # SPARQL Query to check if a Customer with the given username exists
    sparql_query = f"""
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    ASK {{
        ?customer a A3:Customer ;
                  A3:userName "{customer_username}" .
    }}
    """
    url = "http://localhost:3030/A3/query"
    PARAMS = {"query": sparql_query}
    response = requests.get(url, PARAMS)
    if response.status_code == 200:
        data = response.json()
        return data["boolean"]  # This will be True if the Customer exists, False otherwise
    else:
        raise Exception(f"Failed with status code: {response.status_code}. Message: {response.text}")

if __name__ == "__main__":
    app.run(debug=True, port=8080)


