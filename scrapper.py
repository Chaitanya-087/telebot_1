# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

# options = Options()
# options.add_argument("--headless")

# URL = "https://erp.cbit.org.in/beeserp/login.aspx"

# driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

# def getElement(driver,id):
#   return WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, id))
#         )

# def getAttendance(usr,pwd):
#   att,name = "",""
#   try:
#     driver.get(URL)
#     getElement(driver,"txtUserName").send_keys(usr)
#     getElement(driver,"btnNext").click()
#     getElement(driver,"txtPassword").send_keys(pwd)
#     getElement(driver,"btnSubmit").click()
#     att += getElement(driver,"ctl00_cpStud_lblTotalPercentage").text
#     name += getElement(driver,"ctl00_cpHeader_ucStud_lblStudentName").text[8:]
#     driver.quit()
#     return {"success":True,"message":"{}\n{}".format(name,att)}
#   except Exception as e:
#     print(e)
#     return {"success":False,"message":"error"}

# #testing code
# if __name__ == "__main__":
#   print(getAttendance("160119735087", "160119735087"))