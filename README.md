# Configure Inotify

Use Python pyinotify module to monitor `config/config.ini` file change. While this file has changed, monitor thread will auto to reparse the configure file.

Default configure file is `config/config.ini`

# Note

* ConfigureInotify class is a **singleton mode** class.
* Parsing configure with getting configure infomations is Thread safe.
  * `get_sections()`
  * `get_section_value(section, key)`
* [ConfigureInotify](ConfigureInotify.py) monitor the `config` direcotry and filter for `config/config.ini`.
* [ConfigureInotifyV2](ConfigureInotifyV2.py) monitor just a configure file(`config/config.ini`). **This Just A Demo, It Will Be Finish In The Future.**

# Example

```Python
    if __name__ == '__main__':

        # 输出信息：
        #     < __main__.Configures object at 0x000001F27F04DE48 >
        #     < __main__.Configures object at 0x000001F27F04DE48 >
        #     < __main__.Configures object at 0x000001F27F04DE48 >
        print(ConfigureInotify())
        print(ConfigureInotify())
        print(configureInotify)

        configureInotify.set_config_file("config/config.ini")
        configureInotify.start()

        while True:
            print(configureInotify.get_sections())
            print(configureInotify.get_section_value("remote", "IP"))
            # time.sleep(50 / 1000)
            time.sleep(1)

```

