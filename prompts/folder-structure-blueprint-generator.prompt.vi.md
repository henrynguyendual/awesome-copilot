---
description: "Prompt toàn diện, không phụ thuộc vào công nghệ để phân tích và lập tài liệu về cấu trúc thư mục dự án. Tự động phát hiện các loại dự án (.NET, Java, React, Angular, Python, Node.js, Flutter), tạo ra các sơ đồ chi tiết với các tùy chọn trực quan hóa, quy ước đặt tên, các mẫu sắp xếp tệp và các mẫu mở rộng để duy trì tổ chức mã nguồn nhất quán trên các ngăn xếp công nghệ đa dạng."
---

# Trình tạo Sơ đồ Cấu trúc Thư mục Dự án

## Biến Cấu hình

${PROJECT_TYPE="Tự động phát hiện|.NET|Java|React|Angular|Python|Node.js|Flutter|Khác"}

<!-- Chọn công nghệ chính -->

${INCLUDES_MICROSERVICES="Tự động phát hiện|true|false"}

<!-- Đây có phải là kiến trúc microservices không? -->

${INCLUDES_FRONTEND="Tự động phát hiện|true|false"}

<!-- Dự án có bao gồm các thành phần frontend không? -->

${IS_MONOREPO="Tự động phát hiện|true|false"}

<!-- Đây có phải là monorepo với nhiều dự án không? -->

${VISUALIZATION_STYLE="ASCII|Danh sách Markdown|Bảng"}

<!-- Cách trực quan hóa cấu trúc -->

${DEPTH_LEVEL=1-5}

<!-- Số cấp thư mục cần ghi lại chi tiết -->

${INCLUDE_FILE_COUNTS=true|false}

<!-- Bao gồm thống kê số lượng tệp -->

${INCLUDE_GENERATED_FOLDERS=true|false}

<!-- Bao gồm các thư mục được tạo tự động -->

${INCLUDE_FILE_PATTERNS=true|false}

<!-- Ghi lại các mẫu đặt tên/vị trí tệp -->

${INCLUDE_TEMPLATES=true|false}

<!-- Bao gồm các mẫu tệp/thư mục cho các tính năng mới -->

## Prompt được tạo

"Phân tích cấu trúc thư mục của dự án và tạo một tài liệu 'Project_Folders_Structure_Blueprint.md' toàn diện, đóng vai trò là hướng dẫn cuối cùng để duy trì tổ chức mã nguồn nhất quán. Sử dụng phương pháp sau:

### Giai đoạn Tự động Phát hiện Ban đầu

${PROJECT_TYPE == "Tự động phát hiện" ?
"Bắt đầu bằng cách quét cấu trúc thư mục để tìm các tệp chính giúp xác định loại dự án:

- Tìm các tệp solution/project (.sln, .csproj, .fsproj, .vbproj) để xác định các dự án .NET
- Kiểm tra các tệp build (pom.xml, build.gradle, settings.gradle) cho các dự án Java
- Xác định package.json với các dependency cho các dự án JavaScript/TypeScript
- Tìm các tệp framework cụ thể (angular.json, các mục trong react-scripts, next.config.js)
- Kiểm tra các định danh dự án Python (requirements.txt, setup.py, pyproject.toml)
- Kiểm tra các định danh ứng dụng di động (pubspec.yaml, thư mục android/ios)
- Ghi lại tất cả các dấu hiệu công nghệ được tìm thấy và phiên bản của chúng" :
  "Tập trung phân tích vào cấu trúc dự án ${PROJECT_TYPE}"}

