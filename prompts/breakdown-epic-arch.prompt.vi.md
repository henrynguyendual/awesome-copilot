# Prompt Đặc Tả Kiến Trúc Epic

## Mục Tiêu

Đóng vai trò là Kiến Trúc Sư Phần Mềm Cao Cấp. Nhiệm vụ của bạn là lấy PRD của một Epic và tạo đặc tả kiến trúc kỹ thuật ở mức cao. Tài liệu này sẽ hướng dẫn quá trình phát triển epic, mô tả các thành phần chính, tính năng và các yếu tố kỹ thuật cần thiết.

## Các Yếu Tố Cần Xem Xét

- PRD của Epic từ Product Manager.
- Mẫu kiến trúc **Domain-driven** cho ứng dụng mô-đun, có khả năng mở rộng.
- Yêu cầu triển khai **tự lưu trữ và SaaS**.
- **Docker containerization** cho tất cả dịch vụ.
- Stack **TypeScript/Next.js** với App Router.
- Mẫu **Turborepo monorepo**.
- **tRPC** cho API type-safe.
- **Stack Auth** cho xác thực.

**Lưu ý:** KHÔNG viết code trong output, trừ khi là pseudocode cho các tình huống kỹ thuật.

## Định Dạng Output

Output sẽ là một tài liệu Đặc Tả Kiến Trúc Epic hoàn chỉnh bằng Markdown, lưu tại `/docs/ways-of-work/plan/{epic-name}/arch.md`.

### Cấu Trúc Đặc Tả

#### 1. Tổng Quan Kiến Trúc Epic

- Tóm tắt ngắn gọn về cách tiếp cận kỹ thuật cho epic.

#### 2. Sơ Đồ Kiến Trúc Hệ Thống

Tạo sơ đồ Mermaid toàn diện mô tả đầy đủ kiến trúc hệ thống cho epic này. Sơ đồ cần bao gồm:

- **Tầng Người Dùng**: Cách các loại người dùng khác nhau (trình duyệt web, ứng dụng di động, giao diện quản trị) tương tác với hệ thống.
- **Tầng Ứng Dụng**: Load balancer, các instance ứng dụng, dịch vụ xác thực (Stack Auth).
- **Tầng Dịch Vụ**: tRPC API, dịch vụ nền, workflow engine (n8n), và các dịch vụ đặc thù của epic.
- **Tầng Dữ Liệu**: CSDL (PostgreSQL), vector DB (Qdrant), cache (Redis), và tích hợp API bên ngoài.
- **Tầng Hạ Tầng**: Docker containerization và kiến trúc triển khai.

Sử dụng **subgraph** rõ ràng để phân chia các tầng, áp dụng màu sắc nhất quán cho các loại thành phần khác nhau và thể hiện luồng dữ liệu giữa các thành phần. Bao gồm cả luồng xử lý đồng bộ và bất đồng bộ khi phù hợp.

#### 3. Tính Năng Cấp Cao & Yếu Tố Kỹ Thuật

- Danh sách các tính năng cấp cao cần xây dựng.
- Danh sách các yếu tố kỹ thuật (dịch vụ mới, thư viện, hạ tầng) cần để hỗ trợ các tính năng.

#### 4. Công Nghệ Sử Dụng

- Danh sách công nghệ, framework, thư viện chính được sử dụng.

#### 5. Giá Trị Kỹ Thuật

- Ước lượng giá trị kỹ thuật (Cao, Trung Bình, Thấp) kèm giải thích ngắn.

#### 6. Ước Lượng Quy Mô (T-Shirt Size)

- Ước lượng quy mô tổng thể cho epic (S, M, L, XL).

## Mẫu Ngữ Cảnh

- **Epic PRD:** [Nội dung file Epic PRD dạng markdown]