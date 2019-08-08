from app.controller import run
#import run functino from controller

if __name__ == "__main__":
    print(__name__)
    run()

#If the name of the file is __main__ then it returns true and runs everything underneath
#will only return true if its running on the main file, only will run in controller because its the main file 
#that is importing things from other files