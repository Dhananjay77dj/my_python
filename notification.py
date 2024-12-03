from plyer import notification
import time
try:
    while True:

        notification.notify(
        title='Hey DJ!',
        message='Don\'t forget to take a break and stretch!',
        app_name='DJ_Reminder',
        )
        time.sleep(2)
except:
    print('error')