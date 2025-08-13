---
title: Hướng dẫn Phát triển Lược đồ cho Power Platform Connectors
description: "Hướng dẫn phát triển toàn diện cho các Trình kết nối tùy chỉnh (Custom Connectors) của Power Platform sử dụng định nghĩa Lược đồ JSON (JSON Schema). Bao gồm các định nghĩa API (Swagger 2.0), thuộc tính API và cấu hình cài đặt với các tiện ích mở rộng của Microsoft."
applyTo: "**/*.{json,md}"
---

# Hướng dẫn Phát triển Lược đồ cho Power Platform Connectors

## Tổng quan Dự án

Không gian làm việc này chứa các định nghĩa Lược đồ JSON (JSON Schema) cho các Trình kết nối tùy chỉnh (Custom Connectors) của Power Platform, đặc biệt dành cho công cụ `paconn` (Power Apps Connector). Các lược đồ này xác thực và cung cấp IntelliSense cho:

- **Định nghĩa API** (định dạng Swagger 2.0)
- **Thuộc tính API** (siêu dữ liệu và cấu hình của trình kết nối)
- **Cài đặt** (cấu hình môi trường và triển khai)

## Tìm hiểu Cấu trúc Tệp

### 1\. apiDefinition.swagger.json

- **Mục đích**: Tệp này chứa các định nghĩa API Swagger 2.0 với các tiện ích mở rộng của Power Platform.
- **Tính năng chính**:
  - Các thuộc tính tiêu chuẩn của Swagger 2.0 bao gồm info, paths, definitions, và nhiều hơn nữa.
  - Các tiện ích mở rộng dành riêng cho Microsoft bắt đầu bằng tiền tố `x-ms-*`.
  - Các loại định dạng tùy chỉnh được thiết kế riêng cho Power Platform như `date-no-tz` và `html`.
  - Hỗ trợ lược đồ động (dynamic schema) cung cấp sự linh hoạt trong thời gian chạy.
  - Các định nghĩa bảo mật hỗ trợ các phương thức xác thực OAuth2, API Key, và Basic Auth.

### 2\. apiProperties.json

- **Mục đích**: Tệp này định nghĩa siêu dữ liệu của trình kết nối, cấu hình xác thực, và cấu hình chính sách.
- **Thành phần chính**:
  - **Tham số Kết nối (Connection Parameters)**: Hỗ trợ nhiều loại xác thực bao gồm OAuth, API Key, và cấu hình Gateway.
  - **Các bản mẫu Chính sách (Policy Template Instances)**: Xử lý các chính sách chuyển đổi dữ liệu và định tuyến cho trình kết nối.
  - **Siêu dữ liệu Trình kết nối (Connector Metadata)**: Bao gồm thông tin nhà phát hành, các khả năng, và các yếu tố thương hiệu.

### 3\. settings.json

- **Mục đích**: Tệp này cung cấp các cài đặt cấu hình môi trường và triển khai cho công cụ paconn.
- **Tùy chọn Cấu hình**:
  - Nhắm mục tiêu theo GUID môi trường cho các môi trường Power Platform cụ thể.
  - Ánh xạ đường dẫn tệp cho các tài sản và tệp cấu hình của trình kết nối.
  - URL điểm cuối API cho cả môi trường sản xuất và thử nghiệm (PROD/TIP1).
  - Quy định phiên bản API để đảm bảo tương thích với các dịch vụ Power Platform.

---

## Hướng dẫn Phát triển

### Khi làm việc với Định nghĩa API (Swagger)

1.  **Luôn xác thực theo đặc tả Swagger 2.0** - Lược đồ này bắt buộc tuân thủ nghiêm ngặt Swagger 2.0.

