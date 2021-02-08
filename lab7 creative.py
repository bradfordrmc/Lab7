from guizero import App, PushButton, Picture, Text
from gpiozero import LED

def close_application(): #function declaration for closing application
    if app.yesno("OK", "Do you want to quit image?"): #check for whether x is hit or not
        app.destroy()  # close app


led17 = LED(17)

def GPIO_17():

    if button1.text == "ON ":
        button1.text ="OFF"
        pic=Picture(app, image="light.png")  #SELECT PICTURe
        led17.on()
    else:
        button1.text="ON "
        pic=Picture(app, image="offlight.png")  #SELECT PICTURe
        led17.off()
        
if __name__ == '__main__':
    
    app = App("Activation GPIO")
    button1 = PushButton(app, command=GPIO_17, text="ON ")
    app.when_closed = close_application  #CALL CLOSE POPUP WHEN X IS HIT
    app.display()
    led17.off()