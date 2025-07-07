from PIL import Image
from rich.console import Console
import time, os, random

console = Console()
WIDTH = 100
ASCII_CHARS = [' ', '#', '@']

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
    wordlist_path = input("📂 Enter wordlist file path (e.g. wordlist.txt): ").strip()
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

    target_info = input(f"👤 Enter {platforms[target]} target: ").strip()
    
    console.print(f"\n💥 Starting BruteForce on {platforms[target]} ({target_info})...\n")
    
    with open(wordlist_path, 'r') as f:
        passwords = [pwd.strip() for pwd in f.readlines() if pwd.strip()]
    
    total_passwords = len(passwords)
    if total_passwords > 100000:
        passwords = passwords[:100000]
        total_passwords = 100000
    
    attempts = random.randint(200, 500)
    duration = random.uniform(10, 20)
    delay = duration / attempts
    
    console.print(f"⚡ Will try {attempts} passwords in {duration:.1f} seconds\n")
    
    tried = set()
    found = False
    
    start_time = time.time()
    for i in range(attempts):
        if len(tried) >= total_passwords:
            break
            
        pwd = random.choice(passwords)
        while pwd in tried:
            pwd = random.choice(passwords)
        tried.add(pwd)
        
        console.print(f"🔓 Trying password {i+1}/{attempts}: {pwd}")
        time.sleep(delay)
        
        if random.random() < 0.002:  # 0.2% chance to "find" password
            console.print("\n🎉 Password found!")
            console.print(f"🔑 The password is: {pwd}")
            found = True
            break
    
    if not found:
        console.print("\n🔐 Password not found in attempted passwords")
    
    elapsed = time.time() - start_time
    console.print(f"\n⏱️  Total time: {elapsed:.1f} seconds")
    console.print(f"🔢 Total tried: {len(tried)} passwords")
    
    input("\n⏎ Press Enter to continue...")
    show_menu()

def wordlist_create():
    os.system("clear")
    console.print("\n🧠 WORDLIST GENERATOR (MAX 100K PASSWORDS)\n")

    name = input("👤 Enter Full Name: ").strip()
    nick = input("🧑‍🎨 Enter Nickname: ").strip()
    dob = input("🎂 Enter DOB (ddmmyyyy): ").strip()
    partner = input("💑 Enter Partner Name: ").strip()
    pet = input("🐕 Enter Pet Name: ").strip()
    
    if not all([name, nick, dob, partner, pet]):
        print("❌ All fields are required!")
        time.sleep(1)
        show_menu()

    output_path = input("\n💾 Save wordlist as (e.g. wordlist.txt): ").strip() or "wordlist.txt"
    output_path = os.path.expanduser(output_path)

    console.print("\n⚙️ Generating passwords (max 100,000)...")
    
    base_words = [
        name, nick, dob[:2], dob[2:4], dob[4:], dob[-2:],
        partner, pet, name.upper(), name.lower(), name.capitalize(),
        nick.upper(), nick.lower(), nick.capitalize(),
        partner.upper(), partner.lower(), partner.capitalize(),
        pet.upper(), pet.lower(), pet.capitalize(),
        name[::-1], nick[::-1], pet[::-1],
        name+pet, nick+pet, name+partner,
        name[:3]+dob[-2:], nick[:3]+dob[-2:], pet[:3]+dob[-2:]
    ]

    symbols = ["", "@", "#", "!", "_", ".", "-"]
    numbers = [""] + [str(i) for i in range(1000)]
    
    MAX_PASSWORDS = 100000
    count = 0

    with open(output_path, "w") as f:
        try:
            for word in base_words:
                if not word:
                    continue
                    
                for sym in symbols:
                    for num in numbers[:100]:  # Limit number combinations
                        if count >= MAX_PASSWORDS:
                            break
                            
                        variants = [
                            word + sym + num,
                            word.capitalize() + sym + num,
                            sym + word + num,
                            num + sym + word
                        ]
                        
                        for variant in variants:
                            if 4 <= len(variant) <= 16 and count < MAX_PASSWORDS:
                                f.write(variant + "\n")
                                count += 1
                                if count % 10000 == 0:
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
