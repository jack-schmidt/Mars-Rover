import StarLAB
StarLAB.version()
myStarLAB = StarLAB.Connect(IP="192.168.86.104")
tempdata = myStarLAB.atmos.getTempC()
print("Temperature", tempdata)
myStarLAB.enableRover()
run = myStarLAB.motors.setMotorPower(60,60)

