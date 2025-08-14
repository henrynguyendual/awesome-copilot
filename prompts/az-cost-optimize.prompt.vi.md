---
mode: "agent"
description: "Phân tích các tài nguyên Azure được sử dụng trong ứng dụng (tệp IaC và/hoặc tài nguyên trong một rg mục tiêu) và tối ưu hóa chi phí - tạo các issue trên GitHub cho các tối ưu hóa được xác định."
---

# Tối ưu hóa Chi phí Azure

Quy trình này phân tích các tệp Infrastructure-as-Code (IaC - Cơ sở hạ tầng dưới dạng mã) và tài nguyên Azure để tạo ra các đề xuất tối ưu hóa chi phí. Nó tạo các issue riêng lẻ trên GitHub cho mỗi cơ hội tối ưu hóa cộng với một EPIC issue để điều phối việc triển khai, cho phép theo dõi và thực hiện hiệu quả các sáng kiến tiết kiệm chi phí.

## Điều kiện tiên quyết

- Máy chủ Azure MCP đã được cấu hình và xác thực
- Máy chủ GitHub MCP đã được cấu hình và xác thực
- Kho lưu trữ GitHub mục tiêu đã được xác định
- Các tài nguyên Azure đã được triển khai (tệp IaC không bắt buộc nhưng hữu ích)
- Ưu tiên sử dụng các công cụ Azure MCP (`azmcp-*`) hơn là Azure CLI trực tiếp khi có sẵn

## Các bước của Quy trình

### Bước 1: Lấy các Phương pháp Tốt nhất của Azure

**Hành động**: Truy xuất các phương pháp tốt nhất về tối ưu hóa chi phí trước khi phân tích
**Công cụ**: Công cụ phương pháp tốt nhất của Azure MCP
**Quy trình**:

1.  **Tải các Phương pháp Tốt nhất**:
    - Thực thi `azmcp-bestpractices-get` để nhận một số hướng dẫn tối ưu hóa Azure mới nhất. Điều này có thể không bao gồm tất cả các kịch bản nhưng cung cấp một nền tảng.
    - Sử dụng các phương pháp này để cung cấp thông tin cho các phân tích và đề xuất tiếp theo càng nhiều càng tốt
    - Tham chiếu các phương pháp tốt nhất trong các đề xuất tối ưu hóa, từ đầu ra của công cụ MCP hoặc tài liệu chung của Azure

### Bước 2: Khám phá Cơ sở hạ tầng Azure

**Hành động**: Tự động khám phá và phân tích các tài nguyên và cấu hình Azure
**Công cụ**: Công cụ Azure MCP + Azure CLI dự phòng + Truy cập hệ thống tệp cục bộ
**Quy trình**:

1.  **Khám phá Tài nguyên**:

    - Thực thi `azmcp-subscription-list` để tìm các subscription có sẵn
    - Thực thi `azmcp-group-list --subscription <subscription-id>` để tìm các resource group
    - Lấy danh sách tất cả các tài nguyên trong (các) group liên quan:
      - Sử dụng `az resource list --subscription <id> --resource-group <name>`
    - Đối với mỗi loại tài nguyên, hãy sử dụng công cụ MCP trước nếu có thể, sau đó dùng CLI dự phòng:
      - `azmcp-cosmos-account-list --subscription <id>` - Tài khoản Cosmos DB
      - `azmcp-storage-account-list --subscription <id>` - Tài khoản lưu trữ
      - `azmcp-monitor-workspace-list --subscription <id>` - Không gian làm việc Log Analytics
      - `azmcp-keyvault-key-list` - Key Vaults
      - `az webapp list` - Web Apps (dự phòng - không có công cụ MCP)
      - `az appservice plan list` - App Service Plans (dự phòng)
      - `az functionapp list` - Function Apps (dự phòng)
      - `az sql server list` - SQL Servers (dự phòng)
      - `az redis list` - Redis Cache (dự phòng)
      - ... và tương tự cho các loại tài nguyên khác

