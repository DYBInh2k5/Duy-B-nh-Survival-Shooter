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





Dưới đây là tổng quan và hướng dẫn chi tiết từng bước để bạn tự làm lại dự án game bắn zombie bằng Python và Pygame:

1. Chuẩn bị môi trường
Cài đặt Python (khuyên dùng 3.11 trở lên).
Cài đặt Pygame:
Tạo thư mục dự án, ví dụ: Game
Tạo các thư mục con:
assets (lưu ảnh: player.png, zombie.png, map.png)
File chính: main.py
2. Tạo file ảnh
Tìm hoặc tự thiết kế các file ảnh PNG cho nhân vật, zombie, bản đồ và lưu vào assets/.
3. Viết code game (main.py)
Khởi tạo cửa sổ game, load ảnh nền, ảnh nhân vật, zombie.
Tạo các class:
Player: Điều khiển di chuyển, sử dụng ảnh player.
Zombie: Di chuyển về phía player, sử dụng ảnh zombie.
Bullet: Đạn bắn ra từ player.
Quản lý các nhóm sprite: player, zombie, bullet.
Thêm các skill:
Rapid Fire (Space): Bắn liên tục.
Bomb (B): Tiêu diệt toàn bộ zombie trên màn hình.
Slow (S): Làm chậm zombie.
Xử lý va chạm, điểm số, game over, chơi lại (phím R).
Vẽ hướng dẫn phím bấm và điểm số lên màn hình.
4. Tích hợp hình ảnh
Sử dụng pygame.image.load() để load ảnh cho player, zombie, map.
Nếu không có ảnh, dùng hình vuông màu làm mặc định.
5. Chạy game
Mở terminal, chuyển vào thư mục Game:
Chạy game:
Thao tác bằng các phím:
Di chuyển: Mũi tên hoặc WASD
Bắn: Chuột
Skill: Space (bắn nhanh), B (bom), S (làm chậm)
R: Chơi lại khi thua

<img width="796" height="628" alt="Screenshot 2025-11-19 101140" src="https://github.com/user-attachments/assets/548af6ae-cbdf-4fbb-9516-0dcc868b7ded" />



