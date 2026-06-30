# Modi Sözdizimi Rehberi

Modi sade ve tek biçimli bir dildir: komutlar parantezle yazılır, değişkenler `set` ile atanır, fonksiyonlar `func` ile tanımlanır, olaylar `event(...)` ile bağlanır.

---

## 1. Temel Yapı

### Yazdırma / Yorum

```modi
say("Merhaba!")
say(42)
say("Sonuc: " + str(100))

// Bu bir yorum satırıdır
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

```modi
func selamla(isim):
    say("Merhaba " + isim)

selamla("Ada")
```

---

## 2. Pencere ve Kapsayıcılar

| Komut | Açıklama |
|---|---|
| `window(baslik, w, h)` | Ana pencere oluştur |
| `popup(baslik, w, h)` | İkincil/diyalog penceresi (modal) |
| `frame(parent)` | Çerçeve / panel |
| `scroll_frame(parent, etiket)` | Kaydırılabilir çerçeve |
| `tabview(parent)` | Sekmeli görünüm |
| `add_tab(tv, isim)` | Sekme ekle, sekme panelini döndürür |
| `separator(parent)` | Yatay ayırıcı çizgi |
| `run(app)` | Uygulamayı başlat |
| `close(app)` | Pencereyi kapat |

```modi
set app = window("Uygulamam", 420, 320)
set panel = frame(app)
run(app)
```

```modi
// Sekmeli arayüz
set app = window("Sekmeler", 480, 360)
set tv = tabview(app)
set sayfa1 = add_tab(tv, "Birinci")
set sayfa2 = add_tab(tv, "Ikinci")
set lbl = label(sayfa1, "Birinci sekme", 16)
run(app)
```

---

## 3. Yerleşim

| Komut | Açıklama |
|---|---|
| `pack(widget)` | Widget'i pakete ekle (varsayılan) |
| `hide(widget)` | Widget'i gizle (pack veya grid ile çalışır) |
| `show(widget)` | Gizlenmiş widget'i tekrar göster |
| `destroy(widget)` | Widget'i tamamen sil |

```modi
set btn = button(panel, "Gizle")

func gizle():
    hide(btn)

event(clicked, btn, gizle)
```

---

## 4. Metin ve Buton

| Komut | Açıklama |
|---|---|
| `label(parent, metin, boyut)` | Metin etiketi |
| `set_text(widget, metin)` | Etiket metnini değiştir |
| `get_label(widget)` | Etiket metnini oku |
| `button(parent, metin)` | Tıklanabilir buton |
| `button(parent, metin, on_click=f)` | Fonksiyon bağlı buton |

```modi
set lbl = label(panel, "Merhaba", 18)
set btn = button(panel, "Tikla")

func tikla():
    set_text(lbl, "Tiklandi!")

event(clicked, btn, tikla)
```

---

## 5. Giriş Alanları

| Komut | Açıklama |
|---|---|
| `entry(parent, placeholder, width)` | Tek satır metin girişi |
| `password_entry(parent, placeholder)` | Maskelenmiş şifre girişi |
| `get_text(widget)` | Giriş içeriğini oku |
| `set_entry(widget, metin)` | Giriş içeriğini ayarla |
| `clear(widget)` | Girişi temizle |
| `textbox(parent, w, h)` | Çok satırlı metin kutusu |
| `textbox(parent, w, h, readonly=True)` | Salt okunur metin kutusu |
| `get_box(widget)` | Tüm metni oku |
| `set_box(widget, metin)` | Tüm metni ayarla |
| `append_box(widget, metin)` | Kutunun sonuna satır ekle |

```modi
set giris = entry(panel, "Adınızı girin")
set sifre = password_entry(panel, "Şifreniz")
set notlar = textbox(panel, 360, 140)

func kaydet():
    set ad = get_text(giris)
    append_box(notlar, "Kaydedildi: " + ad)
    clear(giris)

set btn = button(panel, "Kaydet")
event(clicked, btn, kaydet)
```

---

## 6. Seçim Bileşenleri

| Komut | Açıklama |
|---|---|
| `checkbox(parent, metin)` | Onay kutusu |
| `switch(parent, metin)` | Aç/kapat anahtarı |
| `is_checked(widget)` | Seçili mi? (True/False) |
| `set_checked(widget, True/False)` | Seçim durumunu ayarla |
| `combobox(parent, liste)` | Salt okunur açılır liste |
| `optionmenu(parent, liste)` | Açılır menü |
| `get_selected(widget)` | Seçilen değeri oku |
| `set_selected(widget, deger)` | Seçimi ayarla |
| `update_list(widget, liste)` | Listeyi güncelle |

```modi
set cb = combobox(panel, ["Kolay", "Orta", "Zor"])
set sw = switch(panel, "Karanlık Mod")

