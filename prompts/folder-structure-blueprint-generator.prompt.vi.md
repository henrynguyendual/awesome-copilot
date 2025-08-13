# Trình tạo bản thiết kế cấu trúc thư mục dự án

## Biến cấu hình

${PROJECT_TYPE="Tự động phát hiện|.NET|Java|React|Angular|Python|Node.js|Flutter|Khác"} 
<!-- Chọn công nghệ chính -->

${INCLUDES_MICROSERVICES="Tự động phát hiện|true|false"} 
<!-- Dự án có kiến trúc microservices không? -->

${INCLUDES_FRONTEND="Tự động phát hiện|true|false"} 
<!-- Dự án có chứa thành phần frontend không? -->

${IS_MONOREPO="Tự động phát hiện|true|false"} 
<!-- Đây có phải là monorepo với nhiều dự án không? -->

${VISUALIZATION_STYLE="ASCII|Danh sách Markdown|Bảng"} 
<!-- Cách hiển thị cấu trúc -->

${DEPTH_LEVEL=1-5} 
<!-- Mức độ sâu của thư mục cần tài liệu chi tiết -->

${INCLUDE_FILE_COUNTS=true|false} 
<!-- Bao gồm thống kê số lượng file -->

${INCLUDE_GENERATED_FOLDERS=true|false} 
<!-- Bao gồm thư mục được tạo tự động -->

${INCLUDE_FILE_PATTERNS=true|false} 
<!-- Ghi lại quy tắc đặt tên và vị trí file -->

${INCLUDE_TEMPLATES=true|false} 
<!-- Bao gồm mẫu file/thư mục cho tính năng mới -->

## Prompt được tạo

"Phân tích cấu trúc thư mục của dự án và tạo tài liệu 'Project_Folders_Structure_Blueprint.md' làm hướng dẫn chính thức để duy trì sự nhất quán trong tổ chức mã nguồn. Thực hiện theo cách tiếp cận sau:

### Giai đoạn tự động phát hiện ban đầu

${PROJECT_TYPE == "Tự động phát hiện" ? 
"Bắt đầu bằng cách quét cấu trúc thư mục để tìm file nhận diện loại dự án:
- Tìm file giải pháp/dự án (.sln, .csproj, .fsproj, .vbproj) để nhận diện dự án .NET
- Kiểm tra file build (pom.xml, build.gradle, settings.gradle) cho dự án Java
- Nhận diện package.json với dependencies cho dự án JavaScript/TypeScript
- Tìm file framework cụ thể (angular.json, react-scripts, next.config.js)
- Kiểm tra file Python (requirements.txt, setup.py, pyproject.toml)
- Xem file ứng dụng mobile (pubspec.yaml, thư mục android/ios)
- Ghi nhận công nghệ và phiên bản" : 
"Tập trung phân tích cấu trúc dự án ${PROJECT_TYPE}"}

