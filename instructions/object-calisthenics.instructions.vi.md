---
applyTo: "**/*.{cs,ts,java}"
description: Thực thi các nguyên tắc Object Calisthenics cho mã nguồn nghiệp vụ (business domain code) để đảm bảo mã sạch, dễ bảo trì và mạnh mẽ
---

# Các Quy Tắc Object Calisthenics

> ⚠️ **Cảnh báo:** Tệp này chứa 9 quy tắc Object Calisthenics gốc. Không được thêm bất kỳ quy tắc bổ sung nào, và không được thay thế hoặc xóa bỏ bất kỳ quy tắc nào trong số này.
> Các ví dụ có thể được thêm vào sau nếu cần.

## Mục Tiêu

Quy tắc này thực thi các nguyên tắc của Object Calisthenics để đảm bảo mã nguồn ở backend sạch, dễ bảo trì và mạnh mẽ, **chủ yếu dành cho mã nguồn nghiệp vụ (business domain code)**.

## Phạm Vi và Áp Dụng

- **Tập trung chính**: Các lớp thuộc miền nghiệp vụ (aggregates, entities, value objects, domain services)
- **Tập trung thứ hai**: Các dịch vụ ở tầng ứng dụng (application layer) và các trình xử lý trường hợp sử dụng (use case handlers)
- **Ngoại lệ**:
  - DTOs (Data Transfer Objects)
  - Các mô hình/hợp đồng API (API models/contracts)
  - Các lớp cấu hình (Configuration classes)
  - Các đối tượng chứa dữ liệu đơn giản không có logic nghiệp vụ
  - Mã nguồn thuộc tầng cơ sở hạ tầng (infrastructure) nơi cần sự linh hoạt

## Các Nguyên Tắc Chính

1. **Một Cấp Thụt Lề cho Mỗi Phương Thức**:

   - Đảm bảo các phương thức đơn giản và không vượt quá một cấp thụt lề.

   ```csharp
   // Ví dụ tồi - phương thức này có nhiều cấp thụt lề
   public void SendNewsletter() {
         foreach (var user in users) {
            if (user.IsActive) {
               // Làm gì đó
               mailer.Send(user.Email);
            }
         }
   }
   // Ví dụ tốt - Tách phương thức để giảm thụt lề
   public void SendNewsletter() {
       foreach (var user in users) {
           SendEmail(user);
       }
   }
   private void SendEmail(User user) {
       if (user.IsActive) {
           mailer.Send(user.Email);
       }
   }

   // Ví dụ tốt - Lọc người dùng trước khi gửi email
   public void SendNewsletter() {
       var activeUsers = users.Where(user => user.IsActive);

       foreach (var user in activeUsers) {
           mailer.Send(user.Email);
       }
   }
   ```

2. **Không Sử Dụng Từ Khóa ELSE**:

   - Tránh sử dụng từ khóa `else` để giảm độ phức tạp và cải thiện khả năng đọc.
   - Sử dụng return sớm (early returns) để xử lý các điều kiện.
   - Sử dụng nguyên tắc Fail Fast (Thất bại nhanh).
   - Sử dụng Guard Clauses để xác thực đầu vào và các điều kiện ở đầu phương thức.

   ```csharp
   // Ví dụ tồi - Sử dụng else
   public void ProcessOrder(Order order) {
       if (order.IsValid) {
           // Xử lý đơn hàng
       } else {
           // Xử lý đơn hàng không hợp lệ
       }
   }
   // Ví dụ tốt - Tránh sử dụng else
   public void ProcessOrder(Order order) {
       if (!order.IsValid) return;
       // Xử lý đơn hàng
   }
   ```

   Ví dụ về nguyên tắc Fail Fast:

   ```csharp
   public void ProcessOrder(Order order) {
       if (order == null) throw new ArgumentNullException(nameof(order));
       if (!order.IsValid) throw new InvalidOperationException("Đơn hàng không hợp lệ");
       // Xử lý đơn hàng
   }
   ```

