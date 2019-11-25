# Projectssl2k19
Question Bank Application

-> Go to Project/my_project/ and open terminal there

-> Type commands : 
	1> python3 manage.py makemigrations
	2> python3 manage.py migrate
	3> python3 manage.py runserver

-> Open a web browser and type URL: http://127.0.0.1:8000/

##usage
-> New users need to sign up 

-> Login to move to Home of application

-> Click on  Add Question Bank button to create a new empty question bank

-> Click on See Your Question Papers :
	-> Click on Create a Question paper to create new paper :
		-> Give name and duration of paper 
		-> click on question or module name to view it in a new tab
		-> Click on the checkbox to select question and question module for paper
	->	Click on heading row cells of question papers list to sort the table wrt to selected column
	->  Click on name of question paper in the table :
		-> Filter questions using Search
		-> Click on names of question or module name to view it in new tab
		-> Click on Export PDF to generate question paper in the form of a formatted PDF, opened in new tab

-> Click on question bank name in question bank list :
	-> Add file in ini format with question statements and answers (if given) in latex
	-> Add question and question module manually
	-> Delete question bank
	-> Filter questions in bank using search
	-> Click on table cells to view question statement and answer in a new tab   
	-> Click on Edit button to edit corresponding question 
	-> Click on question module name in question modules list to view the complete module in a new tab

-> Links to edit profile, change password and logout below Question Bank list