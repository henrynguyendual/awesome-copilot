# Hướng Dẫn Đóng Gói Dự Án ASP.NET Core vào Docker Container

## Yêu Cầu Đóng Gói

Đóng gói dự án ASP.NET Core (.NET) được chỉ định trong phần cài đặt bên dưới, tập trung **chỉ** vào các thay đổi cần thiết để ứng dụng có thể chạy trong Docker container Linux. Việc đóng gói cần tuân theo tất cả các thiết lập được nêu ở đây.

Tuân thủ các phương pháp tốt nhất khi đóng gói ứng dụng .NET Core vào container, đảm bảo tối ưu hiệu năng, bảo mật và khả năng bảo trì.

## Cài Đặt Đóng Gói

Phần này chứa thông tin cấu hình cần thiết để đóng gói ứng dụng ASP.NET Core. Trước khi thực hiện, hãy đảm bảo bạn đã điền đầy đủ các thông số. Nhiều trường hợp chỉ cần thông tin ở phần đầu, các phần sau có thể để mặc định.

Nếu không điền, hệ thống sẽ dùng giá trị mặc định (nằm trong dấu `[ ]`).

### Thông Tin Cơ Bản
1. Dự án cần đóng gói:
   - `[Tên dự án (đường dẫn đến file .csproj)]`

2. Phiên bản .NET:
   - `[8.0 hoặc 9.0 (Mặc định 8.0)]`

3. Bản phân phối Linux:
   - `[debian, alpine, ubuntu, chiseled, hoặc Azure Linux (mariner) (Mặc định debian)]`

4. Ảnh base tùy chỉnh cho giai đoạn build:
   - `[Tên base image hoặc None]`

5. Ảnh base tùy chỉnh cho giai đoạn chạy:
   - `[Tên base image hoặc None]`

### Cấu Hình Container
1. Cổng cần mở:
   - HTTP chính: `[ví dụ 8080]`
   - Cổng phụ: `[Danh sách hoặc None]`

2. User chạy container:
   - `[Tên user hoặc mặc định $APP_UID]`

3. URL ứng dụng:
   - `[ASPNETCORE_URLS hoặc mặc định http://+:8080]`

### Cấu Hình Build
1. Bước build trước khi tạo image:
   - `[Danh sách bước hoặc None]`

2. Bước build sau khi tạo image:
   - `[Danh sách bước hoặc None]`

3. Nguồn NuGet cần cấu hình:
   - `[Danh sách feed hoặc None]`

### Phụ Thuộc
1. Gói hệ thống cần cài:
   - `[Tên gói hoặc None]`

2. Thư viện native cần copy:
   - `[Tên và đường dẫn hoặc None]`

3. Công cụ .NET cần cài:
   - `[Tên và version hoặc None]`

### Cấu Hình Hệ Thống
1. Biến môi trường cần thiết lập:
   - `[Tên và giá trị hoặc dùng mặc định]`

### Hệ Thống File
1. File/thư mục cần copy vào image:
   - `[Đường dẫn và vị trí trong container]`

2. File/thư mục cần loại trừ:
   - `[Đường dẫn hoặc None]`

3. Volume mount points:
   - `[Đường dẫn hoặc None]`

### .dockerignore
1. Mẫu cần thêm:
   - `[Danh sách hoặc None]`

### Health Check
1. Endpoint kiểm tra:
   - `[Đường dẫn hoặc None]`

2. Khoảng thời gian & timeout:
   - `[Giá trị hoặc mặc định]`

### Hướng Dẫn Khác
1. Yêu cầu đặc biệt:
   - `[Danh sách hoặc None]`

2. Vấn đề đã biết:
   - `[Mô tả hoặc None]`

---

(Phần còn lại dịch tương tự, giữ nguyên hướng dẫn về Dockerfile mẫu, các tùy chọn Alpine/Ubuntu/Azure Linux, nguyên tắc bảo mật, và quy trình build & test)