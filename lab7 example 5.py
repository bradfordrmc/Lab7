from guizero import App, Text
from gpiozero import Button # import module button
from gpiozero import LED # import module LED

button = Button(2)
led = LED(17)

def scanInput():
    if button.is_pressed:
        text.value = 1 #"GPIO2 ON "
        led.on()
    else:
        text.value = 0 #"GPIO2 OFF"
        led.off()
        
def exitGUI():
    text.destroy()
    if app.yesno("Close", "Do you want to quit?"):
        app.destroy()
        print("Adios")
        
if __name__ == '__main__':
    
    app = App("Reading GPIO")
    text = Text(app, text="1")
    text.repeat(10, scanInput)  # Schedule call to scan GPIO
    
    app.when_closed = exitGUI
    app.display()