import math

# Öklid mesafesi hesaplama fonksiyonu
def euclideanDistance(point1, point2):
    # İki nokta arasındaki Öklid mesafesini hesapla
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 2D uzaydaki noktaları temsil eden 'points' adlı liste
points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

# Mesafeleri saklayacak boş bir liste oluştur
distances = []

# Her nokta çifti arasındaki mesafeyi hesapla
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        # Her benzersiz nokta çifti için Öklid mesafesini hesapla
        distance = euclideanDistance(points[i], points[j])
        # Mesafeyi 'distances' listesine ekle
        distances.append(distance)

# Mesafeler listesindeki en küçük mesafeyi bul ve yazdır
min_distance = min(distances)
print("Minimum mesafe:", min_distance)
