"""【库存管理：页面元素操作方法】"""
import datetime



# 输入内容
def inputContent(self, e, Content):
    e.clear()
    e.send_keys(Content)

# 下拉框选择,针对text:元素值
def dropDownBox_text(self, es, text, second=15):  # 传入仓名
    """es:下拉框元素名称组，text:点击元素值为text的元素"""
    for e in es:            # 遍历仓库名
        if e.text == text:     # 选择所需仓库
            t = 0
            starttime = datetime.datetime.now()
            while t <= second:
                endtime = datetime.datetime.now()
                t = (endtime - starttime).seconds
                try:
                    e.click()
                    break
                except:
                    pass
            if t > second:
                raise NameError('点击元素失败:已经超过设置时间')
            break

# 下拉框选择，针对attribute:属性名
def dropDownBox_attribute(self, es, type_name, type_value, second=15):
    """es:下拉框元素名称组，type_name:元素的属性名，type_value:点击元素属性值为type_value的元素"""
    for e in es:
        if e.get_attribute(type_name) == type_value:
            t = 0
            starttime = datetime.datetime.now()
            while t <= second:
                endtime = datetime.datetime.now()
                t = (endtime - starttime).seconds
                try:
                    e.click()
                    break
                except:
                    pass
            if t > second:
                raise NameError('点击元素失败:已经超过设置时间')
            break

# 单击===“没必要单独建一个方法”










