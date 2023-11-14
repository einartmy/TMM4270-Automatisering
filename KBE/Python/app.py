from GeneticPumpOptimizer import GeneticPumpOptimizer
import requests
import os
from flask import Flask, send_file, url_for, render_template_string, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    with open("KBE/Python/vpm.html", "r") as file:
        html_content = file.read()
    return render_template_string(html_content)


@app.route("/latest-image")
def latest_image():
    currentDirectory = os.path.dirname(os.path.abspath(__file__))
    image_directory_name = "Images"
    ImageFolderPath = os.path.join(currentDirectory, image_directory_name)
    images = [f for f in os.listdir(ImageFolderPath) if f.endswith(".png")]
    latest_image = sorted(images)[-1]
    return send_file(os.path.join(ImageFolderPath, latest_image), mimetype="image/png")


@app.route("/create-pump", methods=["POST"])
def calculate():
    target_vpm = float(request.form["targetVPM"])
 
    # Check if pump already exists
    if pump_exists(target_vpm):
        # If pump exists, get the details
        #pump_details = get_pump_details(target_vpm)  
        #Må lage en funksjon som henter ut detaljene til pumpen
        #Så det kan vises til brukeren
        #Kan ikke bruke get_pump_info fordi den bruker et pump objekt
        #Vår pump er en String hentet fra databasen. 
        pump = get_pump(target_vpm)
        print(pump)
        print("Pump exists", pump)
        pump_details = get_pump_details(target_vpm)
        print(pump_details)
        output_info = get_html_pump_info(pump_details["gearRadius"], pump_details["toothRadius"], pump_details["depth"], pump_details["thickness"], pump_exists=True)
        results = f"""
        A pump with the target VPM {target_vpm} already exists with the name: {pump} <br> <br>
       
        Optimized parameters to achieve close to {target_vpm} VPM are:<br><br> {output_info}
        """
    else:
        optimizer = GeneticPumpOptimizer(target_vpm)
        best_pump = optimizer.run()
        thickness = 10.0
        results = f"Optimized parameters to achieve close to {target_vpm} VPM are:<br><br>" + get_html_pump_info(best_pump.radius, best_pump.teethDiameter, thickness, best_pump.depth, calculated_vpm=best_pump.vpm(), pump_exists=False)
        
        # Run all update functions
        insert_data(target_vpm)        
        get_pump_list()
    
    image_button = f"""
    <html>
    <body>
        <br>
        <a href="{url_for('latest_image')}"><button>View Image</button></a>
    </body>
    </html>
    """
    return results + image_button


#Må legge til anglespeed og numberofteeth 
def get_html_pump_info(radius, teethDiameter, thickness, depth, calculated_vpm=None, pump_exists=False):
        #Calculations based on the target VPM using GA
        
        
        # Add result to a string
        results = """
        <style>
        td {
                text-align: center:
        }
        </style>"""+f"""
        <table>
    <tr>
        <th>Parameter</th>
        <th>Value</th>
    </tr>
    <tr>
        <td>Gear Radius</td>
        <td>{round(radius * 1000, 4)} mm</td>
    </tr>
    <tr>
        <td>Teeth Diameter</td>
        <td>{round(teethDiameter * 1000, 4)} mm</td>
    </tr>
    <tr>
        <td>Depth</td>
        <td>{round(depth * 1000, 4)} mm</td>
    </tr>
        <td>Case Thickness</td>
        <td>{thickness} mm</td>
    </tr>
    """
        if not pump_exists:
            results += f"""
            <tr>
                <td>Calculated VPM</td>
                <td>{round(calculated_vpm, 6)} cubic meters pr min</td>
            </tr>
            """
        results += "</table>"

        return results


def get_sparql_pump_list(sparql_query):
    url = "http://localhost:3030/A3/query"
    
    PARAMS = {"query": sparql_query}

    response = requests.get(url, PARAMS)
    data = response.json()
    for binding in data["results"]["bindings"]:
        print(binding["pump"]["value"].split("#")[1], ":", binding["targetVPM"]["value"])

    if response.status_code == 200:
        return "Update successful!"
    else:
        return f"Failed with status code: {response.status_code}. Message: {response.text}"

