---
mode: "agent"
description: "Phân tích tình trạng tài nguyên Azure, chẩn đoán sự cố từ log và dữ liệu đo từ xa, và tạo kế hoạch khắc phục cho các vấn đề được xác định."
---

# Tình trạng Tài nguyên Azure & Chẩn đoán Sự cố

Quy trình này phân tích một tài nguyên Azure cụ thể để đánh giá tình trạng hoạt động, chẩn đoán các sự cố tiềm ẩn bằng cách sử dụng log và dữ liệu đo từ xa, và phát triển một kế hoạch khắc phục toàn diện cho bất kỳ vấn đề nào được phát hiện.

## Điều kiện tiên quyết

- Máy chủ Azure MCP đã được cấu hình và xác thực
- Tài nguyên Azure mục tiêu đã được xác định (tên và tùy chọn nhóm tài nguyên/subscription)
- Tài nguyên phải được triển khai và đang chạy để tạo log/dữ liệu đo từ xa
- Ưu tiên các công cụ Azure MCP (`azmcp-*`) hơn Azure CLI trực tiếp khi có sẵn

## Các bước trong Quy trình

### Bước 1: Nhận các Phương pháp Tốt nhất của Azure

**Hành động**: Truy xuất các phương pháp tốt nhất về chẩn đoán và khắc phục sự cố
**Công cụ**: Công cụ phương pháp tốt nhất của Azure MCP
**Quy trình**:

1.  **Tải các Phương pháp Tốt nhất**:
    - Thực thi công cụ phương pháp tốt nhất của Azure để nhận hướng dẫn chẩn đoán
    - Tập trung vào giám sát tình trạng, phân tích log và các mẫu giải quyết sự cố
    - Sử dụng các phương pháp này để định hướng phương pháp chẩn đoán và các đề xuất khắc phục

### Bước 2: Khám phá & Nhận dạng Tài nguyên

**Hành động**: Định vị và xác định tài nguyên Azure mục tiêu
**Công cụ**: Công cụ Azure MCP + Azure CLI làm phương án dự phòng
**Quy trình**:

1.  **Tra cứu Tài nguyên**:

    - Nếu chỉ cung cấp tên tài nguyên: Tìm kiếm trên các subscription bằng `azmcp-subscription-list`
    - Sử dụng `az resource list --name <resource-name>` để tìm các tài nguyên khớp
    - Nếu tìm thấy nhiều kết quả khớp, yêu cầu người dùng chỉ định subscription/nhóm tài nguyên
    - Thu thập thông tin chi tiết về tài nguyên:
      - Loại tài nguyên và trạng thái hiện tại
      - Vị trí, thẻ và cấu hình
      - Các dịch vụ và phụ thuộc liên quan

2.  **Phát hiện Loại Tài nguyên**:
    - Xác định loại tài nguyên để quyết định phương pháp chẩn đoán phù hợp:
      - **Web Apps/Function Apps**: Log ứng dụng, chỉ số hiệu suất, theo dõi phụ thuộc
      - **Virtual Machines**: Log hệ thống, bộ đếm hiệu suất, chẩn đoán khởi động
      - **Cosmos DB**: Chỉ số yêu cầu, điều tiết, thống kê phân vùng
      - **Storage Accounts**: Log truy cập, chỉ số hiệu suất, tính khả dụng
      - **SQL Database**: Hiệu suất truy vấn, log kết nối, sử dụng tài nguyên
      - **Application Insights**: Dữ liệu đo từ xa của ứng dụng, ngoại lệ, phụ thuộc
      - **Key Vault**: Log truy cập, trạng thái chứng chỉ, sử dụng secret
      - **Service Bus**: Chỉ số tin nhắn, hàng đợi thư chết, thông lượng

### Bước 3: Đánh giá Tình trạng Hoạt động

**Hành động**: Đánh giá tình trạng hoạt động và tính khả dụng hiện tại của tài nguyên
**Công cụ**: Công cụ giám sát Azure MCP + Azure CLI
**Quy trình**:

1.  **Kiểm tra Tình trạng Cơ bản**:

    - Kiểm tra trạng thái cấp phép và trạng thái hoạt động của tài nguyên
    - Xác minh tính khả dụng và khả năng phản hồi của dịch vụ
    - Xem xét các thay đổi về triển khai hoặc cấu hình gần đây
    - Đánh giá mức sử dụng tài nguyên hiện tại (CPU, bộ nhớ, lưu trữ, v.v.)

