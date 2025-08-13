---
description: "Hướng dẫn toàn diện về cách làm việc với cấu trúc YAML của Power Apps Canvas Apps dựa trên lược đồ Microsoft Power Apps YAML v3.0. Bao gồm các công thức Power Fx, cấu trúc điều khiển, kiểu dữ liệu và các phương pháp hay nhất về kiểm soát nguồn."
applyTo: "**/*.{yaml,yml,md,pa.yaml}"
---

# Hướng dẫn Cấu trúc YAML của Power Apps Canvas Apps

## Tổng quan

Tài liệu này cung cấp hướng dẫn toàn diện về cách làm việc với mã YAML cho các ứng dụng canvas Power Apps dựa trên lược đồ Microsoft Power Apps YAML chính thức (v3.0) và tài liệu Power Fx.

**Nguồn Lược đồ Chính thức**: https://raw.githubusercontent.com/microsoft/PowerApps-Tooling/refs/heads/master/schemas/pa-yaml/v3.0/pa.schema.yaml

## Nguyên tắc Thiết kế Power Fx

Power Fx là ngôn ngữ công thức được sử dụng trong toàn bộ các ứng dụng canvas Power Apps. Nó tuân theo các nguyên tắc cốt lõi sau:

### Nguyên tắc Thiết kế

- **Đơn giản**: Sử dụng các khái niệm quen thuộc từ công thức Excel
- **Nhất quán với Excel**: Tương đồng với cú pháp và hành vi của công thức Excel
- **Khai báo**: Mô tả những gì bạn muốn, không phải cách để đạt được nó
- **Hàm**: Tránh các hiệu ứng phụ; hầu hết các hàm đều là hàm thuần túy
- **Kết hợp**: Logic phức tạp được xây dựng bằng cách kết hợp các hàm đơn giản hơn
- **Kiểu dữ liệu mạnh**: Hệ thống kiểu đảm bảo tính toàn vẹn của dữ liệu
- **Tích hợp**: Hoạt động liền mạch trên toàn bộ Power Platform

### Triết lý Ngôn ngữ

Power Fx thúc đẩy:

- Phát triển low-code thông qua các công thức quen thuộc giống như Excel
- Tự động tính toán lại khi các phụ thuộc thay đổi
- An toàn kiểu với kiểm tra tại thời điểm biên dịch
- Các mẫu lập trình hàm

## Cấu trúc Gốc

Mọi tệp YAML của Power Apps đều tuân theo cấu trúc cấp cao nhất này:

```yaml
App:
  Properties:
    # Thuộc tính và công thức cấp ứng dụng
    StartScreen: =Screen1

Screens:
  # Định nghĩa các màn hình

ComponentDefinitions:
  # Định nghĩa các thành phần tùy chỉnh

DataSources:
  # Cấu hình nguồn dữ liệu

EditorState:
  # Siêu dữ liệu của trình soạn thảo (thứ tự màn hình, v.v.)
```

## 1. Phần App

Phần `App` định nghĩa các thuộc tính và cấu hình ở cấp độ ứng dụng.

```yaml
App:
  Properties:
    StartScreen: =Screen1
    BackEnabled: =false
    # Các thuộc tính ứng dụng khác với công thức Power Fx
```

### Điểm chính:

- Chứa các cài đặt trên toàn ứng dụng
- Các thuộc tính sử dụng công thức Power Fx (có tiền tố `=`)
- Thuộc tính `StartScreen` thường được chỉ định

## 2. Phần Screens

Định nghĩa tất cả các màn hình trong ứng dụng dưới dạng một bản đồ không có thứ tự.

```yaml
Screens:
  Screen1:
    Properties:
      # Thuộc tính màn hình
    Children:
      - Label1:
          Control: Label
          Properties:
            Text: ="Hello World"
            X: =10
            Y: =10
      - Button1:
          Control: Button
          Properties:
            Text: ="Click Me"
            X: =10
            Y: =100
```

