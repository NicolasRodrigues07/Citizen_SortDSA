from app.menu import Menu

if __name__ == "__main__":
    try:
        Menu().executar()
    except (KeyboardInterrupt, EOFError):
        print("\nEncerrando o sistema. Até logo!")
