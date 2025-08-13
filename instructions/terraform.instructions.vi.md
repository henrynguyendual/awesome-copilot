---
description: "Quy ước và Hướng dẫn Terraform"
applyTo: "**/*.tf"
---

# Quy ước Terraform

## Hướng dẫn Chung

- Sử dụng Terraform để cung cấp và quản lý cơ sở hạ tầng.
- Sử dụng hệ thống quản lý phiên bản cho các cấu hình Terraform của bạn.

## Bảo mật

- Luôn sử dụng phiên bản ổn định mới nhất của Terraform và các nhà cung cấp (provider) của nó.
  - Thường xuyên cập nhật cấu hình Terraform của bạn để tích hợp các bản vá bảo mật và cải tiến.
- Lưu trữ thông tin nhạy cảm một cách an toàn, chẳng hạn như sử dụng AWS Secrets Manager hoặc SSM Parameter Store.
  - Thường xuyên xoay vòng (rotate) thông tin xác thực và bí mật.
  - Tự động hóa việc xoay vòng bí mật, nếu có thể.
- Sử dụng các biến môi trường AWS để tham chiếu các giá trị được lưu trữ trong AWS Secrets Manager hoặc SSM Parameter Store.
  - Điều này giúp giữ các giá trị nhạy cảm khỏi các tệp trạng thái (state file) Terraform của bạn.
- Không bao giờ commit thông tin nhạy cảm như thông tin xác thực AWS, khóa API, mật khẩu, chứng chỉ hoặc trạng thái Terraform vào hệ thống quản lý phiên bản.
  - Sử dụng `.gitignore` để loại trừ các tệp chứa thông tin nhạy cảm khỏi hệ thống quản lý phiên bản.
- Luôn đánh dấu các biến nhạy cảm là `sensitive = true` trong cấu hình Terraform của bạn.
  - Điều này ngăn các giá trị nhạy cảm hiển thị trong kết quả của `terraform plan` hoặc `apply`.
- Sử dụng vai trò (role) và chính sách (policy) IAM để kiểm soát quyền truy cập vào tài nguyên.
  - Tuân theo nguyên tắc đặc quyền tối thiểu (principle of least privilege) khi gán quyền.
- Sử dụng các nhóm bảo mật (security group) và ACL mạng (network ACL) để kiểm soát quyền truy cập mạng vào tài nguyên.
- Triển khai tài nguyên trong các mạng con riêng (private subnet) bất cứ khi nào có thể.
  - Chỉ sử dụng các mạng con công cộng (public subnet) cho các tài nguyên yêu cầu truy cập internet trực tiếp, chẳng hạn như bộ cân bằng tải (load balancer) hoặc cổng NAT (NAT gateway).
- Sử dụng mã hóa cho dữ liệu nhạy cảm ở trạng thái nghỉ (at rest) và đang truyền (in transit).
  - Bật mã hóa cho các ổ đĩa EBS, bucket S3 và các phiên bản RDS.
  - Sử dụng TLS để giao tiếp giữa các dịch vụ.
- Thường xuyên xem xét và kiểm tra các cấu hình Terraform của bạn để tìm các lỗ hổng bảo mật.
  - Sử dụng các công cụ như `trivy`, `tfsec`, hoặc `checkov` để quét các cấu hình Terraform của bạn nhằm tìm ra các vấn đề bảo mật.

## Tính Mô-đun (Modularity)

- Sử dụng các dự án riêng biệt cho từng thành phần chính của cơ sở hạ tầng; điều này:
  - Giảm độ phức tạp
  - Giúp quản lý và bảo trì cấu hình dễ dàng hơn
  - Tăng tốc các hoạt động `plan` và `apply`
  - Cho phép phát triển và triển khai các thành phần một cách độc lập
  - Giảm nguy cơ thay đổi vô tình đối với các tài nguyên không liên quan
- Sử dụng các mô-đun (module) để tránh lặp lại cấu hình.
  - Sử dụng mô-đun để đóng gói các tài nguyên và cấu hình liên quan.
  - Sử dụng mô-đun để đơn giản hóa các cấu hình phức tạp và cải thiện khả năng đọc.
  - Tránh các phụ thuộc vòng tròn (circular dependencies) giữa các mô-đun.
  - Tránh các lớp trừu tượng không cần thiết; chỉ sử dụng mô-đun khi chúng mang lại giá trị.
    - Tránh sử dụng mô-đun cho các tài nguyên đơn lẻ; chỉ sử dụng chúng cho các nhóm tài nguyên liên quan.
    - Tránh lồng ghép các mô-đun quá mức; giữ cho hệ thống phân cấp mô-đun nông.
- Sử dụng các khối `output` để hiển thị thông tin quan trọng về cơ sở hạ tầng của bạn.
  - Sử dụng output để cung cấp thông tin hữu ích cho các mô-đun khác hoặc cho người dùng cấu hình.
  - Tránh để lộ thông tin nhạy cảm trong output; đánh dấu output là `sensitive = true` nếu chúng chứa dữ liệu nhạy cảm.

## Khả năng bảo trì (Maintainability)

