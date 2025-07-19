from website import create_app

app= create_app()
if __name__ == '__main__':
    app.run(debug=True)  
    #as soon as we save this file,it automaticallu debugs the files    
# This will start the Flask application with debugging enabled, which is useful during development.
# The application can be run by executing this script, which will start the Flask development server.
# The `if __name__ == '__main__':` block ensures that the app runs
# only when this script is executed directly, not when imported as a module.
# This is a common pattern in Flask applications to allow for easy testing and development.
# The `debug=True` option enables the Flask debugger, which provides detailed error messages and automatic reloading
# of the server when code changes are made. This is very useful during development but should be set to `False` in production
# to avoid exposing sensitive information and to improve performance.
# The `create_app` function is a common pattern in Flask applications, allowing for better organization
# and configuration management. It allows for the application to be created with specific settings,
# such as the secret key, and can be extended to include additional configurations, blueprints, 
# and other application components as needed.
# This structure is particularly useful for larger applications where modularity and maintainability are important.
# The `app.run()` method starts the Flask development server, which listens for incoming requests.
