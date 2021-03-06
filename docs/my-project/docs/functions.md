# Here is a list of all the functions available to be used in our app:

Documentation for: 

    studyapp/
        routes.py

* `splash():`

	User is shown the splash page for the web app.

* `log():`

	User will be redirected to this webpage only if the user is logged into their account.

* `logout():`

	User is redirected to homepage after logging out of account.

* `login():`

	User is able to log into their account after signing up using a username and password.
	
                Parameters:
                        Username and Password
                Returns:
                        Account for user

* `signup():`

	User enters a username and password and is able to create and accountthat will be used to log in.
                
                Parameters:
                        Username and password used to create account
                Return:
                        An account username and password to use when logging in.


* `markdown_to_flashcard():` 

    Converts markdown files to flash cards.

            Parameters:
                    file (md): A markdown file

            Returns:
                    file (html): The HTML version of the markdown file.

* `flashcard_to_pdf():`

    Converts markdown files to flash cards.

            Parameters:
                    file (html): A flashcard (html file)

            Returns:
                    file (pdf): The PDF version of the flashcard (html file).

* `md_to_pdf():`

    
    Converts markdown files to PDF's.

            Parameters:
                    file (md): A markdown file

            Returns:
                    file (PDF): The PDF version of the markdown file.
    
* `render_md():`

    Converts markdown files to flash cards.

            Parameters:
                    file (md): A markdown file

            Returns:
                    file (html): Outputs the markdown file as HTML.


* `timeTracker()`

    creates a timer for the user

* `allowed_files(filename)`

    Checks if the file uploaded is of supported format..

            Parameters:
                    filename: naem of the to check

            Returns:
                    boolean: True if the file is allowed, else false.

* `searchTextForm()`

    Emboldens a specified text on an input file.

            Parameters:
                    file (pdf,txt,md): A text file of allowed extension.

            Returns:
                    file (html): outputs the text of the file in html and emboldens the searched text.

* `createflashcard():`

    Creates a flashcard and adds it to our DB

            Parameters:
                    file (md): MD File to be converted to flash card and added to our DB

            Returns:
                    text (html): Outputs a success message if the flashcard was added successfully.

* `pomodoro_timer():`

    Checks if the file uploaded is of supported format..
            Parameters:
                    filename: name of the to check

            Returns:
                    boolean: True if the file is allowed, else false.
* `change_file():`
	User is able to change name of a file by entering current file name and new name of file.

	Parameters:
		exisiting file name and new file name
	Returns:
		file with updated name 