${IS_MONOREPO == "Tự động phát hiện" ? 
"Xác định monorepo bằng cách tìm:
- Nhiều dự án với file cấu hình riêng
- File cấu hình workspace (lerna.json, nx.json, turborepo.json,...)
- Tham chiếu chéo và dependency dùng chung
- Script và cấu hình điều phối ở root" : ""}

${INCLUDES_MICROSERVICES == "Tự động phát hiện" ? 
"Kiểm tra kiến trúc microservices:
- Nhiều thư mục service cấu trúc tương tự
- Dockerfile hoặc cấu hình triển khai riêng cho từng service
- Mô hình giao tiếp giữa service (API, message broker)
- Cấu hình service registry/discovery
- File cấu hình API gateway
- Thư viện hoặc tiện ích dùng chung" : ""}

${INCLUDES_FRONTEND == "Tự động phát hiện" ? 
"Nhận diện thành phần frontend:
- Thư mục tài nguyên web (wwwroot, public, dist, static)
- File framework UI (components, modules, pages)
- Cấu hình build frontend (webpack, vite, rollup, ...)
- Tổ chức CSS/SCSS, styled-components
- Tổ chức tài nguyên tĩnh (images, fonts, icons)" : ""}

### 1. Tổng quan cấu trúc

Ghi lại nguyên tắc tổ chức và cấu trúc thư mục của dự án ${PROJECT_TYPE == "Tự động phát hiện" ? "được phát hiện" : PROJECT_TYPE}:

- Tài liệu về kiến trúc tổng thể
- Nguyên tắc tổ chức chính (theo chức năng, theo tầng, theo domain,...)
- Mô hình cấu trúc lặp lại
- Lý do tổ chức cấu trúc (nếu có thể suy luận)

${IS_MONOREPO == "Tự động phát hiện" ? 
"Nếu là monorepo, mô tả cách tổ chức và mối quan hệ giữa các dự án." : 
IS_MONOREPO ? "Mô tả cách tổ chức monorepo và mối quan hệ giữa các dự án." : ""}

${INCLUDES_MICROSERVICES == "Tự động phát hiện" ? 
"Nếu có microservices, mô tả cách cấu trúc và tổ chức." : 
INCLUDES_MICROSERVICES ? "Mô tả cấu trúc và tổ chức microservices." : ""}

### 2. Trực quan hóa thư mục

${VISUALIZATION_STYLE == "ASCII" ? 
"Tạo sơ đồ cây ASCII đến độ sâu ${DEPTH_LEVEL}." : ""}

${VISUALIZATION_STYLE == "Danh sách Markdown" ? 
"Sử dụng danh sách Markdown lồng nhau đến độ sâu ${DEPTH_LEVEL}." : ""}

${VISUALIZATION_STYLE == "Bảng" ? 
"Tạo bảng gồm Cột Đường dẫn, Mục đích, Loại nội dung và Quy ước." : ""}

${INCLUDE_GENERATED_FOLDERS ? 
"Bao gồm cả thư mục được tạo tự động." : 
"Loại trừ thư mục auto-gen như bin/, obj/, node_modules/."}

### 3. Phân tích thư mục chính

Ghi lại mục đích, nội dung và mẫu cấu trúc của từng thư mục quan trọng.

... (giữ nguyên nội dung phân tích công nghệ cụ thể như bản gốc nhưng dịch toàn bộ sang tiếng Việt) ...

### 9. Mở rộng và tiến hóa
Ghi lại cách thiết kế dự án để mở rộng:

- **Điểm mở rộng**:
  - Cách thêm module/tính năng mới
  - Mẫu thư mục plugin/extension
  - Thư mục tùy chỉnh

- **Mẫu mở rộng quy mô**:
  - Cách cấu trúc mở rộng cho tính năng lớn
  - Chiến lược tách module lớn
  - Chiến lược chia nhỏ code

- **Mẫu refactor**:
  - Cách refactor thường thấy
  - Quản lý thay đổi cấu trúc
  - Mẫu tổ chức lại từng bước

${INCLUDE_TEMPLATES ? 
"### 10. Mẫu cấu trúc

Cung cấp mẫu tạo mới theo quy ước dự án:

- **Mẫu tính năng mới**:
  - Thư mục và file cần thiết
  - Quy tắc đặt tên

- **Mẫu component mới**:
  - Cấu trúc thư mục component
  - File thiết yếu
  - Điểm tích hợp với cấu trúc hiện có

- **Mẫu service mới**:
  - Cấu trúc thêm service mới
  - Vị trí interface và implementation
  - Cấu hình và đăng ký

- **Mẫu kiểm thử mới**:
  - Cấu trúc thư mục test
  - Tổ chức file test
  - Tài nguyên test" : ""}

### ${INCLUDE_TEMPLATES ? "11" : "10"}. Duy trì cấu trúc

- **Kiểm tra cấu trúc**:
  - Công cụ/script kiểm tra
  - Build check đảm bảo tuân thủ
  - Quy tắc lint liên quan

- **Thực hành tài liệu**:
  - Cách ghi lại thay đổi cấu trúc
  - Nơi lưu trữ quyết định kiến trúc
  - Lịch sử tiến hóa cấu trúc

Kết thúc với phần duy trì bản thiết kế và ngày cập nhật gần nhất.