2.  **Các Chỉ số Tình trạng theo Dịch vụ**:
    - **Web Apps**: Mã phản hồi HTTP, thời gian phản hồi, thời gian hoạt động
    - **Cơ sở dữ liệu**: Tỷ lệ kết nối thành công, hiệu suất truy vấn, deadlock
    - **Lưu trữ**: Tỷ lệ phần trăm khả dụng, tỷ lệ yêu cầu thành công, độ trễ
    - **VMs**: Chẩn đoán khởi động, chỉ số hệ điều hành khách, kết nối mạng
    - **Functions**: Tỷ lệ thực thi thành công, thời gian, tần suất lỗi

### Bước 4: Phân tích Log & Dữ liệu đo từ xa

**Hành động**: Phân tích log và dữ liệu đo từ xa để xác định các sự cố và mẫu
**Công cụ**: Công cụ giám sát Azure MCP cho các truy vấn Log Analytics
**Quy trình**:

1.  **Tìm Nguồn Giám sát**:

    - Sử dụng `azmcp-monitor-workspace-list` để xác định các không gian làm việc Log Analytics
    - Định vị các phiên bản Application Insights được liên kết với tài nguyên
    - Xác định các bảng log có liên quan bằng `azmcp-monitor-table-list`

2.  **Thực thi Truy vấn Chẩn đoán**:
    Sử dụng `azmcp-monitor-log-query` với các truy vấn KQL được nhắm mục tiêu dựa trên loại tài nguyên:

    **Phân tích Lỗi Chung**:

    ```kql
    // Các lỗi và ngoại lệ gần đây
    union isfuzzy=true
        AzureDiagnostics,
        AppServiceHTTPLogs,
        AppServiceAppLogs,
        AzureActivity
    | where TimeGenerated > ago(24h)
    | where Level == "Error" or ResultType != "Success"
    | summarize ErrorCount=count() by Resource, ResultType, bin(TimeGenerated, 1h)
    | order by TimeGenerated desc
    ```

    **Phân tích Hiệu suất**:

    ```kql
    // Các mẫu suy giảm hiệu suất
    Perf
    | where TimeGenerated > ago(7d)
    | where ObjectName == "Processor" and CounterName == "% Processor Time"
    | summarize avg(CounterValue) by Computer, bin(TimeGenerated, 1h)
    | where avg_CounterValue > 80
    ```

    **Truy vấn theo Ứng dụng**:

    ```kql
    // Application Insights - Các yêu cầu thất bại
    requests
    | where timestamp > ago(24h)
    | where success == false
    | summarize FailureCount=count() by resultCode, bin(timestamp, 1h)
    | order by timestamp desc

    // Cơ sở dữ liệu - Các kết nối thất bại
    AzureDiagnostics
    | where ResourceProvider == "MICROSOFT.SQL"
    | where Category == "SQLSecurityAuditEvents"
    | where action_name_s == "CONNECTION_FAILED"
    | summarize ConnectionFailures=count() by bin(TimeGenerated, 1h)
    ```

3.  **Nhận dạng Mẫu**:
    - Xác định các mẫu lỗi lặp lại hoặc các điểm bất thường
    - Tương quan lỗi với thời gian triển khai hoặc thay đổi cấu hình
    - Phân tích xu hướng hiệu suất và các mẫu suy giảm
    - Tìm kiếm các lỗi phụ thuộc hoặc các vấn đề dịch vụ bên ngoài

### Bước 5: Phân loại Sự cố & Phân tích Nguyên nhân Gốc rễ

**Hành động**: Phân loại các sự cố đã xác định và xác định nguyên nhân gốc rễ
**Quy trình**:

1.  **Phân loại Sự cố**:

    - **Nghiêm trọng**: Dịch vụ không khả dụng, mất dữ liệu, vi phạm bảo mật
    - **Cao**: Suy giảm hiệu suất, lỗi không liên tục, tỷ lệ lỗi cao
    - **Trung bình**: Cảnh báo, cấu hình không tối ưu, vấn đề hiệu suất nhỏ
    - **Thấp**: Thông báo thông tin, cơ hội tối ưu hóa

