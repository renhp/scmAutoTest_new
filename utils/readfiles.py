# 读取测试数据文件类
from utils.configs import Configs
from aifc import Error
import os
from xlrd import open_workbook


# 读取Excel表格文件测试数据【注意表中的数字需要处理，不然获得数字字符时会有小数点】
class ExcelReader():
    """
        读取excel文件中的内容。返回list。
        如：
        excel中内容为：
        | A  | B  | C  |
        | A1 | B1 | C1 |
        | A2 | B2 | C2 |
        如果 print(ExcelReader(excel, title_line=True).data)，输出结果：
        [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]
        如果 print(ExcelReader(excel, title_line=False).data)，输出结果：
        [[A,B,C], [A1,B1,C1], [A2,B2,C2]]
        可以指定sheet，通过index或者name：
        ExcelReader(excel, sheet=2)
        ExcelReader(excel, sheet='BaiDuTest')
        """

    def __init__(self, in_test_data_catalog, sheet=0, title_line=True):
        # 初始化测试用例数据根目录，精确到每个环境的根目录
        conf = Configs()
        self.file_path = conf.getDataPath()
        excel_path = self.file_path + '\\' + in_test_data_catalog
        if os.path.exists(excel_path):
            self.excel = excel_path
        else:
            raise FileNotFoundError('文件不存在！')
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    # 获取测试数据
    @property
    def getTestData(self):      # 此方法调用时不能带括号
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int, str]:
                raise Error('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                title = s.row_values(0)  # 首行为title
                for col in range(1, s.nrows):
                    # 依次遍历其余行，与首行组成dict，拼到self._data中
                    self._data.append(dict(zip(title, s.row_values(col))))
            else:
                for col in range(0, s.nrows):
                    # 遍历所有行，拼到self._data中
                    self._data.append(s.row_values(col))
        return self._data



if __name__=='__main__':
    # 读取库存查询数据
    er = ExcelReader(r'\scm_stockmanage\stocksee_data.xlsx')
    ds = er.getTestData
    print('====', ds)
    for y in ds:
        print(y.get('ChangKu'), y.get('KuWei'), y.get('goods'), y.get('brand'), y.get('category'),
              y.get('goodscode'))

    # 读取效期规则数据
    er = ExcelReader(r'\scm_stockmanage\expiryrule_data.xlsx')
    ds = er.getTestData
    print('====', ds)
    for y in ds:
        print(y.get('ChangKu'), y.get('goods'), y.get('DueYellow'),
              y.get('DueRed'), y.get('AssertValue'))

    # 读取效期预警数据
    er = ExcelReader(r'\scm_stockmanage\expirwarn_data.xlsx')
    ds = er.getTestData
    print('====', ds)
    for y in ds:
        print(y.get('ChangKu'), y.get('goods'), y.get('shopName'),
              y.get('colour'))

    # 读取下架规则_类目数据
    er = ExcelReader(r'\scm_stockmanage\categoryrule_data.xlsx')
    ds = er.getTestData
    print('====', ds)
    for y in ds:
        print(y.get('category'), y.get('ChangKuCode'), y.get('Rule'))
