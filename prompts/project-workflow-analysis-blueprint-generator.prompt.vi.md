---
description: "Trình tạo prompt toàn diện, không phụ thuộc vào công nghệ, dùng để tài liệu hóa các luồng công việc ứng dụng từ đầu đến cuối. Tự động phát hiện các mẫu kiến trúc dự án, các chồng công nghệ, và các mẫu luồng dữ liệu để tạo ra các bản thiết kế chi tiết về việc triển khai, bao gồm các điểm vào, các lớp dịch vụ, truy cập dữ liệu, xử lý lỗi, và các phương pháp kiểm thử trên nhiều công nghệ bao gồm .NET, Java/Spring, React, và kiến trúc microservices."
---

# Trình Tạo Tài Liệu Luồng Công Việc Dự Án

## Biến Cấu Hình

```
${PROJECT_TYPE="Tự động phát hiện|.NET|Java|Spring|Node.js|Python|React|Angular|Microservices|Khác"}
<!-- Chồng công nghệ chính -->

${ENTRY_POINT="API|GraphQL|Frontend|CLI|Message Consumer|Scheduled Job|Tùy chỉnh"}
<!-- Điểm bắt đầu của luồng -->

${PERSISTENCE_TYPE="Tự động phát hiện|Cơ sở dữ liệu SQL|Cơ sở dữ liệu NoSQL|Hệ thống tệp|API bên ngoài|Hàng đợi tin nhắn|Cache|Không có"}
<!-- Loại lưu trữ dữ liệu -->

${ARCHITECTURE_PATTERN="Tự động phát hiện|Layered|Clean|CQRS|Microservices|MVC|MVVM|Serverless|Event-Driven|Khác"}
<!-- Mẫu kiến trúc chính -->

${WORKFLOW_COUNT=1-5}
<!-- Số lượng luồng công việc cần tài liệu hóa -->

${DETAIL_LEVEL="Tiêu chuẩn|Sẵn sàng triển khai"}
<!-- Mức độ chi tiết triển khai -->

${INCLUDE_SEQUENCE_DIAGRAM=true|false}
<!-- Tạo biểu đồ tuần tự (sequence diagram) -->

${INCLUDE_TEST_PATTERNS=true|false}
<!-- Bao gồm phương pháp kiểm thử -->
```

## Prompt Được Tạo Ra

```
"Phân tích codebase và tài liệu hóa ${WORKFLOW_COUNT} luồng công việc đại diện từ đầu đến cuối
có thể dùng làm mẫu triển khai cho các tính năng tương tự. Sử dụng phương pháp sau:
```

### Giai Đoạn Phát Hiện Ban Đầu

```
${PROJECT_TYPE == "Tự động phát hiện" ?
  "Bắt đầu bằng cách kiểm tra cấu trúc codebase để xác định các công nghệ:
   - Kiểm tra các solution/project .NET, cấu hình Spring, tệp Node.js/Express, v.v.
   - Xác định (các) ngôn ngữ lập trình chính và các framework đang được sử dụng
   - Xác định các mẫu kiến trúc dựa trên cấu trúc thư mục và các thành phần chính"
  : "Tập trung vào các mẫu và quy ước của ${PROJECT_TYPE}"}
```

```
${ENTRY_POINT == "Tự động phát hiện" ?
  "Xác định các điểm vào điển hình bằng cách tìm kiếm:
   - Các API controller hoặc định nghĩa route
   - Các GraphQL resolver
   - Các thành phần UI khởi tạo yêu cầu mạng
   - Các trình xử lý tin nhắn hoặc đăng ký sự kiện
   - Các định nghĩa công việc theo lịch trình"
  : "Tập trung vào các điểm vào ${ENTRY_POINT}"}
```

```
${PERSISTENCE_TYPE == "Tự động phát hiện" ?
  "Xác định các cơ chế lưu trữ bằng cách kiểm tra:
   - Các cấu hình context/kết nối cơ sở dữ liệu
   - Các triển khai Repository
   - Các ánh xạ ORM
   - Các client API bên ngoài
   - Các tương tác với hệ thống tệp"
  : "Tập trung vào các tương tác ${PERSISTENCE_TYPE}"}
```

