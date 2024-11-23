import turtle
import time

# Pencere Yapımı

ekran = turtle.Screen()
ekran.title("PongGame")
ekran.bgcolor("black")
ekran.setup(width=1000, height=600)  # Burda ekran boyutunu belirledik 1000x600 piksel olacak

# Sol Raket

left_ped = turtle.Turtle()
left_ped.speed(0)
left_ped.shape("square")
left_ped.color("white")
left_ped.shapesize(stretch_wid=5, stretch_len=1)
left_ped.penup()
left_ped.goto(-400,0)

# Sağ Raket

right_ped = turtle.Turtle()
right_ped.speed(0)
right_ped.shape("square")
right_ped.color("white")
right_ped.shapesize(stretch_wid=5, stretch_len=1)
right_ped.penup()
right_ped.goto(400,0)

# Daire Şeklinde Top

top = turtle.Turtle()
top.speed(40)
top.shape("circle")
top.color("red")
top.penup()
top.goto(0,0)
top.dx = 5
top.dy = -5

"""
dx ve dy, burada topun hareketini kontrol eden hız ve yön değerleridir:

dx (delta x): Topun x ekseninde, yani yatay yönde ne kadar hareket edeceğini belirtir. Eğer dx pozitif bir değerse, top sağa doğru hareket eder. 
Eğer negatifse, sola doğru hareket eder.

dy (delta y): Topun y ekseninde, yani dikey yönde ne kadar hareket edeceğini belirtir. dy pozitifse top yukarı doğru hareket eder; 
negatifse aşağıya doğru hareket eder.

Her dx ve dy güncellemesi, topun ekrandaki konumunu bir miktar değiştirir, bu da topun hareket etmesini sağlar. Oyunda top bir kenara veya pad'e
çarptığında, dx veya dy negatif ile çarpılarak yön değiştirilir. Örneğin, top üst kenara çarptığında dy çarpanı ters çevrilerek 
topun aşağı yönelmesi sağlanır.
"""

# Skoru Başlatma

left_player = 0
right_player = 0

# Skoru Görüntüler

skor = turtle.Turtle()
skor.speed(0)
skor.color("blue")
skor.penup()
skor.hideturtle()
skor.goto(0,260)
skor.write("Left Player : 0         Right Player : 0", align = "center" , font = ("Courier",24,"normal"))

"""
skor.hideturtle()

Bu özellikle, çizim yapmadan yalnızca metin veya şekil göstermek istediğiniz durumlarda yararlıdır. Bu örnekte skor nesnesi, yalnızca skoru 
güncellemek için kullanılır; çizim yapması gerekmez. hideturtle() komutu ile kaplumbağa simgesi gizlenir, böylece sadece skor yazısı ekranda 
görünür ve oyun ekranı daha temiz görünür.
"""

"""
skor.write(text, align="center", font=("Courier", 24, "normal"))

text: yazılacak metin 
aligin: Yazının hizalanma yönünü ayarlar. "center" ortalamak, "left" sola yaslamak ve "right" sağa yaslamak için kullanılır
font: font: Yazının font ayarlarını belirler. Bu parametre bir demet (tuple) olarak verilir ve sırasıyla font tipi, boyutu ve stili şeklindedir.
"""

# Raketin Hareketi için Fonksiyonlar

def sol_raket_yukari():
    y = left_ped.ycor()     # ycor, turtleın mevcuz y kordinatını verir 
    if (y < 240):           # Kürek hareketini sınırlama
        y += 20
        left_ped.sety(y)    # sety, turtleın x değerine karışmadan y değerini istenilen değer olarak değiştirir

def sol_raket_assagi():
    y = left_ped.ycor() 
    if (y > -240):
        y -= 20
        left_ped.sety(y)

def sağ_raket_yukari():
    y = right_ped.ycor()      
    if (y < 240):           
        y += 20
        right_ped.sety(y)

def sağ_raket_assagi():
    y = right_ped.ycor() 
    if (y > -240):
        y -= 20
        right_ped.sety(y)   

