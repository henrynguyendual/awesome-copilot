---
mode: "agent"
description: "Prompt để tạo kiến trúc kỹ thuật cấp cao cho một Epic, dựa trên Tài liệu Yêu cầu Sản phẩm."
---

# Prompt Đặc tả Kiến trúc Epic

## Mục tiêu

Đóng vai một Kiến trúc sư Phần mềm Cấp cao. Nhiệm vụ của bạn là lấy một PRD của Epic và tạo ra một bản đặc tả kiến trúc kỹ thuật cấp cao. Tài liệu này sẽ hướng dẫn việc phát triển epic, phác thảo các thành phần chính, tính năng và các yếu tố hỗ trợ kỹ thuật cần thiết.

## Các yếu tố cần xem xét trong bối cảnh

- PRD của Epic từ Giám đốc Sản phẩm.
- Mẫu **kiến trúc hướng tên miền (domain-driven architecture)** cho các ứng dụng modular, có khả năng mở rộng.
- Yêu cầu triển khai **tự lưu trữ (self-hosted) và SaaS**.
- **Container hóa bằng Docker** cho tất cả các dịch vụ.
- Stack **TypeScript/Next.js** với App Router.
- Các mẫu **monorepo của Turborepo**.
- **tRPC** cho các API an toàn về kiểu dữ liệu (type-safe).
- **Stack Auth** để xác thực.

**Lưu ý:** KHÔNG viết mã trong đầu ra trừ khi đó là mã giả cho các tình huống kỹ thuật.

## Định dạng đầu ra

Đầu ra phải là một bản Đặc tả Kiến trúc Epic hoàn chỉnh ở định dạng Markdown, được lưu vào `/docs/ways-of-work/plan/{epic-name}/arch.md`.

### Cấu trúc Đặc tả

#### 1. Tổng quan Kiến trúc Epic

- Tóm tắt ngắn gọn về phương pháp tiếp cận kỹ thuật cho epic.

#### 2. Sơ đồ Kiến trúc Hệ thống

Tạo một sơ đồ Mermaid toàn diện minh họa kiến trúc hệ thống hoàn chỉnh cho epic này. Sơ đồ nên bao gồm:

- **Lớp Người dùng (User Layer)**: Hiển thị cách các loại người dùng khác nhau (trình duyệt web, ứng dụng di động, giao diện quản trị) tương tác với hệ thống.
- **Lớp Ứng dụng (Application Layer)**: Mô tả các bộ cân bằng tải, các phiên bản ứng dụng và dịch vụ xác thực (Stack Auth).
- **Lớp Dịch vụ (Service Layer)**: Bao gồm các API tRPC, dịch vụ nền, các công cụ quy trình làm việc (n8n) và bất kỳ dịch vụ nào dành riêng cho epic.
- **Lớp Dữ liệu (Data Layer)**: Hiển thị cơ sở dữ liệu (PostgreSQL), cơ sở dữ liệu vector (Qdrant), các lớp bộ nhớ đệm (Redis) và tích hợp API bên ngoài.
- **Lớp Cơ sở hạ tầng (Infrastructure Layer)**: Thể hiện việc container hóa bằng Docker và kiến trúc triển khai.

Sử dụng các đồ thị con (subgraph) rõ ràng để tổ chức các lớp này, áp dụng mã màu nhất quán cho các loại thành phần khác nhau và hiển thị luồng dữ liệu giữa các thành phần. Bao gồm cả các đường dẫn yêu cầu đồng bộ và các luồng xử lý không đồng bộ có liên quan đến epic.

#### 3. Các tính năng cấp cao & Yếu tố hỗ trợ kỹ thuật

- Một danh sách các tính năng cấp cao sẽ được xây dựng.
- Một danh sách các yếu tố hỗ trợ kỹ thuật (ví dụ: dịch vụ mới, thư viện, cơ sở hạ tầng) cần thiết để hỗ trợ các tính năng.

#### 4. Ngăn xếp Công nghệ (Technology Stack)

- Một danh sách các công nghệ, framework và thư viện chính sẽ được sử dụng.

#### 5. Giá trị Kỹ thuật

- Ước tính giá trị kỹ thuật (ví dụ: Cao, Trung bình, Thấp) kèm theo một lý giải ngắn gọn.

#### 6. Ước tính Kích thước (T-Shirt Size)

- Cung cấp một ước tính kích thước cấp cao cho epic (ví dụ: S, M, L, XL).

## Mẫu Bối cảnh

- **PRD của Epic:** [Nội dung của tệp markdown PRD của Epic]
