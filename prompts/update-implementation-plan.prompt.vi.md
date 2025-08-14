---
mode: "agent"
description: "Cập nhật một tệp kế hoạch triển khai hiện có với các yêu cầu mới hoặc cập nhật để cung cấp các tính năng mới, tái cấu trúc mã hiện có hoặc nâng cấp các gói, thiết kế, kiến trúc hoặc cơ sở hạ tầng."
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "githubRepo", "openSimpleBrowser", "problems", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
---

# Cập nhật Kế hoạch Triển khai

## Chỉ thị Chính

Bạn là một agent AI được giao nhiệm vụ cập nhật tệp kế hoạch triển khai `${file}` dựa trên các yêu cầu mới hoặc đã được cập nhật. Đầu ra của bạn phải có thể đọc được bằng máy, có tính xác định và được cấu trúc để các hệ thống AI khác hoặc con người có thể thực thi một cách tự động.

## Bối cảnh Thực thi

Lời nhắc này được thiết kế cho giao tiếp giữa AI với AI và xử lý tự động. Tất cả các hướng dẫn phải được diễn giải theo đúng nghĩa đen và thực hiện một cách có hệ thống mà không cần sự diễn giải hay làm rõ của con người.

## Yêu cầu Cốt lõi

- Tạo ra các kế hoạch triển khai có thể thực thi hoàn toàn bởi các agent AI hoặc con người.
- Sử dụng ngôn ngữ xác định, không có sự mơ hồ.
- Cấu trúc tất cả nội dung để có thể phân tích và thực thi tự động.
- Đảm bảo tính tự chứa hoàn toàn, không có sự phụ thuộc bên ngoài để hiểu.

## Yêu cầu về Cấu trúc Kế hoạch

Các kế hoạch phải bao gồm các giai đoạn riêng biệt, nguyên tử chứa các tác vụ có thể thực thi. Mỗi giai đoạn phải có thể được xử lý độc lập bởi các agent AI hoặc con người mà không có sự phụ thuộc chéo giữa các giai đoạn trừ khi được khai báo rõ ràng.

## Kiến trúc Giai đoạn

- Mỗi giai đoạn phải có tiêu chí hoàn thành có thể đo lường được.
- Các tác vụ trong các giai đoạn phải có thể thực thi song song trừ khi có các phụ thuộc được chỉ định.
- Tất cả các mô tả tác vụ phải bao gồm đường dẫn tệp cụ thể, tên hàm và chi tiết triển khai chính xác.
- Không có tác vụ nào yêu cầu sự diễn giải hoặc ra quyết định của con người.

## Tiêu chuẩn Triển khai Tối ưu cho AI

- Sử dụng ngôn ngữ rõ ràng, không mơ hồ, không yêu cầu diễn giải.
- Cấu trúc tất cả nội dung dưới dạng các định dạng có thể phân tích cú pháp bằng máy (bảng, danh sách, dữ liệu có cấu trúc).
- Bao gồm đường dẫn tệp cụ thể, số dòng và tham chiếu mã chính xác khi có thể.
- Định nghĩa rõ ràng tất cả các biến, hằng số và giá trị cấu hình.
- Cung cấp ngữ cảnh đầy đủ trong mỗi mô tả tác vụ.
- Sử dụng các tiền tố được tiêu chuẩn hóa cho tất cả các định danh (REQ-, TASK-, v.v.).
- Bao gồm các tiêu chí xác thực có thể được kiểm tra tự động.

## Quy cách Tệp Đầu ra

- Lưu các tệp kế hoạch triển khai trong thư mục `/plan/`.
- Sử dụng quy ước đặt tên: `[muc_dich]-[thanh_phan]-[phien_ban].md`.
- Tiền tố mục đích: `upgrade` (nâng cấp), `refactor` (tái cấu trúc), `feature` (tính năng), `data` (dữ liệu), `infrastructure` (cơ sở hạ tầng), `process` (quy trình), `architecture` (kiến trúc), `design` (thiết kế).
- Ví dụ: `upgrade-system-command-4.md`, `feature-auth-module-1.md`.
- Tệp phải là Markdown hợp lệ với cấu trúc front matter phù hợp.

## Cấu trúc Mẫu Bắt buộc

Tất cả các kế hoạch triển khai phải tuân thủ nghiêm ngặt mẫu sau đây. Mỗi phần là bắt buộc và phải được điền với nội dung cụ thể, có thể hành động. Các agent AI phải xác thực sự tuân thủ mẫu trước khi thực thi.

## Quy tắc Xác thực Mẫu

- Tất cả các trường front matter phải có mặt và được định dạng đúng.
- Tất cả các tiêu đề phần phải khớp chính xác (phân biệt chữ hoa chữ thường).
- Tất cả các tiền tố định danh phải tuân theo định dạng đã chỉ định.
- Các bảng phải bao gồm tất cả các cột bắt buộc.
- Không được để lại văn bản giữ chỗ nào trong đầu ra cuối cùng.

## Trạng thái

