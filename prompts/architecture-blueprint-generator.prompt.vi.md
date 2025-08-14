---
description: "Trình tạo sơ đồ kiến trúc dự án toàn diện, phân tích mã nguồn để tạo tài liệu kiến trúc chi tiết. Tự động phát hiện các chồng công nghệ và mẫu kiến trúc, tạo sơ đồ trực quan, ghi lại các mẫu triển khai và cung cấp các sơ đồ có khả năng mở rộng để duy trì tính nhất quán của kiến trúc và hướng dẫn phát triển mới."
---

# Trình tạo Sơ đồ Kiến trúc Dự án Toàn diện

## Biến Cấu hình

${PROJECT_TYPE="Tự động phát hiện|.NET|Java|React|Angular|Python|Node.js|Flutter|Khác"} <!-- Công nghệ chính -->
${ARCHITECTURE_PATTERN="Tự động phát hiện|Clean Architecture|Microservices|Layered|MVVM|MVC|Hexagonal|Event-Driven|Serverless|Monolithic|Khác"} <!-- Mẫu kiến trúc chính -->
${DIAGRAM_TYPE="C4|UML|Flow|Component|Không có"} <!-- Loại sơ đồ kiến trúc -->
${DETAIL_LEVEL="Cấp cao|Chi tiết|Toàn diện|Sẵn sàng triển khai"} <!-- Mức độ chi tiết cần bao gồm -->
${INCLUDES_CODE_EXAMPLES=true|false} <!-- Bao gồm mã nguồn mẫu để minh họa các mẫu -->
${INCLUDES_IMPLEMENTATION_PATTERNS=true|false} <!-- Bao gồm các mẫu triển khai chi tiết -->
${INCLUDES_DECISION_RECORDS=true|false} <!-- Bao gồm các bản ghi quyết định kiến trúc -->
${FOCUS_ON_EXTENSIBILITY=true|false} <!-- Nhấn mạnh vào các điểm và mẫu mở rộng -->

## Lời nhắc được Tạo ra

"Tạo một tài liệu 'Project_Architecture_Blueprint.md' toàn diện, phân tích kỹ lưỡng các mẫu kiến trúc trong mã nguồn để làm tài liệu tham khảo chính thức nhằm duy trì tính nhất quán của kiến trúc. Sử dụng cách tiếp cận sau:

### 1. Phát hiện và Phân tích Kiến trúc

