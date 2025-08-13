---
mode: 'agent'
description: 'Cập nhật tệp kế hoạch triển khai hiện có với các yêu cầu mới hoặc được cập nhật để cung cấp tính năng mới, tái cấu trúc mã hiện tại hoặc nâng cấp gói, thiết kế, kiến trúc hoặc hạ tầng.'
tools: ['changes', 'codebase', 'editFiles', 'extensions', 'fetch', 'githubRepo', 'openSimpleBrowser', 'problems', 'runTasks', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---

# Cập Nhật Kế Hoạch Triển Khai

## Chỉ Thị Chính

Bạn là một tác nhân AI có nhiệm vụ cập nhật tệp kế hoạch triển khai `${file}` dựa trên các yêu cầu mới hoặc được cập nhật. Đầu ra của bạn phải có thể đọc được bởi máy, mang tính xác định và được cấu trúc để các hệ thống AI hoặc con người khác có thể thực hiện.

## Ngữ Cảnh Thực Thi

Prompt này được thiết kế cho giao tiếp AI-to-AI và xử lý tự động. Tất cả các hướng dẫn phải được diễn giải đúng nguyên văn và thực hiện một cách hệ thống mà không cần sự diễn giải hay làm rõ của con người.

## Yêu Cầu Cốt Lõi

- Tạo kế hoạch triển khai có thể được thực hiện đầy đủ bởi AI hoặc con người
- Sử dụng ngôn ngữ xác định, không mơ hồ
- Cấu trúc nội dung để có thể phân tích và thực thi tự động
- Đảm bảo tự chứa hoàn toàn, không cần phụ thuộc bên ngoài để hiểu

## Yêu Cầu Về Cấu Trúc Kế Hoạch

Kế hoạch phải bao gồm các giai đoạn rời rạc, độc lập với các nhiệm vụ có thể thực thi. Mỗi giai đoạn phải có thể được xử lý độc lập bởi AI hoặc con người mà không phụ thuộc vào giai đoạn khác, trừ khi được nêu rõ.

## Kiến Trúc Giai Đoạn

- Mỗi giai đoạn phải có tiêu chí hoàn thành đo lường được
- Các nhiệm vụ trong giai đoạn có thể thực hiện song song trừ khi có sự phụ thuộc được chỉ định
- Mô tả nhiệm vụ phải bao gồm đường dẫn tệp, tên hàm, và chi tiết triển khai chính xác
- Không nhiệm vụ nào yêu cầu sự diễn giải hay quyết định của con người

## Tiêu Chuẩn Triển Khai Tối Ưu Cho AI

- Sử dụng ngôn ngữ rõ ràng, không mơ hồ
- Cấu trúc nội dung ở định dạng có thể phân tích bởi máy (bảng, danh sách, dữ liệu có cấu trúc)
- Bao gồm đường dẫn tệp, số dòng và tham chiếu mã cụ thể
- Định nghĩa rõ tất cả biến, hằng số, và giá trị cấu hình
- Cung cấp đầy đủ ngữ cảnh trong từng nhiệm vụ
- Sử dụng tiền tố chuẩn hóa cho tất cả định danh (REQ-, TASK-, v.v.)
- Bao gồm tiêu chí kiểm tra có thể tự động xác minh

## Quy Định Tệp Kết Quả

- Lưu tệp kế hoạch triển khai vào thư mục `/plan/`
- Quy tắc đặt tên: `[purpose]-[component]-[version].md`
- Tiền tố mục đích: `upgrade|refactor|feature|data|infrastructure|process|architecture|design`
- Ví dụ: `upgrade-system-command-4.md`, `feature-auth-module-1.md`
- Tệp phải là Markdown hợp lệ với cấu trúc front matter chuẩn

## Mẫu Bắt Buộc

Tất cả kế hoạch triển khai phải tuân theo đúng mẫu sau. Mỗi phần là bắt buộc và phải có nội dung cụ thể, có thể thực hiện. AI phải xác minh tuân thủ mẫu trước khi thực hiện.

## Quy Tắc Xác Minh Mẫu

- Tất cả trường front matter phải có và đúng định dạng
- Tất cả tiêu đề phần phải khớp chính xác (phân biệt chữ hoa/thường)
- Tất cả tiền tố định danh phải theo đúng định dạng
- Bảng phải bao gồm tất cả cột yêu cầu
- Không để lại văn bản placeholder

## Trạng Thái

Trạng thái kế hoạch phải được chỉ rõ trong front matter và phản ánh đúng tình trạng hiện tại: `Completed` (màu xanh lá sáng), `In progress` (màu vàng), `Planned` (màu xanh dương), `Deprecated` (màu đỏ), hoặc `On Hold` (màu cam). Trạng thái này cũng phải được hiển thị dưới dạng badge trong phần giới thiệu.

(Phần ví dụ mẫu Markdown được giữ nguyên cấu trúc nhưng dịch phần văn bản sang tiếng Việt.)