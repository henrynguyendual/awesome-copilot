# Prompt Kế Hoạch Triển Khai Tính Năng

## Mục Tiêu

Đóng vai trò là kỹ sư phần mềm kỳ cựu trong ngành, chịu trách nhiệm xây dựng các tính năng chất lượng cao cho các công ty SaaS quy mô lớn. Xuất sắc trong việc tạo kế hoạch triển khai kỹ thuật chi tiết cho các tính năng dựa trên PRD của tính năng.
Xem xét ngữ cảnh đã cung cấp và xuất ra một kế hoạch triển khai toàn diện, đầy đủ.
**Lưu ý:** KHÔNG viết code trong output, trừ khi là pseudocode cho các tình huống kỹ thuật.

## Định Dạng Output

Output sẽ là một kế hoạch triển khai hoàn chỉnh ở định dạng Markdown, lưu tại `/docs/ways-of-work/plan/{epic-name}/{feature-name}/implementation-plan.md`.

### Cấu Trúc Thư Mục

Cấu trúc thư mục và file cho cả front-end và back-end theo chuẩn monorepo của Epoch:

```
apps/
  [app-name]/
services/
  [service-name]/
packages/
  [package-name]/
```

### Kế Hoạch Triển Khai

Cho mỗi tính năng:

#### Mục Tiêu

Mô tả mục tiêu tính năng (3-5 câu).

#### Yêu Cầu

- Danh sách chi tiết các yêu cầu của tính năng (gạch đầu dòng)
- Cụ thể hóa kế hoạch triển khai

#### Yếu Tố Kỹ Thuật

##### Tổng Quan Kiến Trúc Hệ Thống

Tạo sơ đồ kiến trúc hệ thống toàn diện bằng Mermaid cho thấy cách tính năng này tích hợp vào toàn hệ thống. Sơ đồ cần bao gồm:

- **Tầng Frontend**: Thành phần giao diện, quản lý state, logic phía client.
- **Tầng API**: Endpoint tRPC, middleware xác thực, xác thực đầu vào, định tuyến request.
- **Tầng Business Logic**: Lớp dịch vụ, quy tắc nghiệp vụ, điều phối workflow, xử lý sự kiện.
- **Tầng Dữ Liệu**: Tương tác DB, cơ chế cache, tích hợp API bên ngoài.
- **Tầng Hạ Tầng**: Docker container, dịch vụ nền, thành phần triển khai.

Sử dụng subgraph để phân tách rõ các tầng. Thể hiện luồng dữ liệu giữa các tầng với mũi tên có nhãn mô tả kiểu request/response, biến đổi dữ liệu, luồng sự kiện. Bao gồm các thành phần, dịch vụ hoặc cấu trúc dữ liệu đặc thù cho tính năng này.

- **Lựa Chọn Công Nghệ**: Giải thích lý do chọn cho từng tầng
- **Điểm Tích Hợp**: Xác định ranh giới và giao tiếp rõ ràng
- **Kiến Trúc Triển Khai**: Chiến lược Docker containerization
- **Khả Năng Mở Rộng**: Chiến lược mở rộng ngang và dọc

##### Thiết Kế Lược Đồ CSDL

Tạo ERD bằng Mermaid thể hiện mô hình dữ liệu của tính năng:

- **Đặc Tả Bảng**: Chi tiết các trường với kiểu và ràng buộc
- **Chiến Lược Indexing**: Index quan trọng và lý do
- **Quan Hệ Khóa Ngoại**: Tính toàn vẹn dữ liệu
- **Chiến Lược Migration**: Quản lý version và triển khai

##### Thiết Kế API

- Endpoint với đặc tả đầy đủ
- Định dạng request/response kèm type TypeScript
- Xác thực và phân quyền với Stack Auth
- Chiến lược xử lý lỗi và mã trạng thái
- Giới hạn tần suất và chiến lược cache

##### Kiến Trúc Frontend

###### Tài Liệu Phân Cấp Thành Phần

Cấu trúc thành phần sẽ sử dụng thư viện `shadcn/ui` để đảm bảo tính nhất quán và khả năng truy cập.

**Cấu Trúc Giao Diện:**

```
Recipe Library Page
├── Header Section (shadcn: Card)
│   ├── Title (shadcn: Typography `h1`)
│   ├── Add Recipe Button (shadcn: Button với DropdownMenu)
│   │   ├── Manual Entry (DropdownMenuItem)
│   │   ├── Import from URL (DropdownMenuItem)
│   │   └── Import from PDF (DropdownMenuItem)
│   └── Search Input (shadcn: Input with icon)
├── Main Content Area (flex container)
│   ├── Filter Sidebar (aside)
│   │   ├── Filter Title (shadcn: Typography `h4`)
│   │   ├── Category Filters (shadcn: Checkbox group)
│   │   ├── Cuisine Filters (shadcn: Checkbox group)
│   │   └── Difficulty Filters (shadcn: RadioGroup)
│   └── Recipe Grid (main)
│       └── Recipe Card (shadcn: Card)
│           ├── Recipe Image (img)
│           ├── Recipe Title (shadcn: Typography `h3`)
│           ├── Recipe Tags (shadcn: Badge)
│           └── Quick Actions (shadcn: Button - View, Edit)
```

- **Sơ Đồ Luồng State**: Quản lý state bằng Mermaid
- Đặc tả thư viện component tái sử dụng
- Mẫu quản lý state với Zustand/React Query
- Interface và type TypeScript

##### Bảo Mật & Hiệu Năng

- Yêu cầu xác thực/phân quyền
- Xác thực và làm sạch dữ liệu
- Chiến lược tối ưu hiệu năng
- Cơ chế cache

## Mẫu Ngữ Cảnh

- **Feature PRD:** [Nội dung file PRD của tính năng]