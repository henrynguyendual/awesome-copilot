---
description: "Trình tạo nhánh Git Flow thông minh, phân tích git status/diff và tạo các nhánh phù hợp theo mô hình phân nhánh Git Flow của nvie."
tools: ["run_in_terminal", "get_terminal_output"]
---

### Hướng dẫn

```xml
<instructions>
    <title>Trình tạo nhánh Git Flow</title>
    <description>Prompt này phân tích các thay đổi git hiện tại của bạn bằng cách sử dụng git status và git diff (hoặc git diff --cached), sau đó xác định một cách thông minh loại nhánh phù hợp theo mô hình phân nhánh Git Flow và tạo ra một tên nhánh có ngữ nghĩa.</description>
    <note>
        Chỉ cần chạy prompt này và Copilot sẽ phân tích các thay đổi của bạn và tạo nhánh Git Flow phù hợp cho bạn.
    </note>
</instructions>
```

### Quy trình làm việc

**Thực hiện theo các bước sau:**

1.  Chạy `git status` để xem lại trạng thái kho lưu trữ hiện tại và các tệp đã thay đổi.
2.  Chạy `git diff` (đối với các thay đổi chưa được staged) hoặc `git diff --cached` (đối với các thay đổi đã được staged) để phân tích bản chất của các thay đổi.
3.  Phân tích các thay đổi bằng cách sử dụng Khung phân tích nhánh Git Flow dưới đây.
4.  Xác định loại nhánh phù hợp dựa trên phân tích.
5.  Tạo một tên nhánh có ngữ nghĩa theo quy ước của Git Flow.
6.  Tự động tạo nhánh và chuyển sang nhánh đó.
7.  Cung cấp một bản tóm tắt về phân tích và các bước tiếp theo.

### Khung phân tích nhánh Git Flow

```xml
<analysis-framework>
    <branch-types>
        <feature>
            <purpose>Tính năng mới, cải tiến, các cải thiện không quan trọng</purpose>
            <branch-from>develop</branch-from>
            <merge-to>develop</merge-to>
            <naming>feature/ten-mo-ta hoặc feature/so-ticket-mo-ta</naming>
            <indicators>
                <indicator>Chức năng mới đang được thêm vào</indicator>
                <indicator>Cải tiến UI/UX</indicator>
                <indicator>Các endpoint hoặc phương thức API mới</indicator>
                <indicator>Bổ sung lược đồ cơ sở dữ liệu (không gây lỗi)</indicator>
                <indicator>Tùy chọn cấu hình mới</indicator>
                <indicator>Cải thiện hiệu suất (không quan trọng)</indicator>
            </indicators>
        </feature>

        <release>
            <purpose>Chuẩn bị phát hành, tăng phiên bản, kiểm thử cuối cùng</purpose>
            <branch-from>develop</branch-from>
            <merge-to>develop VÀ master</merge-to>
            <naming>release-X.Y.Z</naming>
            <indicators>
                <indicator>Thay đổi số phiên bản</indicator>
                <indicator>Cập nhật cấu hình build</indicator>
                <indicator>Hoàn thiện tài liệu</indicator>
                <indicator>Sửa các lỗi nhỏ trước khi phát hành</indicator>
                <indicator>Cập nhật ghi chú phát hành</indicator>
                <indicator>Khóa phiên bản các dependency</indicator>
            </indicators>
        </release>

        <hotfix>
            <purpose>Sửa lỗi nghiêm trọng trên production cần triển khai ngay lập tức</purpose>
            <branch-from>master</branch-from>
            <merge-to>develop VÀ master</merge-to>
            <naming>hotfix-X.Y.Z hoặc hotfix/mo-ta-van-de-nghiem-trong</naming>
            <indicators>
                <indicator>Sửa lỗi lỗ hổng bảo mật</indicator>
                <indicator>Lỗi nghiêm trọng trên production</indicator>
                <indicator>Sửa lỗi hỏng dữ liệu</indicator>
                <indicator>Giải quyết sự cố ngừng dịch vụ</indicator>
                <indicator>Thay đổi cấu hình khẩn cấp</indicator>
            </indicators>
        </hotfix>
    </branch-types>
</analysis-framework>
```

### Quy ước đặt tên nhánh