def get_pump_list():
    sparql_query = """
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    SELECT ?pump ?targetVPM
    WHERE {
	?pump a A3:Pump.
    ?pump A3:targetVPM ?targetVPM.
    }
    ORDER BY (?pump)
    """
    result = get_sparql_pump_list(sparql_query)
    return result

def insert_data(target_vpm):
    count = get_pump_count()
    #Må få inn alle verdiene fra pumpen og erstatte 10.0 med de verdiene
    sparql_upperCase_query = f"""
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    INSERT {{
        A3:upperCase_{count} a A3:UpperCase .
        A3:upperCase_{count} A3:depth 10.0 .
  		A3:upperCase_{count} A3:thickness 10.0 .
  		A3:upperCase_{count} A3:gearRadius 10.0 .
  		A3:upperCase_{count} A3:toothRadius 10.0 .
  		A3:upperCase_{count} A3:outerRadius 10.0 .
  		A3:upperCase_{count} A3:x 10.0 .
  		A3:upperCase_{count} A3:y 10.0 .
  		A3:upperCase_{count} A3:z 10.0 .
  		
    }}
    WHERE {{
    }}
    """
    insert_sparql_data(sparql_upperCase_query)

    sparql_lowerCase_query = f"""
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    INSERT {{
        A3:lowerCase_{count} a A3:LowerCase .
        A3:lowerCase_{count} A3:depth 10.0 .
        A3:lowerCase_{count} A3:thickness 10.0 .
        A3:lowerCase_{count} A3:gearRadius 10.0 .
        A3:lowerCase_{count} A3:toothRadius 10.0 .
        A3:lowerCase_{count} A3:outerRadius 10.0 .
        A3:lowerCase_{count} A3:x 10.0 .
        A3:lowerCase_{count} A3:y 10.0 .
        A3:lowerCase_{count} A3:z 10.0 .
    }}
    WHERE {{
    }}
    """
    insert_sparql_data(sparql_lowerCase_query)
    
    sparql_upperGear_query = f"""
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    INSERT {{
        A3:gear1_{count} a A3:PumpGear .
        A3:gear1_{count} A3:depth 10.0 .
        A3:gear1_{count} A3:offset true .
        A3:gear1_{count} A3:gearRadius 10.0 .
        A3:gear1_{count} A3:toothRadius 10.0 .
        A3:gear1_{count} A3:x 10.0 .
        A3:gear1_{count} A3:y 10.0 .
        A3:gear1_{count} A3:z 10.0 .
    }}
    WHERE {{
    }}
    """

    insert_sparql_data(sparql_upperGear_query)

    sparql_lowerGear_query = f"""
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    INSERT {{
        A3:gear2_{count} a A3:PumpGear .
        A3:gear2_{count} A3:depth 10.0 .
        A3:gear2_{count} A3:offset false .
        A3:gear2_{count} A3:gearRadius 10.0 .
        A3:gear2_{count} A3:toothRadius 10.0 .
        A3:gear2_{count} A3:x 10.0 .
        A3:gear2_{count} A3:y 10.0 .
        A3:gear2_{count} A3:z 10.0 .
    }}
    WHERE {{
    }}
    """
    insert_sparql_data(sparql_lowerGear_query)

    sparql_pump_query = f"""
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    INSERT {{
        A3:pump_{count} a A3:Pump;
            A3:targetVPM {target_vpm}.
    }}
    WHERE {{
    }}
    """
    insert_sparql_data(sparql_pump_query)

    sparql_has_query = f"""
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    INSERT {{
        A3:pump_{count} A3:hasGear A3:gear1_{count}.
        A3:pump_{count} A3:hasGear A3:gear2_{count}.
        A3:pump_{count} A3:hasUpperCase A3:upperCase_{count}.
        A3:pump_{count} A3:hasLowerCase A3:lowerCase_{count}.
    }}
    WHERE {{
    }}
    """

    insert_sparql_data(sparql_has_query)



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

if __name__ == "__main__":
    app.run(debug=True, port=8080)


