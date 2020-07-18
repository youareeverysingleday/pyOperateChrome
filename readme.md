# 使用说明

## 编译环境
|编号|环境名称|版本|
|---|---|---|
|1|操作系统|windows 7 x64|
|2|python|3.7.5|
|3|selenium|3.141.0|
|4|pandas|0.25.3|
|5|numpy|1.16.1|

## 操作步骤
- 有两种方式运行。
    1. python的各种IDE中直接运行pyOperateChrome文件。
    2. 在windows环境中，使用批处理文件运行。Use bat file run the program, in windwos.

## 注意事项
- 要求lots_user_agent.csv或者ua.csv文件和pyOperateChrome.py在同一个文件夹中。
- 在VPS是使用中可能碰到的问题及解决步骤：
    1. 运行python.exe。
        1. 安装完Python.exe之后，如果发现site-packages中没有Pip的存在。也就是说pip在python安装过程中没有安装成功，那么需要在命令行中输入python -m ensurepip --default-pip，来单独安装pip。
            - 可能的原因是VPS对对外访问的端口做出了限制，导致安装pip失败了。
        2. 安装vc_redist.x64.exe。
        3. 安装过程中一定要勾选PATH的选项（添加到系统环境变量中）。
        4. 如果python第三方库安装失败，可能是因为pip没有更新。需要使用命令：python -m pip install --upgrade pip来解决。 
    2. 在第一步完成之后在windows cmd中输入以下命令：
        - pip install selenium
        - pip install pandas
        - pip install argparse
    3. 目前所有的文件都需要放在d:\project目录下。
    4. 运行command.bat文件。
    5. 其他VPS中chrome的版本必须和当前VPS中chrome的版本一致。
