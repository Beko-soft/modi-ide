<div align="center">

<h1>🚀 Modi IDE</h1>

<p><strong>Çocuklar için Python tabanlı, Türkçe sözdizimli IDE</strong></p>

<p>
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PySide6-GUI-green?style=for-the-badge&logo=qt&logoColor=white" alt="PySide6">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Status-Beta-orange?style=for-the-badge" alt="Status">
</p>

<p>
  <a href="#kurulum">Kurulum</a> •
  <a href="#kullanım">Kullanım</a> •
  <a href="#sözdizimi-rehberi">Sözdizimi</a> •
  <a href="#özellikler">Özellikler</a> •
  <a href="#katkı">Katkı</a>
</p>

</div>

---

## 📖 Nedir?

**Modi**, çocukların ve programlamaya yeni başlayanların kolaylıkla uygulama geliştirebilmesi için tasarlanmış, **Python tabanlı, sadeleştirilmiş bir programlama dilidir.**

**Modi IDE** ise bu dili çalıştırmak, hata ayıklamak ve gerçek `.exe` / ikili dosyalara derlemek için geliştirilmiş minimalist, karanlık temalı bir entegre geliştirme ortamıdır.

> "Kodu basit yaz, sonucu büyük al."

---

## ✨ Özellikler

| Özellik | Açıklama |
|---|---|
| 🖊️ **Akıllı Editör** | Otomatik girinti, parantez/tırnak tamamlama |
| ▶️ **Anında Çalıştır** | Kodu doğrudan terminalde başlat (F5) |
| 🐛 **Hata Ayıklama** | Dahili konsol çıktısı ile hata izleme (F6) |
| 📦 **Derleme** | PyInstaller ile tek dosya `.exe` / binary üret (F7) |
| 🎨 **GUI Desteği** | CustomTkinter ile pencere/buton/giriş/slider vb. |
| 🔁 **Otomatik Bağımlılık** | `customtkinter` eksikse otomatik yükler |
| 🌐 **Çapraz Platform** | Windows, Linux ve macOS desteği |

---

## 🖥️ Ekran Görüntüsü

> Karanlık, minimalist ve odak odaklı arayüz.

*(Ekran görüntüsü yakında eklenecek)*

---

## 📦 Kurulum

### Gereksinimler

- Python **3.9+**
- pip

### Adımlar

```bash
# Repoyu klonla
git clone https://github.com/Beko-soft/modi-ide.git
cd modi-ide

# Bağımlılıkları yükle
pip install -r requirements.txt

# Çalıştır
python main.py
```

---

## 🚀 Kullanım

### IDE Kısayolları

| Kısayol | Eylem |
|---|---|
| `Ctrl+Enter` veya `F5` | Kodu çalıştır |
| `F6` | Hata ayıklama modu |
| `F7` | Derleme (PyInstaller) |

### Proje Klasörü

Modi, çalıştırılan ve derlenen dosyaları otomatik olarak oluşturulan **`~/Modi Projects/`** klasörüne kaydeder.

---

## 📝 Sözdizimi Rehberi

Modi sözdizimi kasıtlı olarak basit tutulmuştur. Tüm komutlar parantezle yazılır.

### Temel Komutlar

```modi
// Yorum satırı
say("Merhaba Dünya!")

set isim = "Ada"
set yas = 12

repeat(5):
    say("Tekrar!")

if yas >= 10:
    say("Büyük!")
else:
    say("Küçük!")
```

### Fonksiyon Tanımlama

```modi
func selamla(isim):
    say("Merhaba " + isim)

selamla("Ada")
```

### GUI Uygulaması

```modi
func tikla():
    set ad = get_text(giris)
    set_text(baslik, "Merhaba " + ad)

set app = window("Uygulamam", 420, 320)
set panel = frame(app)
set baslik = label(panel, "Adinizi girin", 18)
set giris  = entry(panel, "Ad")
set btn    = button(panel, "Tikla")

event(clicked, btn, tikla)
event(enter, giris, tikla)

run(app)
```

### Mevcut CTK Bileşenleri

| Komut | Açıklama |
|---|---|
| `window(baslik, w, h)` | Ana pencere oluştur |
| `frame(parent)` | Çerçeve / panel |
| `label(parent, metin, boyut)` | Metin etiketi |
| `entry(parent, placeholder)` | Metin giriş alanı |
| `button(parent, metin)` | Tıklanabilir buton |
| `textbox(parent, w, h)` | Çok satırlı metin kutusu |
| `checkbox(parent, metin)` | Onay kutusu |
| `switch(parent, metin)` | Aç/kapa anahtarı |
| `slider(parent, min, max)` | Kaydırıcı |
| `progressbar(parent)` | İlerleme çubuğu |
| `combobox(parent, liste)` | Açılır liste |
| `tabview(parent)` | Sekmeli görünüm |
| `alert(baslik, mesaj)` | Bilgi diyaloğu |
| `ask(baslik, soru)` | Evet/Hayır diyaloğu |

### Event Sistemi

```modi
event(clicked, btn, fonksiyon)   // butona tıklanınca
event(enter, giris, fonksiyon)   // Enter'a basılınca
event(changed, combo, fonksiyon) // değer değişince
```

> Tam sözdizimi rehberi için [`syntax_guide.md`](syntax_guide.md) dosyasına bakın.

---

## 📁 Proje Yapısı

```
modi-ide/
├── main.py            # IDE ana uygulaması ve Modi çevirici
├── syntax_guide.md    # Sözdizimi dokümantasyonu
├── requirements.txt   # Python bağımlılıkları
├── .gitignore
└── README.md
```

---

## 🛠️ Nasıl Çalışır?

Modi kodu → **Çevirici** → Python kodu → **Python yorumlayıcı / PyInstaller**

```
say("Merhaba")         →   print("Merhaba")
set x = 5              →   x = 5
repeat(3):             →   for _ in range(3):
func tikla():          →   def tikla():
event(clicked, b, f)   →   event("clicked", b, f)
```

Çevirici (`translate()` fonksiyonu), Modi sözdizimini satır satır Python'a dönüştürür. Çevrilen kod anında `compile()` ile Python tarafından doğrulanır.

---

## 📋 Gereksinimler (requirements.txt)

```
PySide6>=6.5.0
```

> `customtkinter` çalışma zamanında **otomatik yüklenir**, elle kurmanıza gerek yoktur.

---

## 🤝 Katkı

Katkılar her zaman memnuniyetle karşılanır!

1. Bu repoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b ozellik/yeni-komut`)
3. Değişikliklerinizi commit edin (`git commit -m 'feat: yeni komut eklendi'`)
4. Branch'i push edin (`git push origin ozellik/yeni-komut`)
5. Pull Request açın

---

## 🗺️ Yol Haritası

- [ ] Sözdizimi renklendirme (syntax highlighting)
- [ ] Dosya aç / kaydet
- [ ] Proje yöneticisi
- [ ] Daha fazla CTK bileşeni
- [ ] Hata mesajları Türkçeleştirme
- [ ] Hazır örnek şablonlar

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.

---

<div align="center">
  <sub>Sevgiyle yapıldı 💙 — Beko-soft</sub>
</div>
