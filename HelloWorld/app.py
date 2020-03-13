while True:
    user_input = input("> ").lower()
    if user_input == "help":
        print("start - to start the car\n"
              "stop - to stop the car\n"
              "quit - to exit\n")
    elif user_input == "start":
        print("Car started... Ready to go!")
    elif user_input == "stop":
        print("Car stopped.")
    elif user_input == "quit":
        break
    else:
        print("I don't undestand that...")