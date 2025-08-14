---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems"]
description: "Tạo các endpoint ASP.NET Minimal API với tài liệu OpenAPI phù hợp"
---

# ASP.NET Minimal API với OpenAPI

Mục tiêu của bạn là giúp tôi tạo ra các endpoint ASP.NET Minimal API có cấu trúc tốt với các kiểu dữ liệu chính xác và tài liệu OpenAPI/Swagger đầy đủ.

## Tổ chức API

- Nhóm các endpoint liên quan bằng cách sử dụng extension `MapGroup()`
- Sử dụng bộ lọc endpoint (endpoint filters) cho các mối quan tâm xuyên suốt (cross-cutting concerns)
- Cấu trúc các API lớn hơn với các lớp endpoint riêng biệt
- Cân nhắc sử dụng cấu trúc thư mục dựa trên tính năng (feature-based) cho các API phức tạp

## Các kiểu Yêu cầu (Request) và Phản hồi (Response)

- Định nghĩa rõ ràng các DTO/model cho yêu cầu và phản hồi
- Tạo các lớp model rõ ràng với các thuộc tính xác thực (validation attributes) phù hợp
- Sử dụng kiểu `record` cho các đối tượng yêu cầu/phản hồi bất biến (immutable)
- Sử dụng tên thuộc tính có ý nghĩa, phù hợp với tiêu chuẩn thiết kế API
- Áp dụng `[Required]` và các thuộc tính xác thực khác để thực thi các ràng buộc
- Sử dụng `ProblemDetailsService` và `StatusCodePages` để nhận các phản hồi lỗi tiêu chuẩn

## Xử lý kiểu dữ liệu

- Sử dụng tham số định tuyến (route parameters) có kiểu dữ liệu tường minh (strongly-typed) với liên kết kiểu (type binding) rõ ràng
- Sử dụng `Results<T1, T2>` để đại diện cho nhiều kiểu phản hồi
- Trả về `TypedResults` thay vì `Results` để có các phản hồi có kiểu dữ liệu tường minh
- Tận dụng các tính năng của C# 10+ như chú thích cho phép giá trị null (nullable annotations) và thuộc tính chỉ khởi tạo (init-only properties)

## Tài liệu OpenAPI

- Sử dụng hỗ trợ tài liệu OpenAPI tích hợp sẵn được thêm vào trong .NET 9
- Định nghĩa tóm tắt (summary) và mô tả (description) cho hoạt động (operation)
- Thêm `operationId` bằng cách sử dụng phương thức mở rộng `WithName`
- Thêm mô tả cho các thuộc tính và tham số bằng `[Description()]`
- Thiết lập các kiểu nội dung (content types) phù hợp cho yêu cầu và phản hồi
- Sử dụng bộ biến đổi tài liệu (document transformers) để thêm các yếu tố như máy chủ (servers), thẻ (tags) và lược đồ bảo mật (security schemes)
- Sử dụng bộ biến đổi lược đồ (schema transformers) để áp dụng các tùy chỉnh cho lược