### Cấu trúc Màn hình:

- **Properties**: Các thuộc tính và công thức ở cấp độ màn hình
- **Children**: Mảng các điều khiển trên màn hình (được sắp xếp theo z-index)

### Định dạng Định nghĩa Điều khiển:

```yaml
ControlName:
  Control: ControlType # Bắt buộc: Mã định danh loại điều khiển
  Properties:
    PropertyName: =PowerFxFormula
  # Các thuộc tính tùy chọn:
  Group: GroupName # Để tổ chức các điều khiển trong Studio
  Variant: VariantName # Biến thể điều khiển (ảnh hưởng đến các thuộc tính mặc định)
  MetadataKey: Key # Mã định danh siêu dữ liệu cho điều khiển
  Layout: LayoutName # Cấu hình bố cục
  IsLocked: true/false # Điều khiển có bị khóa trong trình soạn thảo hay không
  Children: [] # Đối với các điều khiển vùng chứa (được sắp xếp theo z-index)
```

### Phiên bản Điều khiển:

Bạn có thể chỉ định phiên bản điều khiển bằng toán tử `@`:

```yaml
MyButton:
  Control: Button@2.1.0 # Phiên bản cụ thể
  Properties:
    Text: ="Click Me"

MyLabel:
  Control: Label # Sử dụng phiên bản mới nhất theo mặc định
  Properties:
    Text: ="Hello World"
```

## 3. Các loại Điều khiển

### Điều khiển Tiêu chuẩn

Các điều khiển của bên thứ nhất phổ biến bao gồm:

- **Điều khiển Cơ bản**: `Label`, `Button`, `TextInput`, `HTMLText`
- **Điều khiển Nhập liệu**: `Slider`, `Toggle`, `Checkbox`, `Radio`, `Dropdown`, `Combobox`, `DatePicker`, `ListBox`
- **Điều khiển Hiển thị**: `Image`, `Icon`, `Video`, `Audio`, `PDF viewer`, `Barcode scanner`
- **Điều khiển Bố cục**: `Container`, `Rectangle`, `Circle`, `Gallery`, `DataTable`, `Form`
- **Điều khiển Biểu đồ**: `Column chart`, `Line chart`, `Pie chart`
- **Điều khiển Nâng cao**: `Timer`, `Camera`, `Microphone`, `Add picture`, `Import`, `Export`

### Điều khiển Vùng chứa và Bố cục

Lưu ý đặc biệt đối với các điều khiển vùng chứa và các con của chúng:

```yaml
MyContainer:
  Control: Container
  Properties:
    Width: =300
    Height: =200
    Fill: =RGBA(240, 240, 240, 1)
  Children:
    - Label1:
        Control: Label
        Properties:
          Text: ="Inside Container"
          X: =10 # Tương đối so với vùng chứa
          Y: =10 # Tương đối so với vùng chứa
    - Button1:
        Control: Button
        Properties:
          Text: ="Container Button"
          X: =10
          Y: =50
```

### Thành phần Tùy chỉnh

```yaml
MyCustomControl:
  Control: Component
  ComponentName: MyComponent
  Properties:
    X: =10
    Y: =10
    # Các thuộc tính thành phần tùy chỉnh
```

### Thành phần Mã (PCF)

```yaml
MyPCFControl:
  Control: CodeComponent
  ComponentName: publisherprefix_namespace.classname
  Properties:
    X: =10
    Y: =10
```

## 4. Định nghĩa Thành phần

Định nghĩa các thành phần tùy chỉnh có thể tái sử dụng:

