from guizero import App, Text, Picture  #IMPORT LIBRARIES

def close_application(): #function declaration for closing application
    if app.yesno("OK", "Do you want to quit image?"): #check for whether x is hit or not
        app.destroy()  # close app

if __name__ == '__main__': #GENERIC MAIN STATEMENT
    
    app = App("He's sitting there") #He is
    app.bg = "red" #make app background red
    wanted_text = Text(app, "BIG YOSHI") #ADD TEXT TO APP
    wanted_text.text_size = 100  # SET FONT SIZE
    wanted_text.font = "Comic Sans"  # SET FONT TO COMIC SANS
    cat = Picture(app, image="beeg yoshi.png")  #SELECT PICTURE
    app.when_closed = close_application  #CALL CLOSE POPUP WHEN X IS HIT
    app.display() #RUN APP