### Hướng Dẫn Tài Liệu Hóa Luồng Công Việc

Đối với mỗi luồng công việc đại diện nhất trong hệ thống (${WORKFLOW_COUNT} luồng):

#### 1. Tổng Quan Luồng Công Việc

- Cung cấp tên và mô tả ngắn gọn về luồng công việc
- Giải thích mục đích nghiệp vụ mà nó phục vụ
- Xác định hành động hoặc sự kiện kích hoạt
- Liệt kê tất cả các tệp/lớp liên quan trong toàn bộ luồng công việc

#### 2. Triển Khai Điểm Vào (Entry Point)

**Điểm Vào API:**

```
${ENTRY_POINT == "API" || ENTRY_POINT == "Tự động phát hiện" ?
  "- Tài liệu hóa lớp API controller và phương thức nhận yêu cầu
   - Hiển thị chữ ký phương thức hoàn chỉnh bao gồm các thuộc tính/chú thích
   - Bao gồm định nghĩa lớp DTO/model của yêu cầu đầy đủ
   - Tài liệu hóa các thuộc tính xác thực và các trình xác thực tùy chỉnh
   - Hiển thị các thuộc tính và kiểm tra xác thực/ủy quyền" : ""}
```

**Điểm Vào GraphQL:**

```
${ENTRY_POINT == "GraphQL" || ENTRY_POINT == "Tự động phát hiện" ?
  "- Tài liệu hóa lớp GraphQL resolver và phương thức
   - Hiển thị định nghĩa schema hoàn chỉnh cho query/mutation
   - Bao gồm các định nghĩa kiểu đầu vào
   - Hiển thị việc triển khai phương thức resolver với xử lý tham số" : ""}
```

**Điểm Vào Frontend:**

```
${ENTRY_POINT == "Frontend" || ENTRY_POINT == "Tự động phát hiện" ?
  "- Tài liệu hóa thành phần khởi tạo lệnh gọi API
   - Hiển thị trình xử lý sự kiện kích hoạt yêu cầu
   - Bao gồm phương thức dịch vụ client API
   - Hiển thị mã quản lý trạng thái liên quan đến yêu cầu" : ""}
```

**Điểm Vào Xử Lý Tin Nhắn (Message Consumer):**

```
${ENTRY_POINT == "Message Consumer" || ENTRY_POINT == "Tự động phát hiện" ?
  "- Tài liệu hóa lớp và phương thức xử lý tin nhắn
   - Hiển thị cấu hình đăng ký tin nhắn
   - Bao gồm định nghĩa model tin nhắn hoàn chỉnh
   - Hiển thị logic giải tuần tự hóa và xác thực" : ""}
```

#### 3. Triển Khai Lớp Dịch Vụ (Service Layer)

- Tài liệu hóa mỗi lớp dịch vụ liên quan cùng với các phụ thuộc của chúng
- Hiển thị chữ ký phương thức hoàn chỉnh với các tham số và kiểu trả về
- Bao gồm các triển khai phương thức thực tế với logic nghiệp vụ chính
- Tài liệu hóa các định nghĩa interface nếu có
- Hiển thị các mẫu đăng ký dependency injection

**Các Mẫu CQRS:**

```
${ARCHITECTURE_PATTERN == "CQRS" || ARCHITECTURE_PATTERN == "Tự động phát hiện" ?
  "- Bao gồm các triển khai command/query handler hoàn chỉnh" : ""}
```

**Các Mẫu Kiến Trúc Sạch (Clean Architecture):**

```
${ARCHITECTURE_PATTERN == "Clean" || ARCHITECTURE_PATTERN == "Tự động phát hiện" ?
  "- Hiển thị các triển khai use case/interactor" : ""}
```

#### 4. Các Mẫu Ánh Xạ Dữ Liệu (Data Mapping)

- Tài liệu hóa mã ánh xạ từ DTO sang model domain
- Hiển thị cấu hình của object mapper hoặc các phương thức ánh xạ thủ công
- Bao gồm logic xác thực trong quá trình ánh xạ
- Tài liệu hóa bất kỳ sự kiện domain nào được tạo ra trong quá trình ánh xạ