2.  **Tiện ích mở rộng của Microsoft cho các Thao tác (Operations)**:

    - `x-ms-summary`: Sử dụng để cung cấp tên hiển thị thân thiện với người dùng và đảm bảo bạn sử dụng định dạng Viết Hoa Từng Chữ (Title Case).
    - `x-ms-visibility`: Sử dụng để kiểm soát khả năng hiển thị của tham số với các giá trị `important`, `advanced`, hoặc `internal`.
    - `x-ms-trigger`: Sử dụng để đánh dấu các thao tác là trình kích hoạt (trigger) với các giá trị `batch` hoặc `single`.
    - `x-ms-trigger-hint`: Sử dụng để cung cấp văn bản gợi ý hữu ích hướng dẫn người dùng khi làm việc với trình kích hoạt.
    - `x-ms-trigger-metadata`: Sử dụng để định nghĩa các cài đặt cấu hình trình kích hoạt bao gồm các thuộc tính kind và mode.
    - `x-ms-notification`: Sử dụng để cấu hình các thao tác webhook cho thông báo thời gian thực.
    - `x-ms-pageable`: Sử dụng để bật chức năng phân trang bằng cách chỉ định thuộc tính `nextLinkName`.
    - `x-ms-safe-operation`: Sử dụng để đánh dấu các thao tác POST là an toàn khi chúng không có tác dụng phụ.
    - `x-ms-no-generic-test`: Sử dụng để vô hiệu hóa việc kiểm thử tự động cho các thao tác cụ thể.
    - `x-ms-operation-context`: Sử dụng để cấu hình các cài đặt mô phỏng thao tác cho mục đích kiểm thử.

3.  **Tiện ích mở rộng của Microsoft cho các Tham số (Parameters)**:

    - `x-ms-dynamic-list`: Sử dụng để bật danh sách thả xuống động được điền từ các lệnh gọi API.
    - `x-ms-dynamic-values`: Sử dụng để cấu hình các nguồn giá trị động điền vào các tùy chọn tham số.
    - `x-ms-dynamic-tree`: Sử dụng để tạo các bộ chọn phân cấp cho các cấu trúc dữ liệu lồng nhau.
    - `x-ms-dynamic-schema`: Sử dụng để cho phép thay đổi lược đồ trong thời gian chạy dựa trên lựa chọn của người dùng.
    - `x-ms-dynamic-properties`: Sử dụng cho cấu hình thuộc tính động thích ứng với ngữ cảnh.
    - `x-ms-enum-values`: Sử dụng để cung cấp các định nghĩa enum nâng cao với tên hiển thị để có trải nghiệm người dùng tốt hơn.
    - `x-ms-test-value`: Sử dụng để cung cấp các giá trị mẫu cho việc kiểm thử, nhưng không bao giờ bao gồm bí mật hoặc dữ liệu nhạy cảm.
    - `x-ms-trigger-value`: Sử dụng để chỉ định các giá trị dành riêng cho các tham số của trình kích hoạt với các thuộc tính `value-collection` và `value-path`.
    - `x-ms-url-encoding`: Sử dụng để chỉ định kiểu mã hóa URL là `single` hoặc `double` (mặc định là `single`).
    - `x-ms-parameter-location`: Sử dụng để cung cấp gợi ý vị trí tham số cho API (tiện ích mở rộng của AutoRest - bị Power Platform bỏ qua).
    - `x-ms-localizeDefaultValue`: Sử dụng để bật bản địa hóa cho các giá trị tham số mặc định.
    - `x-ms-skip-url-encoding`: Sử dụng để bỏ qua mã hóa URL cho các tham số đường dẫn (tiện ích mở rộng của AutoRest - bị Power Platform bỏ qua).