```xml
<naming-conventions>
    <feature-branches>
        <format>feature/[so-ticket-]ten-mo-ta</format>
        <examples>
            <example>feature/user-authentication</example>
            <example>feature/PROJ-123-shopping-cart</example>
            <example>feature/api-rate-limiting</example>
            <example>feature/dashboard-redesign</example>
        </examples>
    </feature-branches>

    <release-branches>
        <format>release-X.Y.Z</format>
        <examples>
            <example>release-1.2.0</example>
            <example>release-2.1.0</example>
            <example>release-1.0.0</example>
        </examples>
    </release-branches>

    <hotfix-branches>
        <format>hotfix-X.Y.Z HOẶC hotfix/mo-ta-nghiem-trong</format>
        <examples>
            <example>hotfix-1.2.1</example>
            <example>hotfix/security-patch</example>
            <example>hotfix/payment-gateway-fix</example>
            <example>hotfix-2.1.1</example>
        </examples>
    </hotfix-branches>
</naming-conventions>
```

### Quy trình phân tích

```xml
<analysis-process>
    <step-1>
        <title>Phân tích bản chất thay đổi</title>
        <description>Kiểm tra các loại tệp đã sửa đổi và bản chất của các thay đổi</description>
        <criteria>
            <files-modified>Xem xét phần mở rộng của tệp, cấu trúc thư mục và mục đích</files-modified>
            <change-scope>Xác định xem các thay đổi là bổ sung, sửa chữa hay chuẩn bị</change-scope>
            <urgency-level>Đánh giá xem các thay đổi có giải quyết các vấn đề nghiêm trọng hay chỉ là phát triển</urgency-level>
        </criteria>
    </step-1>

    <step-2>
        <title>Phân loại Git Flow</title>
        <description>Ánh xạ các thay đổi vào loại nhánh Git Flow phù hợp</description>
        <decision-tree>
            <question>Đây có phải là các bản sửa lỗi nghiêm trọng cho các vấn đề trên production không?</question>
            <if-yes>Cân nhắc nhánh hotfix</if-yes>
            <if-no>
                <question>Đây có phải là các thay đổi chuẩn bị cho việc phát hành (tăng phiên bản, tinh chỉnh cuối cùng) không?</question>
                <if-yes>Cân nhắc nhánh release</if-yes>
                <if-no>Mặc định là nhánh feature</if-no>
            </if-no>
        </decision-tree>
    </step-2>

    <step-3>
        <title>Tạo tên nhánh</title>
        <description>Tạo tên nhánh có ngữ nghĩa, mang tính mô tả</description>
        <guidelines>
            <use-kebab-case>Sử dụng chữ thường với dấu gạch ngang</use-kebab-case>
            <be-descriptive>Tên phải chỉ ra rõ ràng mục đích</be-descriptive>
            <include-context>Thêm số ticket hoặc ngữ cảnh dự án khi có sẵn</include-context>
            <keep-concise>Tránh các tên quá dài</keep-concise>
        </guidelines>
    </step-3>
</analysis-process>
```

### Các trường hợp đặc biệt và xác thực

```xml
<edge-cases>
    <mixed-changes>
        <scenario>Các thay đổi bao gồm cả tính năng và sửa lỗi</scenario>
        <resolution>Ưu tiên loại thay đổi quan trọng nhất hoặc đề xuất tách thành nhiều nhánh</resolution>
    </mixed-changes>

    <no-changes>
        <scenario>Không phát hiện thay đổi nào trong git status/diff</scenario>
        <resolution>Thông báo cho người dùng và đề nghị kiểm tra git status hoặc thực hiện thay đổi trước</resolution>
    </no-changes>

    <existing-branch>
        <scenario>Đã ở trên một nhánh feature/hotfix/release</scenario>
        <resolution>Phân tích xem có cần nhánh mới hay không hoặc nhánh hiện tại có phù hợp không</resolution>
    </existing-branch>

    <conflicting-names>
        <scenario>Tên nhánh được đề xuất đã tồn tại</scenario>
        <resolution>Thêm hậu tố tăng dần hoặc đề xuất một tên khác</resolution>
    </conflicting-names>
</edge-cases>
```

### Ví dụ

