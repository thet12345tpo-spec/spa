if __name__ == "__main__":
    # Logo() လို့ ရေးမယ့်အစား m1.Logo() လို့ ပြင်ပါ
    m1.Logo() 
    
    user_input = input(f"{g}[?] Enter the encrypted string: {w}")
    mac_input = input(f"{g}[?] Enter MAC address (e.g. 24:06:aa:4d:3f:13): {w}")
    
    # ဒီနေရာမှာလည်း ခုနက ပြောသလို keyword နဲ့ သုံးကြည့်ပါ
    m1.run_session(encrypted_str=user_input, new_mac=mac_input)
    