4.  **Tiện ích mở rộng của Microsoft cho các Lược đồ (Schemas)**:

    - `x-ms-notification-url`: Sử dụng để đánh dấu một thuộc tính lược đồ là URL thông báo cho các cấu hình webhook.
    - `x-ms-media-kind`: Sử dụng để chỉ định loại phương tiện cho nội dung, với các giá trị được hỗ trợ là `image` hoặc `audio`.
    - `x-ms-enum`: Sử dụng để cung cấp siêu dữ liệu enum nâng cao (tiện ích mở rộng của AutoRest - bị Power Platform bỏ qua).
    - Lưu ý rằng tất cả các tiện ích mở rộng tham số được liệt kê ở trên cũng áp dụng cho các thuộc tính lược đồ và có thể được sử dụng trong các định nghĩa lược đồ.

5.  **Tiện ích mở rộng ở cấp độ Gốc (Root-Level)**:

    - `x-ms-capabilities`: Sử dụng để định nghĩa các khả năng của trình kết nối như chức năng file-picker và testConnection.
    - `x-ms-connector-metadata`: Sử dụng để cung cấp siêu dữ liệu bổ sung cho trình kết nối ngoài các thuộc tính tiêu chuẩn.
    - `x-ms-docs`: Sử dụng để cấu hình các cài đặt tài liệu và tham chiếu cho trình kết nối.
    - `x-ms-deployment-version`: Sử dụng để theo dõi thông tin phiên bản cho việc quản lý triển khai.
    - `x-ms-api-annotation`: Sử dụng để thêm các chú thích ở cấp độ API cho chức năng nâng cao.

6.  **Tiện ích mở rộng ở cấp độ Đường dẫn (Path-Level)**:

    - `x-ms-notification-content`: Sử dụng để định nghĩa các lược đồ nội dung thông báo cho các mục đường dẫn webhook.

7.  **Khả năng ở cấp độ Thao tác (Operation-Level)**:

    - `x-ms-capabilities` (ở cấp độ thao tác): Sử dụng để bật các khả năng cụ thể của thao tác như `chunkTransfer` cho việc truyền tệp lớn.

8.  **Lưu ý về Bảo mật**:

    - Bạn nên định nghĩa `securityDefinitions` phù hợp cho API của mình để đảm bảo xác thực đúng cách.
    - **Cho phép nhiều định nghĩa bảo mật** - bạn có thể định nghĩa tối đa hai phương thức xác thực (ví dụ: oauth2 + apiKey, basic + apiKey).
    - **Ngoại lệ**: Nếu sử dụng xác thực "None", không có định nghĩa bảo mật nào khác có thể tồn tại trong cùng một trình kết nối.
    - Bạn nên sử dụng `oauth2` cho các API hiện đại, `apiKey` cho xác thực bằng token đơn giản, và chỉ xem xét `basic` auth cho các hệ thống nội bộ/cũ.
    - Mỗi định nghĩa bảo mật phải thuộc chính xác một loại (ràng buộc này được thực thi bằng xác thực oneOf).

9.  **Thực hành tốt nhất cho Tham số**:

    - Bạn nên sử dụng các trường `description` mô tả để giúp người dùng hiểu mục đích của mỗi tham số.
    - Bạn nên triển khai `x-ms-summary` để có trải nghiệm người dùng tốt hơn (yêu cầu định dạng viết hoa từng chữ).
    - Bạn phải đánh dấu các tham số bắt buộc một cách chính xác để đảm bảo xác thực đúng.
    - Bạn nên sử dụng các giá trị `format` phù hợp (bao gồm các tiện ích mở rộng của Power Platform) để cho phép xử lý dữ liệu đúng cách.
    - Bạn nên tận dụng các tiện ích mở rộng động để có trải nghiệm người dùng và xác thực dữ liệu tốt hơn.

10. **Tiện ích mở rộng Định dạng của Power Platform**:

    - `date-no-tz`: Đại diện cho một ngày-giờ không có thông tin chênh lệch múi giờ.
    - `html`: Định dạng này yêu cầu client hiển thị một trình soạn thảo HTML khi chỉnh sửa và một trình xem HTML khi xem nội dung.
    - Các định dạng tiêu chuẩn bao gồm: `int32`, `int64`, `float`, `double`, `byte`, `binary`, `date`, `date-time`, `password`, `email`, `uri`, `uuid`.

