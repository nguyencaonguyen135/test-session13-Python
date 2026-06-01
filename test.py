parking_lot = [
    {'id': 1, 'type': 'Xe may', 'owner': 'Nguyen Van A'},
    {'id': 2, 'type': 'O to', 'owner': 'Tran Van B'}
]
while True:
    choice = input('''
QUẢN LÝ BÃI XE - SMART PARKING

1. Thêm xe mới vào bãi
2. Hiển thị danh sách xe trong bãi
3. Tìm kiêm xe theo mã (id)
4. Xóa xe khỏi bãi (khi xe ra)
5. Thoat chưong trinh

Mời nhập chức năng: ''').strip()
# [Chức năng 1] Thêm xe mới: 
# Tự động gán ID tăng dần (mặc định bắt đầu từ 1).
# Loại xe và Chủ xe không được để trống. Nếu trường nào để trống yêu cầu người dùng nhập lại.
# [Chức năng 2] Hiển thị danh sách: 
# Nếu List rỗng, thông báo: "Bãi xe hiện đang trống!".
# Nếu có dữ liệu, trình bày dưới dạng bảng:

# [Chức năng 3] Tìm kiếm theo ID: 
# Nhập ID từ bàn phím. Thực hiện tìm kiếm trong List
# Nếu tìm thấy, in thông tin chi tiết của xe. Ví dụ: {'id': 1, 'type': 'Xe may', 'owner': 'Nguyen Van A'}.
# Nếu không tìm thấy: Thông báo "Không tìm thấy xe có ID [id]!".
# [Chức năng 4] Xóa xe khỏi bãi: 
# Tìm kiếm ID, nếu tồn tại thì xóa khỏi List và in ra thông báo “Đã xóa xe ID [id] thành công!”.
# Nếu không tồn tại: Thông báo "Không tìm thấy xe để xóa!".
    match choice:
        case "1":
            new_id = len(parking_lot) + 1
            new_type = input("Nhập loại xe: ")
            new_owner = input("Nhập tên chủ xe: ")
            if not new_type or not new_owner:
                print("Không được để trống thông tin xe!")
                continue
            else:
                parking_lot.append({'id': new_id, 'type': new_type, 'owner': new_owner})
            print("Thêm xe thành công!")
        case "2":
            if not parking_lot:
                print("Bãi xe hiện đang trống!")
            else:
                for i in parking_lot:
                    print(f"{i['id']} - {i['type']} - {i['owner']}")
        case "3":
            search_id = int(input("Nhập mã xe cần tìm: "))
            found = False
            for i in parking_lot:
                if i['id'] == search_id:
                    print(i)
                    found = True
                    break
            if not found:
                print(f"Không tìm thấy xe có ID {search_id}!")
        case "4":
            delete_id = int(input("Nhập mã xe cần xóa: "))
            found = False
            for i in parking_lot:
                if i['id'] == delete_id:
                    parking_lot.remove(i)
                    print("Xóa xe thành công!")
                    found = True
                    break
            if not found:
                print("Không tìm thấy xe với mã đã nhập!")
        case "5":
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ! Vui lòng nhâp lại")