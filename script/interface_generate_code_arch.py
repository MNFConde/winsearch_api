'''
指定interface路径，执行这个脚本，生成函数框架
'''

import re
from pathlib import Path

def extract_with_positions(source_file: Path, output_file):
    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 收集所有函数名
    function_names = []
    for i, line in enumerate(lines):
        if '@interface' in line:
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                func_match = re.search(r'def (\w+)\(\):', next_line)
                if func_match:
                    function_names.append(func_match.group(1))
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # 写入import语句
        f.write('from winsearch.core.registry import Registry')
        f.write(f'from {source_file.stem} import (\n')
        for func_name in function_names:
            f.write(f'    {func_name},\n')
        f.write(')\n\n')
        f.write('from pathlib import Path')
        f.write('import ctypes')
        f.write('from ctypes import wintypes')
        
        # 写入函数定义
        current_section_comment = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # 检查是否是注释行
            if line.strip().startswith('#'):
                current_section_comment.append(line)
                i += 1
                continue
                
            # 检查是否是函数定义行
            if '@interface' in line:
                # 写入当前段的注释
                if current_section_comment:
                    f.writelines(current_section_comment)
                    current_section_comment = []
                
                # 获取下一行的函数定义
                if i + 1 < len(lines):
                    next_line = lines[i + 1]
                    # func_match = re.search(r'def (\w+)\(\):', next_line)
                    func_match = re.search(r'def (\w+)\((.*?)\):', next_line)
                    if func_match:
                        func_name = func_match.group(1)
                        func_args = func_match.group(2)
                        generate_text(f, func_name, func_args)
                i += 2
                continue
                
            i += 1

def snake_to_upper(name: str) -> str:
    name_list = name.split('_')
    return ''.join([i[0].upper() + i[1:] for i in name_list])

num = 1
from io import TextIOWrapper
def generate_text(f: TextIOWrapper, name, func_args):
    global num
    f.write(f'\n@{name}.init\n')
    f.write(f'def fn{num}_init({func_args}) -> None:\n')
    f.write(f'    everything_dll.Everything_{snake_to_upper(name)}.argtypes = [\n')
    f.write(f'    \n')
    f.write(f'    ]\n')
    f.write(f'    everything_dll.Everything_{snake_to_upper(name)}.restype  = []\n')
    f.write(f'\n')
    f.write(f"@everything('{name}')\n")
    f.write(f"@{name}.impl\n")
    f.write(f"def fn{num}({func_args}) -> :\n")
    f.write(f"    everything_dll.Everything_{snake_to_upper(name)}()\n")
    
    num += 1
    

if __name__ == "__main__":
    extract_with_positions(
        Path(__file__).parent / 'everything_base_interface.py',
        Path(__file__).parent / 'new_functions.py',
    )
