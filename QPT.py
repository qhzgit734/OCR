# 导入QPT
from qpt.executor import CreateExecutableModule as CEM
from qpt.smart_opt import set_default_pip_source

# 镜像源
set_default_pip_source("https://pypi.tuna.tsinghua.edu.cn/simple")

if __name__ == '__main__':
              #-----关于路径的部分，强烈建议使用绝对路径避免出现问题-----
              # [项目文件夹]待打包的目录，并且该目录下需要有↓下方提到的py文件
  module = CEM(work_dir="F:\\work\\other\\py_cnocr",
              # [主程序文件]用户启动EXE文件后，QPT要执行的py文件 
              launcher_py_path="F:\\work\\other\\py_cnocr\\OCR.py",
              # [输出目录]打包后相关文件的输出目录
              save_path="F:\\work\\other\\py_ocr",
              # [Python依赖]此处可填入依赖文件路径，也可设置为auto自动搜索依赖
              requirements_file="auto",
              # [终端窗口]设置为True后，运行时将不会展示黑色终端窗口
              hidden_terminal=True,
              # [跨版本编译]需要预先from qpt.modules.python_env import Python37
              # 好奇什么时候需要跨版本编译？可参考下方"进阶使用QPT"一节的《打包兼容性更强的Python解释器》  
            # interpreter_module=Python37(),                         
              # [自定义图标文件]支持将exe文件设置为ico/JPG/PNG等格式的自定义图标                                                      
              icon="F:\\work\\other\\py_cnocr\\Development tools.ico")                         
  # 开始打包
  module.make()