3. **Bọc Tất Cả Các Kiểu Dữ Liệu Nguyên Thủy và Chuỗi**:

   - Tránh sử dụng trực tiếp các kiểu dữ liệu nguyên thủy trong mã của bạn.
   - Bọc chúng trong các lớp để cung cấp ngữ cảnh và hành vi có ý nghĩa.

   ```csharp
   // Ví dụ tồi - Sử dụng trực tiếp các kiểu dữ liệu nguyên thủy
   public class User {
       public string Name { get; set; }
       public int Age { get; set; }
   }
   // Ví dụ tốt - Bọc các kiểu dữ liệu nguyên thủy
   public class User {
       private string name;
       private Age age;
       public User(string name, Age age) {
           this.name = name;
           this.age = age;
       }
   }
   public class Age {
       private int value;
       public Age(int value) {
           if (value < 0) throw new ArgumentOutOfRangeException(nameof(value), "Tuổi không thể âm");
           this.value = value;
       }
   }
   ```

4. **First Class Collections (Bộ Sưu Tập Hạng Nhất)**:
   - Sử dụng các bộ sưu tập để đóng gói dữ liệu và hành vi, thay vì để lộ các cấu trúc dữ liệu thô.
     First Class Collections: một lớp chứa một mảng như một thuộc tính không nên chứa bất kỳ thuộc tính nào khác.

```csharp
   // Ví dụ tồi - Để lộ bộ sưu tập thô
   public class Group {
      public int Id { get; private set; }
      public string Name { get; private set; }
      public List<User> Users { get; private set; }

      public int GetNumberOfUsersIsActive() {
         return Users
            .Where(user => user.IsActive)
            .Count();
      }
   }

   // Ví dụ tốt - Đóng gói hành vi của bộ sưu tập
   public class Group {
      public int Id { get; private set; }
      public string Name { get; private set; }

      public GroupUserCollection userCollection { get; private set; } // Danh sách người dùng được đóng gói trong một lớp

      public int GetNumberOfUsersIsActive() {
         return userCollection
            .GetActiveUsers()
            .Count();
      }
   }
```

5. **Một Dấu Chấm trên Mỗi Dòng**:

   - Hạn chế số lượng lời gọi phương thức trên một dòng để cải thiện khả năng đọc và bảo trì.

   ```csharp
   // Ví dụ tồi - Nhiều dấu chấm trên một dòng
   public void ProcessOrder(Order order) {
       var userEmail = order.User.GetEmail().ToUpper().Trim();
       // Làm gì đó với userEmail
   }
   // Ví dụ tốt - Một dấu chấm trên mỗi dòng
   public void ProcessOrder(Order order) {
       var user = order.User;
       var email = user.GetEmail();
       var userEmail = email.ToUpper().Trim();
       // Làm gì đó với userEmail
   }
   ```

6. **Không Viết Tắt**:

   - Sử dụng tên có ý nghĩa cho các lớp, phương thức và biến.
   - Tránh viết tắt có thể gây nhầm lẫn.

   ```csharp
   // Ví dụ tồi - Tên viết tắt
   public class U {
       public string N { get; set; }
   }
   // Ví dụ tốt - Tên có ý nghĩa
   public class User {
       public string Name { get; set; }
   }
   ```

7. **Giữ các thực thể nhỏ (Lớp, phương thức, namespace hoặc package)**:

   - Hạn chế kích thước của các lớp và phương thức để cải thiện khả năng đọc và bảo trì mã.
   - Mỗi lớp nên có một trách nhiệm duy nhất và càng nhỏ càng tốt.

   Các ràng buộc:

   - Tối đa 10 phương thức mỗi lớp
   - Tối đa 50 dòng mỗi lớp
   - Tối đa 10 lớp mỗi package hoặc namespace

   ```csharp
   // Ví dụ tồi - Lớp lớn với nhiều trách nhiệm
   public class UserManager {
       public void CreateUser(string name) { /*...*/ }
       public void DeleteUser(int id) { /*...*/ }
       public void SendEmail(string email) { /*...*/ }
   }

   // Ví dụ tốt - Các lớp nhỏ với trách nhiệm duy nhất
   public class UserCreator {
       public void CreateUser(string name) { /*...*/ }
   }
   public class UserDeleter {
       public void DeleteUser(int id) { /*...*/ }
   }

   public class UserUpdater {
       public void UpdateUser(int id, string name) { /*...*/ }
   }
   ```