#### 5. Triển Khai Truy Cập Dữ Liệu (Data Access)

- Tài liệu hóa các interface repository và các triển khai của chúng
- Hiển thị chữ ký phương thức hoàn chỉnh với các tham số và kiểu trả về
- Bao gồm các triển khai truy vấn thực tế
- Tài liệu hóa các định nghĩa lớp entity/model với tất cả các thuộc tính
- Hiển thị các mẫu xử lý giao dịch (transaction)

**Các Mẫu Cơ Sở Dữ Liệu SQL:**

```
${PERSISTENCE_TYPE == "Cơ sở dữ liệu SQL" || PERSISTENCE_TYPE == "Tự động phát hiện" ?
  "- Bao gồm các cấu hình ORM, chú thích, hoặc việc sử dụng Fluent API
   - Hiển thị các câu lệnh SQL thực tế hoặc các câu lệnh ORM" : ""}
```

**Các Mẫu Cơ Sở Dữ Liệu NoSQL:**

```
${PERSISTENCE_TYPE == "Cơ sở dữ liệu NoSQL" || PERSISTENCE_TYPE == "Tự động phát hiện" ?
  "- Hiển thị các định nghĩa cấu trúc tài liệu (document)
   - Bao gồm các hoạt động truy vấn/cập nhật tài liệu" : ""}
```

#### 6. Xây Dựng Phản Hồi (Response)

- Tài liệu hóa các định nghĩa lớp DTO/model của phản hồi
- Hiển thị ánh xạ từ các model domain/entity sang các model phản hồi
- Bao gồm logic lựa chọn mã trạng thái (status code)
- Tài liệu hóa cấu trúc và việc tạo ra phản hồi lỗi

#### 7. Các Mẫu Xử Lý Lỗi (Error Handling)

- Tài liệu hóa các loại ngoại lệ (exception) được sử dụng trong luồng công việc
- Hiển thị các mẫu try/catch ở mỗi lớp
- Bao gồm các cấu hình xử lý ngoại lệ toàn cục
- Tài liệu hóa các triển khai ghi log lỗi
- Hiển thị các chính sách thử lại (retry policies) hoặc các mẫu circuit breaker
- Bao gồm các hành động bù trừ (compensating actions) cho các kịch bản thất bại

#### 8. Các Mẫu Xử Lý Bất Đồng Bộ (Asynchronous Processing)

- Tài liệu hóa mã lập lịch công việc nền (background job)
- Hiển thị các triển khai phát hành sự kiện (event publication)
- Bao gồm các mẫu gửi tin nhắn vào hàng đợi
- Tài liệu hóa các triển khai callback hoặc webhook
- Hiển thị cách các hoạt động bất đồng bộ được theo dõi và giám sát

**Phương Pháp Kiểm Thử (Tùy chọn):**

```
${INCLUDE_TEST_PATTERNS ?
  "9. **Phương Pháp Kiểm Thử**
     - Tài liệu hóa các triển khai unit test cho mỗi lớp
     - Hiển thị các mẫu mocking và thiết lập test fixture
     - Bao gồm các triển khai integration test
     - Tài liệu hóa các phương pháp tạo dữ liệu kiểm thử
     - Hiển thị các triển khai kiểm thử API/controller" : ""}
```

**Biểu Đồ Tuần Tự (Sequence Diagram) (Tùy chọn):**

```
${INCLUDE_SEQUENCE_DIAGRAM ?
  "10. **Biểu Đồ Tuần Tự**
      - Tạo một biểu đồ tuần tự chi tiết hiển thị tất cả các thành phần
      - Bao gồm các lệnh gọi phương thức với kiểu tham số
      - Hiển thị các giá trị trả về giữa các thành phần
      - Tài liệu hóa các luồng điều kiện và các đường dẫn lỗi" : ""}
```

#### 11. Quy Ước Đặt Tên

Tài liệu hóa các mẫu nhất quán cho:

- Đặt tên Controller (ví dụ: `EntityNameController`)
- Đặt tên Service (ví dụ: `EntityNameService`)
- Đặt tên Repository (ví dụ: `IEntityNameRepository`)
- Đặt tên DTO (ví dụ: `EntityNameRequest`, `EntityNameResponse`)
- Các mẫu đặt tên phương thức cho các hoạt động CRUD
- Quy ước đặt tên biến
- Các mẫu tổ chức tệp

#### 12. Mẫu Triển Khai (Implementation Templates)

Cung cấp các mẫu mã có thể tái sử dụng cho:

- Tạo một endpoint API mới theo mẫu
- Triển khai một phương thức service mới
- Thêm một phương thức repository mới
- Tạo các lớp model domain mới
- Triển khai xử lý lỗi đúng cách

### Các Mẫu Triển Khai Cụ Thể Theo Công Nghệ

**Các Mẫu Triển Khai .NET (nếu được phát hiện):**

```
${PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Tự động phát hiện" ?
  "- Lớp controller hoàn chỉnh với các thuộc tính, filter, và dependency injection
   - Đăng ký service trong Startup.cs hoặc Program.cs
   - Cấu hình Entity Framework DbContext
   - Triển khai Repository với EF Core hoặc Dapper
   - Cấu hình AutoMapper profile
   - Triển khai Middleware cho các mối quan tâm xuyên suốt (cross-cutting concerns)
   - Các mẫu phương thức mở rộng (extension method)
   - Triển khai Options pattern cho cấu hình
   - Triển khai ghi log với ILogger
   - Triển khai filter hoặc policy xác thực/ủy quyền" : ""}
```

**Các Mẫu Triển Khai Spring (nếu được phát hiện):**

```
${PROJECT_TYPE == "Java" || PROJECT_TYPE == "Spring" || PROJECT_TYPE == "Tự động phát hiện" ?
  "- Lớp controller hoàn chỉnh với các chú thích và dependency injection
   - Triển khai Service với các ranh giới giao dịch (transaction boundaries)
   - Interface và triển khai Repository
   - Các định nghĩa entity JPA với các mối quan hệ
   - Các triển khai lớp DTO
   - Cấu hình Bean và quét thành phần (component scanning)
   - Các triển khai trình xử lý ngoại lệ (exception handler)
   - Các triển khai trình xác thực tùy chỉnh" : ""}
```

**Các Mẫu Triển Khai React (nếu được phát hiện):**

```
${PROJECT_TYPE == "React" || PROJECT_TYPE == "Tự động phát hiện" ?
  "- Cấu trúc component với props và state
   - Các mẫu triển khai Hook (useState, useEffect, custom hooks)
   - Triển khai dịch vụ API
   - Các mẫu quản lý trạng thái (Context, Redux)
   - Các triển khai xử lý form
   - Cấu hình route" : ""}
```

### Hướng Dẫn Triển Khai

Dựa trên các luồng công việc đã được tài liệu hóa, cung cấp hướng dẫn cụ thể để triển khai các tính năng mới:

#### 1. Quy Trình Triển Khai Từng Bước

- Bắt đầu từ đâu khi thêm một tính năng tương tự
- Thứ tự triển khai (ví dụ: model → repository → service → controller)
- Cách tích hợp với các mối quan tâm xuyên suốt hiện có

#### 2. Những Cạm Bẫy Thường Gặp Cần Tránh

- Xác định các khu vực dễ xảy ra lỗi trong triển khai hiện tại
- Lưu ý các cân nhắc về hiệu suất
- Liệt kê các lỗi hoặc vấn đề thường gặp

#### 3. Cơ Chế Mở Rộng

- Tài liệu hóa cách kết nối vào các điểm mở rộng hiện có
- Hiển thị cách thêm hành vi mới mà không sửa đổi mã hiện có
- Giải thích các mẫu tính năng được điều khiển bằng cấu hình

**Kết luận:**
Kết thúc bằng một bản tóm tắt về các mẫu quan trọng nhất cần được tuân theo khi
triển khai các tính năng mới để duy trì sự nhất quán với codebase."
