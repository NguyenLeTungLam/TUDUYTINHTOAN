so_du = 1000000  # Khởi tạo 1 triệu đồng

while True:
    print("\n========= MENU ATM =========")
    print("1. Kiểm tra số dư")
    print("2. Nạp tiền")
    print("3. Rút tiền")
    print("4. Thoát")
    
    lua_chon = input("Nhập lựa chọn của bạn (1-4): ")

    if lua_chon == "1":
        print(f"Số dư hiện tại của bạn là: {so_du:,} VNĐ")
    
    elif lua_chon == "2":
        tien_nap = int(input("Nhập số tiền muốn nạp: "))
        so_du += tien_nap
        print(f"Nạp tiền thành công! Số dư mới: {so_du:,} VNĐ")
        
    elif lua_chon == "3":
        tien_rut = int(input("Nhập số tiền muốn rút: "))
        if tien_rut > so_du:
            print("Giao dịch thất bại! Số dư không đủ.")
        else:
            so_du -= tien_rut
            print(f"Rút tiền thành công! Số dư còn lại: {so_du:,} VNĐ")
            
    elif lua_chon == "4":
        print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
        break  # Thoát vòng lặp
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
