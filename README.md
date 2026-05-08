# 🔐 Random Password Generator (Python)

Bu proje, Python kullanılarak geliştirilmiş güvenli ve rastgele şifre üretici bir komut satırı (CLI) aracıdır.  
Şifreler `secrets` modülü ile kriptografik olarak güvenli şekilde oluşturulur.

---

## 🚀 Özellikler

- 🔒 Güvenli şifre üretimi (`secrets` modülü)
- 🧠 Türkçe karakter desteği (ç, ğ, ı, ö, ş, ü vb.)
- 🔢 Harf, sayı ve sembol karışımı
- 📏 Otomatik şifre uzunluğu (16–40 arası)
- ⚡ Gerçek zamanlı şifre üretimi (CTRL + C ile durdurulur)
- 🎨 Renkli terminal çıktısı (ANSI colors)
- 📊 Şifre güç seviyesi analizi

---

## 🧪 Şifre Güç Seviyeleri

| Uzunluk | Seviye        |
|--------|--------------|
| < 12   | Zayıf        |
| 12-19  | Orta         |
| 20-29  | Güçlü        |
| 30+    | Çok Güçlü    |

---

## 📦 Gereksinimler

Python 3.x kurulu olması yeterlidir.

Ek kütüphane gerekmez:
```bash
secrets
string
time
