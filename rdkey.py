import random
import string
# Hàm Này Tạo Key K Cần Quan Tâm !
def randomKEY(length=12):
    chars = string.ascii_letters + string.digits  
    return ''.join(random.choice(chars) for _ in range(length))


# Thư Mục Chứa Các User Trong SMP Của Bạn
userPlayer = [ # thay thế bằng các user của bạn nhé
    "truongvinh244", "truongvinhdz", "zinsy"
]

# Đường Dẫn File Bạn Muốn Chứa User Và Key !
# Có Thể Thay Thế Đường Dẫn Của Bạn Cho Đúng >>>
path = str("PY/key_file")

# Độ Dài Của Doạn Mã Key Tạo
# Có Thể Thay Số 24 Bằng Độ Dài Bạn Mong Muốn
length = 24

# Nội Dung Trước Key !
# CÓ THỂ THAY THẾ BẰNG TÊN SMP CỦA BẠN !
# Nếu Không Muốn Thêm Hãy Bỏ Trống Như Thế Này >> content1 = ""
content1 = "ZinSY_" # đầu content
content2 = "_SummerSMP" # cuối content

# Cơ Chế Tạo File_User Và Key
for userFile in userPlayer:
    with open(str(path+"/"+userFile), "w") as keyFile:
        keyFile.write(
            str(content1) + 
            str(randomKEY(length)) +
            str(content2)
        )
## Made By TruongVinh244
## linkbio.co/truongvinh244

### Project Login IPS and etc here 
# https://github.com/truongvinh244/Login_IPs
