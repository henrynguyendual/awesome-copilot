---
description: "Trình tạo prompt không phụ thuộc vào công nghệ, giúp tạo ra các prompt AI có thể tùy chỉnh để quét codebase và xác định các mẫu mã chất lượng cao. Hỗ trợ nhiều ngôn ngữ lập trình (.NET, Java, JavaScript, TypeScript, React, Angular, Python) với độ sâu phân tích, phương pháp phân loại và định dạng tài liệu có thể cấu hình để thiết lập các tiêu chuẩn mã hóa và duy trì tính nhất quán trong các nhóm phát triển."
---

# Trình tạo Bản thiết kế Mẫu mã (Code Exemplars)

## Biến Cấu hình

${PROJECT_TYPE="Tự động phát hiện|.NET|Java|JavaScript|TypeScript|React|Angular|Python|Khác"} <!-- Công nghệ chính -->
${SCAN_DEPTH="Cơ bản|Tiêu chuẩn|Toàn diện"} <!-- Mức độ phân tích codebase -->
${INCLUDE_CODE_SNIPPETS=true|false} <!-- Bao gồm các đoạn mã thực tế ngoài các tham chiếu tệp -->
${CATEGORIZATION="Loại Mẫu|Lớp Kiến trúc|Loại Tệp"} <!-- Cách tổ chức các mẫu mã -->
${MAX_EXAMPLES_PER_CATEGORY=3} <!-- Số lượng ví dụ tối đa cho mỗi danh mục -->
${INCLUDE_COMMENTS=true|false} <!-- Bao gồm nhận xét giải thích cho mỗi mẫu mã -->

## Prompt Được tạo

"Quét codebase này và tạo một tệp exemplars.md xác định các ví dụ mã chất lượng cao, mang tính đại diện. Các mẫu mã này phải thể hiện các tiêu chuẩn và mẫu mã hóa của chúng tôi để giúp duy trì tính nhất quán. Sử dụng phương pháp sau:

### 1. Giai đoạn Phân tích Codebase

- ${PROJECT_TYPE == "Tự động phát hiện" ? "Tự động phát hiện các ngôn ngữ lập trình và framework chính bằng cách quét phần mở rộng của tệp và các tệp cấu hình" : `Tập trung vào các tệp mã ${PROJECT_TYPE}`}
- Xác định các tệp có chất lượng triển khai cao, tài liệu tốt và cấu trúc rõ ràng
- Tìm kiếm các mẫu thường được sử dụng, các thành phần kiến trúc và các triển khai có cấu trúc tốt
- Ưu tiên các tệp thể hiện các phương pháp hay nhất cho ngăn xếp công nghệ của chúng tôi
- Chỉ tham chiếu đến các tệp thực tế tồn tại trong codebase - không có ví dụ giả định

### 2. Tiêu chí Xác định Mẫu mã

- Mã có cấu trúc tốt, dễ đọc với quy ước đặt tên rõ ràng
- Nhận xét và tài liệu toàn diện
- Xử lý lỗi và xác thực đúng cách
- Tuân thủ các mẫu thiết kế và nguyên tắc kiến trúc
- Tách biệt các mối quan tâm và nguyên tắc trách nhiệm đơn lẻ
- Triển khai hiệu quả không có "code smells" (mã có mùi)
- Đại diện cho các phương pháp tiếp cận tiêu chuẩn của chúng tôi

### 3. Các Danh mục Mẫu Cốt lõi

${PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Tự động phát hiện" ? `#### Mẫu mã .NET (nếu được phát hiện)

- **Mô hình Miền (Domain Models)**: Tìm các thực thể triển khai đúng cách tính đóng gói và logic miền
- **Triển khai Repository**: Ví dụ về cách tiếp cận truy cập dữ liệu của chúng tôi
- **Thành phần Lớp Dịch vụ (Service Layer)**: Các triển khai logic nghiệp vụ có cấu trúc tốt
- **Mẫu Controller**: Các API controller sạch với xác thực và phản hồi phù hợp
- **Sử dụng Dependency Injection**: Các ví dụ tốt về cấu hình và sử dụng DI
- **Thành phần Middleware**: Các triển khai middleware tùy chỉnh
- **Mẫu Unit Test**: Các bài kiểm thử có cấu trúc tốt với sự sắp xếp và xác nhận phù hợp` : ""}

${(PROJECT_TYPE == "JavaScript" || PROJECT_TYPE == "TypeScript" || PROJECT_TYPE == "React" || PROJECT_TYPE == "Angular" || PROJECT_TYPE == "Tự động phát hiện") ? `#### Mẫu mã Frontend (nếu được phát hiện)

- **Cấu trúc Component**: Các component sạch, có cấu trúc tốt
- **Quản lý Trạng thái (State Management)**: Các ví dụ tốt về xử lý trạng thái
- **Tích hợp API**: Các lệnh gọi dịch vụ và xử lý dữ liệu được triển khai tốt
- **Xử lý Form**: Các mẫu xác thực và gửi
- **Triển khai Routing**: Cấu hình điều hướng và định tuyến
- **Thành phần UI**: Các yếu tố UI có thể tái sử dụng, có cấu trúc tốt
- **Ví dụ Unit Test**: Các bài kiểm thử component và dịch vụ` : ""}

${PROJECT_TYPE == "Java" || PROJECT_TYPE == "Tự động phát hiện" ? `#### Mẫu mã Java (nếu được phát hiện)

- **Lớp Thực thể (Entity Classes)**: Các thực thể JPA hoặc mô hình miền được thiết kế tốt
- **Triển khai Dịch vụ (Service Implementations)**: Các thành phần lớp dịch vụ sạch
- **Mẫu Repository**: Các triển khai truy cập dữ liệu
- **Lớp Controller/Resource**: Các triển khai điểm cuối API
- **Lớp Cấu hình (Configuration Classes)**: Cấu hình ứng dụng
- **Unit Tests**: Các bài kiểm thử JUnit có cấu trúc tốt` : ""}

${PROJECT_TYPE == "Python" || PROJECT_TYPE == "Tự động phát hiện" ? `#### Mẫu mã Python (nếu được phát hiện)

- **Định nghĩa Lớp (Class Definitions)**: Các lớp có cấu trúc tốt với tài liệu phù hợp
- **API Routes/Views**: Các triển khai API sạch
- **Mô hình Dữ liệu (Data Models)**: Các định nghĩa mô hình ORM
- **Hàm Dịch vụ (Service Functions)**: Các triển khai logic nghiệp vụ
- **Mô-đun Tiện ích (Utility Modules)**: Các hàm trợ giúp và tiện ích
- **Trường hợp Kiểm thử (Test Cases)**: Các bài kiểm thử đơn vị có cấu trúc tốt` : ""}

### 4. Mẫu mã theo Lớp Kiến trúc

- **Lớp Trình bày (Presentation Layer)**:
  - Các thành phần giao diện người dùng
  - Các điểm cuối Controllers/API
  - Các View models/DTOs
- **Lớp Logic Nghiệp vụ (Business Logic Layer)**:
  - Các triển khai dịch vụ
  - Các thành phần logic nghiệp vụ
  - Điều phối quy trình công việc
- **Lớp Truy cập Dữ liệu (Data Access Layer)**:
  - Các triển khai repository
  - Các mô hình dữ liệu
  - Các mẫu truy vấn
- **Các Mối quan tâm Xuyên suốt (Cross-Cutting Concerns)**:
  - Các triển khai ghi log
  - Xử lý lỗi
  - Xác thực/ủy quyền
  - Xác thực

### 5. Định dạng Tài liệu Mẫu mã

Đối với mỗi mẫu mã được xác định, hãy ghi lại:

- Đường dẫn tệp (tương đối so với thư mục gốc của repository)
- Mô tả ngắn gọn về điều gì làm cho nó trở thành mẫu mực
- Loại mẫu hoặc thành phần mà nó đại diện
  ${INCLUDE_COMMENTS ? "- Các chi tiết triển khai chính và các nguyên tắc mã hóa được thể hiện" : ""}
${INCLUDE_CODE_SNIPPETS ? "- Một đoạn mã nhỏ, đại diện (nếu có)" : ""}

${SCAN_DEPTH == "Toàn diện" ? `### 6. Tài liệu Bổ sung

- **Các Mẫu Nhất quán**: Ghi lại các mẫu nhất quán được quan sát trên toàn bộ codebase
- **Quan sát về Kiến trúc**: Ghi lại các mẫu kiến trúc rõ ràng trong mã
- **Quy ước Triển khai**: Xác định các quy ước đặt tên và cấu trúc
- **Các Mẫu không nên dùng (Anti-patterns)**: Ghi lại bất kỳ khu vực nào mà codebase đi chệch khỏi các phương pháp hay nhất` : ""}

### ${SCAN_DEPTH == "Toàn diện" ? "7" : "6"}. Định dạng Đầu ra

Tạo tệp exemplars.md với:

1. Lời giới thiệu giải thích mục đích của tài liệu
2. Mục lục với các liên kết đến các danh mục
3. Các phần được tổ chức dựa trên ${CATEGORIZATION}
4. Tối đa ${MAX_EXAMPLES_PER_CATEGORY} mẫu mã cho mỗi danh mục
5. Kết luận với các khuyến nghị để duy trì chất lượng mã

Tài liệu phải có tính ứng dụng cho các nhà phát triển cần hướng dẫn về việc triển khai các tính năng mới phù hợp với các mẫu hiện có.

Quan trọng: Chỉ bao gồm các tệp thực tế từ codebase. Xác minh tất cả các đường dẫn tệp đều tồn tại. Không bao gồm các ví dụ giữ chỗ hoặc giả định.
"

## Đầu ra Dự kiến

Khi chạy prompt này, GitHub Copilot sẽ quét codebase của bạn và tạo ra một tệp exemplars.md chứa các tham chiếu thực tế đến các ví dụ mã chất lượng cao trong repository của bạn, được tổ chức theo các tham số