${IS_MONOREPO == "Tự động phát hiện" ?
"Xác định xem đây có phải là monorepo không bằng cách tìm kiếm:

- Nhiều dự án riêng biệt với các tệp cấu hình riêng
- Các tệp cấu hình workspace (lerna.json, nx.json, turborepo.json, v.v.)
- Các tham chiếu chéo dự án và các mẫu dependency được chia sẻ
- Các script điều phối và cấu hình ở cấp độ gốc" : ""}

${INCLUDES_MICROSERVICES == "Tự động phát hiện" ?
"Kiểm tra các chỉ số kiến trúc microservices:

- Nhiều thư mục dịch vụ với cấu trúc tương tự/lặp lại
- Các Dockerfile hoặc cấu hình triển khai dành riêng cho dịch vụ
- Các mẫu giao tiếp giữa các dịch vụ (API, message broker)
- Cấu hình đăng ký hoặc khám phá dịch vụ
- Các tệp cấu hình API gateway
- Các thư viện hoặc tiện ích được chia sẻ giữa các dịch vụ" : ""}

${INCLUDES_FRONTEND == "Tự động phát hiện" ?
"Xác định các thành phần frontend bằng cách tìm kiếm:

- Các thư mục tài sản web (wwwroot, public, dist, static)
- Các tệp framework UI (components, modules, pages)
- Cấu hình build frontend (webpack, vite, rollup, v.v.)
- Tổ chức stylesheet (CSS, SCSS, styled-components)
- Tổ chức tài sản tĩnh (hình ảnh, phông chữ, biểu tượng)" : ""}

### 1. Tổng quan về Cấu trúc

Cung cấp một cái nhìn tổng quan cấp cao về các nguyên tắc tổ chức và cấu trúc thư mục của dự án ${PROJECT_TYPE == "Tự động phát hiện" ? "loại dự án được phát hiện" : PROJECT_TYPE}:

- Ghi lại phương pháp kiến trúc tổng thể được phản ánh trong cấu trúc thư mục
- Xác định các nguyên tắc tổ chức chính (theo tính năng, theo lớp, theo miền, v.v.)
- Ghi lại bất kỳ mẫu cấu trúc nào lặp lại trong toàn bộ codebase
- Ghi lại lý do đằng sau cấu trúc nơi có thể suy ra được

${IS_MONOREPO == "Tự động phát hiện" ?
"Nếu được phát hiện là monorepo, hãy giải thích cách monorepo được tổ chức và mối quan hệ giữa các dự án." :
IS_MONOREPO ? "Giải thích cách monorepo được tổ chức và mối quan hệ giữa các dự án." : ""}

${INCLUDES_MICROSERVICES == "Tự động phát hiện" ?
"Nếu phát hiện có microservices, hãy mô tả cách chúng được cấu trúc và tổ chức." :
INCLUDES_MICROSERVICES ? "Mô tả cách các microservices được cấu trúc và tổ chức." : ""}

### 2. Trực quan hóa Thư mục

${VISUALIZATION_STYLE == "ASCII" ?
"Tạo một biểu diễn cây ASCII của hệ thống phân cấp thư mục đến độ sâu ${DEPTH_LEVEL}." : ""}

${VISUALIZATION_STYLE == "Danh sách Markdown" ?
"Sử dụng danh sách markdown lồng nhau để biểu diễn hệ thống phân cấp thư mục đến độ sâu ${DEPTH_LEVEL}." : ""}

${VISUALIZATION_STYLE == "Bảng" ?
"Tạo một bảng với các cột cho Đường dẫn, Mục đích, Loại nội dung và Quy ước." : ""}

${INCLUDE_GENERATED_FOLDERS ?
"Bao gồm tất cả các thư mục kể cả những thư mục được tạo tự động." :
"Loại trừ các thư mục được tạo tự động như bin/, obj/, node_modules/, v.v."}

### 3. Phân tích Thư mục Chính

Ghi lại mục đích, nội dung và các mẫu của mỗi thư mục quan trọng:

${PROJECT_TYPE == "Tự động phát hiện" ?
"Đối với mỗi công nghệ được phát hiện, hãy phân tích cấu trúc thư mục dựa trên các mẫu sử dụng được quan sát:" : ""}

${(PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Tự động phát hiện") ?
"#### Cấu trúc Dự án .NET (nếu phát hiện)

- **Tổ chức Solution**:

  - Cách các dự án được nhóm và liên kết
  - Các mẫu tổ chức thư mục solution
  - Các mẫu dự án đa mục tiêu

- **Tổ chức Dự án**:

  - Các mẫu cấu trúc thư mục nội bộ
  - Phương pháp tổ chức mã nguồn
  - Tổ chức tài nguyên
  - Các dependency và tham chiếu của dự án

- **Tổ chức theo Miền/Tính năng**:

  - Cách các miền nghiệp vụ hoặc tính năng được phân tách
  - Các mẫu thực thi ranh giới miền

- **Tổ chức theo Lớp**:

  - Phân tách các mối quan tâm (Controllers, Services, Repositories, v.v.)
  - Tương tác giữa các lớp và các mẫu dependency

- **Quản lý Cấu hình**:

  - Vị trí và mục đích của các tệp cấu hình
  - Cấu hình theo môi trường cụ thể
  - Phương pháp quản lý bí mật

- **Tổ chức Dự án Test**:
  - Cấu trúc và đặt tên dự án test
  - Các danh mục và tổ chức test
  - Vị trí dữ liệu test và mock" : ""}

${(PROJECT_TYPE == "React" || PROJECT_TYPE == "Angular" || PROJECT_TYPE == "Tự động phát hiện") ?
"#### Cấu trúc Dự án UI (nếu phát hiện)

- **Tổ chức Component**:

  - Các mẫu cấu trúc thư mục component
  - Các chiến lược nhóm (theo tính năng, loại, v.v.)
  - Các component được chia sẻ so với các component dành riêng cho tính năng

- **Quản lý Trạng thái (State Management)**:

  - Tổ chức tệp liên quan đến trạng thái
  - Cấu trúc store cho trạng thái toàn cục
  - Các mẫu quản lý trạng thái cục bộ

- **Tổ chức Routing**:

  - Vị trí định nghĩa route
  - Tổ chức component trang/view
  - Xử lý tham số route

- **Tích hợp API**:

  - Tổ chức API client
  - Cấu trúc lớp dịch vụ
  - Các mẫu tìm nạp dữ liệu

- **Quản lý Tài sản (Asset Management)**:
  - Tổ chức tài nguyên tĩnh
  - Cấu trúc tệp hình ảnh/media
  - Tổ chức phông chữ và biểu tượng
- **Tổ chức Style**:
  - Cấu trúc tệp CSS/SCSS
  - Tổ chức theme
  - Các mẫu module style" : ""}

### 4. Các Mẫu Sắp xếp Tệp

${INCLUDE_FILE_PATTERNS ?
"Ghi lại các mẫu xác định nơi các loại tệp khác nhau nên được đặt:

- **Tệp Cấu hình**:
  - Vị trí cho các loại cấu hình khác nhau
  - Các mẫu cấu hình theo môi trường cụ thể
- **Định nghĩa Model/Entity**:
  - Nơi các mô hình miền được định nghĩa
  - Vị trí đối tượng truyền dữ liệu (DTO)
  - Vị trí định nghĩa schema
- **Logic Nghiệp vụ**:
  - Vị trí triển khai dịch vụ
  - Tổ chức quy tắc nghiệp vụ
  - Vị trí các hàm tiện ích và trợ giúp
- **Định nghĩa Interface**:
  - Nơi các interface và abstraction được định nghĩa
  - Cách các interface được nhóm và tổ chức
- **Tệp Test**:
  - Các mẫu vị trí unit test
  - Vị trí integration test
  - Vị trí các tiện ích test và mock
- **Tệp Tài liệu**:
  - Vị trí tài liệu API
  - Tổ chức tài liệu nội bộ
  - Phân phối tệp README" :
    "Ghi lại vị trí của các loại tệp chính trong dự án."}

### 5. Quy ước Đặt tên và Tổ chức

Ghi lại các quy ước đặt tên và tổ chức được quan sát trên toàn dự án:

- **Các Mẫu Đặt tên Tệp**:
  - Quy ước về kiểu chữ (PascalCase, camelCase, kebab-case)
  - Các mẫu tiền tố và hậu tố
  - Các chỉ báo loại trong tên tệp
- **Các Mẫu Đặt tên Thư mục**:
  - Quy ước đặt tên cho các loại thư mục khác nhau
  - Các mẫu đặt tên phân cấp
  - Các quy ước nhóm và phân loại
- **Các Mẫu Namespace/Module**:

  - Cách namespace/module ánh xạ tới cấu trúc thư mục
  - Tổ chức câu lệnh import/using
  - Phân tách API nội bộ và công khai

- **Các Mẫu Tổ chức**:
  - Các chiến lược đồng vị trí mã nguồn
  - Các phương pháp đóng gói tính năng
  - Tổ chức các mối quan tâm xuyên suốt (cross-cutting concern)

### 6. Luồng Điều hướng và Phát triển

Cung cấp hướng dẫn để điều hướng và làm việc với cấu trúc codebase:

- **Điểm bắt đầu (Entry Points)**:

  - Các điểm bắt đầu chính của ứng dụng
  - Các điểm bắt đầu cấu hình chính
  - Các tệp ban đầu để hiểu dự án

- **Các Tác vụ Phát triển Phổ biến**:
  - Nơi để thêm các tính năng mới
  - Cách mở rộng chức năng hiện có
  - Nơi đặt các bài test mới
  - Vị trí sửa đổi cấu hình
- **Các Mẫu Dependency**:
  - Cách các dependency luân chuyển giữa các thư mục
  - Các mẫu import/tham chiếu
  - Vị trí đăng ký dependency injection

${INCLUDE_FILE_COUNTS ?
"- **Thống kê Nội dung**:

- Phân tích số tệp trên mỗi thư mục
- Các chỉ số phân phối mã nguồn
- Các khu vực tập trung độ phức tạp" : ""}

### 7. Tổ chức Build và Đầu ra

Ghi lại quy trình build và tổ chức đầu ra:

- **Cấu hình Build**:
  - Vị trí và mục đích của các script build
  - Tổ chức pipeline build
  - Định nghĩa các tác vụ build
- **Cấu trúc Đầu ra**:
  - Vị trí đầu ra đã biên dịch/build
  - Các mẫu tổ chức đầu ra
  - Cấu trúc gói phân phối
- **Build theo Môi trường Cụ thể**:
  - Sự khác biệt giữa môi trường phát triển và sản xuất
  - Các chiến lược cấu hình môi trường
  - Tổ chức các biến thể build

### 8. Tổ chức theo Công nghệ Cụ thể

${(PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Tự động phát hiện") ?
"#### Các Mẫu Cấu trúc Cụ thể cho .NET (nếu phát hiện)

- **Tổ chức Tệp Dự án**:
  - Cấu trúc và các mẫu tệp dự án
  - Cấu hình target framework
  - Tổ chức property group
  - Các mẫu item group
- **Tổ chức Assembly**:
  - Các mẫu đặt tên assembly
  - Kiến trúc đa assembly
  - Các mẫu tham chiếu assembly
- **Tổ chức Tài nguyên**:
  - Các mẫu tài nguyên nhúng
  - Cấu trúc tệp bản địa hóa
  - Tổ chức tài sản web tĩnh
- **Quản lý Gói (Package Management)**:
  - Vị trí cấu hình NuGet
  - Tổ chức tham chiếu gói
  - Quản lý phiên bản gói" : ""}

${(PROJECT_TYPE == "Java" || PROJECT_TYPE == "Tự động phát hiện") ?
"#### Các Mẫu Cấu trúc Cụ thể cho Java (nếu phát hiện)

- **Hệ thống Phân cấp Gói (Package Hierarchy)**:
  - Quy ước đặt tên và lồng gói
  - Gói theo miền so với gói kỹ thuật
  - Các mẫu hiển thị và truy cập
- **Tổ chức Công cụ Build**:
  - Các mẫu cấu trúc Maven/Gradle
  - Tổ chức module
  - Các mẫu cấu hình plugin
- **Tổ chức Tài nguyên**:
  - Cấu trúc thư mục tài nguyên
  - Tài nguyên theo môi trường cụ thể
  - Tổ chức tệp properties" : ""}

${(PROJECT_TYPE == "Node.js" || PROJECT_TYPE == "Tự động phát hiện") ?
"#### Các Mẫu Cấu trúc Cụ thể cho Node.js (nếu phát hiện)

- **Tổ chức Module**:
  - Tổ chức CommonJS so với ESM
  - Các mẫu module nội bộ
  - Quản lý dependency của bên thứ ba
- **Tổ chức Script**:
  - Các mẫu định nghĩa script npm/yarn
  - Vị trí các script tiện ích
  - Các script công cụ phát triển
- **Quản lý Cấu hình**:
  - Vị trí tệp cấu hình
  - Quản lý biến môi trường
  - Các phương pháp quản lý bí mật" : ""}

### 9. Mở rộng và Phát triển

Ghi lại cách cấu trúc dự án được thiết kế để mở rộng:

- **Điểm Mở rộng**:
  - Cách thêm các module/tính năng mới trong khi vẫn duy trì các quy ước
  - Các mẫu thư mục plugin/extension
  - Cấu trúc thư mục tùy chỉnh
- **Các Mẫu về Khả năng Mở rộng (Scalability)**:
  - Cách cấu trúc mở rộng cho các tính năng lớn hơn
  - Phương pháp chia nhỏ các module lớn
  - Các chiến lược chia tách mã (code splitting)
- **Các Mẫu Tái cấu trúc (Refactoring)**:
  - Các phương pháp tái cấu trúc phổ biến được quan sát
  - Cách quản lý các thay đổi về cấu trúc
  - Các mẫu tái tổ chức tăng dần

${INCLUDE_TEMPLATES ?
"### 10. Các Mẫu Cấu trúc

Cung cấp các mẫu để tạo các thành phần mới tuân theo các quy ước của dự án:

- **Mẫu Tính năng Mới**:
  - Cấu trúc thư mục để thêm một tính năng hoàn chỉnh
  - Các loại tệp bắt buộc và vị trí của chúng
  - Các mẫu đặt tên cần tuân theo
- **Mẫu Component Mới**:
  - Cấu trúc thư mục cho một component điển hình
  - Các tệp thiết yếu cần bao gồm
  - Các điểm tích hợp với cấu trúc hiện có
- **Mẫu Dịch vụ Mới**:
  - Cấu trúc để thêm một dịch vụ mới
  - Vị trí interface và triển khai
  - Các mẫu cấu hình và đăng ký
- **Cấu trúc Test Mới**:
  - Cấu trúc thư mục cho các dự án/tệp test
  - Các mẫu tổ chức tệp test
  - Tổ chức tài nguyên test" : ""}

### ${INCLUDE_TEMPLATES ? "11" : "10"}. Thực thi Cấu trúc

Ghi lại cách cấu trúc dự án được duy trì và thực thi:

- **Xác thực Cấu trúc**:
  - Các công cụ/script thực thi cấu trúc
  - Các kiểm tra trong quá trình build để đảm bảo tuân thủ cấu trúc
  - Các quy tắc linting liên quan đến cấu trúc
- **Thực hành Lập tài liệu**:
  - Cách các thay đổi về cấu trúc được ghi lại
  - Nơi các quyết định về kiến trúc được ghi lại
  - Lịch sử phát triển cấu trúc

Bao gồm một phần ở cuối về việc duy trì sơ đồ này và thời điểm nó được cập nhật
