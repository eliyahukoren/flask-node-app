from website import create_app
import os


app = create_app()

if __name__ == '__main__':
    port = os.environ.get('PORT', 8000)
    # use this for local env
    # app.run(debug=True, port=5001)
    
    # use this for docker container
    app.run(debug=True, port=port, host="0.0.0.0")