2.  **Phát hiện IaC**:

    - Sử dụng `file_search` để quét các tệp IaC: "**/\*.bicep", "**/*.tf", "**/main.json", "**/*template\*.json"
    - Phân tích các định nghĩa tài nguyên để hiểu các cấu hình dự kiến
    - So sánh với các tài nguyên đã khám phá để xác định sự khác biệt
    - Ghi nhận sự hiện diện của các tệp IaC để đưa ra các đề xuất triển khai sau này
    - KHÔNG sử dụng bất kỳ tệp nào khác từ kho lưu trữ, chỉ các tệp IaC. Việc sử dụng các tệp khác KHÔNG được phép vì nó không phải là nguồn đáng tin cậy.
    - Nếu bạn không tìm thấy tệp IaC, hãy DỪNG LẠI và báo cáo cho người dùng rằng không tìm thấy tệp IaC.

3.  **Phân tích Cấu hình**:
    - Trích xuất các SKU, bậc và cài đặt hiện tại cho mỗi tài nguyên
    - Xác định các mối quan hệ và sự phụ thuộc của tài nguyên
    - Lập bản đồ các mẫu sử dụng tài nguyên nếu có

### Bước 3: Thu thập Số liệu Sử dụng & Xác thực Chi phí Hiện tại

**Hành động**: Thu thập dữ liệu sử dụng VÀ xác minh chi phí tài nguyên thực tế
**Công cụ**: Công cụ giám sát Azure MCP + Azure CLI
**Quy trình**:

1.  **Tìm Nguồn Giám sát**:

    - Sử dụng `azmcp-monitor-workspace-list --subscription <id>` để tìm các không gian làm việc Log Analytics
    - Sử dụng `azmcp-monitor-table-list --subscription <id> --workspace <name> --table-type "CustomLog"` để khám phá dữ liệu có sẵn

2.  **Thực thi các Truy vấn Sử dụng**:

    - Sử dụng `azmcp-monitor-log-query` với các truy vấn được xác định trước này:
      - Truy vấn: "recent" cho các mẫu hoạt động gần đây
      - Truy vấn: "errors" cho các nhật ký cấp độ lỗi chỉ ra sự cố
    - Để phân tích tùy chỉnh, hãy sử dụng các truy vấn KQL:

    ```kql
    // Mức sử dụng CPU cho App Services
    AppServiceAppLogs
    | where TimeGenerated > ago(7d)
    | summarize avg(CpuTime) by Resource, bin(TimeGenerated, 1h)

    // Mức tiêu thụ RU của Cosmos DB
    AzureDiagnostics
    | where ResourceProvider == "MICROSOFT.DOCUMENTDB"
    | where TimeGenerated > ago(7d)
    | summarize avg(RequestCharge) by Resource

    // Các mẫu truy cập tài khoản lưu trữ
    StorageBlobLogs
    | where TimeGenerated > ago(7d)
    | summarize RequestCount=count() by AccountName, bin(TimeGenerated, 1d)
    ```

3.  **Tính toán các Số liệu Cơ bản**:

    - Trung bình sử dụng CPU/Bộ nhớ
    - Các mẫu thông lượng cơ sở dữ liệu
    - Tần suất truy cập lưu trữ
    - Tỷ lệ thực thi hàm

4.  **XÁC THỰC CHI PHÍ HIỆN TẠI**:
    - Sử dụng các cấu hình SKU/bậc đã khám phá ở Bước 2
    - Tra cứu giá Azure hiện tại tại https://azure.microsoft.com/pricing/ hoặc sử dụng lệnh `az billing`
    - Ghi lại: Tài nguyên → SKU hiện tại → Chi phí hàng tháng ước tính
    - Tính toán tổng chi phí hàng tháng thực tế hiện tại trước khi chuyển sang các đề xuất

### Bước 4: Tạo các Đề xuất Tối ưu hóa Chi phí

**Hành động**: Phân tích tài nguyên để xác định các cơ hội tối ưu hóa
**Công cụ**: Phân tích cục bộ bằng dữ liệu đã thu thập
**Quy trình**:

