from config.database import Base, engine 
from database.models.user import User  
from database.models.pet import Pet  
from database.models.clinic import Clinic  

def create_database():
    print("Criando banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Banco de dados criado com sucesso!")

if __name__ == "__main__":
    create_database()