```yaml
ComponentDefinitions:
  MyComponent:
    DefinitionType: CanvasComponent
    Description: "Một thành phần có thể tái sử dụng"
    AllowCustomization: true
    AccessAppScope: false
    CustomProperties:
      InputText:
        PropertyKind: Input
        DataType: Text
        Description: "Thuộc tính văn bản đầu vào"
        Default: ="Default Value"
      OutputValue:
        PropertyKind: Output
        DataType: Number
        Description: "Giá trị số đầu ra"
    Properties:
      Fill: =RGBA(255, 255, 255, 1)
      Height: =100
      Width: =200
    Children:
      - Label1:
          Control: Label
          Properties:
            Text: =Parent.InputText
```

### Các loại Thuộc tính Tùy chỉnh:

- **Input**: Nhận giá trị từ cha
- **Output**: Gửi giá trị đến cha
- **InputFunction**: Hàm được gọi bởi cha
- **OutputFunction**: Hàm được định nghĩa trong thành phần
- **Event**: Kích hoạt sự kiện đến cha
- **Action**: Hàm có hiệu ứng phụ

### Các loại Dữ liệu:

- `Text`, `Number`, `Boolean`
- `DateAndTime`, `Color`, `Currency`
- `Record`, `Table`, `Image`
- `VideoOrAudio`, `Screen`

## 5. Nguồn Dữ liệu

Cấu hình các kết nối dữ liệu:

```yaml
DataSources:
  MyTable:
    Type: Table
    Parameters:
      TableLogicalName: account

  MyActions:
    Type: Actions
    ConnectorId: shared_office365users
    Parameters:
      # Các tham số kết nối bổ sung
```

### Các loại Nguồn Dữ liệu:

- **Table**: Bảng Dataverse hoặc dữ liệu dạng bảng khác
- **Actions**: Các hành động của trình kết nối và các luồng

## 6. Trạng thái Trình soạn thảo

Duy trì tổ chức của trình soạn thảo:

```yaml
EditorState:
  ScreensOrder:
    - Screen1
    - Screen2
    - Screen3
  ComponentDefinitionsOrder:
    - MyComponent
    - AnotherComponent
```

## Hướng dẫn Công thức Power Fx

### Cú pháp Công thức:

- Tất cả các công thức phải bắt đầu bằng `=`
- Sử dụng cú pháp Power Fx cho các biểu thức
- Giá trị null có thể được biểu diễn là `null` (không có dấu ngoặc kép)
- Ví dụ:
  ```yaml
  Text: ="Hello World"
  X: =10
  Visible: =Toggle1.Value
  OnSelect: =Navigate(Screen2, ScreenTransition.Fade)
  OptionalProperty: null # Biểu thị không có giá trị
  ```

### Các Mẫu Công thức Phổ biến:

```yaml
# Giá trị tĩnh
Text: ="Static Text"
X: =50
Visible: =true

# Tham chiếu điều khiển
Text: =TextInput1.Text
Visible: =Toggle1.Value

# Tham chiếu cha (đối với các điều khiển trong vùng chứa/thư viện)
Width: =Parent.Width - 20
Height: =Parent.TemplateHeight    # Trong các mẫu thư viện

# Hàm
OnSelect: =Navigate(NextScreen, ScreenTransition.Slide)
Text: =Concatenate("Hello ", User().FullName)

# Logic điều kiện
Visible: =If(Toggle1.Value, true, false)
Fill: =If(Button1.Pressed, RGBA(255,0,0,1), RGBA(0,255,0,1))

# Thao tác dữ liệu
Items: =Filter(DataSource, Status = "Active")
Text: =LookUp(Users, ID = 123).Name
```

### Z-Index và Thứ tự Điều khiển:

- Các điều khiển trong mảng `Children` được sắp xếp theo z-index
- Điều khiển đầu tiên trong mảng = lớp dưới cùng (z-index 1)
- Điều khiển cuối cùng trong mảng = lớp trên cùng (z-index cao nhất)
- Tất cả các điều khiển sử dụng thứ tự tăng dần bắt đầu từ 1

## Quy ước Đặt tên

### Tên Thực thể:

- Tên màn hình: Mô tả và duy nhất
- Tên điều khiển: TypeName + Number (ví dụ: `Button1`, `Label2`)
- Tên thành phần: PascalCase

