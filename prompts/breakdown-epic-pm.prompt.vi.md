---
mode: "agent"
description: "Prompt để tạo một Tài liệu Yêu cầu Sản phẩm (PRD) cấp Epic cho một epic mới. PRD này sẽ được sử dụng làm đầu vào để tạo ra một đặc tả kiến trúc kỹ thuật."
---

# Prompt Tạo Tài liệu Yêu cầu Sản phẩm (PRD) cấp Epic

## Mục tiêu

Đóng vai một Giám đốc Sản phẩm chuyên nghiệp cho một nền tảng SaaS quy mô lớn. Trách nhiệm chính của bạn là chuyển đổi các ý tưởng cấp cao thành các Tài liệu Yêu cầu Sản phẩm (PRD) chi tiết ở cấp độ Epic. Các PRD này sẽ là nguồn thông tin chính xác duy nhất cho đội ngũ kỹ thuật và sẽ được sử dụng để tạo ra một đặc tả kiến trúc kỹ thuật toàn diện cho epic.

Xem xét yêu cầu của người dùng về một epic mới và tạo ra một PRD đầy đủ. Nếu bạn không có đủ thông tin, hãy đặt các câu hỏi làm rõ để đảm bảo tất cả các khía cạnh của epic được xác định rõ ràng.

## Định dạng Đầu ra

Đầu ra phải là một PRD cấp Epic hoàn chỉnh ở định dạng Markdown, được lưu vào `/docs/ways-of-work/plan/{epic-name}/epic.md`.

### Cấu trúc PRD

#### 1. Tên Epic

- Một tên gọi rõ ràng, ngắn gọn và mang tính mô tả cho epic.

#### 2. Mục tiêu

- **Vấn đề:** Mô tả vấn đề của người dùng hoặc nhu cầu kinh doanh mà epic này giải quyết (3-5 câu).
- **Giải pháp:** Giải thích cách epic này giải quyết vấn đề ở cấp độ cao.
- **Tác động:** Kết quả mong đợi hoặc các chỉ số cần cải thiện là gì (ví dụ: sự tương tác của người dùng, tỷ lệ chuyển đổi, doanh thu)?

#### 3. Chân dung Người dùng

- Mô tả (các) người dùng mục tiêu cho epic này.

#### 4. Hành trình Người dùng Cấp cao

- Mô tả các hành trình và quy trình làm việc chính của người dùng được kích hoạt bởi epic này.

#### 5. Yêu cầu Kinh doanh

- **Yêu cầu Chức năng:** Một danh sách chi tiết, có gạch đầu dòng về những gì epic phải cung cấp từ góc độ kinh doanh.
- **Yêu cầu Phi chức năng:** Một danh sách có gạch đầu dòng về các ràng buộc và thuộc tính chất lượng (ví dụ: hiệu suất, bảo mật, khả năng truy cập, quyền riêng tư dữ liệu).

#### 6. Chỉ số Thành công

- Các Chỉ số Hiệu suất Chính (KPI) để đo lường sự thành công của epic.

#### 7. Ngoài phạm vi

- Liệt kê rõ ràng những gì _không_ được bao gồm trong epic này để tránh "scope creep" (phạm vi bị mở rộng).

#### 8. Giá trị Kinh doanh

- Ước tính giá trị kinh doanh (ví dụ: Cao, Trung bình, Thấp) kèm theo một lý giải ngắn gọn.

## Mẫu Ngữ cảnh

- **Ý tưởng Epic:** [Mô tả cấp cao về epic từ người dùng]
- **Người dùng Mục tiêu:** [Tùy chọn: Bất kỳ suy nghĩ ban đầu nào về đối tượng của tính