1.  **Áp dụng các Mẫu Tối ưu hóa** dựa trên các loại tài nguyên được tìm thấy:

    **Tối ưu hóa Tính toán**:

    - App Service Plans: Điều chỉnh kích thước phù hợp dựa trên mức sử dụng CPU/bộ nhớ
    - Function Apps: Chuyển từ gói Premium → Consumption cho mức sử dụng thấp
    - Virtual Machines: Thu nhỏ các máy ảo có kích thước quá lớn

    **Tối ưu hóa Cơ sở dữ liệu**:

    - Cosmos DB:
      - Chuyển từ Provisioned → Serverless cho khối lượng công việc thay đổi
      - Điều chỉnh kích thước RU/s phù hợp dựa trên mức sử dụng thực tế
    - SQL Database: Điều chỉnh kích thước các bậc dịch vụ phù hợp dựa trên mức sử dụng DTU

    **Tối ưu hóa Lưu trữ**:

    - Triển khai các chính sách vòng đời (Hot → Cool → Archive)
    - Hợp nhất các tài khoản lưu trữ dư thừa
    - Điều chỉnh kích thước các bậc lưu trữ phù hợp dựa trên các mẫu truy cập

    **Tối ưu hóa Cơ sở hạ tầng**:

    - Loại bỏ các tài nguyên không sử dụng/dư thừa
    - Triển khai tự động thay đổi quy mô ở những nơi có lợi
    - Lên lịch cho các môi trường không phải sản xuất

2.  **Tính toán Tiết kiệm dựa trên Bằng chứng**:

    - Chi phí đã xác thực hiện tại → Chi phí mục tiêu = Tiết kiệm
    - Ghi lại nguồn giá cho cả cấu hình hiện tại và mục tiêu

3.  **Tính toán Điểm Ưu tiên** cho mỗi đề xuất:

    ```
    Điểm Ưu tiên = (Điểm Giá trị × Tiết kiệm Hàng tháng) / (Điểm Rủi ro × Số ngày Triển khai)

    Ưu tiên Cao: Điểm > 20
    Ưu tiên Trung bình: Điểm 5-20
    Ưu tiên Thấp: Điểm < 5
    ```

4.  **Xác thực các Đề xuất**:
    - Đảm bảo các lệnh Azure CLI là chính xác
    - Xác minh các tính toán tiết kiệm ước tính
    - Đánh giá các rủi ro và điều kiện tiên quyết khi triển khai
    - Đảm bảo tất cả các tính toán tiết kiệm đều có bằng chứng hỗ trợ

### Bước 5: Xác nhận từ Người dùng

**Hành động**: Trình bày tóm tắt và nhận sự chấp thuận trước khi tạo các issue trên GitHub
**Quy trình**:

1.  **Hiển thị Tóm tắt Tối ưu hóa**:

    ```
    🎯 Tóm tắt Tối ưu hóa Chi phí Azure

    📊 Kết quả Phân tích:
    • Tổng số Tài nguyên đã Phân tích: X
    • Chi phí Hàng tháng Hiện tại: $X
    • Tiết kiệm Hàng tháng Tiềm năng: $Y
    • Cơ hội Tối ưu hóa: Z
    • Các mục Ưu tiên Cao: N

    🏆 Đề xuất:
    1. [Tài nguyên]: [SKU hiện tại] → [SKU mục tiêu] = tiết kiệm $X/tháng - [Mức độ Rủi ro] | [Nỗ lực Triển khai]
    2. [Tài nguyên]: [Cấu hình hiện tại] → [Cấu hình mục tiêu] = tiết kiệm $Y/tháng - [Mức độ Rủi ro] | [Nỗ lực Triển khai]
    3. [Tài nguyên]: [Cấu hình hiện tại] → [Cấu hình mục tiêu] = tiết kiệm $Z/tháng - [Mức độ Rủi ro] | [Nỗ lực Triển khai]
    ... và tương tự

    💡 Thao tác này sẽ tạo ra:
    • Y issue riêng lẻ trên GitHub (một cho mỗi tối ưu hóa)
    • 1 EPIC issue để điều phối việc triển khai

    ❓ Tiếp tục tạo các issue trên GitHub? (y/n)
    ```