func degisti():
    if is_checked(sw):
        say("Karanlık mod açık")

event(changed, sw, degisti)
```

---

## 7. Kaydırıcı ve İlerleme

| Komut | Açıklama |
|---|---|
| `slider(parent, min, max)` | Kaydırıcı (0-100 varsayılan) |
| `get_value(widget)` | Değeri oku |
| `set_value(widget, deger)` | Değeri ayarla |
| `progressbar(parent)` | İlerleme çubuğu |
| `set_progress(widget, deger)` | İlerlemeyi ayarla (0-100) |

```modi
set bar = progressbar(panel)
set sl = slider(panel, 0, 100)

func guncelle(val):
    set_progress(bar, val)

event(changed, sl, guncelle)
```

---

## 8. Stil ve Görünüm

| Komut | Açıklama |
|---|---|
| `set_color(widget, renk)` | Arka plan veya yazı rengini ayarla |
| `set_text_color(widget, renk)` | Yazı rengini ayarla |
| `set_enabled(widget, True/False)` | Aktif/pasif yap |
| `set_theme(mod)` | `"dark"` veya `"light"` |
| `set_color_theme(tema)` | `"blue"`, `"green"`, `"dark-blue"` |

```modi
set lbl = label(panel, "Renkli Metin", 16)
set_text_color(lbl, "#ff6b6b")

set btn = button(panel, "Pasif")
set_enabled(btn, False)
```

---

## 9. Event Sistemi

Tek form: `event(olay, widget, fonksiyon)`

| Olay | Ne Zaman Tetiklenir |
|---|---|
| `clicked` | Butona tıklanınca |
| `enter` | Entry içinde Enter'a basılınca |
| `changed` | Slider/combobox/switch değişince |

```modi
func tikla():
    set_text(lbl, "Tiklandi!")

func guncelle(val):
    set_text(lbl, "Deger: " + str(int(val)))

event(clicked, btn, tikla)
event(enter, giris, kaydet)
event(changed, sl, guncelle)
```

---

## 10. Diyaloglar ve Zamanlama

| Komut | Açıklama |
|---|---|
| `alert(baslik, mesaj)` | Bilgi diyaloğu |
| `ask(baslik, soru)` | Evet/Hayır diyaloğu → True/False |
| `after(widget, ms, fonksiyon)` | ms sonra fonksiyonu çağır |

```modi
func onayla():
    set cevap = ask("Onay", "Devam edilsin mi?")
    if cevap:
        alert("Tamam", "Isleme devam ediliyor.")

set btn = button(panel, "Onayla")
event(clicked, btn, onayla)
```

---

## 11. Dosya İşlemleri

| Komut | Açıklama |
|---|---|
| `open_file(baslik)` | Dosya seçme diyaloğu → yol |
| `save_file(baslik)` | Dosya kaydetme diyaloğu → yol |
| `read_file(yol)` | Dosyayı oku → içerik |
| `write_file(yol, icerik)` | Dosyaya yaz → True/False |

```modi
set notlar = textbox(panel, 360, 200)

func ac():
    set yol = open_file("Dosya Sec")
    if yol:
        set icerik = read_file(yol)
        set_box(notlar, icerik)

func kaydet():
    set yol = save_file("Kaydet")
    if yol:
        set icerik = get_box(notlar)
        write_file(yol, icerik)

set app = window("Not Defteri", 480, 400)
set panel = frame(app)
set notlar = textbox(panel, 440, 280)
set btn_ac = button(panel, "Ac")
set btn_kaydet = button(panel, "Kaydet")

event(clicked, btn_ac, ac)
event(clicked, btn_kaydet, kaydet)
run(app)
```

---

## 12. Genel Kurallar

- `func isim(...):` → fonksiyon tanımı
- `event(olay, widget, fonksiyon)` → olay bağlama
- `set x = ...` → değişken atama
- `say(...)` → konsola yazdırma
- `repeat(n):` → n kez tekrarla
- Bloklardan sonra `:` koyun, 4 boşluk girinti bırakın
- Arayüzlü programlarda son satır `run(app)` olur
- `//` ile yorum satırı açılır
