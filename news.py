import random

def get_info():
    haberler = [
        "Yeni bir AI modeli Turing testini gecti!",
        "Mars'ta ilk kez sivi su bulundu.",
        "Python 4.0 duyuruldu: Performans %50 artti.",
        "Kuantum bilgisayarlar artik evlere giriyor."
    ]
    secilen_haber = random.choice(haberler)
    return f"FLAS HABER: {secilen_haber}"