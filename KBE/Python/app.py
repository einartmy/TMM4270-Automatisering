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
        #pump_details = get_pump_details(target_vpm)  #Må lage en funksjon som henter ut detaljene til pumpen
        pump = get_pump(target_vpm)
        print("Pump exists", pump)
        results = f"""
        A pump with the target VPM {target_vpm} already exists with the values: <br> <br>
        {get_pump_info(pump)}
        """
    else:
        optimizer = GeneticPumpOptimizer(target_vpm)
        best_pump = optimizer.run()
        results = f"Optimized parameters to achieve close to {target_vpm} VPM are:<br><br>" + get_pump_info(best_pump)
        
        # Run all update functions
        insert_data(target_vpm)
        get_data()
        
    
    image_button = f"""
    <html>
    <body>
        <br>
        <a href="{url_for('latest_image')}"><button>View Image</button></a>
    </body>
    </html>
    """
    return results + image_button



def get_pump_info(pump):
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
    <td>{round(pump.radius * 1000, 4)} mm</td>
  </tr>
  <tr>
    <td>Teeth Diameter Ratio</td>
    <td>{round(pump.teethDiameterRatio, 2)}</td>
  </tr>
  <tr>
    <td>Teeth Diameter</td>
    <td>{round(pump.teethDiameter * 1000, 4)} mm</td>
  </tr>
  <tr>
    <td>Angle Speed</td>
    <td>{round(pump.angleSpeed, 2)} rad/s</td>
  </tr>
  <tr>
    <td>Depth</td>
    <td>{round(pump.depth * 1000, 4)} mm</td>
  </tr>
  <tr>
    <td>Number of Teeth</td>
    <td>{pump.numberOfTeeth()}</td>
  </tr>
  <tr>
    <td>Calculated VPM</td>
    <td>{round(pump.vpm(), 4)}</td>
  </tr>
</table>
    """

    
    

    return results


def get_sparql_data(sparql_query):
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

def get_data():
    sparql_query = """
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    SELECT ?pump ?targetVPM
    WHERE {
	?pump a A3:Pump.
    ?pump A3:targetVPM ?targetVPM.
    }
    ORDER BY (?pump)
    """
    result = get_sparql_data(sparql_query)
    return result

def insert_data(target_vpm):
    sparql_query = f"""
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    INSERT {{
        A3:pump_{get_pump_count()} a A3:Pump;
            A3:targetVPM {target_vpm}.
    }}
    WHERE {{
    }}
    """
    result = insert_sparql_data(sparql_query)
    return result

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


