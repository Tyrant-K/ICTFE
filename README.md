# ICTFE
Intergrated CTF Environment

集成式CTF解题环境

采用PyQt5编写, 2020年03月25日开工, 欢迎fork, 开发相关功能并pull到本仓库.

## 如何参与

**ICTFE将于2020年6月进行大规模重构, 包括构建插件系统和各类异常处理, 操作系统集成等, 同时进行代码清理. 敬请期待2.0.**

fork本仓库, 使用PyQt5进行开发, 然后发起一个Pull Request.

如果你没有学习过PyQt5, 可以简单的查看[QuickDevelopingDocs](QuickDevelopingDocs/0_ICTFE密码学插件开发指北.md)中的文档, 然后尝试进行开发.

如果你用有丰富的UI开发经验, 可以帮开发者优化一下界面和逻辑代码并做好模块化, 感激不尽~

## 如何使用

clone本仓库到本地, 安装PyQt5

```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 如果需要在Windows上进行打包，则需要安装 pyinstaller
# 这里请注意, gmpy2在Windows平台上可能不会正常工作.
# 请Windows平台的用户前往 https://www.lfd.uci.edu/~gohlke/pythonlibs/
# 下载对应版本的gmpy2并本地安装.
# 待软件开发完成后将进行不依赖于开发环境的打包工作.
```

请不要使用Windows应用商店提供的python环境， 那个存在问题。

运行

```
./Run.py
```

后续随着工具集成会加入所需要的Python模块说明.

# 目前进度:

## 文件管理

添加暂存池, 方便在不同分类之间传递数据.

## Web

Postwoman

## 数据流

提供绝大多数的编码, 密码工具, 支持状态的保存, 导出与加载, 并具有完善的插件系统, 可以随时扩展,

## 启动器

支持创建 最多 120 个自定义分区, 每个分区支持最多54个链接按钮. 采用SQLite进行自动存储.
支持快速添加和删除按钮, 支持拖放文件, 并支持一次性拖入多个不同种类的文件.

所设定的文件将尝试执行, 若不可执行则调用命令使用相关软件打开当前文件.

## CyberChef

即**数据厨师**分区. 至于为什么要把CyberChef翻译成数据厨师, 这个问题就不必纠结了... 因为实在想不到什么好翻译了

如果直接写CyberChef的话好像会超出按钮的长度所以就翻译成中文了 (逃

本分区集成了CyberChef的所有功能, 支持文件输入输出, 尽力与官方版本保持同步.

## CTF Wiki

集成了完整的离线CTF Wiki. 将来本wiki将会和官方wiki同步更改.

## Kiwix

集成了Kiwix阅读器, 支持阅读zim格式的百科数据文件.

## 浏览器

集成了一个具有基本浏览功能的浏览器. 支持Flash插件的使用.
Windows上的H5不包含h.264的解码器, 无法进行H5播放. Linux上一切正常.

# Release 1.0.0 Alpha
