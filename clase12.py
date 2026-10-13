#USO DE .strip() Y .split(",")
#Cuando lees una línea de un archivo .txt, Python la recibe como un solo texto crudo. 
# .strip() (Limpiador): 
# Quita los espacios invisibles y los saltos de línea (\n) que quedan al final del texto.
#.split(",") (Cortador): Corta el texto por el carácter que le indiques 
# (en este caso la coma) y lo convierte en una lista de elementos separados.

texto_crudo = "Laptop,15000\n"
texto_limpio = texto_crudo.strip() # "Laptop,15000"
datos = texto_limpio.split(",")     # ["Laptop", "15000"]

nombre = datos[0] # "Laptop"
precio = datos[1] # "15000"
