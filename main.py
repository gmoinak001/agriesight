from selenium import  webdriver

# if using chrome
#driver = webdriver.Chrome('./chromedriver')

# uncomment if using Firefox
driver = webdriver.PhantomJS(executable_path= './phantomjs')
driver.set_window_size(1024, 768)

#Tomorrow's Forecast
def daily():
    city = str(input("Enter the name of the city you want the weather forecast for: ")).replace(" ","-")

    try:
        driver.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")
        print("\n")
        print(driver.find_elements_by_class_name("b-forecast__table-days-name")[1].text + " the " + driver.find_elements_by_class_name("b-forecast__table-days-date")[1].text + "'s High Temperature" + " in degree Celsius")
        tmrw = (driver.find_elements_by_class_name("temp-color1")[2].text)
        print(tmrw)
    except:
            print("Something went wrong or Data not available")



#Weekly sorting of weather data
def weekly():
    city = str(input("Enter the name of the city you want the weather forecast for: ")).replace(" ","-")

    try:
        driver.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")
        print("\n")
        print(driver.find_elements_by_class_name("b-forecast__table-days-name")[0].text + " the " + driver.find_elements_by_class_name("b-forecast__table-days-date")[0].text + "'s High Temperature" + " in degree Celsius")
        dOne = int(driver.find_elements_by_class_name("temp-color1")[0].text)
        print(dOne);
        print("\n")
        print(driver.find_elements_by_class_name("b-forecast__table-days-name")[1].text + " the " + driver.find_elements_by_class_name("b-forecast__table-days-date")[1].text + "'s High Temperature" + " in degree Celsius")
        dTwo = int(driver.find_elements_by_class_name("temp-color1")[2].text)
        print(dTwo)
        print("\n")
        print(driver.find_elements_by_class_name("b-forecast__table-days-name")[2].text + " the " + driver.find_elements_by_class_name("b-forecast__table-days-date")[2].text + "'s High Temperature" + " in degree Celsius")
        dThree = int(driver.find_elements_by_class_name("temp-color1")[5].text)
        print(dThree)
        print("\n")
        print(driver.find_elements_by_class_name("b-forecast__table-days-name")[3].text + " the " + driver.find_elements_by_class_name("b-forecast__table-days-date")[3].text + "'s High Temperature" + " in degree Celsius")
        dFour = int(driver.find_elements_by_class_name("temp-color1")[7].text)
        print(dFour)
        print("\n")
        print(driver.find_elements_by_class_name("b-forecast__table-days-name")[4].text + " the " + driver.find_elements_by_class_name("b-forecast__table-days-date")[4].text + "'s High Temperature" + " in degree Celsius")
        dFive = int(driver.find_elements_by_class_name("temp-color1")[9].text)
        print(dFive)
        print("\n")
        print(driver.find_elements_by_class_name("b-forecast__table-days-name")[5].text + " the " + driver.find_elements_by_class_name("b-forecast__table-days-date")[5].text + "'s High Temperature" + " in degree Celsius")
        dSix = int(driver.find_elements_by_class_name("temp-color1")[11].text)
        print(dSix)
        print("\n")
        print(driver.find_elements_by_class_name("b-forecast__table-days-name")[6].text + " the " + driver.find_elements_by_class_name("b-forecast__table-days-date")[6].text + "'s High Temperature" + " in degree Celsius")
        dSeven = int(driver.find_elements_by_class_name("temp-color1")[13].text)
        print(dSeven)
        print("\n")
        print(driver.find_elements_by_class_name("b-forecast__table-days-name")[7].text + " the " + driver.find_elements_by_class_name("b-forecast__table-days-date")[7].text + "'s High Temperature" + " in degree Celsius")
        dEight = int(driver.find_elements_by_class_name("temp-color1")[15].text)
        print(dEight)
        print("\n")

        # Python program to get average of a list
        def Average(lst):
                return sum(lst) / len(lst)

        # Driver Code
        lst = [dTwo, dThree, dFour, dFive, dSix, dSeven, dEight]
        average = Average(lst)

        # Printing average of the list
        print("Average of the list =", round(average, 2))

        
        
    except:
        print("Something went wrong or Data not available")


weekly()
daily()
