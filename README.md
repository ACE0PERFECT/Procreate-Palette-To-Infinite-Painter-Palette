# Procreate Palette To Infinite Painter Palette  / Procreate调色板转Infinite Painter调色板

This is a python script for transfer color palette from Procreate to Infinite Painter.  
一个Python脚本，用于将Procreate调色板的颜色添加到Infinite Painter.  

---

# 1.How to use / 1.如何使用

## 1.1
Download "run.py" and establish the python env. If you dont know how to, I have no idea either. Maybe I will make an out-of-the-box site in the future.  
首先下载"run.py" 并搭建python 环境。不知道的话，我也没办法了。也许以后我会做个点两下就能用的网站。  

## 1.2
Export palette from Procreate (this should be a .swatches file) and save it in the same folder as run.py.  
将导出的Procreate调色板文件(是一个以.swatches结尾的文件)保存到run.py所在目录。  

## 1.3
Open the run.py file (if you don't know how to, just open with any text editor.)  
用记事本打开run.py文件。  
  
Edit this value in the script  
把下面这行等号的右边
```
zip_file_path = "example.swatches"
```
as the full name of the .swatches file. For example if the file is named "123.swatches", then this line should be  
改成你的.swatches文件的全名. 比如说你的叫做123.swatches的话，应该改成下面这样
```
zip_file_path = "123.swatches"
```
Run the run.py script in cmd/terminal.  
在cmd或者终端运行run.py.
```
python run.py
```
## 1.4
There should be a file ended with ".clrs" shows up int he folder. Import this .clrs file in Infinite Painter palette.  
程序运行之后会生成一个以".clrs"结尾的文件，在Infinite Painter中调色板那里导入即可。

---

# 2. Something you should know / 2. 你该知道的一些东西
## 2.1 Capacity and Arrangement Diffrence / 容量与排列不同  
In Procreate, palette is 3x10 (total 30). In Infinite Painter, its 5,5,5,5,4 (total 24). The difference in capacity caused the last 6 colors in the Procrate palette to be discarded.  
在Procreate中，调色板是3行10列（总共30），但是Infinite Painter是55554（总共24）。容量的区别导致Procreate调色板的最后6个颜色无法导入。  
## 2.2 Difference in supporting null color / 对空颜色的支持不同
Procreate supports saving null color to the palette while Infinite Painter doesn't. So if there are unoccupied place in your Procreate palette, it will be discarded. This difference together with the   
Procreate支持在调色板上留空，但是Infinite Painter不行。所以Procreate调色板上没放置颜色的格子会被丢弃。
## 2.3 Difference in display / 显示不同
As joint result of 2.1 and 2.2, after transfer, the displayed arrangement of color in Infinite Painter differs to it in Procreate.    
因为前两点的共同作用，这两个软件对颜色的排布会有些不同。
##  2.4 Color might not exactly the same / 颜色并不是完全一样的
Procreate uses HSB(HSV) model for color storage, while Infinite Painter uses ARGB(AARRGGBB) format. They are not exactly the same color mapping method. But this is trivial since human eye may not notice this difference, mostly.  
Procreate用HSB(HSV)色彩空间存储颜色，Infinite Painter用ARGB(AARRGGBB)格式。这两种颜色映射方式不是完全等价的。但是应该没事，因为人眼大多数情况看不出区别。
