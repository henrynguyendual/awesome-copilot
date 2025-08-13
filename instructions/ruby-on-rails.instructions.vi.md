---
description: "Các quy ước và hướng dẫn lập trình Ruby on Rails"
applyTo: "**/*.rb"
---

# Ruby on Rails

## Hướng dẫn Chung

- Tuân thủ Hướng dẫn Phong cách RuboCop và sử dụng các công cụ như `rubocop`, `standardrb`, hoặc `rufo` để định dạng nhất quán.
- Sử dụng snake_case cho biến/phương thức và CamelCase cho lớp/module.
- Giữ các phương thức ngắn gọn và tập trung; sử dụng return sớm, guard clauses, và các phương thức private để giảm độ phức tạp.
- Ưu tiên các tên có ý nghĩa hơn là các tên ngắn hoặc chung chung.
- Chỉ bình luận khi cần thiết — tránh giải thích những điều hiển nhiên.
- Áp dụng Nguyên tắc Trách nhiệm Đơn lẻ (Single Responsibility Principle) cho các lớp, phương thức và module.
- Ưu tiên composition hơn inheritance; tách logic có thể tái sử dụng vào các module hoặc service.
- Giữ controller gọn nhẹ — chuyển logic nghiệp vụ vào model, service, hoặc các đối tượng command/query.
- Áp dụng mô hình “model béo, controller gầy” một cách có suy xét và với các abstraction rõ ràng.
- Tách logic nghiệp vụ vào các service object để có thể tái sử dụng và dễ kiểm thử.
- Sử dụng partial hoặc view component để giảm trùng lặp và đơn giản hóa view.
- Sử dụng `unless` cho các điều kiện phủ định, nhưng tránh dùng nó với `else` để rõ ràng hơn.
- Tránh các điều kiện lồng nhau sâu — ưu tiên guard clauses và tách phương thức.
- Sử dụng toán tử safe navigation (`&.`) thay vì nhiều lần kiểm tra `nil`.
- Ưu tiên `.present?`, `.blank?`, và `.any?` hơn là kiểm tra nil/rỗng thủ công.
- Tuân thủ các quy ước RESTful trong routing và các action của controller.
- Sử dụng các generator của Rails để tạo scaffold cho các resource một cách nhất quán.
- Sử dụng strong parameters để chỉ định các thuộc tính được phép một cách an toàn.
- Ưu tiên enum và các thuộc tính có kiểu dữ liệu rõ ràng để model rõ ràng và dễ xác thực hơn.
- Giữ các migration độc lập với cơ sở dữ liệu; tránh dùng SQL thô khi có thể.
- Luôn thêm index cho các khóa ngoại và các cột thường xuyên được truy vấn.
- Định nghĩa `null: false` và `unique: true` ở cấp độ cơ sở dữ liệu, không chỉ trong model.
- Sử dụng `find_each` để lặp qua các tập dữ liệu lớn nhằm giảm sử dụng bộ nhớ.
- Giới hạn phạm vi (scope) các truy vấn trong model hoặc sử dụng các query object để rõ ràng và tái sử dụng.
- Sử dụng callback `before_action` một cách tiết kiệm — tránh đặt logic nghiệp vụ trong đó.
- Sử dụng `Rails.cache` để lưu trữ các tính toán tốn kém hoặc dữ liệu thường xuyên truy cập.
- Xây dựng đường dẫn tệp bằng `Rails.root.join(...)` thay vì hardcode.
- Sử dụng `class_name` và `foreign_key` trong các association để khai báo mối quan hệ một cách tường minh.
- Giữ các thông tin bí mật và cấu hình ngoài codebase bằng cách sử dụng `Rails.application.credentials` hoặc biến môi trường (ENV).
- Viết các unit test độc lập cho model, service, và helper.
- Bao phủ logic từ đầu đến cuối bằng các request/system test.
- Sử dụng background job (ActiveJob) cho các hoạt động không chặn như gửi email hoặc gọi API.
- Sử dụng `FactoryBot` (RSpec) hoặc fixtures (Minitest) để thiết lập dữ liệu kiểm thử một cách sạch sẽ.
- Tránh sử dụng `puts` — gỡ lỗi bằng `byebug`, `pry`, hoặc các tiện ích logger.
- Ghi tài liệu cho các đoạn code và phương thức phức tạp bằng YARD hoặc RDoc.

## Cấu trúc Thư mục App

