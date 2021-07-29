from colours import colour
from getpass import getuser
import organizer
import core
import textf
import threading
import os
import time
import start_ignore
import platform
import configparser as cfg

detected_os = platform.system()
config_path = ["config.cfg", f"/home/{getuser()}/.local/share/sticker_info_bot/config.cfg"]


config = cfg.ConfigParser()
if detected_os == "Windows":
    bot = core.telegram_bot_api(config_path[0])
    config.read(config_path[0])
else:
    try:
        bot = core.telegram_bot_api(config_path[0])
        config.read(config_path[0])
    except:
        bot = core.telegram_bot_api(config_path[1])
        config.read(config_path[1])

def do_reply(message_obj):
    msg = organizer.message(message_obj)
    reply = "None"

    if msg.is_forwarded:
        if msg.type != "sticker":
            if msg.forward_from_id is not None:
                reply = f"Forwarded Message:\nName: `{textf.escape(str(msg.forward_sender_name))}`\nID: `{textf.escape(str(msg.forward_from_id))}`"
            elif msg.forward_from_id is None:
                reply = f"Forwarded Message:\nName: `{textf.escape(str(msg.forward_sender_name))}`\nID: Locked by user"

        elif msg.type == "sticker":
            if msg.forward_from_id is None:
                reply = f"Sticker:\nFrom pack: [{textf.escape(str(msg.sticker_set_name))}](https://t.me/addstickers/{textf.escape(str(msg.sticker_set_name))})\nSticker ID\\(File ID\\): `{textf.escape(str(msg.content))}`\nFile unique ID: `{textf.escape(str(msg.file_unique_id))}`\n\nForwarded from: `{textf.escape(str(msg.forward_sender_name))}`\nID: locked by user"
            elif msg.forward_from_id is not None:
                reply = f"Sticker:\nFrom pack: [{textf.escape(str(msg.sticker_set_name))}](https://t.me/addstickers/{textf.escape(str(msg.sticker_set_name))})\nSticker ID\\(File ID\\): `{textf.escape(str(msg.content))}`\nFile unique ID: `{textf.escape(str(msg.file_unique_id))}`\n\nForwarded from: `{textf.escape(str(msg.forward_sender_name))}`\nID: `{textf.escape(str(msg.forward_from_id))}`"

    elif msg.type == "sticker":
        reply = f"Sticker:\nFrom pack: [{textf.escape(str(msg.sticker_set_name))}](https://t.me/addstickers/{textf.escape(str(msg.sticker_set_name))})\nSticker ID\\(File ID\\): `{textf.escape(str(msg.content))}`\nFile unique ID: `{textf.escape(str(msg.file_unique_id))}`"
    
    elif msg.type != "sticker":
        reply = "Not a sticker"
    else:
        pass

    if reply != "None":
        bot.send_message(msg.chat_id, textf.hex(reply), reply_to_message_id=msg.message_id, is_markdown=True)


def main():
    offset = None
    print(f"{colour.GREEN}bot started{colour.reset}")

    while True:
        update = bot.get_updates(offset)
        try:
            for message_obj in update["result"]:
                msg = organizer.message(message_obj)
                offset = msg.update_id
                if msg.is_group == False:
                    try:
                        reply_thread = threading.Thread(target=do_reply(message_obj))
                        reply_thread.start()
                    except RuntimeError as error:
                        print(f"{colour.RED}ERROR: message postponed{colour.reset}\nRuntimeError: {error}")
                        time.sleep(3)
                        reply_thread = threading.Thread(target=do_reply(message_obj))
                        reply_thread.start()
                        print("thread started")
                    
                    except Exception as error:
                        print(f"{colour.WARNING}ERROR: unknown error{colour.reset}, the script will stop\n{error}")
                        exit()
                else:
                    pass

        except KeyError as error:
            print(f"{colour.WARNING}ERROR: no bot token{colour.RED} or another getUpdate session running{colour.reset}\n{colour.YELLOW}plese check 'config.cfg'\n\nKeyError: {error}{colour.reset}\n")
            exit()

        except RuntimeError as error:
            print(f"{colour.RED}ERROR: RuntimeError: {error}{colour.reset}\nwill continue looping")
            time.sleep(3)

        except Exception as error:
            print(f"{colour.WARNING}ERROR: unknown error, the script will stop{colour.reset}\n{error}")
            exit()
    return


start_ignore.main()
main()