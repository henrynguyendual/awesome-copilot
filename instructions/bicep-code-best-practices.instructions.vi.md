---
description: "Cơ sở hạ tầng dưới dạng mã với Bicep"
applyTo: "**/*.bicep"
---

## Quy ước đặt tên

- Khi viết mã Bicep, hãy sử dụng kiểu lowerCamelCase cho tất cả các tên (biến, tham số, tài nguyên)
- Sử dụng tên biểu tượng mô tả loại tài nguyên (ví dụ: 'storageAccount' thay vì 'storageAccountName')
- Tránh sử dụng 'name' trong tên biểu tượng vì nó đại diện cho tài nguyên, không phải tên của tài nguyên
- Tránh phân biệt biến và tham số bằng cách sử dụng hậu tố

## Cấu trúc và Khai báo

- Luôn khai báo các tham số ở đầu tệp với decorator @description
- Sử dụng các phiên bản API ổn định mới nhất cho tất cả các tài nguyên
- Sử dụng decorator @description có tính mô tả cho tất cả các tham số
- Chỉ định độ dài ký tự tối thiểu và tối đa cho các tham số đặt tên

## Tham số (Parameters)

- Đặt các giá trị mặc định an toàn cho môi trường thử nghiệm (sử dụng các bậc giá thấp)
- Sử dụng decorator @allowed một cách tiết kiệm để tránh chặn các lần triển khai hợp lệ
- Sử dụng tham số cho các cài đặt thay đổi giữa các lần triển khai

## Biến (Variables)

- Các biến tự động suy ra kiểu từ giá trị được giải quyết
- Sử dụng biến để chứa các biểu thức phức tạp thay vì nhúng chúng trực tiếp vào thuộc tính tài nguyên

## Tham chiếu tài nguyên

- Sử dụng tên biểu tượng để tham chiếu tài nguyên thay vì các hàm reference() hoặc resourceId()
- Tạo các phụ thuộc tài nguyên thông qua tên biểu tượng (resourceA.id) thay vì phụ thuộc tường minh (explicit dependsOn)
- Để truy cập các thuộc tính từ các tài nguyên khác, hãy sử dụng từ khóa 'existing' thay vì truyền giá trị qua các đầu ra (outputs)

## Tên tài nguyên

- Sử dụng các biểu thức mẫu với uniqueString() để tạo tên tài nguyên có ý nghĩa và duy nhất
- Thêm tiền tố vào kết quả của uniqueString() vì một số tài nguyên không cho phép tên bắt đầu bằng số

## Tài nguyên con (Child Resources)

- Tránh lồng các tài nguyên con quá nhiều cấp
- Sử dụng thuộc tính parent hoặc lồng vào nhau thay vì xây dựng tên tài nguyên cho các tài nguyên con

## Bảo mật

- Không bao giờ bao gồm các bí mật hoặc khóa trong các đầu ra (outputs)
- Sử dụng trực tiếp các thuộc tính tài nguyên trong đầu ra (ví dụ: storageAccount.properties.primaryEndpoints)

## Tài liệu

- Thêm các bình luận // hữu ích vào trong các tệp Bicep của bạn để cải thiện khả
