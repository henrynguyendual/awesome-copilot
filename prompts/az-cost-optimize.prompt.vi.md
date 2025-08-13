# Tối Ưu Chi Phí Azure

Quy trình làm việc này phân tích các tệp Infrastructure-as-Code (IaC) và tài nguyên Azure để tạo ra các đề xuất tối ưu chi phí. Nó sẽ tạo ra các issue riêng biệt trên GitHub cho từng cơ hội tối ưu hóa, cộng thêm một issue EPIC để điều phối triển khai, giúp theo dõi và thực hiện sáng kiến tiết kiệm chi phí hiệu quả.

## Điều Kiện Tiên Quyết
- Máy chủ Azure MCP đã được cấu hình và xác thực
- Máy chủ GitHub MCP đã được cấu hình và xác thực
- Đã xác định repository GitHub mục tiêu
- Tài nguyên Azure đã được triển khai (tệp IaC là tùy chọn nhưng hữu ích)
- Ưu tiên sử dụng các công cụ Azure MCP (`azmcp-*`) thay vì Azure CLI trực tiếp khi có thể

## Các Bước Quy Trình

### Bước 1: Lấy Best Practices của Azure
**Hành động**: Lấy các best practices về tối ưu chi phí trước khi phân tích  
**Công cụ**: Công cụ best practices của Azure MCP  
**Quy trình**:
1. **Tải Best Practices**:
   - Chạy `azmcp-bestpractices-get` để lấy các hướng dẫn tối ưu Azure mới nhất. Điều này có thể không bao quát tất cả tình huống nhưng cung cấp nền tảng ban đầu.
   - Sử dụng các best practices này để hỗ trợ phân tích và đề xuất
   - Tham chiếu best practices trong các khuyến nghị tối ưu

### Bước 2: Khám Phá Hạ Tầng Azure
**Hành động**: Khám phá và phân tích tài nguyên Azure một cách động  
**Công cụ**: Azure MCP tools + Azure CLI (fallback) + quyền truy cập file cục bộ  
**Quy trình**:
1. **Khám Phá Tài Nguyên**:
   - Chạy `azmcp-subscription-list` để tìm subscription
   - Chạy `azmcp-group-list --subscription <subscription-id>` để tìm resource group
   - Lấy danh sách tất cả tài nguyên trong group:
     - `az resource list --subscription <id> --resource-group <name>`
   - Với từng loại tài nguyên, ưu tiên MCP trước, CLI fallback sau.

2. **Phát Hiện IaC**:
   - Tìm tệp IaC: `"**/*.bicep"`, `"**/*.tf"`, `"**/main.json"`, `"**/*template*.json"`
   - Phân tích định nghĩa tài nguyên
   - So sánh với tài nguyên đã phát hiện để tìm khác biệt
   - Nếu không tìm thấy IaC → dừng và báo cáo

3. **Phân Tích Cấu Hình**:
   - Trích xuất SKU, tier và cấu hình hiện tại
   - Xác định quan hệ và phụ thuộc tài nguyên

### Bước 3: Thu Thập Số Liệu Sử Dụng & Xác Minh Chi Phí
**Hành động**: Thu thập dữ liệu sử dụng và xác minh chi phí  
**Công cụ**: Azure MCP monitoring tools + Azure CLI  
**Quy trình**:
1. **Tìm Nguồn Giám Sát**  
2. **Chạy Truy Vấn Sử Dụng** (CPU, Cosmos DB, Storage...)  
3. **Tính Toán Số Liệu Cơ Sở** (trung bình CPU, băng thông DB...)  
4. **Xác Minh Chi Phí Hiện Tại** (từ SKU/tier và bảng giá Azure)

### Bước 4: Tạo Khuyến Nghị Tối Ưu Chi Phí
**Hành động**: Phân tích để tìm cơ hội tối ưu  
**Công cụ**: Phân tích cục bộ với dữ liệu thu thập được  
**Quy trình**:
1. **Áp Dụng Mẫu Tối Ưu** cho Compute, Database, Storage, Hạ tầng  
2. **Tính Tiết Kiệm Có Cơ Sở**  
3. **Tính Điểm Ưu Tiên**  
4. **Xác Thực Khuyến Nghị**

### Bước 5: Xác Nhận Người Dùng
- Hiển thị tóm tắt
- Chỉ tạo issue nếu người dùng đồng ý

### Bước 6: Tạo Issue Riêng Lẻ
- Tạo issue cho từng tối ưu hóa, label "cost-optimization" & "azure"  
- Nội dung issue gồm: mô tả, cách triển khai, bằng chứng, bước xác thực, rủi ro

### Bước 7: Tạo EPIC
- Tạo issue EPIC để điều phối, chứa sơ đồ kiến trúc, danh sách issue con, tiến độ, tiêu chí thành công

## Xử Lý Lỗi
- Xác minh chi phí
- Xử lý lỗi xác thực Azure
- Xử lý khi không tìm thấy tài nguyên
- Ghi chú hạn chế khi thiếu dữ liệu

## Tiêu Chí Thành Công
- ✅ Chi phí được xác minh với bảng giá Azure
- ✅ Tạo issue cho từng tối ưu
- ✅ EPIC bao quát toàn bộ
- ✅ Có lệnh CLI cụ thể
- ✅ Có sơ đồ kiến trúc chính xác