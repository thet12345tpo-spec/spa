import m1

# ... (Logo နဲ့ တခြား function တွေ ဒီအတိုင်းထားပါ) ...

if __name__ == "__main__":
    Logo()
    user_input = input(f"{g}[?] Enter the encrypted string: {w}")
    mac_input = input(f"{g}[?] Enter MAC address (e.g. 24:06:aa:4d:3f:13): {w}")
    
    # ဤနေရာတွင် Position အလိုက်ပေးမည့်အစား 
    # Argument နာမည်ဖြင့် သတ်မှတ်ပေးပါ
    try:
        # m1.py ထဲကမူလ function parameter နာမည်အတိုင်း ထည့်ပေးပါ
        # ဥပမာ - encrypted_str နှင့် new_mac ဆိုရင် ဒီလိုရေးပါ
        m1.run_session(encrypted_str=user_input, new_mac=mac_input)
    except TypeError:
        # တကယ်လို့ အပေါ်က နာမည်တွေ မမှန်ရင် ဒီနည်းနဲ့ ထပ်စမ်းပါ
        # Cython က တစ်ခါတစ်ရံ self ဆိုတဲ့ keyword ကို အလိုအလျောက် ထည့်တတ်ပါတယ်
        m1.run_session(user_input, mac_input)
      