### Tên Thuộc tính:

- Thuộc tính tiêu chuẩn: Sử dụng chính xác cách viết hoa từ lược đồ
- Thuộc tính tùy chỉnh: Khuyến nghị sử dụng PascalCase

## Các Phương pháp Hay nhất

### 1. Tổ chức Cấu trúc:

- Giữ các màn hình được tổ chức một cách hợp lý
- Nhóm các điều khiển liên quan bằng thuộc tính `Group`
- Sử dụng tên có ý nghĩa cho tất cả các thực thể

### 2. Viết Công thức:

- Giữ cho các công thức dễ đọc và được định dạng tốt
- Sử dụng nhận xét trong các công thức phức tạp khi có thể
- Tránh các biểu thức lồng nhau quá phức tạp

### 3. Thiết kế Thành phần:

- Thiết kế các thành phần để có thể tái sử dụng
- Cung cấp mô tả rõ ràng cho các thuộc tính tùy chỉnh
- Sử dụng các loại thuộc tính phù hợp (Input/Output)

### 4. Quản lý Nguồn Dữ liệu:

- Sử dụng tên mô tả cho các nguồn dữ liệu
- Ghi lại các yêu cầu kết nối
- Giữ cấu hình nguồn dữ liệu ở mức tối thiểu

## Quy tắc Xác thực

### Thuộc tính Bắt buộc:

- Tất cả các điều khiển phải có thuộc tính `Control`
- Định nghĩa thành phần phải có `DefinitionType`
- Nguồn dữ liệu phải có `Type`

### Mẫu Đặt tên:

- Tên thực thể: Tối thiểu 1 ký tự, chữ và số
- ID loại điều khiển: Theo mẫu `^([A-Z][a-zA-Z0-9]*/)?[A-Z][a-zA-Z0-9]*(@\d+\.\d+\.\d+)?$`
- Tên thành phần mã: Theo mẫu `^([a-z][a-z0-9]{1,7})_([a-zA-Z0-9]\.)+[a-zA-Z0-9]+$`

## Các Vấn đề Thường gặp và Giải pháp

### 1. Loại Điều khiển không hợp lệ:

- Đảm bảo các loại điều khiển được viết đúng chính tả
- Kiểm tra cách viết hoa phù hợp
- Xác minh loại điều khiển được hỗ trợ trong lược đồ

### 2. Lỗi Công thức:

- Tất cả các công thức phải bắt đầu bằng `=`
- Sử dụng cú pháp Power Fx phù hợp
- Kiểm tra các tham chiếu thuộc tính chính xác

### 3. Xác thực Cấu trúc:

- Duy trì thụt lề YAML phù hợp
- Đảm bảo các thuộc tính bắt buộc có mặt
- Tuân thủ chính xác cấu trúc lược đồ

### 4. Vấn đề về Thành phần Tùy chỉnh:

- Xác minh `ComponentName` khớp với định nghĩa
- Đảm bảo các thuộc tính tùy chỉnh được định nghĩa đúng cách
- Kiểm tra các loại thuộc tính có phù hợp không
- Xác thực các tham chiếu thư viện thành phần nếu sử dụng các thành phần bên ngoài

### 5. Cân nhắc về Hiệu suất:

- Tránh các công thức lồng nhau sâu trong YAML
- Sử dụng các truy vấn nguồn dữ liệu hiệu quả
- Cân nhắc các công thức có thể ủy quyền cho các tập dữ liệu lớn
- Giảm thiểu các tính toán phức tạp trong các thuộc tính được cập nhật thường xuyên

## Các Chủ đề Nâng cao

### 1. Tích hợp Thư viện Thành phần:

```yaml
ComponentDefinitions:
  MyLibraryComponent:
    DefinitionType: CanvasComponent
    AllowCustomization: true
    ComponentLibraryUniqueName: "pub_MyComponentLibrary"
    # Chi tiết định nghĩa thành phần
```