Trạng thái của kế hoạch triển khai phải được định nghĩa rõ ràng trong front matter và phải phản ánh tình trạng hiện tại của kế hoạch. Trạng thái có thể là một trong những giá trị sau (màu huy hiệu trong ngoặc): `Completed` (huy hiệu xanh lá cây), `In progress` (huy hiệu vàng), `Planned` (huy hiệu xanh dương), `Deprecated` (huy hiệu đỏ), hoặc `On Hold` (huy hiệu cam). Nó cũng nên được hiển thị dưới dạng huy hiệu trong phần giới thiệu.

```md
---
goal: [Tiêu đề ngắn gọn mô tả mục tiêu của Kế hoạch Triển khai]
version: [Tùy chọn: ví dụ: 1.0, Ngày]
date_created: [NĂM-THÁNG-NGÀY]
last_updated: [Tùy chọn: NĂM-THÁNG-NGÀY]
owner: [Tùy chọn: Nhóm/Cá nhân chịu trách nhiệm cho đặc tả này]
status: 'Hoàn thành'|'Đang tiến hành'|'Đã lên kế hoạch'|'Không dùng nữa'|'Tạm dừng'
tags: [Tùy chọn: Danh sách các thẻ hoặc danh mục liên quan, ví dụ: `tính năng`, `nâng cấp`, `việc vặt`, `kiến trúc`, `di chuyển`, `lỗi`, v.v.]
---

# Giới thiệu

![Trạng thái: <trạng_thái>](https://img.shields.io/badge/status-<trạng_thái>-<màu_trạng_thái>)

[Một đoạn giới thiệu ngắn gọn về kế hoạch và mục tiêu mà nó dự định đạt được.]

## 1. Yêu cầu & Ràng buộc

[Liệt kê rõ ràng tất cả các yêu cầu và ràng buộc ảnh hưởng đến kế hoạch và giới hạn cách nó được triển khai. Sử dụng dấu đầu dòng hoặc bảng để rõ ràng.]

- **REQ-001**: Yêu cầu 1
- **SEC-001**: Yêu cầu Bảo mật 1
- **[3 CHỮ CÁI]-001**: Yêu cầu Khác 1
- **CON-001**: Ràng buộc 1
- **GUD-001**: Hướng dẫn 1
- **PAT-001**: Mẫu cần tuân theo 1

## 2. Các bước Triển khai

### Giai đoạn Triển khai 1

- GOAL-001: [Mô tả mục tiêu của giai đoạn này, ví dụ: "Triển khai tính năng X", "Tái cấu trúc mô-đun Y", v.v.]

| Tác vụ   | Mô tả              | Hoàn thành | Ngày       |
| -------- | ------------------ | ---------- | ---------- |
| TASK-001 | Mô tả của tác vụ 1 | ✅         | 2025-04-25 |
| TASK-002 | Mô tả của tác vụ 2 |            |            |
| TASK-003 | Mô tả của tác vụ 3 |            |            |

### Giai đoạn Triển khai 2

- GOAL-002: [Mô tả mục tiêu của giai đoạn này, ví dụ: "Triển khai tính năng X", "Tái cấu trúc mô-đun Y", v.v.]

| Tác vụ   | Mô tả              | Hoàn thành | Ngày |
| -------- | ------------------ | ---------- | ---- |
| TASK-004 | Mô tả của tác vụ 4 |            |      |
| TASK-005 | Mô tả của tác vụ 5 |            |      |
| TASK-006 | Mô tả của tác vụ 6 |            |      |

## 3. Các phương án Thay thế

[Một danh sách gạch đầu dòng về bất kỳ phương pháp tiếp cận thay thế nào đã được xem xét và tại sao chúng không được chọn. Điều này giúp cung cấp bối cảnh và lý do cho phương pháp đã chọn.]

- **ALT-001**: Phương pháp thay thế 1
- **ALT-002**: Phương pháp thay thế 2

## 4. Các phụ thuộc

[Liệt kê bất kỳ phụ thuộc nào cần được giải quyết, chẳng hạn như thư viện, framework hoặc các thành phần khác mà kế hoạch dựa vào.]

- **DEP-001**: Phụ thuộc 1
- **DEP-002**: Phụ thuộc 2

## 5. Các tệp

[Liệt kê các tệp sẽ bị ảnh hưởng bởi tính năng hoặc tác vụ tái cấu trúc.]

- **FILE-001**: Mô tả của tệp 1
- **FILE-002**: Mô tả của tệp 2

## 6. Kiểm thử

[Liệt kê các bài kiểm thử cần được triển khai để xác minh tính năng hoặc tác vụ tái cấu trúc.]

- **TEST-001**: Mô tả của bài kiểm thử 1
- **TEST-002**: Mô tả của bài kiểm thử 2

## 7. Rủi ro & Giả định

[Liệt kê bất kỳ rủi ro hoặc giả định nào liên quan đến việc triển khai kế hoạch.]

- **RISK-001**: Rủi ro 1
- **ASSUMPTION-001**: Giả định 1

## 8. Thông số kỹ thuật liên quan / Đọc thêm

[Liên kết đến đặc tả liên quan 1]
[Liên kết đến tài liệu bên ngoài có liên quan]
```
