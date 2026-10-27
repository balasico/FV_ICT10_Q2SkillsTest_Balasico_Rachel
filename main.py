from pyscript import document, display

def check_details (e):
    #list of all non-metals
    non_metals = {
        "H": ("Hydrogen", 1, 1.008),
        "He": ("Helium", 2, 4.003),
        "C": ("Carbon", 6, 12.011),
        "N": ("Nitrogen", 7, 14.007),
        "O": ("Oxygen", 8, 15.999),
        "F": ("Flourine", 9, 18.998),
        "Ne": ("Neon", 10, 20.180),
        "P": ("Phosphorus", 15, 30.974),
        "S": ("Sulfur", 16, 32.065),
        "Cl": ("Clorine", 17, 35.453),
        "Ar": ("Argon", 18, 39.948),
        "Se": ("Selenium", 34, 78.960),
        "Br": ("Bromine", 35, 79.904),
        "Kr": ("Krypton", 36, 83.798),
        "I": ("Iodine", 54, 126.905),
        "Xe": ("Xenon", 54, 131.293),
        "Rn": ("Radon", 86, 222.018),
    }

    #gets the info from index.html
    element_input = document.getElementById("element").value

    element_display = non_metals.get(element_input, ("Element not found", "-", "-"))

    #from ma'am
    result = f"""
    <div>
    <b> Symbol: </b> {element_input} <br>
    <b> Element: </b> {element_display[0]} <br>
    <b> Atomic Number: </b> {element_display[1]} <br>
    <b> Atomic Mass: </b> {element_display[2]}
    </div>
    """

    #displays the result
    display(result, target = "result")


    #make it so display is better
    #Symbol:
    #Element Name:
    #Atomic Number:
    #Atomic Mass: