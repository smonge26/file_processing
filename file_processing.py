#application that performs file processing
import os #import the OS library
# function to create , write and read the file
def createFile():
	fileName = input('enter the name of your new file including .txt: ') # name of the file to be created 
	newFile = open(fileName,'w')                         # open the file created to write in it
	name = input('Please enter your name: ')             # user input name
	address = input('Please enter your address:')        # user input adress
	phoneNum = input('Please enter your phone number:')  # user input phone number
	newLine = (name)+', '+(address)+', '+(phoneNum)      # passing the user inputs to a single line  
	newFile.write(newLine)      # writing the new line in the created file
	newFile.close()   # closing the file
	fileRead = open(fileName) # opening the file to read it's content 
	print('The content of your file is')
	print(fileRead.read()) # displaying the content of the file 

# function to allow the user to change directories
def changeDir():
	newDirectory = input('Enter new directory:') # user input for new directory
	if os.path.exists(newDirectory): # if the directory exists 
		os.chdir(newDirectory)       # it will chage directories
		createFile()
	else:
		os.mkdir(newDirectory) # creating a new directory if it does not exists 
		os.chdir(newDirectory) # changing to the new directory
		createFile()
	
# function to use the current directory
def sameDirecorty():
	createFile()

filePath = os.getcwd() # get current directory
print('File Processing Program\n')
print('This is your courrently file directory', (filePath)) # display the current directory to the user
whichDirectoriy = input('Would you like to change directory yes or no :')
if whichDirectoriy == ('yes'):  # user seclection to use the current directory or change it
	changeDir()
	
else:
	sameDirecorty()
