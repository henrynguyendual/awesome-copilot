---
description: "Trình tạo bản thiết kế kiến trúc dự án toàn diện, phân tích mã nguồn để tạo tài liệu kiến trúc chi tiết. Tự động phát hiện công nghệ và mẫu kiến trúc, tạo sơ đồ trực quan, ghi lại các mẫu triển khai, và cung cấp bản thiết kế mở rộng để duy trì tính nhất quán kiến trúc và hướng dẫn phát triển mới."
---

# Trình Tạo Bản Thiết Kế Kiến Trúc Dự Án Toàn Diện

## Biến cấu hình

${PROJECT_TYPE="Tự động phát hiện|.NET|Java|React|Angular|Python|Node.js|Flutter|Khác"} <!-- Công nghệ chính -->
${ARCHITECTURE_PATTERN="Tự động phát hiện|Clean Architecture|Microservices|Layered|MVVM|MVC|Hexagonal|Event-Driven|Serverless|Monolithic|Khác"} <!-- Mẫu kiến trúc chính -->
${DIAGRAM_TYPE="C4|UML|Flow|Component|Không"} <!-- Loại sơ đồ kiến trúc -->
${DETAIL_LEVEL="Tổng quan|Chi tiết|Toàn diện|Sẵn sàng triển khai"} <!-- Mức độ chi tiết -->
${INCLUDES_CODE_EXAMPLES=true|false} <!-- Bao gồm ví dụ mã minh họa mẫu -->
${INCLUDES_IMPLEMENTATION_PATTERNS=true|false} <!-- Bao gồm mẫu triển khai chi tiết -->
${INCLUDES_DECISION_RECORDS=true|false} <!-- Bao gồm ghi nhận quyết định kiến trúc -->
${FOCUS_ON_EXTENSIBILITY=true|false} <!-- Nhấn mạnh điểm mở rộng và mẫu mở rộng -->

## Prompt Được Tạo

"Tạo tài liệu 'Project_Architecture_Blueprint.md' toàn diện, phân tích kỹ các mẫu kiến trúc trong mã nguồn để làm tài liệu tham khảo duy trì tính nhất quán kiến trúc. Sử dụng cách tiếp cận sau:

### 1. Phát hiện và phân tích kiến trúc

