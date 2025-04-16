import os

def rename_files_in_folder(folder_path):
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)
    
    # 过滤并排序文件（如果需要）
    files = sorted([f for f in files if os.path.isfile(os.path.join(folder_path, f))])

    # 遍历文件并重命名
    for index, file in enumerate(files, start=1):
        # 获取文件的扩展名
        file_extension = os.path.splitext(file)[1]
        
        # 生成新的文件名
        new_name = f"{index}{file_extension}"
        
        # 生成完整的旧文件路径和新文件路径
        old_file_path = os.path.join(folder_path, file)
        new_file_path = os.path.join(folder_path, new_name)
        
        # 重命名文件
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {old_file_path} to {new_file_path}")

# 示例使用
folder_path = "Cleistogenes-songorica"  # 替换为你的文件夹路径
rename_files_in_folder(folder_path)