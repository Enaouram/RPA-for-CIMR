from appJar import gui
app=gui("MA_RPA",(500,500),showIcon=False)
app.setIcon("logo.gif")
app.addLabel("Choose your robot:")
def do(button):
    if button=="ROBOT 01":
        app.startAnimation("hello")
    elif button=="ROBOT 02":
        app.stop()
app.addButtons(["ROBOT 01","ROBOT 02"],do)
app.go()