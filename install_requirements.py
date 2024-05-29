# Arquivo para instalação das dependências da aplicação, recomendado utilizar em um ambiente virtual

import os
list_dir = os.listdir()
if "requirements.txt" in list_dir:
    print("Instalando pacotes...")
    os.system("pip install -r requirements.txt")
    
os.system("cd app && python init_db.py")