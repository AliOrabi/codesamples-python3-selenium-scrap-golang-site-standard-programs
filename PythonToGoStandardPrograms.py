from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
import sys


class seleniumGoSiteParser():
	def __init__(self):		
		self.WebDriver = webdriver.Chrome()
		self.WebDriver.implicitly_wait(10)
		self.WebDriver.get("https://golang.org/")
	def setProgramName(self,standardProgramName):
		self.programName = standardProgramName + ".go"
	def __del__(self):
		self.unlinkDriver()
	def unlinkDriver(self):
		self.WebDriver.quit()
	def goParse(self):
		try:
			#Get Program Selection object
			playgroundSelect = Select(self.WebDriver.find_element_by_class_name("Playground-selectExample"))
			playgroundSelect.select_by_value(self.programName)
			sleep(2)
			#Get open in Playground object
			playgroundPopout = self.WebDriver.find_element_by_class_name("Playground-popout")
			playgroundPopout.click()
			#Get Run Button
			runButton = self.WebDriver.find_element_by_id("run")
			runButton.click()
			outputArea = self.WebDriver.find_element_by_id("output")
			#Wait for GoLang playground to respond
			systemOutput = WebDriverWait(self.WebDriver, 250).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#output > pre > span.system")))
			codeArea = self.WebDriver.find_element_by_id("code")
			returned = {}
			returned["programText"] = codeArea.get_attribute("innerHTML")
			returned["response"] = ""
			if ("Program exited." in systemOutput.get_attribute("innerHTML")):
				stdOutput = WebDriverWait(self.WebDriver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#output > pre > span.stdout')))
				returned["response"] = stdOutput.get_attribute("innerHTML")
			else:
				errorOutput = WebDriverWait(self.WebDriver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#output > pre > span.stderr")))
				returned["response"] = errorOutput.get_attribute("innerHTML")
			return returned
		except Exception as e:
			#formatted string literal(f-string) output for Python 3.6+: https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
			raise
			print(f"Selenium Web Driver Instance Error: {str(e)}")
	def goParseHelp(self):
		try:
			#Get Program Selection object
			playgroundSelect = Select(self.WebDriver.find_element_by_class_name("Playground-selectExample"))
			returned = ""
			for option in playgroundSelect.options:				
				optionName = option.get_attribute("value").replace(".go", "")
				optionDesc = option.text
				returned += optionName + " - " + optionDesc + "\n"
			return returned
		except Exception as e:
			#formatted string literal(f-string) output for Python 3.6+: https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
			print(f"Selenium Web Driver Instance Error: {str(e)}")

def main():
	seleniumGoSiteParserInstance = seleniumGoSiteParser()
	if (len(sys.argv) >= 2):		
		seleniumGoSiteParserInstance.setProgramName(sys.argv[1])
		programResult = seleniumGoSiteParserInstance.goParse()
		if (programResult != None):
			programText = programResult["programText"]
			programResponse = programResult["response"]
			print(f"Program:\n{programText}")
			print(f"Result:\n{programResponse}")
	else:
		helpResult = seleniumGoSiteParserInstance.goParseHelp()
		print("You can choose from the following list of options.")
		print("Please input the option without the .go extension.")
		print("Example: python3 PythonToGoStandardPrograms.py hello")
		print(helpResult)
	del seleniumGoSiteParserInstance
	exit()
if __name__=='__main__': main()