### 2. Cân nhắc về Thiết kế Đáp ứng:

- Sử dụng `Parent.Width` và `Parent.Height` để định kích thước đáp ứng
- Cân nhắc các bố cục dựa trên vùng chứa cho các giao diện người dùng phức tạp
- Sử dụng công thức để định vị và định kích thước động

### 3. Mẫu Thư viện (Gallery):

```yaml
MyGallery:
  Control: Gallery
  Properties:
    Items: =DataSource
    TemplateSize: =100
  Children:
    - GalleryTemplate: # Mẫu cho mỗi mục trong thư viện
        Children:
          - TitleLabel:
              Control: Label
              Properties:
                Text: =ThisItem.Title
                Width: =Parent.TemplateWidth - 20
```

### 4. Điều khiển Biểu mẫu và Thẻ Dữ liệu:

```yaml
MyForm:
  Control: Form
  Properties:
    DataSource: =DataSource
    DefaultMode: =FormMode.New
  Children:
    - DataCard1:
        Control: DataCard
        Properties:
          DataField: ="Title"
        Children:
          - DataCardValue1:
              Control: TextInput
              Properties:
                Default: =Parent.Default
```

### 5. Xử lý Lỗi trong Công thức:

```yaml
Properties:
  Text: =IfError(LookUp(DataSource, ID = 123).Name, "Not Found")
  Visible: =!IsError(DataSource)
  OnSelect: =IfError(
    Navigate(DetailScreen, ScreenTransition.Cover),
    Notify("Navigation failed", NotificationType.Error)
  )
```

## Quản lý Mã nguồn Power Apps

### Truy cập Tệp Mã nguồn:

Các tệp YAML của Power Apps có thể được lấy thông qua một số phương pháp:

1. **Power Platform CLI**:

   ```powershell
   # Liệt kê các ứng dụng canvas trong môi trường
   pac canvas list

   # Tải xuống và giải nén các tệp YAML
   pac canvas download --name "MyApp" --extract-to-directory "C:\path\to\destination"
   ```

2. **Giải nén Thủ công từ .msapp**:

   ```powershell
   # Giải nén tệp .msapp bằng PowerShell
   Expand-Archive -Path "C:\path\to\yourFile.msapp" -DestinationPath "C:\path\to\destination"
   ```

3. **Tích hợp Git với Dataverse**: Truy cập trực tiếp vào các tệp nguồn mà không cần tệp .msapp

### Cấu trúc Tệp trong .msapp:

- `\src\App.pa.yaml` - Đại diện cho cấu hình App chính
- `\src\[ScreenName].pa.yaml` - Một tệp cho mỗi màn hình
- `\src\Component\[ComponentName].pa.yaml` - Định nghĩa thành phần

**Lưu ý Quan trọng**:

- Chỉ các tệp trong thư mục `\src` mới dành cho kiểm soát nguồn
- Các tệp .pa.yaml là **chỉ đọc** và chỉ dành cho mục đích xem xét
- Việc chỉnh sửa, hợp nhất và giải quyết xung đột từ bên ngoài không được hỗ trợ
- Các tệp JSON trong .msapp không ổn định để kiểm soát nguồn

### Sự phát triển của Phiên bản Lược đồ:

1. **Định dạng Thử nghiệm** (\*.fx.yaml): Không còn được phát triển
2. **Bản xem trước Sớm**: Định dạng tạm thời, không còn được sử dụng
3. **Mã nguồn** (\*.pa.yaml): Định dạng hiện tại đang hoạt động với hỗ trợ kiểm soát phiên bản

## Tham khảo Công thức Power Fx

### Các loại Công thức:

#### **Hàm (Functions)**: Nhận tham số, thực hiện các thao tác, trả về giá trị

```yaml
Properties:
  Text: =Concatenate("Hello ", User().FullName)
  X: =Sum(10, 20, 30)
  Items: =Filter(DataSource, Status = "Active")
```