ekran.listen()
ekran.onkeypress(sol_raket_yukari,"w")
ekran.onkeypress(sol_raket_assagi,"s")
ekran.onkeypress(sağ_raket_yukari,"Up")
ekran.onkeypress(sağ_raket_assagi,"Down")
"""
ekran.listen()

Bu komut, Turtle ekranının klavye girişlerini dinlemeye başlamasını sağlar. Yani, kullanıcının klavye tuşlarına bastığında belirli eylemlerin 
tetiklenebilmesi için önce dinleme moduna geçilmesi gerekir. Bu komut çağrılmadan, tuşlara basıldığında herhangi bir tepki verilmez.
"""

"""
onkeypress: Bu metod, belirli bir tuşa basıldığında çağrılacak bir fonksiyonu tanımlar. Bu örnekte, sol_raket_yukari fonksiyonu 
sol raketi yukarı kaydıran bir fonksiyon olduğu için w tuşuna basıldığında çalışacak ve sağ raket yukarı çıkacak.
"""

# Oyunun Ana Döngüsü

while True:

    ekran.update()
    #time.sleep(0.01)  # Oyunu daha akıcı hale getirmek için gecikme ekleyin

    """
    ekran.update()

    turtle modülünde, ekran otomatik olarak sürekli olarak güncellenmez. Bunun yerine, programın daha verimli çalışması için 
    ekrandaki değişikliklerin güncellenmesi belirli bir zamanda yapılır.
    ekran.update() çağrıldığında, önceki tüm hareketler, çizimler veya değişiklikler ekrana yansıtılır.
    """

    top.setx(top.xcor() + top.dx)
    top.sety(top.ycor() + top.dy)

    # Sınırları kontrol etme

    if (top.ycor() > 280):    # bu durum topun üst sınırı (ekranın üst kenarı) geçtiği anlamına gelir.
        top.sety(280)       
        top.dy *= -1        # Burda y kordinatı - ile çarptırılıp yansıma yaptırılır

    if (top.ycor() < -280):    
        top.sety(-280)       
        top.dy *= -1

    if (top.xcor() > 500):
        top.setx(500)
        time.sleep(1)
        top.goto(0,0)
        top.dy *= -1        # Bu kod topun başlangıçta bir önceki başlangıca göre zıt yönde hareket etmesini sağlar
        left_player += 1
        skor.clear()
        skor.write(f"Left Player : {left_player}        Right Player : {right_player}" , align="center" , font=("Courier",24,"normal"))

    if (top.xcor() < -500):
        top.setx(-500)
        time.sleep(1)
        top.goto(0,0)
        top.dy *= -1
        right_player += 1
        skor.clear()
        skor.write(f"Left Player : {left_player}        Right Player : {right_player}" , align="center" , font=("Courier",24,"normal"))

    # Raket topu çarpışması

    if (top.xcor() > 360 and top.xcor() < 370) and (top.ycor() < right_ped.ycor() + 50 and top.ycor() > right_ped.ycor() - 50):
        top.setx(360)
        top.dx *= -1

    """
    top.xcor() > 360 and top.xcor() < 370:

    Bu kısım, topun x koordinatının 360 ile 370 arasında olup olmadığını kontrol eder. Bu, topun sağ raketin konumuna çok yakın olduğunu 
    gösterir. Yani top, sağ raketin kenarına çarpma alanında.

    top.ycor() < right_ped.ycor() + 50 and top.ycor() > right_ped.ycor() - 50:

    Bu kısım, topun y koordinatının sağ raketin y koordinatından +50 ve -50 arasında olup olmadığını kontrol eder. Bu, topun sağ raketin 
    hareketli alanında olduğunu gösterir. Sağ raket, y ekseninde yukarı ve aşağı hareket edebildiği için, bu sınırları kontrol etmek önemlidir.
    """

    if (top.xcor() < -360 and top.xcor() > -370) and (top.ycor() < left_ped.ycor() + 50 and top.ycor() > left_ped.ycor() - 50):
        top.setx(-360)
        top.dx *= -1

    """
    top.sety(280) 

    Topun yukarı sınırda kalmasını sağlamak, oyunun mantığı açısından önemlidir. Oyun mekaniğinde, topun üst kenara çarptığında geri dönmesi 
    gerektiği varsayılır. sety(280) komutuyla, topun y ekseninde 280 piksel yükseklik değerine sabitlenmesi sağlanır ve bu sayede topun hareketi 
    kontrol altında tutulur.
    """

