---
description: "Hướng dẫn tạo mã Terraform hiện đại cho Azure"
applyTo: "**/*.tf"
---

## 1. Sử dụng Terraform và Provider mới nhất

Luôn nhắm đến phiên bản Terraform ổn định mới nhất và các provider của Azure. Trong mã, hãy chỉ định phiên bản Terraform và provider bắt buộc để thực thi điều này. Luôn cập nhật phiên bản provider để nhận các tính năng và bản vá mới.

## 2. Sắp xếp mã nguồn một cách gọn gàng

Cấu trúc các cấu hình Terraform với việc phân tách tệp một cách logic:

- Sử dụng `main.tf` cho các tài nguyên
- Sử dụng `variables.tf` cho các biến đầu vào
- Sử dụng `outputs.tf` cho các giá trị đầu ra
- Tuân thủ các quy ước đặt tên và định dạng nhất quán (`terraform fmt`)

Điều này giúp mã nguồn dễ dàng điều hướng và bảo trì.

## 3. Đóng gói trong các Module

Sử dụng các module Terraform để nhóm các thành phần cơ sở hạ tầng có thể tái sử dụng. Đối với bất kỳ bộ tài nguyên nào sẽ được sử dụng trong nhiều ngữ cảnh:

- Tạo một module với các biến/đầu ra riêng
- Tham chiếu đến nó thay vì sao chép mã
- Điều này thúc đẩy việc tái sử dụng và tính nhất quán

## 4. Tận dụng Biến và Đầu ra

- **Tham số hóa** tất cả các giá trị có thể cấu hình bằng cách sử dụng các biến có kiểu và mô tả
- **Cung cấp giá trị mặc định** khi thích hợp cho các biến tùy chọn
- **Sử dụng các giá trị đầu ra** để hiển thị các thuộc tính chính của tài nguyên cho các module khác hoặc để người dùng tham chiếu
- **Đánh dấu các giá trị nhạy cảm** một cách phù hợp để bảo vệ bí mật

## 5. Lựa chọn Provider (AzureRM vs AzAPI)

- **Sử dụng provider `azurerm`** cho hầu hết các trường hợp – nó cung cấp độ ổn định cao và bao phủ phần lớn các dịch vụ của Azure
- **Chỉ sử dụng provider `azapi`** cho các trường hợp bạn cần:
  - Các tính năng mới nhất của Azure
  - Một tài nguyên chưa được hỗ trợ trong `azurerm`
- **Ghi lại sự lựa chọn** trong các bình luận của mã
- Cả hai provider có thể được sử dụng cùng nhau nếu cần, nhưng hãy ưu tiên `azurerm` khi không chắc chắn

## 6. Phụ thuộc tối thiểu

- **Không thêm** các provider hoặc module bổ sung ngoài phạm vi của dự án mà không có sự xác nhận
- Nếu cần một provider đặc biệt (ví dụ: `random`, `tls`) hoặc một module bên ngoài:
  - Thêm một bình luận để giải thích
  - Đảm bảo người dùng chấp thuận
- Giữ cho ngăn xếp cơ sở hạ tầng gọn gàng và tránh sự phức tạp không cần thiết

## 7. Đảm bảo tính Idempotency (Tính bất biến)

- Viết các cấu hình có thể được áp dụng lặp đi lặp lại với cùng một kết quả
- **Tránh các hành động không có tính idempotency**:
  - Các kịch bản chạy mỗi khi áp dụng
  - Các tài nguyên có thể xung đột nếu được tạo hai lần
- **Kiểm tra bằng cách chạy `terraform apply` nhiều lần** và đảm bảo lần chạy thứ hai không có thay đổi nào
- Sử dụng cài đặt vòng đời tài nguyên hoặc các biểu thức điều kiện để xử lý sự trôi dạt hoặc các thay đổi từ bên ngoài một cách linh hoạt

## 8. Quản lý Trạng thái (State)

- **Sử dụng một backend từ xa** (như Azure Storage với khóa trạng thái) để lưu trữ trạng thái Terraform một cách an toàn
- Cho phép cộng tác nhóm
- **Không bao giờ commit các tệp trạng thái** vào hệ thống quản lý mã nguồn
- Điều này ngăn ngừa xung đột và giữ cho trạng thái cơ sở hạ tầng nhất quán

## 9. Tài liệu hóa và Sơ đồ hóa

- **Duy trì tài liệu được cập nhật**
- **Cập nhật README.md** với bất kỳ biến, đầu ra hoặc hướng dẫn sử dụng mới nào mỗi khi mã thay đổi
- Cân nhắc sử dụng các công cụ như `terraform-docs` để tự động hóa
- **Cập nhật sơ đồ kiến trúc** để phản ánh các thay đổi về cơ sở hạ tầng sau mỗi lần cập nhật quan trọng
- Mã và sơ đồ được tài liệu hóa tốt đảm bảo cả nhóm hiểu rõ về cơ sở hạ tầng

## 10. Xác thực và Kiểm tra các thay đổi

- **Chạy `terraform validate`** và xem lại đầu ra của `terraform plan` trước khi áp dụng các thay đổi
- Phát hiện sớm các lỗi hoặc các sửa đổi không mong muốn
- **Cân nhắc triển khai các kiểm tra tự động**:
  - CI pipeline
  - Pre-commit hooks
  - Thực thi định dạng, kiểm tra mã và xác thực cơ bản
