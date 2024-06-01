import os
#from dotenv import load_dotenv

def main():
    # Cargar las variables de entorno desde el archivo .env
    #load_dotenv()
    
    # Obtener el nombre de usuario desde la variable de entorno USERNAME
    nombre = os.getenv("USERNAME")
    
    # Imprimir el saludo personalizado
    print(f"¡Hola, {nombre} desde GitHub!")
    #print(f"¡Hola desde GitHub!")

if __name__ == "__main__":
    main()