### Khi làm việc với Thuộc tính API

1.  **Tham số Kết nối**:

    - Bạn nên chọn các loại tham số phù hợp như `string`, `securestring`, hoặc `oauthSetting`.
    - Bạn nên cấu hình cài đặt OAuth với các nhà cung cấp danh tính chính xác.
    - Bạn nên sử dụng `allowedValues` cho các tùy chọn thả xuống khi thích hợp.
    - Bạn nên triển khai các phụ thuộc tham số khi cần cho các tham số có điều kiện.

2.  **Mẫu Chính sách (Policy Templates)**:

    - Bạn nên sử dụng `routerequesttoendpoint` để định tuyến backend đến các điểm cuối API khác nhau.
    - Bạn nên triển khai `setqueryparameter` để đặt giá trị mặc định cho các tham số truy vấn.
    - Bạn nên sử dụng `updatenextlink` cho các kịch bản phân trang để xử lý việc phân trang một cách chính xác.
    - Bạn nên áp dụng `pollingtrigger` cho các thao tác trình kích hoạt yêu cầu hành vi thăm dò (polling).

3.  **Thương hiệu và Siêu dữ liệu**:

    - Bạn phải luôn chỉ định `iconBrandColor` vì thuộc tính này là bắt buộc đối với tất cả các trình kết nối.
    - Bạn nên định nghĩa `capabilities` phù hợp để chỉ định liệu trình kết nối của bạn có hỗ trợ các hành động (actions) hay trình kích hoạt (triggers) không.
    - Bạn nên đặt các giá trị `publisher` và `stackOwner` có ý nghĩa để xác định quyền sở hữu của trình kết nối.

### Khi làm việc với Cài đặt

1.  **Cấu hình Môi trường**:

    - Bạn nên sử dụng định dạng GUID phù hợp cho `environment` khớp với mẫu xác thực.
    - Bạn nên đặt `powerAppsUrl` và `flowUrl` chính xác cho môi trường mục tiêu của mình.
    - Bạn nên khớp các phiên bản API với các yêu cầu cụ thể của mình.

2.  **Tham chiếu Tệp**:

    - Bạn nên duy trì việc đặt tên tệp nhất quán với các giá trị mặc định là `apiProperties.json` và `apiDefinition.swagger.json`.
    - Bạn nên sử dụng đường dẫn tương đối cho môi trường phát triển cục bộ.
    - Bạn nên đảm bảo tệp biểu tượng tồn tại và được tham chiếu đúng trong cấu hình của bạn.

---

## Quy tắc Xác thực Lược đồ

### Thuộc tính Bắt buộc

- **Định nghĩa API**: `swagger: "2.0"`, `info` (với `title` và `version`), `paths`
- **Thuộc tính API**: `properties` với `iconBrandColor`
- **Cài đặt**: Không có thuộc tính bắt buộc (tất cả đều tùy chọn với giá trị mặc định)

### Xác thực Mẫu (Pattern)

