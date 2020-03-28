
def poll_target_dates(driver, target_dates):
    target_dates = target_dates.split(',')
    while True:
        print(f'Current time: {datetime.now().strftime("%m/%d/%Y %H:%M:%S")}')
        cur_dates = []
        driver.get("https://www.instacart.com/store/checkout_v3")
        time.sleep(10)
    
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/button').click()
        except:
            pass
        time.sleep(2)
        
        for i in range(1,10):
            ### find each date listed
            try:
                date = driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/ul/li[{i}]')
                cur_date = date.text.split('\n')[1]
                if cur_date not in target_dates: continue
                print(f'Found {date.text}')
                date.click()
                time.sleep(2)
            
                msg = driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[{i}]/div/div')
                print(f'    msg{i}: {msg.text}')
            except:
                pass
            
            try:
                option = driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[{i}]/div/div/label/div/div[1]')
                print(f'    option: {option.text}\n\n')
                cur_dates.append(cur_date)
            except:
                pass
        
        if cur_dates:
            for t in target_dates[::-1]:
                if t in cur_dates:
                    return driver, t
        
        continue

