# Trình tạo nhánh Git Flow thông minh

Mô tả: Công cụ phân tích trạng thái (`git status`) và khác biệt
(`git diff`) của git để tạo nhánh phù hợp theo mô hình Git Flow của
nvie.

------------------------------------------------------------------------

## Hướng dẫn

Chỉ cần chạy prompt này và Copilot sẽ phân tích các thay đổi của bạn rồi
tạo nhánh Git Flow phù hợp.

------------------------------------------------------------------------

## Quy trình làm việc

1.  Chạy `git status` để xem trạng thái kho và các file đã thay đổi.
2.  Chạy `git diff` (cho thay đổi chưa staged) hoặc `git diff --cached`
    (cho thay đổi đã staged) để phân tích bản chất thay đổi.
3.  Phân tích thay đổi dựa trên **Khung phân tích Git Flow Branch**.
4.  Xác định loại nhánh phù hợp.
5.  Tạo tên nhánh theo quy ước Git Flow.
6.  Tạo và chuyển sang nhánh đó.
7.  Cung cấp bản tóm tắt phân tích và bước tiếp theo.

------------------------------------------------------------------------

## Khung phân tích Git Flow Branch

**Các loại nhánh:**

-   **Feature**: Tính năng mới, cải tiến không quan trọng.
    -   Bắt đầu từ: `develop`
    -   Merge vào: `develop`
    -   Tên: `feature/tên-mô-tả` hoặc `feature/số-ticket-mô-tả`
    -   Dấu hiệu: tính năng mới, cải thiện UI/UX, API mới, thay đổi DB
        không phá vỡ, tùy chọn config mới, cải thiện hiệu năng không
        quan trọng.
-   **Release**: Chuẩn bị phát hành, nâng version, kiểm tra cuối.
    -   Bắt đầu từ: `develop`
    -   Merge vào: `develop` và `master`
    -   Tên: `release-X.Y.Z`
    -   Dấu hiệu: thay đổi số version, cập nhật build, hoàn thiện tài
        liệu, sửa lỗi nhỏ, cập nhật ghi chú phát hành, khóa version
        dependency.
-   **Hotfix**: Sửa lỗi nghiêm trọng trên production.
    -   Bắt đầu từ: `master`
    -   Merge vào: `develop` và `master`
    -   Tên: `hotfix-X.Y.Z` hoặc `hotfix/mô-tả-lỗi`
    -   Dấu hiệu: sửa lỗ hổng bảo mật, lỗi nghiêm trọng, sửa hỏng dữ
        liệu, khắc phục ngừng dịch vụ, thay đổi cấu hình khẩn cấp.

------------------------------------------------------------------------

## Quy ước đặt tên nhánh

-   **Feature**: `feature/[số-ticket-]tên-mô-tả`
-   **Release**: `release-X.Y.Z`
-   **Hotfix**: `hotfix-X.Y.Z` hoặc `hotfix/mô-tả-nghiêm-trọng`

------------------------------------------------------------------------

## Quy trình phân tích

1.  **Phân tích bản chất thay đổi**:
    -   Xem loại file thay đổi, phạm vi thay đổi, mức độ khẩn cấp.
2.  **Phân loại Git Flow**:
    -   Nếu là sửa lỗi nghiêm trọng → Hotfix.
    -   Nếu là chuẩn bị phát hành → Release.
    -   Ngược lại → Feature.
3.  **Tạo tên nhánh**:
    -   Viết thường, dùng dấu gạch ngang, mô tả rõ mục đích, có thể thêm
        số ticket, ngắn gọn.

------------------------------------------------------------------------

## Trường hợp đặc biệt

-   Thay đổi hỗn hợp → Ưu tiên loại thay đổi chính hoặc tách nhánh.
-   Không có thay đổi → Báo cho người dùng.
-   Đang ở đúng nhánh → Xem xét có cần nhánh mới không.
-   Tên trùng → Thêm hậu tố hoặc gợi ý tên khác.

------------------------------------------------------------------------

## Ví dụ

1.  Thêm API đăng ký user → Feature → `feature/user-registration-api`
2.  Sửa lỗi bảo mật auth → Hotfix → `hotfix/auth-security-patch`
3.  Tăng version 2.1.0 + finalize notes → Release → `release-2.1.0`
4.  Cải thiện query DB → Feature →
    `feature/database-performance-optimization`

------------------------------------------------------------------------

## Danh sách kiểm tra

-   **Trước phân tích**: repo sạch, đúng nhánh nguồn, remote cập nhật.
-   **Chất lượng phân tích**: bao quát toàn bộ file, chọn đúng loại
    nhánh, tên hợp quy tắc, xét case đặc biệt.
-   **An toàn thực thi**: nhánh nguồn tồn tại, tên không trùng, quyền
    tạo nhánh hợp lệ.

------------------------------------------------------------------------

## Thực thi cuối

-   **Tóm tắt phân tích**: trạng thái git, diff, mô tả thay đổi, lý do
    chọn loại nhánh.
-   **Tạo nhánh**: `git checkout -b [branch-name] [source-branch]`, xác
    nhận nhánh mới, gợi ý bước tiếp theo.
-   **Phương án dự phòng**: tên thay thế, cho phép override thủ công.

------------------------------------------------------------------------

## Tham khảo Git Flow

-   **Nhánh chính**: `master` (sẵn sàng phát hành), `develop` (tích hợp
    tính năng mới).
-   **Nhánh hỗ trợ**: Feature (từ develop), Release (từ develop), Hotfix
    (từ master).
-   **Chiến lược merge**: Luôn `--no-ff`, tag khi release, xóa nhánh sau
    merge.
