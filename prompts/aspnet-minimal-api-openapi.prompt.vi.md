---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems"]
description: "Tạo các endpoint API Minimal ASP.NET với tài liệu OpenAPI phù hợp"
---

# ASP.NET Minimal API với OpenAPI

Mục tiêu của bạn là giúp tôi tạo các endpoint API Minimal ASP.NET được cấu trúc tốt với các loại đúng và tài liệu OpenAPI/Swagger toàn diện.

## Tổ chức API

- Nhóm các endpoint liên quan bằng cách sử dụng phần mở rộng `MapGroup()`
- Sử dụng các bộ lọc endpoint cho các vấn đề xuyên suốt
- Cấu trúc các API lớn hơn với các lớp endpoint riêng biệt
- Xem xét sử dụng cấu trúc thư mục dựa trên tính năng cho các API phức tạp

## Các Loại Yêu Cầu và Phản Hồi

- Định nghĩa các DTO/mô hình yêu cầu và phản hồi rõ ràng
- Tạo các lớp mô hình rõ ràng với các thuộc tính xác thực phù hợp
- Sử dụng các loại record cho các đối tượng yêu cầu/phản hồi bất biến
- Sử dụng tên thuộc tính có ý nghĩa phù hợp với tiêu chuẩn thiết kế API
- Áp dụng `[Required]` và các thuộc tính xác thực khác để thực thi các ràng buộc
- Sử dụng ProblemDetailsService và StatusCodePages để nhận các phản hồi lỗi tiêu chuẩn

## Xử Lý Loại

- Sử dụng các tham số đường dẫn được gõ mạnh mẽ với ràng buộc loại rõ ràng
- Sử dụng `Results<T1, T2>` để đại diện cho nhiều loại phản hồi
- Trả về `TypedResults` thay vì `Results` cho các phản hồi được gõ mạnh mẽ
- Tận dụng các tính năng C# 10+ như chú thích nullable và thuộc tính chỉ khởi tạo

## Tài Liệu OpenAPI

- Sử dụng hỗ trợ tài liệu OpenAPI tích hợp được thêm vào .NET 9
- Định nghĩa tóm tắt và mô tả hoạt động
- Thêm operationIds bằng cách sử dụng phương thức mở rộng `WithName`
- Thêm mô tả cho các thuộc tính và tham số với `[Description()]`
- Đặt các loại nội dung phù hợp cho yêu cầu và phản hồi
- Sử dụng các bộ chuyển đổi tài liệu để thêm các yếu tố như máy chủ, thẻ và sơ đồ bảo mật
- Sử dụng các bộ chuyển đổi schema để áp dụng các tùy chỉnh cho các schema OpenAPI
