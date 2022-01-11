from app import create_app

application = create_app("config")

if __name__ == '__main__':
    application.run()
    # application.run(host='0.0.0.0',port=5000,debug=True)