- Định nghĩa các service object trong thư mục `app/services` để đóng gói logic nghiệp vụ.
- Sử dụng các form object đặt tại `app/forms` để quản lý logic xác thực và gửi biểu mẫu.
- Triển khai các JSON serializer trong thư mục `app/serializers` để định dạng các phản hồi API.
- Định nghĩa các policy phân quyền trong `app/policies` để kiểm soát quyền truy cập của người dùng vào các resource.
- Cấu trúc API GraphQL bằng cách tổ chức các schema, query, và mutation bên trong `app/graphql`.
- Tạo các validator tùy chỉnh trong `app/validators` để thực thi logic xác thực chuyên biệt.
- Tách và đóng gói các truy vấn ActiveRecord phức tạp trong `app/queries` để tái sử dụng và kiểm thử tốt hơn.
- Định nghĩa các kiểu dữ liệu tùy chỉnh và logic ép kiểu trong thư mục `app/types` để mở rộng hoặc ghi đè hành vi của kiểu ActiveModel.

## Các Lệnh

- Sử dụng `rails generate` để tạo model, controller, và migration mới.
- Sử dụng `rails db:migrate` để áp dụng các migration cơ sở dữ liệu.
- Sử dụng `rails db:seed` để điền dữ liệu ban đầu vào cơ sở dữ liệu.
- Sử dụng `rails db:rollback` để hoàn tác migration cuối cùng.
- Sử dụng `rails console` để tương tác với ứng dụng Rails trong môi trường REPL.
- Sử dụng `rails server` để khởi động máy chủ phát triển.
- Sử dụng `rails test` để chạy bộ kiểm thử.
- Sử dụng `rails routes` để liệt kê tất cả các route đã được định nghĩa trong ứng dụng.
- Sử dụng `rails assets:precompile` để biên dịch các asset cho môi trường production.

## Các Thực hành Tốt nhất khi Phát triển API

- Cấu trúc các route bằng `resources` của Rails để tuân thủ quy ước RESTful.
- Sử dụng các route có namespace (ví dụ: `/api/v1/`) để quản lý phiên bản và tương thích trong tương lai.
- Serialize các phản hồi bằng `ActiveModel::Serializer` hoặc `fast_jsonapi` để có đầu ra nhất quán.
- Trả về các mã trạng thái HTTP phù hợp cho mỗi phản hồi (ví dụ: 200 OK, 201 Created, 422 Unprocessable Entity).
- Sử dụng các bộ lọc `before_action` để tải và phân quyền cho resource, không dùng cho logic nghiệp vụ.
- Tận dụng phân trang (ví dụ: `kaminari` hoặc `pagy`) cho các endpoint trả về tập dữ liệu lớn.
- Giới hạn tần suất (rate limit) và điều tiết (throttle) các endpoint nhạy cảm bằng middleware hoặc các gem như `rack-attack`.
- Trả về lỗi ở định dạng JSON có cấu trúc bao gồm mã lỗi, thông báo và chi tiết.
- Làm sạch và chỉ định các tham số đầu vào được phép bằng strong parameters.
- Sử dụng các serializer hoặc presenter tùy chỉnh để tách biệt logic nội bộ khỏi định dạng phản hồi.
- Tránh các truy vấn N+1 bằng cách sử dụng `includes` khi tải trước (eager loading) dữ liệu liên quan.
- Triển khai các background job cho các tác vụ không chặn như gửi email hoặc đồng bộ hóa với các API bên ngoài.
- Ghi lại siêu dữ liệu (metadata) của request/response để gỡ lỗi, quan sát và kiểm toán.
- Ghi tài liệu cho các endpoint bằng OpenAPI (Swagger), `rswag`, hoặc `apipie-rails`.
- Sử dụng các header CORS (`rack-cors`) để cho phép truy cập API từ các nguồn khác khi cần.
- Đảm bảo dữ liệu nhạy cảm không bao giờ bị lộ trong các phản hồi API hoặc thông báo lỗi.

## Các Thực hành Tốt nhất khi Phát triển Frontend