- **Tiện ích mở rộng của Bên thứ ba**: Phải khớp với mẫu `^x-(?!ms-)` cho các tiện ích mở rộng không phải của Microsoft
- **Các mục Đường dẫn**: Phải bắt đầu bằng `/` cho các đường dẫn API
- **GUID Môi trường**: Phải khớp với mẫu định dạng UUID `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
- **URL**: Phải là các URI hợp lệ cho các cấu hình điểm cuối
- **Mẫu Host**: Phải khớp với `^[^{}/ :\\\\]+(?::\\d+)?$` (không có khoảng trắng, giao thức, hoặc đường dẫn)

### Ràng buộc về Loại

- **Định nghĩa Bảo mật**:
  - Cho phép tối đa hai định nghĩa bảo mật trong đối tượng `securityDefinitions`
  - Mỗi định nghĩa bảo mật riêng lẻ phải thuộc chính xác một loại (xác thực oneOf: `basic`, `apiKey`, `oauth2`)
  - **Ngoại lệ**: Xác thực "None" không thể cùng tồn tại với các định nghĩa bảo mật khác
- **Loại Tham số**: Giới hạn trong các giá trị enum cụ thể (`string`, `number`, `integer`, `boolean`, `array`, `file`)
- **Mẫu Chính sách**: Yêu cầu tham số cụ thể theo loại
- **Giá trị Định dạng**: Bộ mở rộng bao gồm các định dạng của Power Platform
- **Giá trị Hiển thị (Visibility)**: Phải là một trong các giá trị `important`, `advanced`, hoặc `internal`
- **Loại Trình kích hoạt**: Phải là `batch` hoặc `single`

### Quy tắc Xác thực Bổ sung

- **Tham chiếu `$ref`**: Chỉ nên trỏ đến `#/definitions/`, `#/parameters/`, hoặc `#/responses/`
- **Tham số Đường dẫn**: Phải được đánh dấu là `required: true`
- **Đối tượng Info**: Mô tả phải khác với tiêu đề
- **Đối tượng Contact**: Email phải có định dạng email hợp lệ, URL phải là URI hợp lệ
- **Đối tượng License**: Tên là bắt buộc, URL phải là URI hợp lệ nếu được cung cấp
- **Tài liệu Bên ngoài**: URL là bắt buộc và phải là URI hợp lệ
- **Thẻ (Tags)**: Phải có tên duy nhất trong mảng
- **Lược đồ (Schemes)**: Phải là các lược đồ HTTP hợp lệ (`http`, `https`, `ws`, `wss`)
- **Loại MIME**: Phải tuân theo định dạng loại MIME hợp lệ trong `consumes` và `produces`

---

## Các Mẫu và Ví dụ Phổ biến

### Ví dụ về Định nghĩa API

#### Thao tác Cơ bản với Tiện ích mở rộng của Microsoft

```json
{
  "get": {
    "operationId": "GetItems",
    "summary": "Get items",
    "x-ms-summary": "Get Items",
    "x-ms-visibility": "important",
    "description": "Retrieves a list of items from the API",
    "parameters": [
      {
        "name": "category",
        "in": "query",
        "type": "string",
        "x-ms-summary": "Category",
        "x-ms-visibility": "important",
        "x-ms-dynamic-values": {
          "operationId": "GetCategories",
          "value-path": "id",
          "value-title": "name"
        }
      }
    ],
    "responses": {
      "200": {
        "description": "Success",
        "x-ms-summary": "Success",
        "schema": {
          "type": "object",
          "properties": {
            "items": {
              "type": "array",
              "x-ms-summary": "Items",
              "items": {
                "$ref": "#/definitions/Item"
              }
            }
          }
        }
      }
    }
  }
}
```

#### Cấu hình Thao tác Trình kích hoạt

```json
{
  "get": {
    "operationId": "WhenItemCreated",
    "x-ms-summary": "When an Item is Created",
    "x-ms-trigger": "batch",
    "x-ms-trigger-hint": "To see it work now, create an item",
    "x-ms-trigger-metadata": {
      "kind": "query",
      "mode": "polling"
    },
    "x-ms-pageable": {
      "nextLinkName": "@odata.nextLink"
    }
  }
}
```

#### Ví dụ về Lược đồ Động

```json
{
  "name": "dynamicSchema",
  "in": "body",
  "schema": {
    "x-ms-dynamic-schema": {
      "operationId": "GetSchema",
      "parameters": {
        "table": {
          "parameter": "table"
        }
      },
      "value-path": "schema"
    }
  }
}
```

#### Khả năng Chọn Tệp (File Picker)

