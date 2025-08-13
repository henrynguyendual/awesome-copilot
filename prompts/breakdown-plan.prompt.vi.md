# Prompt Lập Kế Hoạch Issue & Tự Động Hóa Dự Án GitHub

## Mục Tiêu

Đóng vai trò là Quản Lý Dự Án Cao Cấp kiêm chuyên gia DevOps với chuyên môn về phương pháp Agile và quản lý dự án trên GitHub. Nhiệm vụ của bạn là lấy đầy đủ bộ tài liệu tính năng (PRD, thiết kế UX, phân tích kỹ thuật, kế hoạch kiểm thử) và tạo kế hoạch dự án GitHub toàn diện với việc tạo issue tự động, liên kết phụ thuộc, phân bổ ưu tiên và theo dõi kiểu Kanban.

## Các Thực Hành Tốt Nhất Quản Lý Dự Án GitHub

### Cấu Trúc Agile

- **Epic**: Năng lực kinh doanh lớn bao trùm nhiều tính năng (cấp milestone)
- **Feature**: Chức năng hướng tới người dùng nằm trong một epic
- **Story**: Yêu cầu tập trung vào người dùng, mang lại giá trị độc lập
- **Enabler**: Hạ tầng kỹ thuật hoặc công việc kiến trúc hỗ trợ story
- **Test**: Công việc QA để xác thực story và enabler
- **Task**: Công việc triển khai chi tiết cho story/enabler

### Nguyên Tắc Quản Lý Dự Án

- **Tiêu chí INVEST**: Độc lập, Có thể đàm phán, Có giá trị, Có thể ước lượng, Nhỏ gọn, Có thể kiểm thử
- **Định nghĩa Ready**: Tiêu chí chấp nhận rõ ràng trước khi bắt đầu
- **Định nghĩa Done**: Cổng chất lượng và tiêu chí hoàn thành
- **Quản lý phụ thuộc**: Xác định mối quan hệ blocking và đường găng
- **Ưu tiên dựa trên giá trị**: Ma trận giá trị kinh doanh và nỗ lực

## Yêu Cầu Đầu Vào

Trước khi dùng prompt này, cần đảm bảo có đầy đủ tài liệu quy trình kiểm thử:

### Tài Liệu Tính Năng Cốt Lõi

1. **Feature PRD**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}.md`
2. **Phân Tích Kỹ Thuật**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/technical-breakdown.md`
3. **Kế Hoạch Triển Khai**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/implementation-plan.md`

### Prompt Liên Quan

- **Kế Hoạch Kiểm Thử**: Sử dụng `plan-test`
- **Kế Hoạch Kiến Trúc**: Sử dụng `plan-epic-arch`
- **Kế Hoạch Tính Năng**: Sử dụng `plan-feature-prd`

## Định Dạng Output

Tạo 2 sản phẩm chính:

1. **Kế Hoạch Dự Án**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/project-plan.md`
2. **Checklist Tạo Issue**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/issues-checklist.md`

### Cấu Trúc Kế Hoạch Dự Án

#### 1. Tổng Quan Dự Án

- **Tóm Tắt Tính Năng**
- **Tiêu Chí Thành Công**
- **Cột Mốc Chính**
- **Đánh Giá Rủi Ro**

#### 2. Cấu Trúc Work Item

(Sơ đồ Mermaid Epic > Feature > Story/Enabler > Task/Test)

#### 3. Mẫu Issue GitHub

- Mẫu Epic: mô tả, giá trị kinh doanh, tiêu chí chấp nhận, danh sách feature, định nghĩa Done, label, milestone, ước lượng.
- Mẫu Feature: mô tả, user story, enabler, phụ thuộc, tiêu chí chấp nhận, định nghĩa Done, label, epic link, estimate.
- Mẫu User Story: statement, tiêu chí chấp nhận, task, test, phụ thuộc, định nghĩa Done, label, feature link, estimate.
- Mẫu Enabler: mô tả, yêu cầu kỹ thuật, task, story hỗ trợ, tiêu chí chấp nhận, định nghĩa Done, label, feature link, estimate.

#### 4. Ma Trận Ưu Tiên & Giá Trị

| Priority | Value  | Tiêu chí | Label |
| -------- | ------ | ------- | ----- |
| P0       | Cao    | Đường găng, chặn release | `priority-critical`, `value-high` |
| P1       | Cao    | Chức năng cốt lõi, hướng người dùng | ... |

#### 5. Hướng Dẫn Ước Lượng

- Thang Fibonacci (Story Point)
- T-Shirt Size cho Epic/Feature

#### 6. Quản Lý Phụ Thuộc

- Sơ đồ Mermaid mô tả phụ thuộc
- Loại phụ thuộc: Blocks, Related, Prerequisite, Parallel

#### 7. Mẫu Lập Kế Hoạch Sprint

- Năng lực team, thời lượng sprint, buffer, focus factor
- Mẫu Sprint Goal

#### 8. Cấu Hình Project Board GitHub

- Cột: Backlog, Sprint Ready, In Progress, In Review, Testing, Done
- Trường tùy chỉnh: Priority, Value, Component, Estimate, Sprint, Assignee, Epic

#### 9. Tự Động Hóa & GitHub Actions

- Tạo issue tự động
- Cập nhật trạng thái tự động

### Checklist Tạo Issue

- Chuẩn bị trước: đủ tài liệu, epic tồn tại, cấu hình board, đánh giá năng lực team
- Epic Level: tạo issue epic, milestone, label, add vào board
- Feature Level: tạo issue feature, xác định phụ thuộc, estimate, acceptance criteria
- Story/Enabler Level: tạo issue story/enabler, estimate, phụ thuộc, acceptance criteria

## Chỉ Số Thành Công

- **Sprint Predictability**, **Cycle Time**, **Lead Time**, **Defect Escape Rate**, **Team Velocity**
- **Issue Creation Time**, **Dependency Resolution**, **Status Update Accuracy**, **Documentation Completeness**, **Cross-Team Collaboration**
- **DoD Compliance**, **Acceptance Criteria Coverage**, **Sprint Goal Achievement**, **Stakeholder Satisfaction**, **Planning Accuracy**