# Modi Syntax Rehberi

Modi sade ve tek biçimli bir dildir. Temel fikir şudur: komutlar parantezle yazılır, değişkenler `set` ile atanır, fonksiyonlar `func` ile tanımlanır, olaylar `event(...)` ile bağlanır.

---

## 1. Temel Yapı

### Yazdırma

```modi
say("Merhaba!")
say(42)
say("Sonuc: " + str(100))
```

### Değişken

```modi
set isim = "Ada"
set yas = 12
set sonuc = 3 + 5
```

### Tekrar

```modi
repeat(5):
    say("Tekrar!")
```

### Koşul

```modi
set puan = 85

if puan >= 50:
    say("Gectin!")
else:
    say("Kaldin.")
```

### Fonksiyon

Python `def` yerine Modi'de `func` kullanılır.

```modi
func selamla():
    say("Merhaba")

selamla()
```

Parametreli fonksiyon:

```modi
func selamla(isim):
    say("Merhaba " + isim)

selamla("Ada")
```

---

## 2. CTK Temel Arayüz

```modi
set app = window("Uygulamam", 420, 320)
set panel = frame(app)

set baslik = label(panel, "Merhaba", 20)
set giris = entry(panel, "Adinizi girin")
set btn = button(panel, "Tikla")

run(app)
```

Temel CTK komutları:

```modi
window("Baslik", 420, 320)
frame(app)
label(panel, "Metin", 18)
entry(panel, "Yer tutucu")
button(panel, "Buton")
textbox(panel, 360, 160)
checkbox(panel, "Secenek")
switch(panel, "Ac/Kapat")
slider(panel, 0, 100)
progressbar(panel)
combobox(panel, ["A", "B", "C"])
```

Metin ve değer işlemleri:

```modi
set ad = get_text(giris)
set_text(baslik, "Merhaba " + ad)
set_entry(giris, "Ada")
clear(giris)

set_box(notlar, "Metin")
set metin = get_box(notlar)

set_value(slider1, 50)
set_progress(bar, 75)
set secim = get_selected(combo)
```

---

## 3. Event Sözdizimi

Olay bağlamak için tek yapı kullanılır:

```modi
event(clicked, btn, tikla)
```

Biçim:

```modi
event(olay, hedef, fonksiyon)
```

Temel olaylar:

```modi
event(clicked, btn, tikla)      // butona tiklaninca
event(enter, giris, kaydet)     // entry icinde Enter'a basilinca
event(changed, secim, degisti)  // slider/combobox/option degisince
```

Örnek:

```modi
func tikla():
    set ad = get_text(giris)
    set_text(baslik, "Merhaba " + ad)

set app = window("Event Ornegi", 420, 320)
set panel = frame(app)
set baslik = label(panel, "Adinizi girin", 18)
set giris = entry(panel, "Ad")
set btn = button(panel, "Kaydet")

event(clicked, btn, tikla)
event(enter, giris, tikla)

run(app)
```

---

## 4. Dialog ve Zamanlama

```modi
alert("Bilgi", "Kayit tamamlandi")
set cevap = ask("Onay", "Devam edilsin mi?")
```

```modi
func sonra():
    alert("Hazir", "1 saniye gecti")

after(app, 1000, sonra)
```

---

## 5. Tam Örnek

```modi
func kaydet():
    set ad = get_text(giris)
    if ad:
        set_text(durum, "Kaydedildi: " + ad)
        set_progress(bar, 100)
    else:
        alert("Uyari", "Lutfen ad girin")

func seviye_degisti():
    set_text(durum, "Seviye: " + get_selected(seviye))

set app = window("Modi CTK", 460, 380)
set panel = frame(app)

set durum = label(panel, "Adinizi yazin", 18)
set giris = entry(panel, "Ad")
set btn = button(panel, "Kaydet")
set bar = progressbar(panel)
set seviye = combobox(panel, ["Baslangic", "Orta", "Ileri"])

event(clicked, btn, kaydet)
event(enter, giris, kaydet)
event(changed, seviye, seviye_degisti)

run(app)
```

---

## 6. Genel Kurallar

- Fonksiyon için `func isim(...):` kullanın.
- Olay için her zaman `event(olay, hedef, fonksiyon)` kullanın.
- Değişken için `set x = ...` kullanın.
- CTK komutları normal fonksiyon gibi parantezle yazılır.
- Bloklardan sonra `:` koyun ve 4 boşluk girinti bırakın.
- Arayüzlü programlarda son satır çoğunlukla `run(app)` olur.
