def Get_search_results_bing(query):
    test_url = "http://www.bing.com/search?q=%s" % (urllib.parse.quote_plus(query))
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    chromedriver = "chromedriver.exe"
    browser = webdriver.Chrome(chromedriver, options=option)
    browser.get(test_url)
    temp_list = []
    i = 1
    for j in range(1,6):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        results = soup.findAll('li', { "class" : "b_algo" })


        for result in results:
            temp_dict = {}
            intermediate_result = result.find('h2')
            temp_dict["position"] = str(i)
            try:
                temp_dict["url"] = intermediate_result.find('a')['href']
            except Exception as E:
                temp_dict["url"] = ''

            try:
                temp_dict["title"] = intermediate_result.get_text()
            except Exception as E:
                temp_dict["title"] = ''

            try:
                temp_dict["snippet"] = result.find('p').get_text()
            except Exception as E:
                temp_dict["snippet"] = ''

            temp_list.append(temp_dict)
            #print(intermediate_result.get_text())
            #print(intermediate_result.find('a')['href'])

            #print(result.find('p').get_text())
            #print("*"*20)
            i = i+1
        browser.find_element_by_link_text(str(j+1)).click()
    browser.close()
    print(len(temp_list))
    return temp_list