2.  **Chờ Xác nhận từ Người dùng**: Chỉ tiếp tục nếu người dùng xác nhận

### Bước 6: Tạo các Issue Tối ưu hóa Riêng lẻ

**Hành động**: Tạo các issue riêng biệt trên GitHub cho mỗi cơ hội tối ưu hóa. Gắn nhãn "cost-optimization" (màu xanh lá), "azure" (màu xanh dương).
**Công cụ MCP Bắt buộc**: `create_issue` cho mỗi đề xuất
**Quy trình**:

1.  **Tạo các Issue Riêng lẻ** bằng mẫu này:

    **Định dạng Tiêu đề**: `[COST-OPT] [Loại tài nguyên] - [Mô tả ngắn] - tiết kiệm $X/tháng`

    **Mẫu Nội dung**:

    ````markdown
    ## 💰 Tối ưu hóa Chi phí: [Tiêu đề ngắn]

    **Tiết kiệm Hàng tháng**: $X | **Mức độ Rủi ro**: [Thấp/Trung bình/Cao] | **Nỗ lực Triển khai**: X ngày

    ### 📋 Mô tả

    [Giải thích rõ ràng về việc tối ưu hóa và tại sao nó cần thiết]

    ### 🔧 Triển khai

    **Phát hiện tệp IaC**: [Có/Không - dựa trên kết quả file_search]

    ```bash
    # Nếu tìm thấy tệp IaC: Hiển thị các sửa đổi IaC + triển khai
    # Tệp: infrastructure/bicep/modules/app-service.bicep
    # Thay đổi: sku.name: 'S3' → 'B2'
    az deployment group create --resource-group [rg] --template-file infrastructure/bicep/main.bicep

    # Nếu không có tệp IaC: Lệnh Azure CLI trực tiếp + cảnh báo
    # ⚠️ Không tìm thấy tệp IaC. Nếu chúng tồn tại ở nơi khác, hãy sửa đổi chúng.
    az appservice plan update --name [plan] --sku B2
    ```
    ````

    ### 📊 Bằng chứng

    - Cấu hình Hiện tại: [chi tiết]
    - Mẫu Sử dụng: [bằng chứng từ dữ liệu giám sát]
    - Tác động Chi phí: $X/tháng → $Y/tháng
    - Tuân thủ Phương pháp Tốt nhất: [tham chiếu đến các phương pháp tốt nhất của Azure nếu có]

    ### ✅ Các bước Xác thực

    - [ ] Kiểm tra trong môi trường không phải sản xuất
    - [ ] Xác minh không có sự suy giảm hiệu suất
    - [ ] Xác nhận giảm chi phí trong Azure Cost Management
    - [ ] Cập nhật giám sát và cảnh báo nếu cần

    ### ⚠️ Rủi ro & Cân nhắc

    - [Rủi ro 1 và cách giảm thiểu]
    - [Rủi ro 2 và cách giảm thiểu]

    **Điểm Ưu tiên**: X | **Giá trị**: X/10 | **Rủi ro**: X/10

    ```

    ```

### Bước 7: Tạo EPIC Issue Điều phối

**Hành động**: Tạo issue chính để theo dõi tất cả công việc tối ưu hóa. Gắn nhãn "cost-optimization" (màu xanh lá), "azure" (màu xanh dương), và "epic" (màu tím).
**Công cụ MCP Bắt buộc**: `create_issue` cho EPIC
**Lưu ý về sơ đồ mermaid**: Đảm bảo bạn xác minh cú pháp mermaid là chính xác và tạo sơ đồ có tính đến các nguyên tắc về khả năng truy cập (kiểu dáng, màu sắc, v.v.).
**Quy trình**:

1.  **Tạo EPIC Issue**:

    **Tiêu đề**: `[EPIC] Sáng kiến Tối ưu hóa Chi phí Azure - tiềm năng tiết kiệm $X/tháng`

    **Mẫu Nội dung**:

    ````markdown
    # 🎯 EPIC Tối ưu hóa Chi phí Azure

    **Tổng Tiết kiệm Tiềm năng**: $X/tháng | **Thời gian Triển khai**: X tuần

    ## 📊 Tóm tắt cho Lãnh đạo

    - **Tài nguyên đã Phân tích**: X
    - **Cơ hội Tối ưu hóa**: Y
    - **Tổng Tiềm năng Tiết kiệm Hàng tháng**: $X
    - **Các mục Ưu tiên Cao**: N

    ## 🏗️ Tổng quan Kiến trúc Hiện tại

    ```mermaid
    graph TB
        subgraph "Resource Group: [tên]"
            [Sơ đồ kiến trúc được tạo ra cho thấy các tài nguyên và chi phí hiện tại]
        end
    ```
    ````

    ## 📋 Theo dõi Triển khai

    ### 🚀 Ưu tiên Cao (Triển khai trước)

    - [ ] #[số-issue]: [Tiêu đề] - tiết kiệm $X/tháng
    - [ ] #[số-issue]: [Tiêu đề] - tiết kiệm $X/tháng

    ### ⚡ Ưu tiên Trung bình

    - [ ] #[số-issue]: [Tiêu đề] - tiết kiệm $X/tháng
    - [ ] #[số-issue]: [Tiêu đề] - tiết kiệm $X/tháng

    ### 🔄 Ưu tiên Thấp (Có thì tốt)

    - [ ] #[số-issue]: [Tiêu đề] - tiết kiệm $X/tháng

    ## 📈 Theo dõi Tiến độ

    - **Đã hoàn thành**: 0 trên Y tối ưu hóa
    - **Tiết kiệm đã Thực hiện**: $0 trên $X/tháng
    - **Trạng thái Triển khai**: Chưa bắt đầu

    ## 🎯 Tiêu chí Thành công

    - [ ] Tất cả các tối ưu hóa ưu tiên cao đã được triển khai
    - [ ] > 80% số tiền tiết kiệm ước tính đã được thực hiện
    - [ ] Không quan sát thấy sự suy giảm hiệu suất
    - [ ] Bảng điều khiển giám sát chi phí đã được cập nhật

    ## 📝 Ghi chú

    - Xem xét và cập nhật EPIC này khi các issue được hoàn thành
    - Theo dõi số tiền tiết kiệm thực tế so với ước tính
    - Cân nhắc lên lịch đánh giá tối ưu hóa chi phí định kỳ

    ```

    ```

## Xử lý Lỗi

- **Xác thực Chi phí**: Nếu các ước tính tiết kiệm thiếu bằng chứng hỗ trợ hoặc có vẻ không nhất quán với giá của Azure, hãy xác minh lại các cấu hình và nguồn giá trước khi tiếp tục
- **Lỗi Xác thực Azure**: Cung cấp các bước thiết lập Azure CLI thủ công
- **Không tìm thấy Tài nguyên**: Tạo issue thông tin về việc triển khai tài nguyên Azure
- **Lỗi Tạo trên GitHub**: Xuất các đề xuất đã định dạng ra console
- **Không đủ Dữ liệu Sử dụng**: Ghi nhận các hạn chế và chỉ cung cấp các đề xuất dựa trên cấu hình

## Tiêu chí Thành công

- ✅ Tất cả các ước tính chi phí được xác minh dựa trên cấu hình tài nguyên thực tế và giá của Azure
- ✅ Các issue riêng lẻ được tạo cho mỗi tối ưu hóa (có thể theo dõi và giao việc)
- ✅ EPIC issue cung cấp sự điều phối và theo dõi toàn diện
- ✅ Tất cả các đề xuất bao gồm các lệnh Azure CLI cụ thể, có thể thực thi
- ✅ Việc chấm điểm ưu tiên cho phép triển khai tập trung vào ROI
- ✅ Sơ đồ kiến trúc thể hiện chính xác trạng thái hiện tại
- ✅ Xác nhận của người dùng ngăn chặn việc tạo