2.  **Phân tích Nguyên nhân Gốc rễ**:

    - **Sự cố Cấu hình**: Cài đặt không chính xác, thiếu phụ thuộc
    - **Hạn chế Tài nguyên**: Giới hạn CPU/bộ nhớ/đĩa, điều tiết
    - **Sự cố Mạng**: Vấn đề kết nối, phân giải DNS, quy tắc tường lửa
    - **Sự cố Ứng dụng**: Lỗi mã, rò rỉ bộ nhớ, truy vấn không hiệu quả
    - **Phụ thuộc Bên ngoài**: Lỗi dịch vụ của bên thứ ba, giới hạn API
    - **Sự cố Bảo mật**: Lỗi xác thực, hết hạn chứng chỉ

3.  **Đánh giá Tác động**:
    - Xác định tác động kinh doanh và người dùng/hệ thống bị ảnh hưởng
    - Đánh giá tính toàn vẹn dữ liệu và các hàm ý bảo mật
    - Đánh giá mục tiêu thời gian phục hồi và các ưu tiên

### Bước 6: Tạo Kế hoạch Khắc phục

**Hành động**: Tạo một kế hoạch toàn diện để giải quyết các sự cố đã xác định
**Quy trình**:

1.  **Hành động Ngay lập tức** (sự cố nghiêm trọng):

    - Sửa lỗi khẩn cấp để khôi phục tính khả dụng của dịch vụ
    - Các giải pháp tạm thời để giảm thiểu tác động
    - Quy trình leo thang cho các vấn đề phức tạp

2.  **Sửa lỗi Ngắn hạn** (sự cố mức Cao/Trung bình):

    - Điều chỉnh cấu hình và mở rộng tài nguyên
    - Cập nhật và vá lỗi ứng dụng
    - Cải thiện giám sát và cảnh báo

3.  **Cải tiến Dài hạn** (tất cả các sự cố):

    - Thay đổi kiến trúc để có khả năng phục hồi tốt hơn
    - Các biện pháp phòng ngừa và cải tiến giám sát
    - Cải thiện tài liệu và quy trình

4.  **Các bước Thực hiện**:
    - Các mục hành động được ưu tiên với các lệnh Azure CLI cụ thể
    - Quy trình kiểm tra và xác thực
    - Kế hoạch quay lui cho mỗi thay đổi
    - Giám sát để xác minh việc giải quyết sự cố

### Bước 7: Xác nhận của Người dùng & Tạo Báo cáo

**Hành động**: Trình bày các phát hiện và nhận phê duyệt cho các hành động khắc phục
**Quy trình**:

1.  **Hiển thị Tóm tắt Đánh giá Tình trạng**:

    ```
    🏥 Đánh giá Tình trạng Tài nguyên Azure

    📊 Tổng quan Tài nguyên:
    • Tài nguyên: [Tên] ([Loại])
    • Trạng thái: [Tốt/Cảnh báo/Nghiêm trọng]
    • Vị trí: [Vùng]
    • Phân tích lần cuối: [Dấu thời gian]

    🚨 Các sự cố được xác định:
    • Nghiêm trọng: X sự cố cần chú ý ngay lập tức
    • Cao: Y sự cố ảnh hưởng đến hiệu suất/độ tin cậy
    • Trung bình: Z sự cố cần tối ưu hóa
    • Thấp: N mục thông tin

    🔍 Các sự cố hàng đầu:
    1. [Loại sự cố]: [Mô tả] - Tác động: [Cao/Trung bình/Thấp]
    2. [Loại sự cố]: [Mô tả] - Tác động: [Cao/Trung bình/Thấp]
    3. [Loại sự cố]: [Mô tả] - Tác động: [Cao/Trung bình/Thấp]

    🛠️ Kế hoạch Khắc phục:
    • Hành động Ngay lập tức: X mục
    • Sửa lỗi Ngắn hạn: Y mục
    • Cải tiến Dài hạn: Z mục
    • Thời gian Giải quyết Ước tính: [Mốc thời gian]

    ❓ Tiếp tục với kế hoạch khắc phục chi tiết? (y/n)
    ```

