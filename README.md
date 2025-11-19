1. Khởi tạo game và cửa sổ
Sử dụng pygame.init() để khởi tạo thư viện Pygame.
Tạo cửa sổ game với kích thước cố định (WIDTH, HEIGHT).
Load hình nền map nếu có (map.png).
2. Định nghĩa các class chính
Player
Kế thừa từ pygame.sprite.Sprite.
Trong hàm __init__, load ảnh player.png nếu có, nếu không thì tạo hình vuông màu.
Hàm update xử lý di chuyển bằng phím mũi tên (hoặc WASD), giới hạn nhân vật trong màn hình.
Zombie
Kế thừa từ pygame.sprite.Sprite.
Load ảnh zombie.png nếu có, nếu không thì tạo hình vuông màu.
Zombie xuất hiện ở cạnh màn hình, di chuyển về phía player.
Bullet
Kế thừa từ pygame.sprite.Sprite.
Được tạo ra khi bắn, di chuyển theo hướng chuột, tự hủy khi ra khỏi màn hình.
3. Quản lý các nhóm sprite
Sử dụng pygame.sprite.Group để quản lý player, zombie, bullet.
4. Logic game loop
Lặp vô hạn (while True), xử lý các sự kiện (phím, chuột, timer).
Khi bắn, tạo đối tượng Bullet.
Định kỳ sinh zombie mới.
Xử lý va chạm: Bullet trúng zombie thì zombie biến mất, player trúng zombie thì game over.
5. Thêm các skill
Rapid Fire: Giữ phím Space để bắn liên tục.
Bomb: Nhấn B để tiêu diệt toàn bộ zombie trên màn hình (giới hạn số lần dùng).
Slow: Nhấn S để làm chậm zombie trong vài giây.
6. Vẽ lên màn hình
Vẽ hình nền, các sprite, điểm số, hướng dẫn phím bấm.
Khi game over, hiển thị thông báo và hướng dẫn chơi lại (phím R).
7. Reset game
Khi nhấn R, reset lại tất cả đối tượng, điểm số, skill.