#### **Tín hiệu (Signals)**: Trả về thông tin môi trường (không có tham số)

```yaml
Properties:
  Text: =Location.Latitude & ", " & Location.Longitude
  Visible: =Connection.Connected
  Color: =If(Acceleration.X > 5, Color.Red, Color.Blue)
```

#### **Bảng liệt kê (Enumerations)**: Các giá trị hằng số được xác định trước

```yaml
Properties:
  Fill: =Color.Blue
  Transition: =ScreenTransition.Fade
  Align: =Align.Center
```

#### **Toán tử có tên (Named Operators)**: Truy cập thông tin vùng chứa

```yaml
Properties:
  Text: =ThisItem.Title # Trong thư viện
  Width: =Parent.Width - 20 # Trong vùng chứa
  Height: =Self.Height / 2 # Tự tham chiếu
```

### Các Hàm Power Fx Thiết yếu cho YAML:

#### **Điều hướng & Điều khiển Ứng dụng**:

```yaml
OnSelect: =Navigate(NextScreen, ScreenTransition.Cover)
OnSelect: =Back()
OnSelect: =Exit()
OnSelect: =Launch("https://example.com")
```

#### **Thao tác Dữ liệu**:

```yaml
Items: =Filter(DataSource, Category = "Active")
Text: =LookUp(Users, ID = 123).Name
OnSelect: =Patch(DataSource, ThisItem, {Status: "Complete"})
OnSelect: =Collect(LocalCollection, {Name: TextInput1.Text})
```

#### **Logic Điều kiện**:

```yaml
Visible: =If(Toggle1.Value, true, false)
Text: =Switch(Status, "New", "🆕", "Complete", "✅", "❓")
Fill: =If(Value < 0, Color.Red, Color.Green)
```

#### **Xử lý Văn bản**:

```yaml
Text: =Concatenate("Hello ", User().FullName)
Text: =Upper(TextInput1.Text)
Text: =Substitute(Label1.Text, "old", "new")
Text: =Left(Title, 10) & "..."
```

#### **Phép toán Toán học**:

```yaml
Text: =Sum(Sales[Amount])
Text: =Average(Ratings[Score])
Text: =Round(Calculation, 2)
Text: =Max(Values[Number])
```

#### **Hàm Ngày & Giờ**:

```yaml
Text: =Text(Now(), "mm/dd/yyyy")
Text: =DateDiff(StartDate, EndDate, Days)
Text: =Text(Today(), "dddd, mmmm dd, yyyy")
Visible: =IsToday(DueDate)
```

### Hướng dẫn Cú pháp Công thức:

#### **Quy tắc Cú pháp Cơ bản**:

- Tất cả các công thức bắt đầu bằng `=`
- Không có dấu `+` hoặc `=` đứng trước (không giống Excel)
- Dấu ngoặc kép cho chuỗi văn bản: `="Hello World"`
- Tham chiếu thuộc tính: `ControlName.PropertyName`
- Nhận xét không được hỗ trợ trong ngữ cảnh YAML

#### **Các thành phần của Công thức**:

```yaml
# Giá trị chữ
Text: ="Static Text"
X: =42
Visible: =true

# Tham chiếu thuộc tính điều khiển
Text: =TextInput1.Text
Visible: =Checkbox1.Value

# Lời gọi hàm
Text: =Upper(TextInput1.Text)
Items: =Sort(DataSource, Title)

# Biểu thức phức tạp
Text: =If(IsBlank(TextInput1.Text), "Enter text", Upper(TextInput1.Text))
```

#### **Công thức Hành vi vs. Công thức Thuộc tính**:

```yaml
# Công thức thuộc tính (tính toán giá trị)
Properties:
  Text: =Concatenate("Hello ", User().FullName)
  Visible: =Toggle1.Value

# Công thức hành vi (thực hiện hành động - sử dụng dấu chấm phẩy cho nhiều hành động)
Properties:
  OnSelect: =Set(MyVar, true); Navigate(NextScreen); Notify("Done!")
```

