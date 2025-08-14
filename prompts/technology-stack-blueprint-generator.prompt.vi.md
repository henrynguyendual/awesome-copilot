---
description: "Trình tạo bản thiết kế kiến trúc công nghệ toàn diện, phân tích mã nguồn để tạo tài liệu kiến trúc chi tiết. Tự động phát hiện các bộ công nghệ, ngôn ngữ lập trình và các mẫu triển khai trên nhiều nền tảng (.NET, Java, JavaScript, React, Python). Tạo ra các bản thiết kế có thể cấu hình với thông tin phiên bản, chi tiết giấy phép, các mẫu sử dụng, quy ước viết mã và sơ đồ trực quan. Cung cấp các mẫu sẵn sàng để triển khai và duy trì tính nhất quán về kiến trúc để hướng dẫn phát triển."
---

# Trình Tạo Bản Thiết Kế Kiến Trúc Công Nghệ Toàn Diện

## Biến Cấu Hình

${PROJECT_TYPE="Tự động phát hiện|.NET|Java|JavaScript|React.js|React Native|Angular|Python|Khác"} <!-- Công nghệ chính -->
${DEPTH_LEVEL="Cơ bản|Tiêu chuẩn|Toàn diện|Sẵn sàng triển khai"} <!-- Mức độ phân tích -->
${INCLUDE_VERSIONS=true|false} <!-- Bao gồm thông tin phiên bản -->
${INCLUDE_LICENSES=true|false} <!-- Bao gồm thông tin giấy phép -->
${INCLUDE_DIAGRAMS=true|false} <!-- Tạo sơ đồ kiến trúc -->
${INCLUDE_USAGE_PATTERNS=true|false} <!-- Bao gồm các mẫu sử dụng mã -->
${INCLUDE_CONVENTIONS=true|false} <!-- Ghi lại các quy ước viết mã -->
${OUTPUT_FORMAT="Markdown|JSON|YAML|HTML"} <!-- Chọn định dạng đầu ra -->
${CATEGORIZATION="Loại công nghệ|Lớp|Mục đích"} <!-- Phương pháp phân loại -->

## Prompt Được Tạo Ra

"Phân tích mã nguồn và tạo một bản thiết kế kiến trúc công nghệ ở mức độ ${DEPTH_LEVEL} để ghi lại một cách kỹ lưỡng các công nghệ và mẫu triển khai nhằm tạo điều kiện cho việc sinh mã nhất quán. Sử dụng phương pháp sau:

### 1. Giai Đoạn Nhận Dạng Công Nghệ

- ${PROJECT_TYPE == "Tự động phát hiện" ? "Quét mã nguồn để tìm các tệp dự án, tệp cấu hình và các dependency để xác định tất cả các bộ công nghệ đang được sử dụng" : "Tập trung vào các công nghệ ${PROJECT_TYPE}"}
- Xác định tất cả các ngôn ngữ lập trình bằng cách kiểm tra phần mở rộng của tệp và nội dung
- Phân tích các tệp cấu hình (package.json, .csproj, pom.xml, v.v.) để trích xuất các dependency
- Kiểm tra các script build và định nghĩa pipeline để biết thông tin về công cụ
- ${INCLUDE_VERSIONS ? "Trích xuất thông tin phiên bản chính xác từ các tệp package và cấu hình" : "Bỏ qua chi tiết phiên bản"}
- ${INCLUDE_LICENSES ? "Ghi lại thông tin giấy phép cho tất cả các dependency" : ""}

### 2. Phân Tích Các Công Nghệ Cốt Lõi

${PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Tự động phát hiện" ? "#### Phân Tích Bộ Công Nghệ .NET (nếu phát hiện)

- Các framework mục tiêu và phiên bản ngôn ngữ (phát hiện từ các tệp dự án)
- Tất cả các tham chiếu gói NuGet kèm theo phiên bản và nhận xét về mục đích
- Cấu trúc dự án và các mẫu tổ chức
- Phương pháp cấu hình (appsettings.json, IOptions, v.v.)
- Cơ chế xác thực (Identity, JWT, v.v.)
- Các mẫu thiết kế API (REST, GraphQL, minimal APIs, v.v.)
- Các phương pháp truy cập dữ liệu (EF Core, Dapper, v.v.)
- Các mẫu dependency injection
- Các thành phần trong pipeline middleware" : ""}

${PROJECT_TYPE == "Java" || PROJECT_TYPE == "Tự động phát hiện" ? "#### Phân Tích Bộ Công Nghệ Java (nếu phát hiện)

- Phiên bản JDK và các framework cốt lõi
- Tất cả các dependency Maven/Gradle kèm theo phiên bản và mục đích
- Tổ chức cấu trúc package
- Việc sử dụng và cấu hình Spring Boot
- Các mẫu annotation
- Phương pháp dependency injection
- Các công nghệ truy cập dữ liệu (JPA, JDBC, v.v.)
- Thiết kế API (Spring MVC, JAX-RS, v.v.)" : ""}

${PROJECT_TYPE == "JavaScript" || PROJECT_TYPE == "Tự động phát hiện" ? "#### Phân Tích Bộ Công Nghệ JavaScript (nếu phát hiện)

- Phiên bản ECMAScript và cài đặt trình chuyển mã (transpiler)
- Tất cả các dependency npm được phân loại theo mục đích
- Hệ thống module (ESM, CommonJS)
- Công cụ build (webpack, Vite, v.v.) kèm theo cấu hình
- Việc sử dụng và cấu hình TypeScript
- Các framework và mẫu kiểm thử" : ""}

${PROJECT_TYPE == "React.js" || PROJECT_TYPE == "Tự động phát hiện" ? "#### Phân Tích React (nếu phát hiện)

- Phiên bản React và các mẫu chính (hooks so với class components)
- Phương pháp quản lý trạng thái (Context, Redux, Zustand, v.v.)
- Việc sử dụng thư viện component (Material-UI, Chakra, v.v.)
- Triển khai routing
- Các chiến lược xử lý form
- Các mẫu tích hợp API
- Phương pháp kiểm thử cho các component" : ""}

${PROJECT_TYPE == "Python" || PROJECT_TYPE == "Tự động phát hiện" ? "#### Phân Tích Python (nếu phát hiện)

- Phiên bản Python và các tính năng ngôn ngữ chính được sử dụng
- Các dependency của package và thiết lập môi trường ảo
- Chi tiết về web framework (Django, Flask, FastAPI)
- Các mẫu sử dụng ORM
- Tổ chức cấu trúc dự án
- Các mẫu thiết kế API" : ""}

### 3. Các Mẫu Triển Khai & Quy Ước

${INCLUDE_CONVENTIONS ?
"Ghi lại các quy ước và mẫu viết mã cho từng lĩnh vực công nghệ:

#### Quy Ước Đặt Tên

- Các mẫu đặt tên lớp/kiểu
- Các mẫu đặt tên phương thức/hàm
- Quy ước đặt tên biến
- Quy ước đặt tên và tổ chức tệp
- Các mẫu interface/lớp trừu tượng

#### Tổ Chức Mã

- Cấu trúc và tổ chức tệp
- Các mẫu phân cấp thư mục
- Ranh giới component/module
- Các mẫu phân tách mã và trách nhiệm

#### Các Mẫu Phổ Biến

- Các phương pháp xử lý lỗi
- Các mẫu ghi log
- Truy cập cấu hình
- Triển khai xác thực/ủy quyền
- Các chiến lược xác thực dữ liệu
- Các mẫu kiểm thử" : ""}

### 4. Ví Dụ Sử Dụng

${INCLUDE_USAGE_PATTERNS ?
"Trích xuất các ví dụ mã đại diện cho thấy các mẫu triển khai tiêu chuẩn:

#### Ví Dụ Triển Khai API

- Triển khai controller/endpoint tiêu chuẩn
- Mẫu DTO cho request
- Định dạng response
- Phương pháp xác thực dữ liệu
- Xử lý lỗi

#### Ví Dụ Truy Cập Dữ Liệu

- Triển khai mẫu Repository
- Định nghĩa Entity/model
- Các mẫu truy vấn
- Xử lý giao dịch

#### Ví Dụ Lớp Service

- Triển khai lớp service
- Tổ chức logic nghiệp vụ
- Tích hợp các mối quan tâm xuyên suốt (cross-cutting concerns)
- Sử dụng dependency injection

#### Ví Dụ Component Giao Diện Người Dùng (nếu có)

- Cấu trúc component
- Mẫu quản lý trạng thái
- Xử lý sự kiện
- Mẫu tích hợp API" : ""}

### 5. Sơ Đồ Kiến Trúc Công Nghệ

${DEPTH_LEVEL == "Toàn diện" || DEPTH_LEVEL == "Sẵn sàng triển khai" ?
"Tạo một sơ đồ công nghệ toàn diện bao gồm:

#### Cách Sử Dụng Framework Cốt Lõi

- Các framework chính và cách sử dụng cụ thể của chúng trong dự án
- Các cấu hình và tùy chỉnh dành riêng cho framework
- Các điểm mở rộng và tùy chỉnh

#### Các Điểm Tích Hợp

- Cách các thành phần công nghệ khác nhau tích hợp với nhau
- Luồng xác thực giữa các thành phần
- Luồng dữ liệu giữa frontend và backend
- Các mẫu tích hợp dịch vụ của bên thứ ba

#### Công Cụ Phát Triển

- Cài đặt và quy ước IDE
- Các công cụ phân tích mã
- Các linter và formatter kèm theo cấu hình
- Pipeline build và triển khai
- Các framework và phương pháp kiểm thử

#### Cơ Sở Hạ Tầng

- Chi tiết môi trường triển khai
- Các công nghệ container
- Các dịch vụ đám mây được sử dụng
- Cơ sở hạ tầng giám sát và ghi log" : ""}

### 6. Chi Tiết Triển Khai Theo Từng Công Nghệ

${PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Tự động phát hiện" ?
"#### Chi Tiết Triển Khai .NET (nếu phát hiện)

- **Mẫu Dependency Injection**:
  - Phương pháp đăng ký service (các mẫu Scoped/Singleton/Transient)
  - Các mẫu binding cấu hình
- **Các Mẫu Controller**:
  - Cách sử dụng base controller
  - Các loại và mẫu action result
  - Quy ước về thuộc tính route
  - Cách sử dụng filter (ủy quyền, xác thực dữ liệu, v.v.)
- **Các Mẫu Truy Cập Dữ Liệu**:
  - Cấu hình và sử dụng ORM
  - Phương pháp cấu hình Entity
  - Định nghĩa các mối quan hệ
  - Các mẫu truy vấn và phương pháp tối ưu hóa
- **Các Mẫu Thiết Kế API** (nếu được sử dụng):
  - Tổ chức endpoint
  - Các phương pháp binding tham số
  - Xử lý kiểu response
- **Các Tính Năng Ngôn Ngữ Được Sử Dụng**:
  - Phát hiện các tính năng ngôn ngữ cụ thể từ mã
  - Xác định các mẫu và thành ngữ phổ biến
  - Ghi chú bất kỳ tính năng cụ thể nào phụ thuộc vào phiên bản" : ""}

${PROJECT_TYPE == "React.js" || PROJECT_TYPE == "Tự động phát hiện" ?
"#### Chi Tiết Triển Khai React (nếu phát hiện)

- **Cấu Trúc Component**:
  - Function so với class components
  - Định nghĩa interface cho props
  - Các mẫu kết hợp component
- **Các Mẫu Sử Dụng Hook**:
  - Kiểu triển khai custom hook
  - Các mẫu sử dụng useState
  - Các phương pháp dọn dẹp trong useEffect
  - Các mẫu sử dụng Context
- **Quản Lý Trạng Thái**:
  - Quyết định giữa trạng thái cục bộ và toàn cục
  - Các mẫu thư viện quản lý trạng thái
  - Cấu hình store
  - Các mẫu selector
- **Phương Pháp Tạo Kiểu (Styling)**:
  - Phương pháp CSS (CSS modules, styled-components, v.v.)
  - Triển khai theme
  - Các mẫu thiết kế đáp ứng (responsive)" : ""}

### 7. Bản Thiết Kế Cho Việc Triển Khai Mã Mới

${DEPTH_LEVEL == "Sẵn sàng triển khai" ?
"Dựa trên phân tích, cung cấp một bản thiết kế chi tiết để triển khai các tính năng mới:

- **Mẫu Tệp/Lớp**: Cấu trúc tiêu chuẩn cho các loại component phổ biến
- **Đoạn Mã (Snippets)**: Các mẫu mã sẵn sàng sử dụng cho các hoạt động phổ biến
- **Danh Sách Kiểm Tra Triển Khai**: Các bước tiêu chuẩn để triển khai tính năng từ đầu đến cuối
- **Các Điểm Tích Hợp**: Cách kết nối mã mới với các hệ thống hiện có
- **Yêu Cầu Kiểm Thử**: Các mẫu kiểm thử tiêu chuẩn cho các loại component khác nhau
- **Yêu Cầu Tài Liệu**: Các mẫu tài liệu tiêu chuẩn cho các tính năng mới" : ""}

${INCLUDE_DIAGRAMS ?
"### 8. Sơ Đồ Mối Quan Hệ Công Nghệ

- **Sơ Đồ Kiến Trúc**: Biểu diễn trực quan của toàn bộ kiến trúc công nghệ
- **Luồng Phụ Thuộc**: Cách các công nghệ khác nhau tương tác
- **Mối Quan Hệ Component**: Cách các component chính phụ thuộc lẫn nhau
- **Luồng Dữ Liệu**: Cách dữ liệu chảy qua kiến trúc công nghệ" : ""}

### ${INCLUDE_DIAGRAMS ? "9" : "8"}. Bối Cảnh Quyết Định Công Nghệ

- Ghi lại các lý do rõ ràng cho việc lựa chọn công nghệ
- Ghi chú bất kỳ công nghệ cũ hoặc đã lỗi thời được đánh dấu để thay thế
- Xác định các ràng buộc và giới hạn công nghệ
- Ghi lại các lộ trình nâng cấp công nghệ và các cân nhắc về khả năng tương thích

Định dạng đầu ra là ${OUTPUT_FORMAT} và phân loại các công nghệ theo ${CATEGORIZATION}.

Lưu đầu ra với tên 'Technology_Stack_Blueprint.${OUTPUT_FORMAT == "Markdown" ?
