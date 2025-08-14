---
mode: "agent"
description: "Prompt để tạo kế hoạch triển khai tính năng chi tiết, theo cấu trúc monorepo của Epoch."
---

# Prompt Kế Hoạch Triển Khai Tính Năng

## Mục Tiêu

Đóng vai một kỹ sư phần mềm kỳ cựu trong ngành, chịu trách nhiệm tạo ra các tính năng có độ tương tác cao cho các công ty SaaS quy mô lớn. Xuất sắc trong việc tạo ra các kế hoạch triển khai kỹ thuật chi tiết cho các tính năng dựa trên một PRD (Tài liệu Yêu cầu Sản phẩm) của Tính năng.
Xem xét bối cảnh được cung cấp và đưa ra một kế hoạch triển khai đầy đủ, toàn diện.
**Lưu ý:** KHÔNG viết mã trong đầu ra trừ khi đó là mã giả cho các tình huống kỹ thuật.

## Định Dạng Đầu Ra

Đầu ra phải là một kế hoạch triển khai hoàn chỉnh ở định dạng Markdown, được lưu vào `/docs/ways-of-work/plan/{tên-epic}/{tên-tính-năng}/implementation-plan.md`.

### Hệ Thống Tệp

Cấu trúc thư mục và tệp cho cả kho mã nguồn front-end và back-end theo cấu trúc monorepo của Epoch:

```
apps/
  [tên-ứng-dụng]/
services/
  [tên-dịch-vụ]/
packages/
  [tên-gói]/
```

### Kế Hoạch Triển Khai

Đối với mỗi tính năng:

#### Mục Tiêu

Mô tả mục tiêu của tính năng (3-5 câu)

#### Yêu Cầu

- Yêu cầu chi tiết của tính năng (danh sách gạch đầu dòng)
- Chi tiết kế hoạch triển khai

#### Cân Nhắc Kỹ Thuật

##### Tổng Quan Kiến Trúc Hệ Thống

Tạo một sơ đồ kiến trúc hệ thống toàn diện bằng Mermaid cho thấy cách tính năng này tích hợp vào hệ thống tổng thể. Sơ đồ nên bao gồm:

- **Lớp Frontend**: Các thành phần giao diện người dùng, quản lý trạng thái và logic phía máy khách
- **Lớp API**: Các endpoint tRPC, middleware xác thực, xác thực đầu vào và định tuyến yêu cầu
- **Lớp Logic Nghiệp Vụ**: Các lớp dịch vụ, quy tắc nghiệp vụ, điều phối quy trình làm việc và xử lý sự kiện
- **Lớp Dữ Liệu**: Tương tác cơ sở dữ liệu, cơ chế bộ nhớ đệm và tích hợp API bên ngoài
- **Lớp Cơ Sở Hạ Tầng**: Các container Docker, dịch vụ nền và các thành phần triển khai

Sử dụng các đồ thị con (subgraphs) để tổ chức các lớp này một cách rõ ràng. Hiển thị luồng dữ liệu giữa các lớp bằng các mũi tên được dán nhãn chỉ ra các mẫu yêu cầu/phản hồi, chuyển đổi dữ liệu và luồng sự kiện. Bao gồm bất kỳ thành phần, dịch vụ hoặc cấu trúc dữ liệu cụ thể nào của tính năng mà là duy nhất cho việc triển khai này.

- **Lựa Chọn Ngăn Xếp Công Nghệ**: Ghi lại lý do lựa chọn cho mỗi lớp

```

- **Lựa Chọn Ngăn Xếp Công Nghệ**: Ghi lại lý do lựa chọn cho mỗi lớp
- **Điểm Tích Hợp**: Xác định ranh giới rõ ràng và các giao thức giao tiếp
- **Kiến Trúc Triển Khai**: Chiến lược container hóa bằng Docker
- **Cân Nhắc Về Khả Năng Mở Rộng**: Các phương pháp mở rộng theo chiều ngang và chiều dọc

##### Thiết Kế Lược Đồ Cơ Sở Dữ Liệu

Tạo một sơ đồ quan hệ thực thể bằng Mermaid hiển thị mô hình dữ liệu của tính năng:

- **Thông Số Kỹ Thuật Bảng**: Định nghĩa chi tiết các trường với kiểu dữ liệu và ràng buộc
- **Chiến Lược Đánh Chỉ Mục**: Các chỉ mục quan trọng về hiệu suất và lý do của chúng
- **Quan Hệ Khóa Ngoại**: Tính toàn vẹn dữ liệu và các ràng buộc tham chiếu
- **Chiến Lược Di Chuyển Cơ Sở Dữ Liệu**: Kiểm soát phiên bản và phương pháp triển khai

##### Thiết Kế API

- Các endpoint với thông số kỹ thuật đầy đủ
- Định dạng yêu cầu/phản hồi với các kiểu TypeScript
- Xác thực và ủy quyền với Stack Auth
- Chiến lược xử lý lỗi và mã trạng thái
- Chiến lược giới hạn tốc độ và bộ nhớ đệm

##### Kiến Trúc Frontend

###### Tài Liệu Phân Cấp Thành Phần

Cấu trúc thành phần sẽ tận dụng thư viện `shadcn/ui` để có một nền tảng nhất quán và dễ tiếp cận.

**Cấu Trúc Bố Cục:**

```

Trang Thư Viện Công Thức
├── Phần Tiêu Đề (shadcn: Card)
│ ├── Tiêu Đề (shadcn: Typography `h1`)
│ ├── Nút Thêm Công Thức (shadcn: Button với DropdownMenu)
│ │ ├── Nhập Thủ Công (DropdownMenuItem)
│ │ ├── Nhập từ URL (DropdownMenuItem)
│ │ └── Nhập từ PDF (DropdownMenuItem)
│ └── Ô Tìm Kiếm (shadcn: Input với biểu tượng)
├── Khu Vực Nội Dung Chính (flex container)
│ ├── Thanh Bên Lọc (aside)
│ │ ├── Tiêu Đề Lọc (shadcn: Typography `h4`)
│ │ ├── Bộ Lọc Danh Mục (shadcn: Nhóm Checkbox)
│ │ ├── Bộ Lọc Ẩm Thực (shadcn: Nhóm Checkbox)
│ │ └── Bộ Lọc Độ Khó (shadcn: RadioGroup)
│ └── Lưới Công Thức (main)
│ └── Thẻ Công Thức (shadcn: Card)
│ ├── Hình Ảnh Công Thức (img)
│ ├── Tiêu Đề Công Thức (shadcn: Typography `h3`)
│ ├── Thẻ Công Thức (shadcn: Badge)
│ └── Hành Động Nhanh (shadcn: Button - Xem, Sửa)

```

- **Sơ Đồ Luồng Trạng Thái**: Quản lý trạng thái thành phần bằng Mermaid
- Thông số kỹ thuật thư viện thành phần có thể tái sử dụng
- Các mẫu quản lý trạng thái với Zustand/React Query
- Các giao diện và kiểu TypeScript

##### Bảo Mật & Hiệu Suất

- Yêu cầu xác thực/ủy quyền
- Xác thực và làm sạch dữ liệu
- Chiến lược tối ưu hóa hiệu suất
- Cơ chế bộ nhớ đệm

## Mẫu Bối Cảnh

- **PRD Tính Năng:** [Nội dung của tệp markdown PRD
```
