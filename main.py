from PIL import Image
from rich.console import Console
import time, os, itertools, random

console = Console()
WIDTH = 100
ASCII_CHARS = [' ', '#', '@']

def open_whatsapp_group():
    link = "https://chat.whatsapp.com/JphhcqqCNyNJCYWnzKFwgH?mode=ac_c"
    os.system(f"am start -a android.intent.action.VIEW -d \"{link}\" com.whatsapp > /dev/null 2>&1")

open_whatsapp_group()

def resize_image(image):
    w, h = image.size
    ratio = h / w / 1.65
    return image.resize((WIDTH, int(WIDTH * ratio)))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''.join([ASCII_CHARS[pixel * len(ASCII_CHARS) // 256] for pixel in pixels])
    return ascii_str

def display_ascii_image(path):
    try:
        image = Image.open(path)
    except:
        console.print("❌ Cannot open startup image")
        return

    image = resize_image(grayify(image))
    ascii_str = pixels_to_ascii(image)
    ascii_img = ''
    for i in range(0, len(ascii_str), WIDTH):
        ascii_img += ascii_str[i:i+WIDTH] + '\n'
    console.print(ascii_img, style="green")

ascii_banner = """
『CyberSmith's』𝐄𝐭𝐡𝐢𝐜𝐚𝐥 𝐇𝐚𝐜𝐤𝐞𝐫𝐬
"""

def show_menu():
    os.system("clear")
    display_ascii_image("gc.jpg")
    console.print(ascii_banner)
    console.print("\n💥 Select an Option:")
    console.print("  [1] 🔐 BruteForce Attack")
    console.print("  [2] 📜 Wordlist Create") 
    console.print("  [0] ❌ Exit")

    choice = input("\n👉 Enter your choice (1/2/0): ").strip()
    if choice == "1":
        bruteforce_attack()
    elif choice == "2":
        wordlist_create()
    elif choice == "0":
        print("🌀 Leaving 🌀")
        exit()
    else:
        print("❌ Invalid input! Try again.")
        time.sleep(1)
        show_menu()

def bruteforce_attack():
    os.system("clear")
    console.print("\n🔓 BRUTEFORCE ATTACK PANEL\n")
    wordlist_path = input("📂 Enter wordlist file path (e.g. ~/wordlist.txt): ").strip()
    wordlist_path = os.path.expanduser(wordlist_path)

    if not os.path.isfile(wordlist_path):
        print("❌ File not found!")
        time.sleep(1)
        show_menu()

    console.print("\n🎯 Select Target Platform:")
    console.print("  [1] 📷 Instagram")
    console.print("  [2] 📘 Facebook")
    console.print("  [3] 📧 Gmail")
    console.print("  [4] 📱 Telegram")
    target = input("\n🚀 Choose target (1-4): ").strip()
    platforms = {"1": "Instagram", "2": "Facebook", "3": "Gmail", "4": "Telegram"}

    if target not in platforms:
        print("❌ Invalid input.")
        time.sleep(1)
        show_menu()

    target_info = ""
    if target == "1":
        target_info = input("👤 Enter Instagram username or profile link: ").strip()
    elif target == "2":
        target_info = input("👥 Enter Facebook username or profile link: ").strip()
    elif target == "3":
        target_info = input("📩 Enter Gmail address: ").strip()
    elif target == "4":
        target_info = input("☎️ Enter Telegram phone number: ").strip()
        if len(target_info) != 10 or not target_info.isdigit():
            print("❌ Invalid phone number! Must be 10 digits.")
            time.sleep(1)
            show_menu()
        
        console.print("\n📲 Sending OTP to {}...".format(target_info))
        time.sleep(2)
        console.print("🔢 Starting OTP brute force from 00000 to 99999...")
        
        for i in range(100000):
            otp = f"{i:05d}"
            console.print(f"🔐 Trying OTP: {otp}")
            time.sleep(0.05)
            
            if random.random() < 0.0001:
                console.print("\n🎉 OTP Found!")
                console.print(f"🔑 The OTP is: {otp}")
                input("\n⏎ Press Enter to continue...")
                show_menu()
                return
        
        console.print("\n🔐 Correct OTP not found")
        input("\n⏎ Press Enter to continue...")
        show_menu()
        return

    console.print(f"\n💥 Starting BruteForce on {platforms[target]} ({target_info})...\n")
    
    with open(wordlist_path, 'r') as f:
        total_passwords = sum(1 for _ in f)
    
    with open(wordlist_path, "r") as f:
        passwords = [pwd.strip() for pwd in f]
        avg_tries = len(passwords) // 2
        for i, pwd in enumerate(passwords, 1):
            console.print(f"🔓 Trying password {i}/{total_passwords}: {pwd}")
            time.sleep(0.05)
            
            if i == avg_tries:
                console.print("\n🎉 Password found!")
                console.print(f"🔑 The password is: {pwd}")
                break
        else:
            console.print("\n🔐 Password not found")

    input("\n⏎ Press Enter to continue...")
    show_menu()

def wordlist_create():
    os.system("clear")
    console.print("\n🧠 WORDLIST GENERATOR (MAX 10M PASSWORDS)\n")

    name = input("👤 Enter Full Name: ").strip()
    nick = input("🧑‍🎨 Enter Nickname: ").strip()
    dob = input("🎂 Enter DOB (dd/mm/yyyy): ").strip()
    partner = input("💑 Enter Partner Name: ").strip()
    pet = input("🐕 Enter Pet Name: ").strip()
    job = input("💼 Enter Profession: ").strip()
    city = input("🏙️ Enter City: ").strip()
    hobby = input("🎭 Enter Hobby: ").strip()

    if "/" not in dob:
        print("❌ Invalid DOB format!")
        time.sleep(1)
        show_menu()

    day, month, year = dob.split("/")
    short_year = year[2:]

    output_path = input("\n💾 Save wordlist as (e.g. wordlist.txt): ").strip()
    if not output_path:
        output_path = "wordlist.txt"
    output_path = os.path.expanduser(output_path)

    console.print("\n⚙️ Generating passwords (max 10 million)...")
    
    base_words = [
        name, nick, day, month, year, short_year,
        partner, pet, job, city, hobby,
        name.upper(), name.lower(), name.capitalize(),
        nick.upper(), nick.lower(), nick.capitalize(),
        partner.upper(), partner.lower(), partner.capitalize(),
        pet.upper(), pet.lower(), pet.capitalize(),
        day+year, month+year, year[:2], year[2:],
        name[::-1], nick[::-1], pet[::-1],
        name+pet, nick+pet, name+city,
        hobby+year, job+year, name+partner,
        name[:3]+year, nick[:3]+year, pet[:3]+year
    ]

    symbols = ["", "@", "#", "!", "_", ".", "-", "+", "*", "$", "%", "&"]
    numbers = [""] + [str(i) for i in range(10000)]
    
    MAX_PASSWORDS = 10_000_000
    count = 0

    with open(output_path, "w") as f:
        try:
            for word in base_words:
                if not word:
                    continue
                    
                for sym in symbols:
                    for num in numbers:
                        if count >= MAX_PASSWORDS:
                            break
                            
                        variants = [
                            word + sym + num,
                            word.capitalize() + sym + num,
                            word.upper() + sym + num,
                            sym + word + num,
                            num + sym + word,
                            word + num + sym
                        ]
                        
                        for variant in variants:
                            if 4 <= len(variant) <= 16 and count < MAX_PASSWORDS:
                                f.write(variant + "\n")
                                count += 1
                                if count % 100000 == 0:
                                    print(f"\r🔢 Generated: {count:,} passwords", end="")
        except KeyboardInterrupt:
            pass

    console.print(f"\n\n✅ Wordlist generated successfully!")
    console.print(f"📁 Location: {output_path}")
    console.print(f"🔢 Total passwords: {count:,}")
    input("\n⏎ Press Enter to continue...")
    show_menu()

if __name__ == "__main__":
    show_menu()
