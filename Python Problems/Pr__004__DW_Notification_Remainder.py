import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = " **Please Drink Water Now!** ",
            message = "About 15.5 cups (3.7 liters) of fluids a day for men."
            "About 11.5 cups (2.7 liters) of fluids a day for women."
            " Drinking Water is Necessary For Good Health! ",
            app_icon = "F:\Python Language\Python Problems\icon.ico",
            timeout = 15
        )
        time.sleep(60*60)
        #time.sleep(5)

        