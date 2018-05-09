from appium import webdriver

# 初始化信息
desired_caps = {}
desired_caps["platformName"] = "Android"        # 设备系统
desired_caps["platformVersion"] = "7.0"         # 设备系统版本
desired_caps["deviceName"] = "MI5"              # 设备名称
desired_caps["appPackage"] = "com.jingdong.app.mall"            # 包名
desired_caps["appActivity"] = "com.jingdong.app.mall.MainFrameActivity"       # ActivityName
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)   # 启动app

# 安装应用到设备中去。需要apk包的路径。
driver.install_app("path/to/my.apk")
driver.install_app("D:\\android\\apk\\ContactManager.apk")

# 从设备中删除/卸载一个应用:需要传参应用包的名字.
driver.remove_app("com.example.android.apis")

# 关闭应用:默认关闭当前打开的应用，所以不需要入参。这个方法并非真正的关闭应用，相当于按home键将应用置于后台.
driver.close_app()

# 启动应用:重新启动应用也是一个测试点，该方法需要配合close_app()使用的.
driver.launch_app()

# 启动activity:
driver.start_activity("包名", "activity名")

# 截屏:
driver.get_screenshot_as_file("test.png")

# 获取上下文:
cont = driver.contexts
ct = driver.context

# 切换当前的上下文:混合APP中，切换到web、原生上下文，传入上下文的名字即可
driver.switch_to.context('WEBVIEW_0')

# 检查应用是否安装:需要传参应用包的名字,返回结果为Ture或False
driver.is_app_installed('com.example.android.apis')

# 将应用置于后台:将当前活跃的应用程序发送到后台。这个方法需要入参，需要指定应用置于后台的时长。
# driver.run_app_in_background(2)

# 刷新当前页面
driver.refresh()

# 在设备上重新设置当前的应用程序:重置当前被测程序到出始化状态
driver.reset()

# 获取当前所有的可用的上下文。该方法不需要入参。
#

# 返回一组字典，对应于当前会话中可见的cookie
driver.get_cookies()
# 如果传入的名字能匹配到cookie，则返回这个cookie
driver.get_cookie("name")

# 当前所有上下文句柄
#

# 跳转窗口
driver.switch_to_window("window_name")
# 跳转入frame
driver.switch_to_frame("frame_reference")

#
driver.press_keycode('keycode:整形数字', 'metastate')     # 字母“a”

# 滚动:由原元素滚动到目标元素
driver.scroll('els[10]:原元素', 'els[0]:目标元素')

# 拖拽:将原元素拖拽到目标元素
driver.drag_and_drop('els[10]:原元素', 'els[0]:目标元素')

# 滑动:传入x1, y1, x2, y2       (若能用上面两个方法最好不用此法)
driver.swipe(100, 750, 100, 100)

# 点击:某个位置（列表中可有多个元组，代表多点触控）
driver.tap([(100, 750), (102, 100)])

# 快速滑动:特点快速
driver.flick(100, 750, 100, 100)

# 获取Activity名字:为类的属性值
ac = driver.current_activity

# 将APP置于后台:传入时间
driver.background_app(3)

# 等待指定activity显示:wait_activity("等待某个活动(页面)"，等待时间，多久检查一次页面是否显示了；
# 返回True或False
driver.wait_activity(".CustomLocaleActivity", 3, 1)

# 获取元素的某些东西
e = driver.find_element_by_xpath("aa")
e.get_property("name")
e.get_attribute("name")


""" 操作Js:
    执行js一般有两种场景：
        一种是在页面上直接执行JS
        另一种是在某个已经定位的元素上执行JS
    js解释:
        q = document.getElementById(\"user_name\")
            元素q的id 为user_name
        q.style.border=\"1px solid red\
            元素q的样式，边框为1个像素红色
"""
# 操作js
# 给用户名的输入框标红
js = "var q=document.getElementById(\"user_name\");q.style.border=\"1px solid red\";"
# 调用js
driver.execute_script(js)



