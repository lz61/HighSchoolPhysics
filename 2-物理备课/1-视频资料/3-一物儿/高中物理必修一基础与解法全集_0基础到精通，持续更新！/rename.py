import os


def rename_videos(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否是mp4格式
        if filename.endswith('.mp4'):
            # 找到需要删除的前缀的结束位置（即"-"的位置）
            dash_index = filename.find('-')
            if dash_index != -1:
                # 提取"-"之后的新文件名
                new_filename = filename[dash_index + 1:]
                # 构建原文件路径和新文件路径
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_filename)
                # 重命名文件
                os.rename(old_path, new_path)
                print(f"已将 {filename} 重命名为 {new_filename}")


# 输入文件夹路径
folder = input("请输入文件夹路径：")
rename_videos(folder)
print("重命名完成！")