```json
{
  "x-ms-capabilities": {
    "file-picker": {
      "open": {
        "operationId": "OneDriveFilePickerOpen",
        "parameters": {
          "dataset": {
            "value-property": "dataset"
          }
        }
      },
      "browse": {
        "operationId": "OneDriveFilePickerBrowse",
        "parameters": {
          "dataset": {
            "value-property": "dataset"
          }
        }
      },
      "value-title": "DisplayName",
      "value-collection": "value",
      "value-folder-property": "IsFolder",
      "value-media-property": "MediaType"
    }
  }
}
```

#### Khả năng Kiểm tra Kết nối (Lưu ý: Không được hỗ trợ cho Trình kết nối Tùy chỉnh)

```json
{
  "x-ms-capabilities": {
    "testConnection": {
      "operationId": "TestConnection",
      "parameters": {
        "param1": "literal-value"
      }
    }
  }
}
```

#### Ngữ cảnh Thao tác để Mô phỏng

```json
{
  "x-ms-operation-context": {
    "simulate": {
      "operationId": "SimulateOperation",
      "parameters": {
        "param1": {
          "parameter": "inputParam"
        }
      }
    }
  }
}
```

### Cấu hình OAuth Cơ bản

```json
{
  "type": "oauthSetting",
  "oAuthSettings": {
    "identityProvider": "oauth2",
    "clientId": "your-client-id",
    "scopes": ["scope1", "scope2"],
    "redirectMode": "Global"
  }
}
```

#### Ví dụ về Nhiều Định nghĩa Bảo mật

```json
{
  "securityDefinitions": {
    "oauth2": {
      "type": "oauth2",
      "flow": "accessCode",
      "authorizationUrl": "https://api.example.com/oauth/authorize",
      "tokenUrl": "https://api.example.com/oauth/token",
      "scopes": {
        "read": "Read access",
        "write": "Write access"
      }
    },
    "apiKey": {
      "type": "apiKey",
      "name": "X-API-Key",
      "in": "header"
    }
  }
}
```

**Lưu ý**: Tối đa hai định nghĩa bảo mật có thể cùng tồn tại, nhưng xác thực "None" không thể kết hợp với các phương thức khác.

### Thiết lập Tham số Động

```json
{
  "x-ms-dynamic-values": {
    "operationId": "GetItems",
    "value-path": "id",
    "value-title": "name"
  }
}
```

### Mẫu Chính sách để Định tuyến

```json
{
  "templateId": "routerequesttoendpoint",
  "title": "Route to backend",
  "parameters": {
    "x-ms-apimTemplate-operationName": ["GetData"],
    "x-ms-apimTemplateParameter.newPath": "/api/v2/data"
  }
}
```

---

## Các Thực hành Tốt nhất

1.  **Sử dụng IntelliSense**: Các lược đồ này cung cấp khả năng tự động hoàn thành và xác thực phong phú giúp ích trong quá trình phát triển.
2.  **Tuân thủ Quy ước Đặt tên**: Sử dụng tên mô tả cho các thao tác và tham số để cải thiện khả năng đọc mã.
3.  **Triển khai Xử lý Lỗi**: Định nghĩa các lược đồ phản hồi và mã lỗi phù hợp để xử lý các kịch bản thất bại một cách đúng đắn.
4.  **Kiểm tra Kỹ lưỡng**: Xác thực lược đồ trước khi triển khai để phát hiện các vấn đề sớm trong quá trình phát triển.
5.  **Ghi chú các Tiện ích mở rộng**: Thêm nhận xét cho các tiện ích mở rộng dành riêng cho Microsoft để nhóm hiểu và bảo trì trong tương lai.
6.  **Quản lý Phiên bản**: Sử dụng phiên bản ngữ nghĩa (semantic versioning) trong thông tin API để theo dõi các thay đổi và khả năng tương thích.
7.  **Ưu tiên Bảo mật**: Luôn triển khai các cơ chế xác thực phù hợp để bảo vệ các điểm cuối API của bạn.

---

## Gỡ lỗi

### Các lỗi Vi phạm Lược đồ Phổ biến

