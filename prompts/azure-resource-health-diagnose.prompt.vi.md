# Sức Khỏe Tài Nguyên Azure & Chẩn Đoán Sự Cố

Quy trình này phân tích một tài nguyên Azure cụ thể để đánh giá tình trạng sức khỏe, chẩn đoán các vấn đề tiềm ẩn từ log và dữ liệu telemetry, đồng thời xây dựng kế hoạch khắc phục toàn diện cho các vấn đề được phát hiện.

## Điều Kiện Tiên Quyết
- Máy chủ Azure MCP đã cấu hình và xác thực
- Xác định tài nguyên Azure mục tiêu (tên và tùy chọn resource group/subscription)
- Tài nguyên phải được triển khai và chạy để tạo log/telemetry
- Ưu tiên dùng công cụ Azure MCP (`azmcp-*`) thay vì Azure CLI trực tiếp khi có thể

## Các Bước Quy Trình

### Bước 1: Lấy Best Practices của Azure
- Chạy công cụ best practices để lấy hướng dẫn chẩn đoán
- Tập trung vào giám sát sức khỏe, phân tích log và mẫu xử lý sự cố
- Sử dụng các best practices này để xây dựng phương pháp chẩn đoán và khuyến nghị khắc phục

### Bước 2: Khám Phá & Xác Định Tài Nguyên
- Nếu chỉ có tên: tìm trong subscriptions bằng `azmcp-subscription-list`
- Dùng `az resource list --name <tên>` để tìm tài nguyên
- Thu thập thông tin chi tiết: loại, trạng thái, vị trí, tag, cấu hình, dịch vụ liên quan
- Xác định loại tài nguyên để chọn phương pháp chẩn đoán phù hợp (Web App, VM, Cosmos DB, Storage, SQL, App Insights, Key Vault, Service Bus...)

### Bước 3: Đánh Giá Sức Khỏe
- Kiểm tra trạng thái provisioning và hoạt động
- Xác minh tính khả dụng và phản hồi dịch vụ
- Xem thay đổi cấu hình gần đây
- Đánh giá mức sử dụng tài nguyên (CPU, RAM, Storage...)
- Chỉ số sức khỏe theo loại dịch vụ (Web App: mã HTTP, uptime; DB: hiệu năng query; VM: boot diagnostics...)

### Bước 4: Phân Tích Log & Telemetry
- Tìm nguồn giám sát (Log Analytics workspace, App Insights)
- Xác định bảng log liên quan
- Chạy truy vấn KQL để phân tích lỗi, hiệu năng, truy vấn đặc thù ứng dụng
- Nhận diện mẫu lỗi lặp lại, suy giảm hiệu năng, lỗi phụ thuộc

### Bước 5: Phân Loại & Phân Tích Nguyên Nhân
- Phân loại mức độ: Critical, High, Medium, Low
- Nguyên nhân: cấu hình sai, giới hạn tài nguyên, lỗi mạng, lỗi ứng dụng, phụ thuộc bên ngoài, vấn đề bảo mật
- Đánh giá tác động: ảnh hưởng kinh doanh, dữ liệu, thời gian khôi phục

### Bước 6: Lập Kế Hoạch Khắc Phục
- **Hành động ngay**: khắc phục khẩn, workaround tạm thời, escalations
- **Ngắn hạn**: điều chỉnh cấu hình, cập nhật ứng dụng, cải thiện giám sát
- **Dài hạn**: thay đổi kiến trúc, phòng ngừa, cải tiến quy trình
- Các bước triển khai: lệnh Azure CLI, kiểm thử, rollback, giám sát kết quả

### Bước 7: Xác Nhận Người Dùng & Báo Cáo
- Hiển thị tóm tắt đánh giá sức khỏe (tài nguyên, trạng thái, số lượng vấn đề theo mức độ)
- Trình bày kế hoạch khắc phục (ngay lập tức, ngắn hạn, dài hạn)
- Tạo báo cáo chi tiết gồm: tóm tắt, số liệu sức khỏe, vấn đề phát hiện, kế hoạch khắc phục, khuyến nghị giám sát, bước xác minh, biện pháp phòng ngừa

## Xử Lý Lỗi
- Không tìm thấy tài nguyên: hướng dẫn xác định lại
- Lỗi xác thực: hướng dẫn thiết lập
- Thiếu quyền: liệt kê role RBAC cần có
- Không có log: khuyến nghị bật chẩn đoán
- Timeout truy vấn: chia nhỏ thời gian phân tích
- Vấn đề đặc thù dịch vụ: cung cấp đánh giá chung kèm giới hạn

## Tiêu Chí Thành Công
- ✅ Đánh giá chính xác tình trạng sức khỏe
- ✅ Xác định và phân loại mọi vấn đề quan trọng
- ✅ Hoàn thành phân tích nguyên nhân gốc
- ✅ Có kế hoạch khắc phục chi tiết và khả thi
- ✅ Bao gồm khuyến nghị giám sát và phòng ngừa
- ✅ Ưu tiên rõ ràng theo tác động kinh doanh
- ✅ Các bước triển khai có xác minh và rollback