# PicuTxt 字符串与图片合并脚本

能把图片与字符串合并的Python脚本，使这个图片能正常浏览，但字符串被写入了文件末尾，能够被该脚本读取。

A Python script which can combine an image with a string so that the image can be browsed as usual, but the text is written to the end of the file which can be read by this script.

## 依赖 Dependency

Python 3

## 用法 Usage

**合并：**

下载项目，选中图片和要合并的txt文件，同时拖入PicuTxt.py，即可合并另存为新的图片，保存在图片所在目录。

或者只拖入图片到PicuTxt.py，输入文字后回车，即可把输入的文字写入图片。 

**读取：**

把图片拖入PicuTxt.py即可输出文字。



**Combine:**
Download the project, select the picture and the txt file together, and drag them into PicuTxt.py, a new picture will be saved to the directory of the picture.
Or just drag a picture to PicuTxt.py, enter the text and press enter to combine the text and picture together.
**Read:**
Drag the picture into PicuTxt.py to output text.

## 原理 Principles 

把文本转换为utf-8编码，然后把图片、一个标记、文本依次以二进制写入新的图片即可。读取时，以二进制找到标记，然后以utf-8编码读取标记后的文字。实际上，用记事本打开图片拉到最后也能找到文字，不过只能正常显示英文和数字。

Encoding the text as UTF-8, then write the picture, the mark and text into the new picture in binary. When reading, find the mark in binary, and then read the text after the mark with UTF-8 decoding. In fact, you can also open the picture in Notepad and go to the end in order to find the text, but only the English and numbers can be displayed.

## License

The project is released under MIT License.