- **Thiếu các thuộc tính bắt buộc**: `swagger: "2.0"`, `info.title`, `info.version`, `paths`
- **Định dạng mẫu không hợp lệ**:
  - GUID phải khớp chính xác định dạng `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
  - URL phải là URI hợp lệ với lược đồ phù hợp
  - Đường dẫn phải bắt đầu bằng `/`
  - Host không được bao gồm giao thức, đường dẫn hoặc khoảng trắng
- **Đặt tên tiện ích mở rộng của bên thứ ba không chính xác**: Sử dụng `x-ms-*` cho các tiện ích mở rộng của Microsoft, `^x-(?!ms-)` cho các tiện ích khác
- **Loại định nghĩa bảo mật không khớp**: Mỗi định nghĩa bảo mật phải thuộc chính xác một loại
- **Giá trị enum không hợp lệ**: Kiểm tra các giá trị được phép cho `x-ms-visibility`, `x-ms-trigger`, các loại tham số
- **`$ref` trỏ đến các vị trí không hợp lệ**: Phải trỏ đến `#/definitions/`, `#/parameters/`, hoặc `#/responses/`
- **Tham số đường dẫn không được đánh dấu là bắt buộc**: Tất cả các tham số đường dẫn phải có `required: true`
- **Loại 'file' trong ngữ cảnh sai**: Chỉ được phép trong các tham số `formData`, không được phép trong các lược đồ

### Các vấn đề Cụ thể về Định nghĩa API

- **Xung đột lược đồ động**: Không thể sử dụng `x-ms-dynamic-schema` với các thuộc tính lược đồ cố định
- **Lỗi cấu hình trình kích hoạt**: `x-ms-trigger-metadata` yêu cầu cả `kind` và `mode`
- **Thiết lập phân trang**: `x-ms-pageable` yêu cầu thuộc tính `nextLinkName`
- **Cấu hình sai trình chọn tệp**: Phải bao gồm cả thao tác `open` và các thuộc tính bắt buộc
- **Xung đột khả năng**: Một số khả năng có thể xung đột với một số loại tham số nhất định
- **Bảo mật giá trị kiểm thử**: Không bao giờ bao gồm bí mật hoặc PII trong `x-ms-test-value`
- **Thiết lập ngữ cảnh thao tác**: `x-ms-operation-context` yêu cầu một đối tượng `simulate` với `operationId`
- **Lược đồ nội dung thông báo**: `x-ms-notification-content` ở cấp độ đường dẫn phải định nghĩa cấu trúc lược đồ phù hợp
- **Hạn chế loại phương tiện**: `x-ms-media-kind` chỉ hỗ trợ các giá trị `image` hoặc `audio`
- **Cấu hình giá trị trình kích hoạt**: `x-ms-trigger-value` phải có ít nhất một thuộc tính (`value-collection` hoặc `value-path`)

### Công cụ Xác thực

- Sử dụng các trình xác thực Lược đồ JSON để kiểm tra sự tuân thủ của các định nghĩa lược đồ của bạn.
- Tận dụng tính năng xác thực lược đồ tích hợp sẵn của VS Code để phát hiện lỗi trong quá trình phát triển.
- Kiểm tra bằng paconn CLI trước khi triển khai bằng cách sử dụng: `paconn validate --api-def apiDefinition.swagger.json`
- Xác thực theo các yêu cầu của trình kết nối Power Platform để đảm bảo khả năng tương thích.
- Sử dụng cổng thông tin Power Platform Connector để xác thực và kiểm thử trong môi trường mục tiêu.
- Kiểm tra xem các phản hồi của thao tác có khớp với các lược đồ dự kiến để ngăn ngừa lỗi thời gian chạy hay không.

Hãy nhớ: Các lược đồ này đảm bảo các trình kết nối Power Platform của bạn được định dạng đúng và sẽ hoạt động chính xác trong hệ sinh thái Power Platform.
