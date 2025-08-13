---
applyTo: "*"
description: "Các tiêu chuẩn và hướng dẫn phát triển Quarkus"
---

- Hướng dẫn cho các ứng dụng Quarkus chất lượng cao với Java 17 trở lên.

## Bối cảnh dự án

- Phiên bản Quarkus mới nhất: 3.x
- Phiên bản Java: 17 trở lên
- Sử dụng Maven hoặc Gradle để quản lý build.
- Tập trung vào kiến trúc sạch, khả năng bảo trì và hiệu suất.

## Tiêu chuẩn phát triển

- Viết bình luận rõ ràng và ngắn gọn cho mỗi lớp, phương thức và logic phức tạp.
- Sử dụng Javadoc cho các API và phương thức công khai để đảm bảo sự rõ ràng cho người dùng.
- Duy trì một phong cách viết mã nhất quán trong toàn bộ dự án, tuân thủ các quy ước của Java.
- Tuân thủ các tiêu chuẩn và thực tiễn tốt nhất của Quarkus để có hiệu suất và khả năng bảo trì tối ưu.
- Tuân theo các quy ước của Jakarta EE và MicroProfile, đảm bảo sự rõ ràng trong việc tổ chức gói.
- Sử dụng các tính năng của Java 17 trở lên khi thích hợp, chẳng hạn như records và sealed classes.

## Quy ước đặt tên

- Sử dụng PascalCase cho tên lớp (ví dụ: `ProductService`, `ProductResource`).
- Sử dụng camelCase cho tên phương thức và biến (ví dụ: `findProductById`, `isProductAvailable`).
- Sử dụng ALL_CAPS cho hằng số (ví dụ: `DEFAULT_PAGE_SIZE`).

## Quarkus

- Tận dụng Chế độ phát triển (Dev Mode) của Quarkus để chu kỳ phát triển nhanh hơn.
- Thực hiện tối ưu hóa tại thời điểm build bằng cách sử dụng các extension và thực tiễn tốt nhất của Quarkus.
- Cấu hình build native với GraalVM để có hiệu suất tối ưu (ví dụ: sử dụng quarkus-maven-plugin).
- Sử dụng khả năng ghi log của Quarkus (JBoss, SL4J hoặc JUL) để thực hành ghi log nhất quán.

### Các mẫu đặc thù của Quarkus

- Sử dụng `@ApplicationScoped` cho các bean singleton thay vì `@Singleton`
- Sử dụng `@Inject` để tiêm phụ thuộc (dependency injection)
- Ưu tiên sử dụng Panache repository hơn là các JPA repository truyền thống
- Sử dụng `@Transactional` trên các phương thức dịch vụ có sửa đổi dữ liệu
- Áp dụng `@Path` với các đường dẫn endpoint REST có tính mô tả
- Sử dụng `@Consumes(MediaType.APPLICATION_JSON)` và `@Produces(MediaType.APPLICATION_JSON)` cho các tài nguyên REST

### Tài nguyên REST

- Luôn sử dụng các annotation của JAX-RS (`@Path`, `@GET`, `@POST`, v.v.)
- Trả về các mã trạng thái HTTP phù hợp (200, 201, 400, 404, 500)
- Sử dụng lớp `Response` cho các phản hồi phức tạp
- Bao gồm xử lý lỗi phù hợp với các khối try-catch
- Xác thực các tham số đầu vào bằng cách sử dụng các annotation của Bean Validation
- Triển khai giới hạn tốc độ (rate limiting) cho các endpoint công khai

### Truy cập dữ liệu

- Ưu tiên sử dụng Panache entity (kế thừa từ `PanacheEntity`) hơn là JPA truyền thống
- Sử dụng Panache repository (`PanacheRepository<T>`) cho các truy vấn phức tạp
- Luôn sử dụng `@Transactional` cho các thao tác sửa đổi dữ liệu
- Sử dụng các truy vấn được đặt tên (named queries) cho các hoạt động cơ sở dữ liệu phức tạp
- Triển khai phân trang phù hợp cho các endpoint trả về danh sách

### Cấu hình

- Sử dụng `application.properties` hoặc `application.yaml` cho cấu hình đơn giản
- Sử dụng `@ConfigProperty` cho các lớp cấu hình an toàn về kiểu
- Ưu tiên sử dụng biến môi trường cho dữ liệu nhạy cảm
- Sử dụng các profile cho các môi trường khác nhau (dev, test, prod)

### Kiểm thử

- Sử dụng `@QuarkusTest` cho kiểm thử tích hợp
- Sử dụng JUnit 5 cho kiểm thử đơn vị
- Sử dụng `@QuarkusIntegrationTest` cho kiểm thử build native
- Mock các phụ thuộc bên ngoài bằng `@QuarkusTestResource`
- Sử dụng RestAssured để kiểm thử endpoint REST (`@QuarkusTestResource`)
- Sử dụng `@Transactional` cho các bài kiểm thử sửa đổi cơ sở dữ liệu
- Sử dụng test-containers cho kiểm thử tích hợp cơ sở dữ liệu

### Không sử dụng các mẫu này:

- Không sử dụng tiêm phụ thuộc qua trường (field injection) trong các bài kiểm thử (sử dụng tiêm phụ thuộc qua hàm khởi tạo)
- Không hardcode các giá trị cấu hình
- Không bỏ qua các ngoại lệ

## Quy trình phát triển

### Khi tạo tính năng mới:

1. Tạo entity với xác thực phù hợp
2. Tạo repository với các truy vấn tùy chỉnh
3. Tạo service với logic nghiệp vụ
4. Tạo tài nguyên REST với các endpoint phù hợp
5. Viết các bài kiểm thử toàn diện
6. Thêm xử lý lỗi phù hợp
7. Cập nhật tài liệu

## Cân nhắc về bảo mật

### Khi triển khai bảo mật:

- Sử dụng các extension bảo mật của Quarkus (ví dụ: `quarkus-smallrye-jwt`, `quarkus-oidc`).
- Triển khai kiểm soát truy cập dựa trên vai trò (RBAC) bằng MicroProfile JWT hoặc OIDC.
- Xác thực tất cả các tham số đầu vào
