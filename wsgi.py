"""App entry point."""
from webapp import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='localhost', port=5000)

