import json
from GeneticPumpOptimizer import GeneticPumpOptimizer
import requests
import os
from flask import Flask, render_template, send_file, url_for, render_template_string, request
import os

app = Flask(__name__)

pumps = {}

@app.route("/")
def index():
    # Get the available pumps as a dictionary
    global pumps
    pumps = get_all_pumps()

    # Render the HTML template with the available pumps
    pumps_table = render_template("pump_table.html", pumps=pumps)

    return render_template("vpm.html", pumps_table=pumps_table)


@app.route("/get-image")
def latest_image():
    target_vpm = request.args.get("targetVPM", default=None, type=float)
    filename = f"pump_{target_vpm}.png"
    currentDirectory = os.path.dirname(os.path.abspath(__file__))
    image_directory_name = "Images"
    image_file_path = os.path.join(currentDirectory, image_directory_name, f"{filename}.png")

    if os.path.exists(image_file_path):
        return send_file(image_file_path, mimetype="image/png")
    else:
        return "No image found for the given targetVPM, 3D model has not been generated yet."

@app.route("/create-pump", methods=["POST"])
def calculate():
    target_vpm = float(request.form["targetVPM"])
 
    # Check if pump already exists
    if pump_exists(target_vpm):
        pump = get_pump(target_vpm)
        print("Pump exists", pump)
        pump_details = get_pump_details(target_vpm)
        print(pump_details)
        output_info = get_html_pump_info(pump_details["gearRadius"], pump_details["toothRadius"], pump_details["thickness"] ,pump_details["depth"], pump_exists=True)
        results = f"""
        A pump with the target VPM {target_vpm} already exists with the name: {pump} <br> <br>
       
        Optimized parameters to achieve close to {target_vpm} VPM are:<br><br> {output_info}
        """
    else:
        optimizer = GeneticPumpOptimizer(target_vpm)
        best_pump = optimizer.run()
        thickness = 10.0
        radius = best_pump.radius
        teethDiameter = best_pump.teethDiameter
        depth = best_pump.depth
        calculated_vpm = best_pump.vpm()
        best_pump_data = {
            "radius": radius,
            "teethDiameter": teethDiameter,
            "depth": depth,
            "angleSpeed": best_pump.angleSpeed,
            "caseThickness": thickness,
            "x": 0,
            "y": 0
        }

        currentDirectory = os.path.dirname(os.path.abspath(__file__))
        inputJsonPath = os.path.join(currentDirectory, "Pump_parameters.json")
        with open(inputJsonPath, "w") as file:
            json.dump(best_pump_data, file)
        

        results = f"Optimized parameters to achieve close to {target_vpm} VPM are:<br><br>" + get_html_pump_info(radius, teethDiameter, thickness, depth, calculated_vpm, pump_exists=False)
        
        # Run all update functions
        insert_data(target_vpm, depth, thickness, radius, teethDiameter)
    
    global pumps
    pumps = get_all_pumps()      

    image_button = f"""
    <html>
    <body>
        <br>
        <a href="{url_for('get_image', targetVPM = target_vpm)}"><button>View Image</button></a>
    </body>
    </html>
    """
    return results + image_button

def get_pump_details(target_vpm):
    # Query to get the Pump with the given targetVPM
    sparql_query = f"""
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    SELECT DISTINCT ?pump ?targetVPM ?gearRadius ?toothRadius ?depth ?thickness
    WHERE {{
        ?pump a A3:Pump ;
            A3:targetVPM "{target_vpm}"^^xsd:decimal ;
            A3:hasLowerCase ?lowerCase ;
            A3:hasGear ?gear .

        ?lowerCase A3:thickness ?thickness .

        ?gear A3:gearRadius ?gearRadius ;
            A3:toothRadius ?toothRadius ;
            A3:depth ?depth . 
    }}

    """
    url = "http://localhost:3030/A3/query"
    PARAMS = {"query": sparql_query}
    response = requests.get(url, PARAMS)
    if response.status_code == 200:
        data = response.json()
        bindings = data["results"]["bindings"] 
        print(bindings)
        if len(bindings) > 0:
            result = {}
            for key, value in bindings[0].items():
                if key == "pump": 
                    result[key] = value["value"].split("#")[1]
                else:
                    result[key] = float(value["value"])
            return result 
        else:
            return None
    else:
        raise Exception(f"Failed with status code: {response.status_code}. Message: {response.text}")

