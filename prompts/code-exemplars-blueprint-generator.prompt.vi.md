# Trình Tạo Blueprint Code Exemplars

## Biến Cấu Hình
${PROJECT_TYPE="Auto-detect|.NET|Java|JavaScript|TypeScript|React|Angular|Python|Other"} <!-- Công nghệ chính -->
${SCAN_DEPTH="Basic|Standard|Comprehensive"} <!-- Mức độ phân tích codebase -->
${INCLUDE_CODE_SNIPPETS=true|false} <!-- Bao gồm đoạn mã minh họa ngoài tham chiếu file -->
${CATEGORIZATION="Pattern Type|Architecture Layer|File Type"} <!-- Cách tổ chức exemplars -->
${MAX_EXAMPLES_PER_CATEGORY=3} <!-- Số lượng ví dụ tối đa mỗi danh mục -->
${INCLUDE_COMMENTS=true|false} <!-- Bao gồm chú thích giải thích cho mỗi exemplar -->

## Prompt Sinh Ra

"Quét codebase này và tạo file exemplars.md xác định các ví dụ code đại diện và chất lượng cao. Các ví dụ này cần thể hiện tiêu chuẩn và mẫu code của chúng ta để duy trì tính nhất quán. Thực hiện theo cách tiếp cận sau:

### 1. Giai Đoạn Phân Tích Codebase
- ${PROJECT_TYPE == "Auto-detect" ? "Tự động phát hiện ngôn ngữ lập trình và framework chính bằng cách quét phần mở rộng file và file cấu hình" : `Tập trung vào các file ${PROJECT_TYPE}`}
- Xác định các file có chất lượng cao, tài liệu tốt và cấu trúc rõ ràng
- Tìm các mẫu thường dùng, thành phần kiến trúc và triển khai tốt
- Ưu tiên file thể hiện best practices cho stack công nghệ của chúng ta
- Chỉ tham chiếu file thực sự tồn tại trong codebase - không tạo ví dụ giả định

### 2. Tiêu Chí Xác Định Exemplars
- Cấu trúc tốt, dễ đọc, đặt tên rõ ràng
- Có tài liệu và chú thích đầy đủ
- Xử lý lỗi và xác thực đúng chuẩn
- Tuân thủ design pattern và nguyên tắc kiến trúc
- Phân tách rõ trách nhiệm (SoC, SRP)
- Tối ưu hiệu suất, không có code smell
- Đại diện cho cách tiếp cận chuẩn của chúng ta

### 3. Danh Mục Mẫu Code Chính

${PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Auto-detect" ? `#### Ví Dụ .NET (nếu phát hiện)
- **Domain Models**: Entity triển khai đầy đủ encapsulation và domain logic
- **Repository Implementations**: Ví dụ cách truy cập dữ liệu
- **Service Layer Components**: Triển khai business logic tốt
- **Controller Patterns**: API controller sạch sẽ, có xác thực và phản hồi chuẩn
- **Dependency Injection Usage**: Ví dụ cấu hình và dùng DI tốt
- **Middleware Components**: Middleware tùy chỉnh
- **Unit Test Patterns**: Test được cấu trúc tốt với sắp xếp và assert chuẩn` : ""}

${(PROJECT_TYPE == "JavaScript" || PROJECT_TYPE == "TypeScript" || PROJECT_TYPE == "React" || PROJECT_TYPE == "Angular" || PROJECT_TYPE == "Auto-detect") ? `#### Ví Dụ Frontend (nếu phát hiện)
- **Component Structure**: Component sạch sẽ, cấu trúc tốt
- **State Management**: Ví dụ quản lý state tốt
- **API Integration**: Gọi API và xử lý dữ liệu chuẩn
- **Form Handling**: Validation và submit
- **Routing Implementation**: Điều hướng và cấu hình route
- **UI Components**: Thành phần UI tái sử dụng
- **Unit Test Examples**: Test cho component và service` : ""}

${PROJECT_TYPE == "Java" || PROJECT_TYPE == "Auto-detect" ? `#### Ví Dụ Java (nếu phát hiện)
- **Entity Classes**: JPA entity hoặc domain model tốt
- **Service Implementations**: Service layer sạch sẽ
- **Repository Patterns**: Truy cập dữ liệu
- **Controller/Resource Classes**: API endpoint
- **Configuration Classes**: Cấu hình ứng dụng
- **Unit Tests**: JUnit test chuẩn` : ""}

${PROJECT_TYPE == "Python" || PROJECT_TYPE == "Auto-detect" ? `#### Ví Dụ Python (nếu phát hiện)
- **Class Definitions**: Class cấu trúc tốt, có tài liệu
- **API Routes/Views**: API sạch sẽ
- **Data Models**: ORM model
- **Service Functions**: Business logic
- **Utility Modules**: Helper/utility
- **Test Cases**: Unit test tốt` : ""}

### 4. Ví Dụ Theo Tầng Kiến Trúc

- **Presentation Layer**:
  - UI components
  - Controllers/API endpoints
  - View models/DTOs
  
- **Business Logic Layer**:
  - Service implementations
  - Business logic components
  - Workflow orchestration
  
- **Data Access Layer**:
  - Repository
  - Data models
  - Query patterns
  
- **Cross-Cutting Concerns**:
  - Logging
  - Error handling
  - Auth
  - Validation

### 5. Định Dạng Tài Liệu Exemplars

Với mỗi exemplar, ghi rõ:
- Đường dẫn file (tương đối)
- Mô tả ngắn vì sao đây là ví dụ tốt
- Pattern hoặc loại thành phần
${INCLUDE_COMMENTS ? "- Chi tiết triển khai và nguyên tắc coding" : ""}
${INCLUDE_CODE_SNIPPETS ? "- Đoạn code minh họa (nếu có)" : ""}

${SCAN_DEPTH == "Comprehensive" ? `### 6. Tài Liệu Bổ Sung

- **Consistency Patterns**: Các pattern nhất quán
- **Architecture Observations**: Quan sát kiến trúc
- **Implementation Conventions**: Quy ước tên và cấu trúc
- **Anti-patterns to Avoid**: Điểm cần tránh` : ""}

### ${SCAN_DEPTH == "Comprehensive" ? "7" : "6"}. Định Dạng Output

Tạo exemplars.md với:
1. Giới thiệu mục đích
2. Mục lục có link tới danh mục
3. Các phần được tổ chức theo ${CATEGORIZATION}
4. Tối đa ${MAX_EXAMPLES_PER_CATEGORY} ví dụ mỗi danh mục
5. Kết luận với khuyến nghị duy trì chất lượng code

Lưu ý: Chỉ bao gồm file thực tế trong codebase, xác minh đường dẫn tồn tại, không dùng ví dụ placeholder.
"

## Output Mong Đợi
Khi chạy prompt này, GitHub Copilot sẽ quét codebase và tạo exemplars.md chứa các tham chiếu thực tế tới ví dụ code chất lượng cao trong repo, được tổ chức theo cấu hình đã chọn.