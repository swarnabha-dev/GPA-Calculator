
# GPA Calculator

![Streamlit](https://img.shields.io/badge/Streamlit-0E1117?style=for-the-badge&logo=streamlit&logoColor=white)

This is a simple web application built with Streamlit to calculate GPA (Grade Point Average) based on user input of grades and course credits.

## Features
 - [ ] Input the number of courses.
 - [ ] Input the credits and grades for each course.
 - [ ] Calculate and display the GPA
## Setup

**To run this app locally, follow these steps:**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourgithubusername/gpa-calculator.git
   cd gpa-calculator
2. **Create and activate a virtual environment:**

   -  **Create venv using vscode**: [Deatils here](https://code.visualstudio.com/docs/python/environments)
   -  **Setting Up a Virtual Environment with Virtualenv:**
   -  **Prerequisites:**
        - Python installed on your system
       - `pip` (Python package installer) installed

    - **Instructions**

	    1. First, install `virtualenv`  using `pip`:
           ```bash
           pip install virtualenv
	    2. Create a Virtual Environment:*
            Navigate to your project directory and run:
             ```bash
             virtualenv venv
	    3. Activate the Virtual Environment:
            - In Command Prompt:
              ```bash 
              venv\Scripts\activate
			- In PowerShell:
                ```bash
                .\venv\Scripts\Activate.ps1
  		   - In linux activate with:
              ```bash
              source venv/bin/activate
	  4. Deactivate the Virtual Environment:
       ```bash
       deactivate    
 3. **Install the required dependencies:**
    
    ```bash
    pip install -r requirements.txt
4. **Run the Streamlit app:**
	```bash
	streamlit run app.py


## Usage

    1. Open your web browser and navigate to `http://localhost:8501`
    2. Enter the number of courses.
    3. For each course, enter the credits and select the grade.
    4. Click the "Calculate GPA" button to see your GPA.
## Custom CSS
The app uses a custom CSS file to style the background, buttons, and footer.
