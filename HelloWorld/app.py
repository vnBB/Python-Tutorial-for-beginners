#comment
started = False

while True:
    user_input = input("> ").lower()
    if user_input == "help":
        print("start - to start the car\n"
              "stop - to stop the car\n"
              "quit - to exit\n")
    elif user_input == "start":
        if started:
            print("The car is already started!")
        else:
            started = True
            print("Car started... Ready to go!")
    elif user_input == "stop":
        if not started:
            print("The car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif user_input == "quit":
        break
    else:
        print("I don't undestand that...")