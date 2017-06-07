import pyinotify

def onChange(ev):
    print("pyinotify.IN_MODIFY on Change.")

if __name__ == '__main__':
    wm = pyinotify.WatchManager()
    notifier = pyinotify.Notifier(wm)

    while True:
        try:
            wm.add_watch('config/config.ini', pyinotify.IN_MODIFY, onChange)
            notifier.process_events()
            print("process events")
            if notifier.check_events():
                notifier.read_events()
        except KeyboardInterrupt:
            print("keyboard Interrupt.")
            notifier.stop()
            break
