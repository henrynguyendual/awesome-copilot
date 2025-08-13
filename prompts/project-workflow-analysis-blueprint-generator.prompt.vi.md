# Trình Tạo Tài Liệu Quy Trình Làm Việc Dự Án

## Biến Cấu Hình

```
${PROJECT_TYPE="Auto-detect|.NET|Java|Spring|Node.js|Python|React|Angular|Microservices|Other"}
${ENTRY_POINT="API|GraphQL|Frontend|CLI|Message Consumer|Scheduled Job|Custom"}
${PERSISTENCE_TYPE="Auto-detect|SQL Database|NoSQL Database|File System|External API|Message Queue|Cache|None"}
${ARCHITECTURE_PATTERN="Auto-detect|Layered|Clean|CQRS|Microservices|MVC|MVVM|Serverless|Event-Driven|Other"}
${WORKFLOW_COUNT=1-5}
${DETAIL_LEVEL="Standard|Implementation-Ready"}
${INCLUDE_SEQUENCE_DIAGRAM=true|false}
${INCLUDE_TEST_PATTERNS=true|false}
```

## Prompt Được Sinh

```
"Phân tích codebase và tài liệu hóa ${WORKFLOW_COUNT} luồng công việc end-to-end tiêu biểu 
làm mẫu triển khai cho các tính năng tương tự. Sử dụng phương pháp sau:
```

### Giai Đoạn Phát Hiện Ban Đầu

- Nếu PROJECT_TYPE = Auto-detect: Xác định công nghệ từ cấu trúc thư mục, file config (.NET, Spring, Node.js,...)
- Nếu ENTRY_POINT = Auto-detect: Tìm điểm bắt đầu như API controller, GraphQL resolver, UI component, event subscriber...
- Nếu PERSISTENCE_TYPE = Auto-detect: Xác định cơ chế lưu trữ (DB config, repository, ORM, API client...)

### Hướng Dẫn Tài Liệu Quy Trình

#### 1. Tổng Quan Quy Trình
- Tên, mô tả, mục đích kinh doanh
- Hành động/kích hoạt
- Danh sách file/class liên quan

#### 2. Triển Khai Entry Point
- API: Controller, method, DTO, validator, auth
- GraphQL: Resolver, schema, input type
- Frontend: Component, handler, API service, state
- Message Consumer: Handler, subscription, model, validate

#### 3. Tầng Dịch Vụ
- Service class, method, logic, interface, DI
- CQRS: Command/query handler
- Clean: Use case/interactor

#### 4. Mapping Dữ Liệu
- DTO → Domain model
- Object mapper hoặc thủ công
- Validate khi mapping
- Domain events

#### 5. Truy Cập Dữ Liệu
- Repository interface/implementation
- Query, entity/model
- Transaction
- SQL: ORM config, query
- NoSQL: Document structure, query/update

#### 6. Xây Dựng Response
- Response DTO
- Mapping domain → response
- Chọn status code
- Cấu trúc lỗi

#### 7. Xử Lý Lỗi
- Exception types
- try/catch patterns
- Global handler
- Logging
- Retry/circuit breaker
- Compensating actions

#### 8. Xử Lý Bất Đồng Bộ
- Job scheduling
- Event publish
- Message queue
- Callback/webhook
- Tracking async

#### 9. Kiểm Thử (nếu INCLUDE_TEST_PATTERNS=true)
- Unit test, mock, fixture
- Integration test
- Test data
- API/controller test

#### 10. Sequence Diagram (nếu INCLUDE_SEQUENCE_DIAGRAM=true)
- Tạo sequence diagram
- Bao gồm method call, return value, flow điều kiện, path lỗi

#### 11. Quy Tắc Đặt Tên
- Controller, Service, Repository, DTO
- Method CRUD
- Biến
- Tổ chức file

#### 12. Template Triển Khai
- API endpoint
- Service method
- Repository method
- Domain model
- Xử lý lỗi chuẩn

### Mẫu Triển Khai Theo Công Nghệ

- .NET: Controller, Startup.cs, EF DbContext, Repository EF/Dapper, AutoMapper, Middleware, Extension method, Options pattern, ILogger, Auth
- Spring: Controller, Service + transaction, Repository, JPA entity, DTO, Bean config, Exception handler, Validator
- React: Component + props/state, Hook (useState, useEffect), API service, State management (Context, Redux), Form, Route

### Hướng Dẫn Triển Khai
1. Quy trình step-by-step
2. Lỗi thường gặp
3. Cơ chế mở rộng

**Kết luận:** Tóm tắt các pattern quan trọng cần theo để giữ nhất quán khi thêm tính năng mới.