- ${PROJECT_TYPE == "Tự động phát hiện" ? "Phân tích cấu trúc dự án để xác định tất cả công nghệ và framework sử dụng bằng cách kiểm tra:
  - File dự án và cấu hình
  - Phụ thuộc gói và câu lệnh import
  - Mẫu và quy ước đặc thù framework
  - Cấu hình build và triển khai" : "Tập trung vào mẫu và thực hành đặc thù ${PROJECT_TYPE}"}
- ${ARCHITECTURE_PATTERN == "Tự động phát hiện" ? "Xác định mẫu kiến trúc bằng cách phân tích:
  - Tổ chức thư mục và đặt tên không gian
  - Luồng phụ thuộc và ranh giới thành phần
  - Mẫu phân tách interface và trừu tượng hóa
  - Cơ chế giao tiếp giữa các thành phần" : "Ghi lại cách triển khai kiến trúc ${ARCHITECTURE_PATTERN}"}

### 2. Tổng quan kiến trúc

- Giải thích rõ ràng, ngắn gọn về cách tiếp cận kiến trúc tổng thể
- Ghi lại nguyên tắc định hướng trong lựa chọn kiến trúc
- Xác định ranh giới kiến trúc và cách thực thi
- Lưu ý các mẫu kiến trúc lai hoặc biến thể của mẫu chuẩn

### 3. Trực quan hóa kiến trúc

${DIAGRAM_TYPE != "Không" ? `Tạo sơ đồ ${DIAGRAM_TYPE} ở nhiều mức trừu tượng:

- Sơ đồ tổng quan kiến trúc cấp cao thể hiện các phân hệ chính
- Sơ đồ tương tác thành phần thể hiện quan hệ và phụ thuộc
- Sơ đồ luồng dữ liệu thể hiện cách thông tin di chuyển trong hệ thống
- Đảm bảo sơ đồ phản ánh đúng triển khai thực tế, không phải lý thuyết` : "Mô tả quan hệ thành phần dựa trên phụ thuộc mã thực tế, cung cấp giải thích rõ ràng về:
- Tổ chức và ranh giới phân hệ
- Hướng phụ thuộc và tương tác thành phần
- Luồng dữ liệu và trình tự xử lý"}

### 4. Thành phần kiến trúc cốt lõi

Với mỗi thành phần kiến trúc phát hiện trong mã nguồn:

- **Mục đích và trách nhiệm**:

  - Chức năng chính trong kiến trúc
  - Miền nghiệp vụ hoặc kỹ thuật giải quyết
  - Ranh giới và giới hạn phạm vi

- **Cấu trúc bên trong**:

  - Tổ chức lớp/module trong thành phần
  - Trừu tượng hóa chính và cách triển khai
  - Mẫu thiết kế sử dụng

- **Mẫu tương tác**:

  - Cách thành phần giao tiếp với thành phần khác
  - Interface cung cấp và sử dụng
  - Mẫu tiêm phụ thuộc
  - Cơ chế xuất bản/đăng ký sự kiện

- **Mẫu tiến hóa**:
  - Cách mở rộng thành phần
  - Điểm biến thể và cơ chế plugin
  - Cách cấu hình và tùy biến

### 5. Các lớp kiến trúc và phụ thuộc

- Sơ đồ cấu trúc lớp như triển khai trong mã nguồn
- Ghi lại quy tắc phụ thuộc giữa các lớp
- Xác định cơ chế trừu tượng hóa giúp phân tách lớp
- Lưu ý phụ thuộc vòng hoặc vi phạm lớp
- Ghi lại mẫu tiêm phụ thuộc duy trì phân tách

### 6. Kiến trúc dữ liệu

- Ghi lại cấu trúc và tổ chức mô hình miền
- Sơ đồ quan hệ thực thể và mẫu tổng hợp
- Xác định mẫu truy cập dữ liệu (repository, data mapper, ...)
- Ghi lại cách chuyển đổi và ánh xạ dữ liệu
- Lưu ý chiến lược và triển khai cache
- Ghi lại mẫu kiểm tra dữ liệu

### 7. Triển khai các mối quan tâm xuyên suốt

Ghi lại mẫu triển khai cho các mối quan tâm xuyên suốt:

- **Xác thực & Phân quyền**:

  - Triển khai mô hình bảo mật
  - Mẫu thực thi quyền truy cập
  - Cách quản lý danh tính
  - Mẫu ranh giới bảo mật

- **Xử lý lỗi & Độ bền**:

  - Mẫu xử lý ngoại lệ
  - Triển khai retry và circuit breaker
  - Chiến lược dự phòng và suy giảm nhẹ nhàng
  - Cách báo cáo lỗi và giám sát

- **Ghi log & Giám sát**:

  - Mẫu đo lường
  - Triển khai khả năng quan sát
  - Luồng thông tin chẩn đoán
  - Cách giám sát hiệu năng

- **Kiểm tra hợp lệ**:

  - Chiến lược kiểm tra đầu vào
  - Triển khai kiểm tra quy tắc nghiệp vụ
  - Phân phối trách nhiệm kiểm tra
  - Mẫu báo lỗi

- **Quản lý cấu hình**:
  - Mẫu nguồn cấu hình
  - Chiến lược cấu hình theo môi trường
  - Cách quản lý bí mật
  - Triển khai feature flag

### 8. Mẫu giao tiếp dịch vụ

- Ghi lại định nghĩa ranh giới dịch vụ
- Xác định giao thức và định dạng giao tiếp
- Sơ đồ giao tiếp đồng bộ và bất đồng bộ
- Ghi lại chiến lược version API
- Xác định cơ chế phát hiện dịch vụ
- Lưu ý mẫu độ bền trong giao tiếp dịch vụ

### 9. Mẫu kiến trúc đặc thù công nghệ

${PROJECT_TYPE == "Tự động phát hiện" ? "Với mỗi công nghệ phát hiện, ghi lại mẫu kiến trúc đặc thù:" : `Ghi lại mẫu kiến trúc đặc thù ${PROJECT_TYPE}:`}

${(PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Tự động phát hiện") ?
"#### Mẫu kiến trúc .NET (nếu phát hiện)

- Triển khai mô hình host và ứng dụng
- Tổ chức pipeline middleware
- Mẫu tích hợp dịch vụ framework
- Cách truy cập dữ liệu ORM
- Mẫu triển khai API (controller, minimal API, ...)
- Cấu hình container tiêm phụ thuộc" : ""}

${(PROJECT_TYPE == "Java" || PROJECT_TYPE == "Tự động phát hiện") ?
"#### Mẫu kiến trúc Java (nếu phát hiện)

- Triển khai container ứng dụng và quá trình bootstrap
- Sử dụng framework tiêm phụ thuộc (Spring, CDI, ...)
- Mẫu triển khai AOP
- Quản lý ranh giới transaction
- Cấu hình và sử dụng ORM
- Mẫu triển khai dịch vụ" : ""}

${(PROJECT_TYPE == "React" || PROJECT_TYPE == "Tự động phát hiện") ?
"#### Mẫu kiến trúc React (nếu phát hiện)

- Chiến lược tổ hợp và tái sử dụng component
- Kiến trúc quản lý trạng thái
- Mẫu xử lý side effect
- Cách routing và điều hướng
- Mẫu lấy dữ liệu và cache
- Chiến lược tối ưu hóa render" : ""}

${(PROJECT_TYPE == "Angular" || PROJECT_TYPE == "Tự động phát hiện") ?
"#### Mẫu kiến trúc Angular (nếu phát hiện)

- Chiến lược tổ chức module
- Thiết kế phân cấp component
- Mẫu dịch vụ và tiêm phụ thuộc
- Cách quản lý trạng thái
- Mẫu lập trình reactive
- Triển khai route guard" : ""}

${(PROJECT_TYPE == "Python" || PROJECT_TYPE == "Tự động phát hiện") ?
"#### Mẫu kiến trúc Python (nếu phát hiện)

- Cách tổ chức module
- Chiến lược quản lý phụ thuộc
- Mẫu triển khai OOP vs hàm
- Mẫu tích hợp framework
- Cách lập trình bất đồng bộ" : ""}

### 10. Mẫu triển khai

${INCLUDES_IMPLEMENTATION_PATTERNS ?
"Ghi lại mẫu triển khai cụ thể cho thành phần kiến trúc chính:

- **Mẫu thiết kế interface**:

  - Cách phân tách interface
  - Quyết định mức độ trừu tượng
  - Mẫu interface tổng quát vs đặc thù
  - Mẫu triển khai mặc định

- **Mẫu triển khai dịch vụ**:

  - Quản lý vòng đời dịch vụ
  - Mẫu tổ hợp dịch vụ
  - Template triển khai thao tác
  - Xử lý lỗi trong dịch vụ

- **Mẫu triển khai repository**:

  - Triển khai mẫu truy vấn
  - Quản lý transaction
  - Xử lý đồng thời
  - Mẫu thao tác hàng loạt

- **Mẫu triển khai Controller/API**:

  - Mẫu xử lý request
  - Cách định dạng response
  - Kiểm tra tham số
  - Triển khai version API

- **Triển khai mô hình miền**:
  - Mẫu triển khai entity
  - Mẫu value object
  - Triển khai domain event
  - Thực thi quy tắc nghiệp vụ" : "Nêu rằng mẫu triển khai chi tiết thay đổi tùy mã nguồn."}

### 11. Kiến trúc kiểm thử

- Ghi lại chiến lược kiểm thử phù hợp kiến trúc
- Xác định mẫu ranh giới kiểm thử (unit, integration, system)
- Sơ đồ test double và cách mock
- Ghi lại chiến lược dữ liệu kiểm thử
- Lưu ý tích hợp công cụ và framework kiểm thử

### 12. Kiến trúc triển khai

- Ghi lại topology triển khai từ cấu hình
- Xác định thích ứng kiến trúc theo môi trường
- Sơ đồ giải quyết phụ thuộc runtime
- Ghi lại quản lý cấu hình theo môi trường
- Xác định cách container hóa và điều phối
- Lưu ý mẫu tích hợp dịch vụ cloud

### 13. Mẫu mở rộng và tiến hóa

${FOCUS_ON_EXTENSIBILITY ?
"Cung cấp hướng dẫn chi tiết mở rộng kiến trúc:

- **Mẫu thêm tính năng**:

  - Cách thêm tính năng mới mà vẫn giữ nguyên kiến trúc
  - Vị trí đặt thành phần mới theo loại
  - Hướng dẫn thêm phụ thuộc
  - Mẫu mở rộng cấu hình

- **Mẫu sửa đổi**:

  - Cách sửa thành phần hiện có an toàn
  - Chiến lược duy trì tương thích ngược
  - Mẫu loại bỏ dần
  - Cách di chuyển/migrate

- **Mẫu tích hợp**:
  - Cách tích hợp hệ thống ngoài mới
  - Mẫu adapter
  - Mẫu anti-corruption layer
  - Triển khai service facade" : "Ghi lại điểm mở rộng chính trong kiến trúc."}

${INCLUDES_CODE_EXAMPLES ?
"### 14. Ví dụ mẫu kiến trúc
Trích xuất ví dụ mã minh họa mẫu kiến trúc chính:

- **Ví dụ phân tách lớp**:

  - Phân tách định nghĩa và triển khai interface
  - Mẫu giao tiếp giữa lớp
  - Ví dụ tiêm phụ thuộc

- **Ví dụ giao tiếp thành phần**:

  - Mẫu gọi dịch vụ
  - Xuất bản và xử lý sự kiện
  - Triển khai truyền thông điệp

- **Ví dụ điểm mở rộng**:
  - Đăng ký và phát hiện plugin
  - Triển khai interface mở rộng
  - Mẫu mở rộng dựa trên cấu hình

Bao gồm đủ ngữ cảnh để minh họa rõ mẫu, nhưng giữ ví dụ ngắn gọn, tập trung vào khái niệm kiến trúc." : ""}

${INCLUDES_DECISION_RECORDS ?
"### 15. Ghi nhận quyết định kiến trúc
Ghi lại quyết định kiến trúc chính thể hiện trong mã nguồn:

- **Quyết định kiểu kiến trúc**:

  - Lý do chọn mẫu kiến trúc hiện tại
  - Các lựa chọn thay thế (dựa trên tiến hóa mã)
  - Ràng buộc ảnh hưởng quyết định

- **Quyết định chọn công nghệ**:

  - Lựa chọn công nghệ chính và ảnh hưởng kiến trúc
  - Lý do chọn framework
  - Quyết định dùng thành phần tự phát triển hay có sẵn

- **Quyết định cách triển khai**:
  - Mẫu triển khai cụ thể được chọn
  - Biến thể mẫu chuẩn
  - Cân nhắc hiệu năng vs khả năng bảo trì

Với mỗi quyết định, ghi lại:

- Bối cảnh dẫn đến quyết định
- Yếu tố cân nhắc khi quyết định
- Hệ quả (tích cực và tiêu cực)
- Tính linh hoạt hoặc hạn chế trong tương lai" : ""}

### ${INCLUDES_DECISION_RECORDS ? "16" : INCLUDES_CODE_EXAMPLES ? "15" : "14"}. Quản trị kiến trúc

- Ghi lại cách duy trì tính nhất quán kiến trúc
- Xác định kiểm tra tự động tuân thủ kiến trúc
- Lưu ý quy trình review kiến trúc thể hiện trong mã nguồn
- Ghi lại thực hành tài liệu kiến trúc

### ${INCLUDES_DECISION_RECORDS ? "17" : INCLUDES_CODE_EXAMPLES ? "16" : "15"}. Bản thiết kế cho phát triển mới

Tạo hướng dẫn kiến trúc rõ ràng cho việc triển khai tính năng mới:

- **Quy trình phát triển**:

  - Điểm bắt đầu cho từng loại tính năng
  - Trình tự tạo thành phần
  - Bước tích hợp với kiến trúc hiện có
  - Cách kiểm thử theo lớp kiến trúc

- **Template triển khai**:

  - Template lớp/interface cơ sở cho thành phần kiến trúc chính
  - Tổ chức file chuẩn cho thành phần mới
  - Mẫu khai báo phụ thuộc
  - Yêu cầu tài liệu hóa

- **Lỗi thường gặp**:
  - Vi phạm kiến trúc cần tránh
  - Sai lầm kiến trúc phổ biến
  - Lưu ý hiệu năng
  - Lỗ hổng kiểm thử

Bao gồm thông tin về thời điểm tạo bản thiết kế này và khuyến nghị cập nhật khi kiến