### Các Mẫu Công thức Nâng cao:

#### **Làm việc với Bộ sưu tập (Collections)**:

```yaml
Properties:
  Items: =Filter(MyCollection, Status = "Active")
  OnSelect: =ClearCollect(MyCollection, DataSource)
  OnSelect: =Collect(MyCollection, {Name: "New Item", Status: "Active"})
```

#### **Xử lý Lỗi**:

```yaml
Properties:
  Text: =IfError(Value(TextInput1.Text), 0)
  OnSelect: =IfError(
    Patch(DataSource, ThisItem, {Field: Value}),
    Notify("Error updating record", NotificationType.Error)
  )
```

#### **Thiết lập Thuộc tính Động**:

```yaml
Properties:
  Fill: =ColorValue("#" & HexInput.Text)
  Height: =Parent.Height * (Slider1.Value / 100)
  X: =If(Alignment = "Center", (Parent.Width - Self.Width) / 2, 0)
```

## Các Phương pháp Hay nhất khi Làm việc với Công thức

### Tổ chức Công thức:

- Chia các công thức phức tạp thành các phần nhỏ hơn, dễ đọc
- Sử dụng biến để lưu trữ các tính toán trung gian
- Bình luận logic phức tạp bằng cách sử dụng tên điều khiển mô tả
- Nhóm các tính toán liên quan lại với nhau

### Tối ưu hóa Hiệu suất:

- Sử dụng các hàm có thể ủy quyền khi làm việc với các tập dữ liệu lớn
- Tránh các lời gọi hàm lồng nhau trong các thuộc tính được cập nhật thường xuyên
- Sử dụng bộ sưu tập cho các phép biến đổi dữ liệu phức tạp
- Giảm thiểu các lời gọi đến các nguồn dữ liệu bên ngoài

## Các loại Dữ liệu và Thao tác trong Power Fx

### Các loại Dữ liệu:

#### **Kiểu Nguyên thủy**:

- **Boolean**: `=true`, `=false`
- **Number**: `=123`, `=45.67`
- **Text**: `="Hello World"`
- **Date**: `=Date(2024, 12, 25)`
- **Time**: `=Time(14, 30, 0)`
- **DateTime**: `=Now()`

#### **Kiểu Phức tạp**:

- **Color**: `=Color.Red`, `=RGBA(255, 128, 0, 1)`
- **Record**: `={Name: "John", Age: 30}`
- **Table**: `=Table({Name: "John"}, {Name: "Jane"})`
- **GUID**: `=GUID()`

#### **Chuyển đổi Kiểu**:

```yaml
Properties:
  Text: =Text(123.45, "#,##0.00")        # Số sang văn bản
  Text: =Value("123.45")                 # Văn bản sang số
  Text: =DateValue("12/25/2024")         # Văn bản sang ngày
  Visible: =Boolean("true")              # Văn bản sang boolean
```

#### **Kiểm tra Kiểu**:

```yaml
Properties:
  Visible: =Not(IsBlank(OptionalField))
  Visible: =Not(IsError(Value(TextInput1.Text)))
  Visible: =IsNumeric(TextInput1.Text)
```

### Thao tác với Bảng:

#### **Tạo Bảng**:

```yaml
Properties:
  Items: =Table(
    {Name: "Product A", Price: 10.99},
    {Name: "Product B", Price: 15.99}
  )
  Items: =["Option 1", "Option 2", "Option 3"]  # Bảng một cột
```

#### **Lọc và Sắp xếp**:

```yaml
Properties:
  Items: =Filter(Products, Price > 10)
  Items: =Sort(Products, Name, Ascending)
  Items: =SortByColumns(Products, "Price", Descending, "Name", Ascending)
```

#### **Biến đổi Dữ liệu**:

