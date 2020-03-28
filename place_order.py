
def place_order(driver, target_date, card_number, card_exp, card_cvc):
    for j in range(1,10):
        try:
            date = driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/ul/li[{j}]')
            my_date = date.text.split('\n')[1]
        except:
            continue

        if my_date != target_date:
            continue
        
        try:
            date.click()
            time.sleep(2)
        except:
            pass

        try:
            option = driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[{j}]/div/div/label/div/div[1]')
        except:
            continue

        ### select delivery time option (click)
        print(f'\n\nPlace order for target date: {target_date}')
        try:
            driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[{j}]/div/div/label/input').click()
            time.sleep(2)
        except:
            print(f'Order for target date failed: {target_date}')
            continue

        ### drop down for instruction
        try:
            driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div/button').click()
        except:
            pass

        ### delivery instructions (text)
        ### leave at my door (click)
        try:
            driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div/div[2]/form/textarea').clear()
            driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div/div[2]/form/textarea').send_keys('None')
            if not driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div/div[2]/form/div[1]/div/input').is_selected():
                driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div/div[2]/form/div[1]/div/input').click()
            time.sleep(2)
        except:
            pass

        ### continue button (click)
        try:
            driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div/div[2]/form/div[2]/button').click()
            time.sleep(2)
        except:
            print(f'Failed to click on continue button 1')
            continue

        ### mobile number (text)
        try:
            driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[4]/div/div/div/button').click()
        except:
            pass
        try:
            driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[4]/div/div/div/div[2]/form/div[1]/div[1]/input').clear()
            driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[4]/div/div/div/div[2]/form/div[1]/div[1]/input').send_keys('8088888888')
            time.sleep(2)
        except:
            print(f'Failed to fill in mobile number')
            continue
    
        ### save button (click)
        try:
            driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[4]/div/div/div/div[2]/form/div[2]/button').click()
            time.sleep(2)
        except:
            print(f'Failed to click on save button 1')
            continue

        ### first name (text)
        ### last name (text)
        try:
            driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[5]/div/div/div/button').click()
        except:
            pass
        try:
            while driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[5]/div/div/div/div[2]/form/div[1]/div[1]/input').get_attribute('value'):
                driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[5]/div/div/div/div[2]/form/div[1]/div[1]/input').send_keys(Keys.BACKSPACE)
            driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[5]/div/div/div/div[2]/form/div[1]/div[1]/input').send_keys('Loyal')
            while driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[5]/div/div/div/div[2]/form/div[2]/div[1]/input').get_attribute('value'):
                driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[5]/div/div/div/div[2]/form/div[2]/div[1]/input').send_keys(Keys.BACKSPACE)
            driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[5]/div/div/div/div[2]/form/div[2]/div[1]/input').send_keys('Customer')
            time.sleep(2)
        except:
            print(f'Failed to fill in names')
            continue

        ### save button (click)
        try:
            driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[5]/div/div/div/div[2]/form/div[3]/button').click()
            time.sleep(2)
        except:
            print(f'Failed to click on save button 2')
            continue

        ### payment drop down (click)
        try:
            driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[6]/div/div/div/button').click()
            time.sleep(2)
        except:
            pass

        ### choose payment method button (click)
        try:
            driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[6]/div/div/div/div[2]/div/div/fieldset/div/button').click()
            time.sleep(2)
        except:
            print(f'Failed to click on choose payment method button')
            continue

        # place order buttion (click)
        try:
            place_button = driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div/button')
            place_button.click()
            print(f'Order placed, please log into instacart for review ...')
            return driver
        except:
            continue
    
    return driver