- ${PROJECT_TYPE == "Tự động phát hiện" ? "Phân tích cấu trúc dự án để xác định tất cả các chồng công nghệ và framework đang được sử dụng bằng cách kiểm tra:
  - Các tệp dự án và cấu hình
  - Các gói phụ thuộc và câu lệnh import
  - Các mẫu và quy ước dành riêng cho framework
  - Các cấu hình xây dựng và triển khai" : "Tập trung vào các mẫu và thực tiễn cụ thể của ${PROJECT_TYPE}"}
- ${ARCHITECTURE_PATTERN == "Tự động phát hiện" ? "Xác định (các) mẫu kiến trúc bằng cách phân tích:
  - Tổ chức thư mục và không gian tên (namespacing)
  - Luồng phụ thuộc và ranh giới thành phần
  - Các mẫu phân tách giao diện và trừu tượng hóa
  - Các cơ chế giao tiếp giữa các thành phần" : "Ghi lại cách kiến trúc ${ARCHITECTURE_PATTERN} được triển khai"}

### 2. Tổng quan về Kiến trúc

- Cung cấp một lời giải thích rõ ràng, ngắn gọn về cách tiếp cận kiến trúc tổng thể
- Ghi lại các nguyên tắc chỉ đạo thể hiện trong các lựa chọn kiến trúc
- Xác định các ranh giới kiến trúc và cách chúng được thực thi
- Ghi chú bất kỳ mẫu kiến trúc lai hoặc các biến thể của các mẫu tiêu chuẩn

### 3. Trực quan hóa Kiến trúc

${DIAGRAM_TYPE != "Không có" ? `Tạo các sơ đồ ${DIAGRAM_TYPE} ở nhiều cấp độ trừu tượng:

- Tổng quan kiến trúc cấp cao cho thấy các hệ thống con chính
- Sơ đồ tương tác thành phần cho thấy các mối quan hệ và sự phụ thuộc
- Sơ đồ luồng dữ liệu cho thấy cách thông tin di chuyển qua hệ thống
- Đảm bảo các sơ đồ phản ánh chính xác việc triển khai thực tế, không phải là các mẫu lý thuyết` : "Mô tả các mối quan hệ thành phần dựa trên các phụ thuộc mã nguồn thực tế, cung cấp giải thích văn bản rõ ràng về:
- Tổ chức và ranh giới của hệ thống con
- Hướng phụ thuộc và tương tác thành phần
- Luồng dữ liệu và chuỗi quy trình"}

### 4. Các Thành phần Kiến trúc Cốt lõi

Đối với mỗi thành phần kiến trúc được phát hiện trong mã nguồn:

- **Mục đích và Trách nhiệm**:

  - Chức năng chính trong kiến trúc
  - Các lĩnh vực nghiệp vụ hoặc các vấn đề kỹ thuật được giải quyết
  - Ranh giới và giới hạn phạm vi

- **Cấu trúc Nội bộ**:

  - Tổ chức của các lớp/mô-đun trong thành phần
  - Các lớp trừu tượng chính và cách triển khai chúng
  - Các mẫu thiết kế được sử dụng

- **Các Mẫu Tương tác**:

  - Cách thành phần giao tiếp với các thành phần khác
  - Các giao diện được cung cấp và sử dụng
  - Các mẫu dependency injection
  - Các cơ chế xuất bản/đăng ký sự kiện

- **Các Mẫu Phát triển**:
  - Cách thành phần có thể được mở rộng
  - Các điểm biến thể và cơ chế plugin
  - Các cách tiếp cận cấu hình và tùy chỉnh

### 5. Các Lớp Kiến trúc và Sự phụ thuộc

- Sơ đồ hóa cấu trúc lớp như được triển khai trong mã nguồn
- Ghi lại các quy tắc phụ thuộc giữa các lớp
- Xác định các cơ chế trừu tượng hóa cho phép tách biệt các lớp
- Ghi chú bất kỳ sự phụ thuộc vòng tròn hoặc vi phạm lớp nào
- Ghi lại các mẫu dependency injection được sử dụng để duy trì sự tách biệt

### 6. Kiến trúc Dữ liệu

- Ghi lại cấu trúc và tổ chức của mô hình miền (domain model)
- Sơ đồ hóa các mối quan hệ thực thể và các mẫu tổng hợp
- Xác định các mẫu truy cập dữ liệu (repositories, data mappers, v.v.)
- Ghi lại các cách tiếp cận chuyển đổi và ánh xạ dữ liệu
- Ghi chú các chiến lược và triển khai bộ nhớ đệm (caching)
- Ghi lại các mẫu xác thực dữ liệu

### 7. Triển khai các Mối quan tâm Xuyên suốt (Cross-Cutting Concerns)

Ghi lại các mẫu triển khai cho các mối quan tâm xuyên suốt:

- **Xác thực & Phân quyền**:

  - Triển khai mô hình bảo mật
  - Các mẫu thực thi quyền
  - Cách tiếp cận quản lý danh tính
  - Các mẫu ranh giới bảo mật

- **Xử lý Lỗi & Khả năng Phục hồi**:

  - Các mẫu xử lý ngoại lệ
  - Các triển khai retry và circuit breaker
  - Các chiến lược dự phòng và suy giảm từ từ (graceful degradation)
  - Các cách tiếp cận báo cáo và giám sát lỗi

- **Ghi nhật ký & Giám sát**:

  - Các mẫu đo lường (instrumentation)
  - Triển khai khả năng quan sát (observability)
  - Luồng thông tin chẩn đoán
  - Cách tiếp cận giám sát hiệu suất

- **Xác thực (Validation)**:

  - Các chiến lược xác thực đầu vào
  - Triển khai xác thực quy tắc nghiệp vụ
  - Phân bổ trách nhiệm xác thực
  - Các mẫu báo cáo lỗi

- **Quản lý Cấu hình**:
  - Các mẫu nguồn cấu hình
  - Các chiến lược cấu hình theo môi trường
  - Cách tiếp cận quản lý bí mật (secret management)
  - Triển khai cờ tính năng (feature flag)

### 8. Các Mẫu Giao tiếp Dịch vụ

- Ghi lại các định nghĩa ranh giới dịch vụ
- Xác định các giao thức và định dạng giao tiếp
- Sơ đồ hóa các mẫu giao tiếp đồng bộ và bất đồng bộ
- Ghi lại các chiến lược quản lý phiên bản API
- Xác định các cơ chế khám phá dịch vụ (service discovery)
- Ghi chú các mẫu phục hồi trong giao tiếp dịch vụ

### 9. Các Mẫu Kiến trúc theo Công nghệ Cụ thể

${PROJECT_TYPE == "Tự động phát hiện" ? "Đối với mỗi chồng công nghệ được phát hiện, ghi lại các mẫu kiến trúc cụ thể:" : `Ghi lại các mẫu kiến trúc cụ thể của ${PROJECT_TYPE}:`}

${(PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Tự động phát hiện") ?
"#### Các Mẫu Kiến trúc .NET (nếu được phát hiện)

- Triển khai mô hình host và ứng dụng
- Tổ chức pipeline middleware
- Các mẫu tích hợp dịch vụ framework
- Các cách tiếp cận ORM và truy cập dữ liệu
- Các mẫu triển khai API (controllers, minimal APIs, v.v.)
- Cấu hình container dependency injection" : ""}

${(PROJECT_TYPE == "Java" || PROJECT_TYPE == "Tự động phát hiện") ?
"#### Các Mẫu Kiến trúc Java (nếu được phát hiện)

- Container ứng dụng và quy trình khởi động (bootstrap)
- Sử dụng framework dependency injection (Spring, CDI, v.v.)
- Các mẫu triển khai AOP
- Quản lý ranh giới giao dịch (transaction)
- Cấu hình và sử dụng ORM
- Các mẫu triển khai dịch vụ" : ""}

${(PROJECT_TYPE == "React" || PROJECT_TYPE == "Tự động phát hiện") ?
"#### Các Mẫu Kiến trúc React (nếu được phát hiện)

- Các chiến lược kết hợp và tái sử dụng component
- Kiến trúc quản lý trạng thái (state management)
- Các mẫu xử lý tác vụ phụ (side effect)
- Cách tiếp cận định tuyến và điều hướng (routing)
- Các mẫu tìm nạp và lưu trữ dữ liệu vào bộ nhớ đệm
- Các chiến lược tối ưu hóa hiển thị (rendering)" : ""}

${(PROJECT_TYPE == "Angular" || PROJECT_TYPE == "Tự động phát hiện") ?
"#### Các Mẫu Kiến trúc Angular (nếu được phát hiện)

- Chiến lược tổ chức module
- Thiết kế hệ thống phân cấp component
- Các mẫu dịch vụ và dependency injection
- Cách tiếp cận quản lý trạng thái
- Các mẫu lập trình phản ứng (reactive programming)
- Triển khai Route guard" : ""}

${(PROJECT_TYPE == "Python" || PROJECT_TYPE == "Tự động phát hiện") ?
"#### Các Mẫu Kiến trúc Python (nếu được phát hiện)

- Cách tiếp cận tổ chức module
- Chiến lược quản lý phụ thuộc
- Các mẫu triển khai OOP so với lập trình hàm
- Các mẫu tích hợp framework
- Cách tiếp cận lập trình bất đồng bộ" : ""}

### 10. Các Mẫu Triển khai

${INCLUDES_IMPLEMENTATION_PATTERNS ?
"Ghi lại các mẫu triển khai cụ thể cho các thành phần kiến trúc chính:

- **Các Mẫu Thiết kế Giao diện (Interface)**:

  - Các cách tiếp cận phân tách giao diện
  - Các quyết định về mức độ trừu tượng
  - Các mẫu giao diện chung so với cụ thể
  - Các mẫu triển khai mặc định

- **Các Mẫu Triển khai Dịch vụ**:

  - Quản lý vòng đời dịch vụ
  - Các mẫu kết hợp dịch vụ
  - Các mẫu triển khai hoạt động
  - Xử lý lỗi trong dịch vụ

- **Các Mẫu Triển khai Repository**:

  - Các triển khai mẫu truy vấn
  - Quản lý giao dịch
  - Xử lý đồng thời (concurrency)
  - Các mẫu hoạt động hàng loạt (bulk operation)

- **Các Mẫu Triển khai Controller/API**:

  - Các mẫu xử lý yêu cầu (request)
  - Các cách tiếp cận định dạng phản hồi (response)
  - Xác thực tham số
  - Triển khai quản lý phiên bản API

- **Triển khai Mô hình Miền (Domain Model)**:
  - Các mẫu triển khai thực thể (entity)
  - Các mẫu đối tượng giá trị (value object)
  - Triển khai sự kiện miền (domain event)
  - Thực thi quy tắc nghiệp vụ" : "Đề cập rằng các mẫu triển khai chi tiết thay đổi trên toàn bộ mã nguồn."}

### 11. Kiến trúc Kiểm thử (Testing)

- Ghi lại các chiến lược kiểm thử phù hợp với kiến trúc
- Xác định các mẫu ranh giới kiểm thử (đơn vị, tích hợp, hệ thống)
- Sơ đồ hóa các cách tiếp cận test double và mocking
- Ghi lại các chiến lược dữ liệu kiểm thử
- Ghi chú việc tích hợp các công cụ và framework kiểm thử

### 12. Kiến trúc Triển khai (Deployment)

- Ghi lại cấu trúc liên kết triển khai (deployment topology) được suy ra từ cấu hình
- Xác định các điều chỉnh kiến trúc theo từng môi trường
- Sơ đồ hóa các mẫu giải quyết phụ thuộc lúc chạy (runtime)
- Ghi lại việc quản lý cấu hình qua các môi trường
- Xác định các cách tiếp cận container hóa và điều phối (orchestration)
- Ghi chú các mẫu tích hợp dịch vụ đám mây

### 13. Các Mẫu Mở rộng và Phát triển

${FOCUS_ON_EXTENSIBILITY ?
"Cung cấp hướng dẫn chi tiết để mở rộng kiến trúc:

- **Các Mẫu Thêm Tính năng**:

  - Cách thêm tính năng mới mà vẫn giữ được tính toàn vẹn của kiến trúc
  - Nơi đặt các thành phần mới theo loại
  - Hướng dẫn giới thiệu phụ thuộc
  - Các mẫu mở rộng cấu hình

- **Các Mẫu Sửa đổi**:

  - Cách sửa đổi các thành phần hiện có một cách an toàn
  - Các chiến lược để duy trì khả năng tương thích ngược
  - Các mẫu ngừng sử dụng (deprecation)
  - Các cách tiếp cận di chuyển (migration)

- **Các Mẫu Tích hợp**:
  - Cách tích hợp các hệ thống bên ngoài mới
  - Các mẫu triển khai Adapter
  - Các mẫu lớp chống tham nhũng (Anti-corruption layer)
  - Triển khai Service facade" : "Ghi lại các điểm mở rộng chính trong kiến trúc."}

${INCLUDES_CODE_EXAMPLES ?
"### 14. Ví dụ về Mẫu Kiến trúc
Trích xuất các ví dụ mã nguồn tiêu biểu minh họa các mẫu kiến trúc chính:

- **Ví dụ về Tách biệt Lớp**:

  - Tách biệt định nghĩa và triển khai giao diện
  - Các mẫu giao tiếp giữa các lớp
  - Ví dụ về dependency injection

- **Ví dụ về Giao tiếp Thành phần**:

  - Các mẫu gọi dịch vụ
  - Xuất bản và xử lý sự kiện
  - Triển khai truyền thông điệp (message passing)

- **Ví dụ về Điểm Mở rộng**:
  - Đăng ký và khám phá plugin
  - Các triển khai giao diện mở rộng
  - Các mẫu mở rộng dựa trên cấu hình

Bao gồm đủ ngữ cảnh với mỗi ví dụ để thể hiện rõ mẫu, nhưng giữ cho các ví dụ ngắn gọn và tập trung vào các khái niệm kiến trúc." : ""}

${INCLUDES_DECISION_RECORDS ?
"### 15. Các Bản ghi Quyết định Kiến trúc
Ghi lại các quyết định kiến trúc quan trọng thể hiện trong mã nguồn:

- **Quyết định về Phong cách Kiến trúc**:

  - Tại sao mẫu kiến trúc hiện tại được chọn
  - Các phương án thay thế đã được xem xét (dựa trên sự phát triển của mã nguồn)
  - Các ràng buộc đã ảnh hưởng đến quyết định

- **Quyết định về Lựa chọn Công nghệ**:

  - Các lựa chọn công nghệ chính và tác động của chúng đến kiến trúc
  - Lý do lựa chọn framework
  - Quyết định sử dụng thành phần tùy chỉnh so với có sẵn

- **Quyết định về Cách tiếp cận Triển khai**:
  - Các mẫu triển khai cụ thể đã được chọn
  - Các biến thể của mẫu tiêu chuẩn
  - Sự đánh đổi giữa hiệu suất và khả năng bảo trì

Đối với mỗi quyết định, ghi chú:

- Bối cảnh khiến quyết định trở nên cần thiết
- Các yếu tố được xem xét khi đưa ra quyết định
- Hậu quả (tích cực và tiêu cực)
- Sự linh hoạt hoặc các hạn chế trong tương lai được tạo ra" : ""}

### ${INCLUDES_DECISION_RECORDS ? "16" : INCLUDES_CODE_EXAMPLES ? "15" : "14"}. Quản trị Kiến trúc

- Ghi lại cách duy trì tính nhất quán của kiến trúc
- Xác định các kiểm tra tự động để tuân thủ kiến trúc
- Ghi chú các quy trình đánh giá kiến trúc thể hiện trong mã nguồn
- Ghi lại các thực tiễn về tài liệu kiến trúc

### ${INCLUDES_DECISION_RECORDS ? "17" : INCLUDES_CODE_EXAMPLES ? "16" : "15"}. Sơ đồ cho Phát triển Mới

Tạo một hướng dẫn kiến trúc rõ ràng để triển khai các tính năng mới:

- **Quy trình Phát triển**:

  - Điểm bắt đầu cho các loại tính năng khác nhau
  - Trình tự tạo thành phần
  - Các bước tích hợp với kiến trúc hiện có
  - Cách tiếp cận kiểm thử theo lớp kiến trúc

- **Các Mẫu Triển khai (Templates)**:

  - Các mẫu lớp/giao diện cơ sở cho các thành phần kiến trúc chính
  - Tổ chức tệp tiêu chuẩn cho các thành phần mới
  - Các mẫu khai báo phụ thuộc
  - Yêu cầu về tài liệu

- **Những Cạm bẫy Thường gặp**:
  - Các vi phạm kiến trúc cần tránh
  - Các lỗi kiến trúc phổ biến
  - Các cân nhắc về hiệu suất
  - Các điểm mù trong kiểm thử

Bao gồm thông tin về thời điểm sơ đồ này được tạo và các khuyến nghị để giữ cho nó được cập nhật khi kiến trúc phát triển."