2.  **Tạo Báo cáo Chi tiết**:

    ````markdown
    # Báo cáo Tình trạng Tài nguyên Azure: [Tên Tài nguyên]

    **Tạo lúc**: [Dấu thời gian]  
    **Tài nguyên**: [ID Tài nguyên đầy đủ]  
    **Tình trạng Tổng thể**: [Trạng thái với chỉ báo màu]

    ## 🔍 Tóm tắt Điều hành

    [Tổng quan ngắn gọn về tình trạng hoạt động và các phát hiện chính]

    ## 📊 Chỉ số Tình trạng

    - **Tính khả dụng**: X% trong 24 giờ qua
    - **Hiệu suất**: [Thời gian phản hồi trung bình/thông lượng]
    - **Tỷ lệ lỗi**: X% trong 24 giờ qua
    - **Sử dụng Tài nguyên**: [Phần trăm CPU/Bộ nhớ/Lưu trữ]

    ## 🚨 Các sự cố được xác định

    ### Sự cố Nghiêm trọng

    - **[Sự cố 1]**: [Mô tả]
      - **Nguyên nhân Gốc rễ**: [Phân tích]
      - **Tác động**: [Tác động kinh doanh]
      - **Hành động Ngay lập tức**: [Các bước cần thiết]

    ### Sự cố Ưu tiên Cao

    - **[Sự cố 2]**: [Mô tả]
      - **Nguyên nhân Gốc rễ**: [Phân tích]
      - **Tác động**: [Tác động hiệu suất/độ tin cậy]
      - **Sửa lỗi Đề xuất**: [Các bước giải pháp]

    ## 🛠️ Kế hoạch Khắc phục

    ### Giai đoạn 1: Hành động Ngay lập tức (0-2 giờ)

    ```bash
    # Các bản sửa lỗi nghiêm trọng để khôi phục dịch vụ
    [Các lệnh Azure CLI với giải thích]
    ```
    ````

    ### Giai đoạn 2: Sửa lỗi Ngắn hạn (2-24 giờ)

    ```bash
    # Cải thiện hiệu suất và độ tin cậy
    [Các lệnh Azure CLI với giải thích]
    ```

    ### Giai đoạn 3: Cải tiến Dài hạn (1-4 tuần)

    ```bash
    # Các biện pháp kiến trúc và phòng ngừa
    [Các lệnh Azure CLI và thay đổi cấu hình]
    ```

    ## 📈 Đề xuất Giám sát

    - **Cảnh báo cần Cấu hình**: [Danh sách các cảnh báo được đề xuất]
    - **Bảng điều khiển cần Tạo**: [Gợi ý bảng điều khiển giám sát]
    - **Kiểm tra Tình trạng Định kỳ**: [Tần suất và phạm vi được đề xuất]

    ## ✅ Các bước Xác thực

    - [ ] Xác minh việc giải quyết sự cố qua log
    - [ ] Xác nhận các cải tiến về hiệu suất
    - [ ] Kiểm tra chức năng ứng dụng
    - [ ] Cập nhật giám sát và cảnh báo
    - [ ] Ghi lại bài học kinh nghiệm

    ## 📝 Các biện pháp Phòng ngừa

    - [Các đề xuất để ngăn chặn các sự cố tương tự]
    - [Cải tiến quy trình]
    - [Cải tiến giám sát]

    ```

    ```

## Xử lý Lỗi

- **Không tìm thấy Tài nguyên**: Cung cấp hướng dẫn về cách chỉ định tên/vị trí tài nguyên
- **Sự cố Xác thực**: Hướng dẫn người dùng thiết lập xác thực Azure
- **Không đủ Quyền**: Liệt kê các vai trò RBAC cần thiết để truy cập tài nguyên
- **Không có Log**: Đề nghị bật cài đặt chẩn đoán và chờ dữ liệu
- **Hết thời gian chờ Truy vấn**: Chia nhỏ phân tích thành các khoảng thời gian nhỏ hơn
- **Sự cố theo Dịch vụ**: Cung cấp đánh giá tình trạng chung với các hạn chế được ghi nhận

## Tiêu chí Thành công

- ✅ Tình trạng hoạt động của tài nguyên được đánh giá chính xác
- ✅ Tất cả các sự cố quan trọng được xác định và phân loại
- ✅ Phân tích nguyên nhân gốc rễ hoàn thành cho các vấn đề lớn
- ✅ Kế hoạch khắc phục có thể hành động với các bước cụ thể được cung cấp
- ✅ Bao gồm các đề xuất giám sát và phòng ngừa
- ✅ Ưu tiên rõ ràng các sự cố theo tác động kinh doanh
- ✅ Các bước thực hiện bao gồm quy trình xác thực và