```xml
<examples>
    <example-1>
        <scenario>Đã thêm endpoint API đăng ký người dùng mới</scenario>
        <analysis>Chức năng mới, thay đổi bổ sung, không nghiêm trọng</analysis>
        <branch-type>feature</branch-type>
        <branch-name>feature/user-registration-api</branch-name>
        <command>git checkout -b feature/user-registration-api develop</command>
    </example-1>

    <example-2>
        <scenario>Đã sửa lỗ hổng bảo mật nghiêm trọng trong xác thực</scenario>
        <analysis>Sửa lỗi bảo mật, nghiêm trọng cho production, cần triển khai ngay</analysis>
        <branch-type>hotfix</branch-type>
        <branch-name>hotfix/auth-security-patch</branch-name>
        <command>git checkout -b hotfix/auth-security-patch master</command>
    </example-2>

    <example-3>
        <scenario>Đã cập nhật phiên bản lên 2.1.0 và hoàn thiện ghi chú phát hành</scenario>
        <analysis>Chuẩn bị phát hành, tăng phiên bản, tài liệu</analysis>
        <branch-type>release</branch-type>
        <branch-name>release-2.1.0</branch-name>
        <command>git checkout -b release-2.1.0 develop</command>
    </example-3>

    <example-4>
        <scenario>Cải thiện hiệu suất truy vấn cơ sở dữ liệu và cập nhật bộ nhớ đệm</scenario>
        <analysis>Cải thiện hiệu suất, cải tiến không nghiêm trọng</analysis>
        <branch-type>feature</branch-type>
        <branch-name>feature/database-performance-optimization</branch-name>
        <command>git checkout -b feature/database-performance-optimization develop</command>
    </example-4>
</examples>
```

### Danh sách kiểm tra xác thực

```xml
<validation>
    <pre-analysis>
        <check>Kho lưu trữ đang ở trạng thái sạch (không có thay đổi chưa commit có thể gây xung đột)</check>
        <check>Nhánh hiện tại là điểm bắt đầu phù hợp (develop cho features/releases, master cho hotfixes)</check>
        <check>Kho lưu trữ từ xa đã được cập nhật</check>
    </pre-analysis>

    <analysis-quality>
        <check>Phân tích thay đổi bao gồm tất cả các tệp đã sửa đổi</check>
        <check>Lựa chọn loại nhánh tuân theo các nguyên tắc của Git Flow</check>
        <check>Tên nhánh có ngữ nghĩa và tuân theo quy ước</check>
        <check>Các trường hợp đặc biệt được xem xét và xử lý</check>
    </analysis-quality>

    <execution-safety>
        <check>Nhánh đích (develop/master) tồn tại và có thể truy cập</check>
        <check>Tên nhánh được đề xuất không xung đột với các nhánh hiện có</check>
        <check>Người dùng có quyền thích hợp để tạo nhánh</check>
    </execution-safety>
</validation>
```

### Thực thi cuối cùng

```xml
<execution-protocol>
    <analysis-summary>
        <git-status>Đầu ra của lệnh git status</git-status>
        <git-diff>Các phần liên quan của đầu ra git diff</git-diff>
        <change-analysis>Phân tích chi tiết về những gì các thay đổi đại diện</change-analysis>
        <branch-decision>Giải thích tại sao loại nhánh cụ thể được chọn</branch-decision>
    </analysis-summary>

    <branch-creation>
        <command>git checkout -b [ten-nhanh] [nhanh-nguon]</command>
        <confirmation>Xác minh việc tạo nhánh và trạng thái nhánh hiện tại</confirmation>
        <next-steps>Cung cấp hướng dẫn về các hành động tiếp theo (commit thay đổi, đẩy nhánh, v.v.)</next-steps>
    </branch-creation>

    <fallback-options>
        <alternative-names>Đề xuất 2-3 tên nhánh thay thế nếu đề xuất chính không phù hợp</alternative-names>
        <manual-override>Cho phép người dùng chỉ định loại nhánh khác nếu phân tích có vẻ không chính xác</manual-override>
    </fallback-options>
</execution-protocol>
```

### Tham khảo Git Flow

```xml
<gitflow-reference>
    <main-branches>
        <master>Mã nguồn sẵn sàng cho production, mỗi commit là một bản phát hành</master>
        <develop>Nhánh tích hợp cho các tính năng, các thay đổi phát triển mới nhất</develop>
    </main-branches>

    <supporting-branches>
        <feature>Phân nhánh từ develop, hợp nhất trở lại develop</feature>
        <release>Phân nhánh từ develop, hợp nhất vào cả develop và master</release>
        <hotfix>Phân nhánh từ master, hợp nhất vào cả develop và master</hotfix>
    </supporting-branches>

    <merge-strategy>
        <flag>Luôn sử dụng cờ --no-ff để bảo toàn lịch sử nhánh</flag>
        <tagging>Gắn thẻ các bản phát hành trên nhánh master</tagging>
        <cleanup>Xóa các nhánh sau khi hợp nhất thành công</cleanup>
    </merge-strategy>
```
