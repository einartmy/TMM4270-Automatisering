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
    
    # Her bruker du koden din til å utføre beregningene basert på den inngitte targetVPM
    optimizer = GeneticPumpOptimizer(target_vpm)
    best_pump = optimizer.run()
    
    # Legg til resultatene i en streng eller hva format du ønsker
    results = f"""
    Optimized parameters to achieve close to {target_vpm} VPM are:<br>
    Radius: {round(best_pump.radius*1000, 4)} mm<br>
    Teeth Diameter Ratio: {round(best_pump.teethDiameterRatio, 2)}<br>
    Teeth Diameter: {round(best_pump.teethDiameter*1000, 4)} mm<br>
    Angle Speed: {round(best_pump.angleSpeed, 2)} rad/s<br>
    Depth: {round(best_pump.depth*1000, 4)} mm<br>
    Number of Teeth: {best_pump.numberOfTeeth()}<br>
    Calculated VPM: {round(best_pump.vpm(), 2)}<br>
    """

    return results





def update_sparql_data(sparql_query):
    endpoint_url = "http://localhost:3030/#/dataset/A3/update"  # Replace dataset_name with your dataset's name.
    
    response = requests.post(endpoint_url, data={"update": sparql_query})
    
    if response.status_code == 200:
        return "Update successful!"
    else:
        return f"Failed with status code: {response.status_code}. Message: {response.text}"

@app.route('/update_data', methods=['POST'])
def update_data():
    sparql_query = """
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    INSERT DATA {
    A3:Pump{targetVPM} a A3:Pump ;
                        A3:name "pump{targetVPM}" .
}
    """
    
    result = update_sparql_data(sparql_query)
    return result

if __name__ == "__main__":
    app.run(debug=True, port=8080)
