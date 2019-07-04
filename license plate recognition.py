"""
先考虑整体问题的话，车牌识别可以分为以下的部分：
定位问题：用于定位车牌的位置
字符分割问题:用于分割每个字符区域的位置
字符识别问题：用于识别字符

"""

# 导入支持库
import cv2
import numpy as np
import matplotlib.pyplot as plt



#读取图像
def readimage(imagename,imageflag,showflage):
    image = cv2.imread(imagename,flags=imageflag)
    #使用except异常处理
    #还可以根据读图的内容来进行异常判断，图像内容为none则代表读图失败
    try:
        print("读图成功")
        if(showflage==True):
            cv2.imshow("image",image)
            print("显示当前图像")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print("关闭当前显示")
        else:
            print("图像不予显示")
    except cv2.error:
        print("读图失败")
    return image


# 实现定位
"""
定位问题还需要考虑的是角度的问题
第一步骤暂时实现的是正面角度的定位
此步骤包含图像的处理
"""
def imagelocation(image):
    print("定位操作")
    """
    形态学操作
    """
    print("灰度处理")
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("gray_image",gray_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print("图像降噪：高斯滤波")
    gb_image = cv2.GaussianBlur(gray_image,(5,5),0)
    # cv2.imshow("gb_image",gb_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # print("形态学处理：开操作")
    #先进行腐蚀再进行膨胀
    op_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    eroded_image = cv2.erode(gb_image,op_kernel)
    cv2.imshow("eroded_image",eroded_image)
    op_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dilated_image = cv2.dilate(eroded_image,op_kernel)
    cv2.imshow("dilated_image", dilated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()






if __name__=="__main__":
    lp_image = readimage('licenseplate.jpg',imageflag=cv2.IMREAD_COLOR,showflage=False)
    imagelocation(lp_image)