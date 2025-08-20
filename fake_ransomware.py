import os, time, base64

WATCH_PATH = r"C:\Users\DILLIRAJ\Downloads\ransomware-detector\test_folder"
os.makedirs(WATCH_PATH, exist_ok=True)

def pseudo_encrypt(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        with open(path, "wb") as f:
            f.write(base64.b64encode(data))
        print("[FAKE] Encrypted:", path)
    except Exception as e:
        print("[FAKE] Error:", e)

if __name__ == "__main__":
    # Create multiple files and "encrypt" quickly
    for i in range(8):
        fp = os.path.join(WATCH_PATH, f"test{i}.txt")
        with open(fp, "w", encoding="utf-8") as f:
            f.write("This is a demo file for pseudo encryption.\n" * 100)
        time.sleep(0.2)
        # rename to a suspicious extension to guarantee a hit
        locked = fp + ".locked"
        os.replace(fp, locked)
        # also increase entropy (2nd heuristic)
        pseudo_encrypt(locked)
        time.sleep(0.2)