8. **Không có Lớp nào có nhiều hơn Hai Biến Thể Hiện (Instance Variables)**:

   - Khuyến khích các lớp có một trách nhiệm duy nhất bằng cách giới hạn số lượng biến thể hiện.
   - Giới hạn số lượng biến thể hiện là hai để duy trì sự đơn giản.
   - Không tính ILogger hoặc bất kỳ logger nào khác là biến thể hiện.

   ```csharp
   // Ví dụ tồi - Lớp có nhiều biến thể hiện
   public class UserCreateCommandHandler {
      // Tồi: Quá nhiều biến thể hiện
      private readonly IUserRepository userRepository;
      private readonly IEmailService emailService;
      private readonly ILogger logger;
      private readonly ISmsService smsService;

      public UserCreateCommandHandler(IUserRepository userRepository, IEmailService emailService, ILogger logger, ISmsService smsService) {
         this.userRepository = userRepository;
         this.emailService = emailService;
         this.logger = logger;
         this.smsService = smsService;
      }
   }

   // Tốt: Lớp có hai biến thể hiện
   public class UserCreateCommandHandler {
      private readonly IUserRepository userRepository;
      private readonly INotificationService notificationService;
      private readonly ILogger logger; // Biến này không được tính là biến thể hiện

      public UserCreateCommandHandler(IUserRepository userRepository, INotificationService notificationService, ILogger logger) {
         this.userRepository = userRepository;
         this.notificationService = notificationService;
         this.logger = logger;
      }
   }
   ```

9. **Không có Getters/Setters trong các Lớp Miền Nghiệp Vụ (Domain Classes)**:

   - Tránh để lộ các setters cho các thuộc tính trong các lớp miền nghiệp vụ.
   - Sử dụng các hàm khởi tạo private và các phương thức factory tĩnh để tạo đối tượng.
   - **Lưu ý**: Quy tắc này chủ yếu áp dụng cho các lớp miền nghiệp vụ, không phải DTOs hoặc các đối tượng truyền dữ liệu.

   ```csharp
   // Ví dụ tồi - Lớp miền nghiệp vụ với các setters public
   public class User {  // Lớp miền nghiệp vụ
       public string Name { get; set; } // Tránh điều này trong các lớp miền nghiệp vụ
   }

   // Ví dụ tốt - Lớp miền nghiệp vụ với tính đóng gói
   public class User {  // Lớp miền nghiệp vụ
       private string name;
       private User(string name) { this.name = name; }
       public static User Create(string name) => new User(name);
   }

   // Ví dụ chấp nhận được - DTO với các setters public
   public class UserDto {  // DTO - áp dụng ngoại lệ
       public string Name { get; set; } // Chấp nhận được đối với DTOs
   }
   ```

## Hướng Dẫn Triển Khai

- **Các Lớp Miền Nghiệp Vụ (Domain Classes)**:

  - Sử dụng các hàm khởi tạo private và các phương thức factory tĩnh để tạo các thể hiện.
  - Tránh để lộ các setters cho các thuộc tính.
  - Áp dụng nghiêm ngặt tất cả 9 quy tắc cho mã nguồn nghiệp vụ.

- **Tầng Ứng Dụng (Application Layer)**:

  - Áp dụng các quy tắc này cho các trình xử lý trường hợp sử dụng và các dịch vụ ứng dụng.
  - Tập trung vào việc duy trì trách nhiệm duy nhất và các trừu tượng hóa sạch sẽ.

- **DTOs và Các Đối Tượng Dữ Liệu**:

  - Các quy tắc 3 (bọc các kiểu nguyên thủy), 8 (hai biến thể hiện), và 9 (không có getters/setters) có thể được nới lỏng cho DTOs.
  - Các thuộc tính public với getters/setters là chấp nhận được cho các đối tượng truyền dữ liệu.

- **Kiểm Thử (Testing)**:

  - Đảm bảo các bài kiểm thử xác thực hành vi của các đối tượng thay vì trạng thái của chúng.
  - Các lớp kiểm thử có thể có các quy tắc được nới lỏng để dễ đọc và dễ bảo trì.

- **Đánh Giá Mã Nguồn (Code Reviews)**:
  - Thực thi các quy tắc này trong quá trình đánh giá mã nguồn cho mã nghiệp vụ và ứng dụng.
  - Hãy thực tế đối với mã nguồn cơ sở hạ tầng và DTO.

## Tài Liệu Tham Khảo

- [Object Calisthenics - 9 Quy Tắc Gốc của Jeff Bay](https://www.cs.helsinki.fi/u/luontola/tdd-2009/ext/ObjectCalisthenics.pdf)
- [ThoughtWorks - Object Calisthenics](https://www.thoughtworks.com/insights/blog/object-calisthenics)
- [Clean Code: A Handbook of Agile Software Craftsmanship - Robert C. Martin](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