- Sử dụng `app/javascript` làm thư mục chính để quản lý các gói JavaScript, module và logic frontend trong Rails 6+ với Webpacker hoặc esbuild.
- Cấu trúc JavaScript của bạn theo component hoặc domain, không phải theo loại tệp, để giữ cho mọi thứ có tính module.
- Tận dụng Hotwire (Turbo + Stimulus) để cập nhật theo thời gian thực và sử dụng JavaScript tối thiểu trong các ứng dụng Rails-native.
- Sử dụng các controller Stimulus để liên kết hành vi với HTML và quản lý logic giao diện người dùng một cách khai báo.
- Tổ chức các style bằng SCSS module, Tailwind, hoặc quy ước BEM dưới `app/assets/stylesheets`.
- Giữ logic của view sạch sẽ bằng cách tách các đoạn mã đánh dấu lặp đi lặp lại vào các partial hoặc component.
- Sử dụng các thẻ HTML ngữ nghĩa và tuân thủ các thực hành tốt nhất về khả năng truy cập (a11y) trên tất cả các view.
- Tránh JavaScript và style nội tuyến; thay vào đó, chuyển logic sang các tệp `.js` hoặc `.scss` riêng biệt để rõ ràng và tái sử dụng.
- Tối ưu hóa các asset (hình ảnh, phông chữ, biểu tượng) bằng asset pipeline hoặc các bundler để lưu vào bộ đệm và nén.
- Sử dụng các thuộc tính `data-*` để kết nối sự tương tác của frontend với HTML do Rails tạo ra và Stimulus.
- Kiểm thử chức năng frontend bằng system test (Capybara) hoặc integration test với các công cụ như Cypress hoặc Playwright.
- Sử dụng cơ chế tải asset theo môi trường cụ thể để ngăn các script hoặc style không cần thiết trong môi trường production.
- Tuân thủ một hệ thống thiết kế hoặc thư viện component để giữ cho giao diện người dùng nhất quán và có thể mở rộng.
- Tối ưu hóa thời gian hiển thị đầu tiên (TTFP) và việc tải asset bằng cách sử dụng lazy loading, Turbo Frames, và trì hoãn (deferring) JS.

## Hướng dẫn Kiểm thử

- Viết unit test cho các model bằng `test/models` (Minitest) hoặc `spec/models` (RSpec) để xác thực logic nghiệp vụ.
- Sử dụng fixtures (Minitest) hoặc factory với `FactoryBot` (RSpec) để quản lý dữ liệu kiểm thử một cách sạch sẽ và nhất quán.
- Tổ chức các controller spec dưới `test/controllers` hoặc `spec/requests` để kiểm thử hành vi API RESTful.
- Ưu tiên các khối `before` trong RSpec hoặc `setup` trong Minitest để khởi tạo dữ liệu kiểm thử chung.
- Tránh gọi các API bên ngoài trong các bài kiểm thử — sử dụng `WebMock`, `VCR`, hoặc `stub_request` để cô lập môi trường kiểm thử.
- Sử dụng `system tests` trong Minitest hoặc `feature specs` với Capybara trong RSpec để mô phỏng các luồng người dùng hoàn chỉnh.
- Tách các bài kiểm thử chậm và tốn kém (ví dụ: dịch vụ bên ngoài, tải tệp lên) thành các loại hoặc thẻ kiểm thử riêng biệt.
- Chạy các công cụ đo độ bao phủ của kiểm thử như `SimpleCov` để đảm bảo độ bao phủ code đầy đủ.
- Tránh `sleep` trong các bài kiểm thử; sử dụng `perform_enqueued_jobs` (Minitest) hoặc `ActiveJob::TestHelper` với RSpec.
- Sử dụng các công cụ dọn dẹp cơ sở dữ liệu (`rails test:prepare`, `DatabaseCleaner`, hoặc `transactional_fixtures`) để duy trì trạng thái sạch sẽ giữa các bài kiểm thử.
- Kiểm thử các background job bằng cách đưa vào hàng đợi và thực hiện các job bằng `ActiveJob::TestHelper` hoặc các matcher `have_enqueued_job`.
- Đảm bảo các bài kiểm thử chạy nhất quán trên các môi trường bằng các công cụ CI (ví dụ: GitHub Actions, CircleCI).
- Sử dụng các matcher tùy chỉnh (RSpec) hoặc các assertion tùy chỉnh (Minitest) để có logic kiểm thử dễ tái sử dụng và biểu cảm.
- Gắn thẻ các bài kiểm thử theo loại (ví dụ: `:model`, `:request`, `:feature`) để chạy kiểm thử nhanh hơn và có mục tiêu hơn.
- Tránh các bài kiểm thử dễ hỏng — không phụ thuộc vào dấu thời gian cụ thể, dữ liệu ngẫu nhiên, hoặc thứ tự trừ khi thực sự cần thiết.
- Viết các integration test cho các luồng từ đầu đến cuối qua nhiều lớp (model, view, controller).
- Giữ cho các bài kiểm thử nhanh, đáng tin cậy và DRY như
