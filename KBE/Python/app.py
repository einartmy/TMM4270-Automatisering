from GeneticPumpOptimizer import GeneticPumpOptimizer
from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route("/")
def index():
    with open("KBE/Python/vpm.html", "r") as file:
        html_content = file.read()
    return render_template_string(html_content)

@app.route("/create-pump", methods=["POST"])
def calculate():
    target_vpm = float(request.form["targetVPM"])

    # Sjekk om pumpen allerede eksisterer
    if pump_exists(target_vpm):
        # Hvis pumpen eksisterer, hent detaljene
        #pump_details = get_pump_details(target_vpm)  #Må lage en funksjon som henter ut detaljene til pumpen
        results = f"""
        A pump with the target VPM {target_vpm} already exists:<br>
        """
    else:
        #Beregninger basert på targetVPM
        optimizer = GeneticPumpOptimizer(target_vpm)
        best_pump = optimizer.run()
        
        # Legg til resultatene i en streng 
        results = f"""
        Optimized parameters to achieve close to {target_vpm} VPM are:<br>
        Gear Radius: {round(best_pump.radius*1000, 4)} mm<br>
        Teeth Diameter Ratio: {round(best_pump.teethDiameterRatio, 2)}<br>
        Teeth Diameter: {round(best_pump.teethDiameter*1000, 4)} mm<br>
        Angle Speed: {round(best_pump.angleSpeed, 2)} rad/s<br>
        Depth: {round(best_pump.depth*1000, 4)} mm<br>
        Number of Teeth: {best_pump.numberOfTeeth()}<br>
        Calculated VPM: {round(best_pump.vpm(), 2)}<br>
        """
    
        # Run all update functions
        insert_data(target_vpm)
        get_data()
    
    return results


def get_sparql_data(sparql_query):
    url = "http://localhost:3030/A3/query"
    
    PARAMS = {"query": sparql_query}

    response = requests.get(url, PARAMS)
    data = response.json()
    print(data)

    if response.status_code == 200:
        return "Update successful!"
    else:
        return f"Failed with status code: {response.status_code}. Message: {response.text}"

def get_data():
    sparql_query = """
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    SELECT ?pump
    WHERE {
	?pump a A3:Pump.
    }
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

def insert_sparql_data(sparql_query):
    url = "http://localhost:3030/A3/update"
    
    PARAMS = {"update": sparql_query}

    response = requests.post(url, PARAMS)

    if response.status_code == 200:
        return "Update successful!"
    else:
        return f"Failed with status code: {response.status_code}. Message: {response.text}"

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
        raise Exception(f"Query failed with status code: {response.status_code}. Message: {response.text}")

if __name__ == "__main__":
    app.run(debug=True, port=8080)