def get_all_pumps():
    # Query to get all pumps
    sparql_query = """
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    SELECT DISTINCT ?pump ?targetVPM ?gearRadius ?toothRadius ?depth ?thickness
    WHERE {
        ?pump a A3:Pump ;
            A3:targetVPM ?targetVPM ;
            A3:hasLowerCase ?lowerCase ;
            A3:hasGear ?gear .

        ?lowerCase A3:thickness ?thickness .

        ?gear A3:gearRadius ?gearRadius ;
            A3:toothRadius ?toothRadius ;
            A3:depth ?depth . 
    }
    ORDER BY (?pump)
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
                "gearRadius": float(binding["gearRadius"]["value"]),
                "toothRadius": float(binding["toothRadius"]["value"]),
                "depth": float(binding["depth"]["value"]),
                "thickness": float(binding["thickness"]["value"])
            }
        print(pumps)
        return pumps
    else:
        raise Exception(f"Failed with status code: {response.status_code}. Message: {response.text}")



#Må legge til anglespeed og numberofteeth 
def get_html_pump_info(radius, teethDiameter, thickness, depth, calculated_vpm=None, pump_exists=False):
    results = f"""
    <style>
        td {{ text-align: center; }}
    </style>
    <table>
        <tr><th>Parameter</th><th>Value</th></tr>
        <tr><td>Gear Radius</td><td>{round(radius * 1000, 4)} mm</td></tr>
        <tr><td>Teeth Diameter</td><td>{round(teethDiameter * 1000, 4)} mm</td></tr>
        <tr><td>Depth</td><td>{round(depth * 1000, 4)} mm</td></tr>
        <tr><td>Case Thickness</td><td>{thickness} mm</td></tr>
    """
    if not pump_exists:
        results += f"<tr><td>Calculated VPM</td><td>{round(calculated_vpm, 6)} cubic meters pr min</td></tr>"
    results += "</table>"
    return results

def insert_data(target_vpm, depth, thickness, gear_radius, tooth_radius): 
        count = get_pump_count()
        sparql_query = f"""
        PREFIX A3: <http://www.kbe.com/pump.owl#>
        INSERT {{
                A3:pump_{count} a A3:Pump;
                        A3:targetVPM {target_vpm};
                        A3:hasGear [ a A3:PumpGear;
                                                    A3:depth {depth};
                                                    A3:gearRadius {gear_radius};
                                                    A3:toothRadius {tooth_radius};
                                                    A3:offset true
                                                ],
                                            [ a A3:PumpGear;
                                                    A3:depth {depth};
                                                    A3:gearRadius {gear_radius};
                                                    A3:toothRadius {tooth_radius};
                                                    A3:offset false
                                                ];
                        A3:hasUpperCase [ a A3:UpperCase;
                                                            A3:depth {depth};
                                                            A3:thickness {thickness};
                                                            A3:gearRadius {gear_radius};
                                                            A3:toothRadius {tooth_radius}
                                                        ];
                        A3:hasLowerCase [ a A3:LowerCase;
                                                            A3:depth {depth};
                                                            A3:thickness {thickness};
                                                            A3:gearRadius {gear_radius};
                                                            A3:toothRadius {tooth_radius}
                                                        ]
        }}
        WHERE {{
        }}
        """
        insert_sparql_data(sparql_query)



def insert_sparql_data(sparql_query):
    url = "http://localhost:3030/A3/update"
    
    PARAMS = {"update": sparql_query}

    response = requests.post(url, PARAMS)

    if response.status_code == 200:
        return "Update successful!"
    else:
        return f"Failed with status code: {response.status_code}. Message: {response.text}"

def get_pump_count():
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



if __name__ == "__main__":
    app.run(debug=True, port=8080)


