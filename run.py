from shawty_app import create_app

url_app = create_app()

if __name__ == "__main__":
	url_app.run(debug=True)