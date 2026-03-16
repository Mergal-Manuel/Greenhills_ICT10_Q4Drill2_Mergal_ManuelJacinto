from pyscript import document, display #drill 2

def area_triangle(base, height):
    return {'base': base, 'height': height}

def cumuterism(e):
    document.getElementById('display1').innerHTML = " "

    base1 = int(document.getElementById('input1').value)
    height1 = int(document.getElementById('input2').value)
    area = (base1 * height1)/2
    triangle_info = area_triangle(base1, height1)

    display(f'Base : {base1}', target="display1")
    display(f'height :  {height1}', target="display2")
    display(f'the area is {area}', target="display3")
    display(triangle_info, target="display4")

