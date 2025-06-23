from pywinauto.application import Application
import time

try:
    # Start the application
    app = Application().start("..\\x64\\Release\\dialog_aha.exe")

    # Wait for the application to start and the window to appear
    # Adjust the timeout as necessary
    main_window = app.window(title_re="Aha!", timeout=10) # Assuming 'Aha!' is part of the window title
    main_window.wait('ready', timeout=30)

    # Find the OK button. Common texts for OK buttons are "OK", "OKAY", "Ok"
    # If the button text is different, this will need to be adjusted.
    ok_button = main_window.child_window(title="OK", class_name="Button")
    ok_button.wait('visible', timeout=10)

    # Click the OK button
    ok_button.click()

    print("Successfully started dialog_aha.exe and clicked the OK button.")

except Exception as e:
    print(f"An error occurred: {e}")
    print("Please ensure that dialog_aha.exe is in the same directory as this script or in your system's PATH.")
    print("Also, verify the window title and button text/class if the script fails to find them.")

finally:
    # Optional: Close the application after clicking the button
    # if 'app' in locals() and app.is_process_running():
    #     app.kill() # Forcefully closes the application
    pass