```yaml
Properties:
  Items: =AddColumns(Products, "Total", Price * Quantity)
  Items: =RenameColumns(Products, "Price", "Cost")
  Items: =ShowColumns(Products, "Name", "Price")
  Items: =DropColumns(Products, "InternalID")
```

#### **Tổng hợp**:

```yaml
Properties:
  Text: =Sum(Products, Price)
  Text: =Average(Products, Rating)
  Text: =Max(Products, Price)
  Text: =CountRows(Products)
```

### Biến và Quản lý Trạng thái:

#### **Biến Toàn cục**:

```yaml
Properties:
  OnSelect: =Set(MyGlobalVar, "Hello World")
  Text: =MyGlobalVar
```

#### **Biến Ngữ cảnh**:

```yaml
Properties:
  OnSelect: =UpdateContext({LocalVar: "Screen Specific"})
  OnSelect: =Navigate(NextScreen, None, {PassedValue: 42})
```

#### **Bộ sưu tập (Collections)**:

```yaml
Properties:
  OnSelect: =ClearCollect(MyCollection, DataSource)
  OnSelect: =Collect(MyCollection, {Name: "New Item"})
  Items: =MyCollection
```

## Trình kết nối Nâng cao và Dữ liệu Ngoài trong Power Fx

### Tích hợp Trình kết nối:

```yaml
DataSources:
  SharePointList:
    Type: Table
    Parameters:
      TableLogicalName: "Custom List"

  Office365Users:
    Type: Actions
    ConnectorId: shared_office365users
```

### Làm việc với Dữ liệu Ngoài:

```yaml
Properties:
  Items: =Filter(SharePointList, Status = "Active")
  OnSelect: =Office365Users.SearchUser({searchTerm: SearchInput.Text})
```

### Cân nhắc về Ủy quyền (Delegation):

```yaml
Properties:
  # Các thao tác có thể ủy quyền (thực thi phía máy chủ)
  Items: =Filter(LargeTable, Status = "Active")    # Hiệu quả

  # Các thao tác không thể ủy quyền (có thể tải xuống tất cả các bản ghi)
  Items: =Filter(LargeTable, Len(Description) > 100)  # Cảnh báo được đưa ra
```

## Gỡ lỗi và các Mẫu Phổ biến

### Các Mẫu Lỗi Phổ biến:

```yaml
# Xử lý giá trị trống
Properties:
  Text: =If(IsBlank(OptionalText), "Default", OptionalText)

# Xử lý lỗi một cách mượt mà
Properties:
  Text: =IfError(RiskyOperation(), "Fallback Value")

# Xác thực đầu vào
Properties:
  Visible: =And(
    Not(IsBlank(NameInput.Text)),
    IsNumeric(AgeInput.Text),
    IsMatch(EmailInput.Text, Email)
  )
```

### Tối ưu hóa Hiệu suất:

```yaml
# Tải dữ liệu hiệu quả
Properties:
  Items: =Filter(LargeDataSource, Status = "Active")    # Lọc phía máy chủ

# Sử dụng các thao tác có thể ủy quyền
Properties:
  Items: =Sort(Filter(DataSource, Active), Name)        # Có thể ủy quyền
  # Tránh: Sort(DataSource, If(Active, Name, ""))       # Không thể ủy quyền
```

### Quản lý Bộ nhớ:

```yaml
# Xóa các bộ sưu tập không sử dụng
Properties:
  OnSelect: =Clear(TempCollection)

# Giới hạn việc truy xuất dữ liệu
Properties:
  Items: =FirstN(Filter(DataSource, Status = "Active"), 50)
```

Hãy nhớ rằng: Hướng dẫn này cung cấp phạm vi bao quát toàn diện về cấu trúc YAML của Power Apps Canvas Apps và các công thức Power Fx. Luôn xác thực YAML của bạn với lược đồ chính thức và kiểm tra các công thức trong môi trường Power Apps
