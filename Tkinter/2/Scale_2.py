# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-08 21:03:39
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-08 21:11:11

# 通过 resolution 选项控制分辨率（步长）
# 通过 tickinterval 选项设置刻度

root = Tk()
Scale(root, from_ = 0, to = 50, tickinterval = 5, length = 200,\
    resolution = 5, orient = VERTICAL).pack()

Scale(root, from_ = 0, to = 200, tickinterval = 10, length = 600,\
    orient = HORIZONTAL).pack()

mainloop()