- Ưu tiên khả năng đọc, sự rõ ràng và khả năng bảo trì.
- Sử dụng nhận xét (comment) để giải thích các cấu hình phức tạp và lý do tại sao một số quyết định thiết kế được đưa ra.
- Viết các cấu hình ngắn gọn, hiệu quả và đúng chuẩn để dễ hiểu.
- Tránh sử dụng các giá trị được mã hóa cứng (hard-coded); thay vào đó hãy sử dụng biến (variable) để cấu hình.
  - Đặt giá trị mặc định cho các biến, khi thích hợp.
- Sử dụng các nguồn dữ liệu (data source) để truy xuất thông tin về các tài nguyên hiện có thay vì yêu cầu cấu hình thủ công.
  - Điều này làm giảm nguy cơ lỗi, đảm bảo rằng các cấu hình luôn được cập nhật và cho phép các cấu hình thích ứng với các môi trường khác nhau.
  - Tránh sử dụng nguồn dữ liệu cho các tài nguyên được tạo trong cùng một cấu hình; thay vào đó hãy sử dụng output.
  - Tránh hoặc loại bỏ các nguồn dữ liệu không cần thiết; chúng làm chậm các hoạt động `plan` và `apply`.
- Sử dụng `locals` cho các giá trị được sử dụng nhiều lần để đảm bảo tính nhất quán.

## Phong cách và Định dạng

- Tuân theo các phương pháp hay nhất của Terraform để đặt tên và tổ chức tài nguyên.
  - Sử dụng tên mô tả cho tài nguyên, biến và output.
  - Sử dụng quy ước đặt tên nhất quán trên tất cả các cấu hình.
- Tuân theo **Hướng dẫn Phong cách Terraform (Terraform Style Guide)** để định dạng.
  - Sử dụng thụt lề nhất quán (2 dấu cách cho mỗi cấp).
- Nhóm các tài nguyên liên quan lại với nhau trong cùng một tệp.
  - Sử dụng quy ước đặt tên nhất quán cho các nhóm tài nguyên (ví dụ: `providers.tf`, `variables.tf`, `network.tf`, `ecs.tf`, `mariadb.tf`).
- Đặt các khối `depends_on` ở ngay đầu định nghĩa tài nguyên để làm rõ các mối quan hệ phụ thuộc.
  - Chỉ sử dụng `depends_on` khi cần thiết để tránh các phụ thuộc vòng tròn.
- Đặt các khối `for_each` và `count` ở đầu định nghĩa tài nguyên để làm rõ logic khởi tạo của tài nguyên.
  - Sử dụng `for_each` cho các tập hợp và `count` cho các vòng lặp số.
  - Đặt chúng sau các khối `depends_on`, nếu có.
- Đặt các khối `lifecycle` ở cuối định nghĩa tài nguyên.
- Sắp xếp các nhà cung cấp, biến, nguồn dữ liệu, tài nguyên và output theo thứ tự bảng chữ cái trong mỗi tệp để dễ dàng điều hướng.
- Nhóm các thuộc tính liên quan lại với nhau trong các khối.
  - Đặt các thuộc tính bắt buộc trước các thuộc tính tùy chọn và nhận xét từng phần tương ứng.
  - Phân tách các phần thuộc tính bằng các dòng trống để cải thiện khả năng đọc.
  - Sắp xếp các thuộc tính theo thứ tự bảng chữ cái trong mỗi phần để dễ dàng điều hướng.
- Sử dụng các dòng trống để phân tách các phần logic của cấu hình của bạn.
- Sử dụng `terraform fmt` để tự động định dạng cấu hình của bạn.
- Sử dụng `terraform validate` để kiểm tra lỗi cú pháp và đảm bảo cấu hình hợp lệ.
- Sử dụng `tflint` để kiểm tra các vi phạm về phong cách và đảm bảo cấu hình tuân theo các phương pháp hay nhất.
  - Chạy `tflint` thường xuyên để phát hiện sớm các vấn đề về phong cách trong quá trình phát triển.

## Tài liệu

- Luôn bao gồm các thuộc tính `description` và `type` cho các biến và output.
  - Sử dụng mô tả rõ ràng và ngắn gọn để giải thích mục đích của mỗi biến và output.
  - Sử dụng các kiểu phù hợp cho các biến (ví dụ: `string`, `number`, `bool`, `list`, `map`).
- Ghi lại tài liệu cho các cấu hình Terraform của bạn bằng cách sử dụng nhận xét, khi thích hợp.
  - Sử dụng nhận xét để giải thích mục đích của tài nguyên và biến.
  - Sử dụng nhận xét để giải thích các cấu hình hoặc quyết định phức tạp.
  - Tránh các nhận xét thừa; nhận xét nên bổ sung giá trị và sự rõ ràng.
- Bao gồm một tệp `README.md` trong mỗi dự án để cung cấp tổng quan về dự án và cấu trúc của nó.
  - Bao gồm hướng dẫn thiết lập và sử dụng các cấu hình.
- Sử dụng `terraform-docs` để tự động tạo tài liệu cho các cấu hình của bạn.

## Kiểm thử (Testing)

- Viết các bài kiểm thử để xác thực chức năng của các cấu hình Terraform của bạn.
  - Sử dụng phần mở rộng `.tftest.hcl` cho các tệp kiểm thử.
  - Viết các bài kiểm thử để bao quát cả các kịch bản tích cực và tiêu cực.
  - Đảm bảo các bài kiểm thử là lũy đẳng (idempotent) và có thể chạy nhiều lần mà không
