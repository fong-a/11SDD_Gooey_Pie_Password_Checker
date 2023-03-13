import gooeypie as gp
import pyhibp
from pyhibp import pwnedpasswords as pw
pyhibp.set_user_agent(ua="Awesome application/0.0.1 (An awesome description)")

# main container
app = gp.GooeyPieApp('Password Utility')
app.width  = 400
app.height = 500
app.set_grid(12,3)

# business logic 
def search_blacklisted_passwords(file_path, word):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            return True
        else:
            return False

def generate_password_rating(event):
    if len(password_check_inp.text) == 0:
        password_review_lbl_title.grid_remove()
        password_review_lbl_one.grid_remove()
        password_review_lbl_two.grid_remove()
        password_review_lbl_three.grid_remove()
        password_review_lbl_four.grid_remove()
        password_review_lbl_five.grid_remove()
        password_rating_lbl.grid_remove()
        password_review_lbl_title.grid()
        password_review_lbl_title.text = "Please enter a password."
    else:
    # unhide the relevant widgets
            password_review_lbl_title.grid_remove()
            password_review_lbl_one.grid_remove()
            password_review_lbl_two.grid_remove()
            password_review_lbl_three.grid_remove()
            password_review_lbl_four.grid_remove()
            password_review_lbl_five.grid_remove()
            password_rating_lbl.grid_remove()
            password_review_lbl_title.text = "Your password review:"
            password_review_lbl_title.grid()
            password_review_lbl_one.grid()
            password_review_lbl_two.grid()
            password_review_lbl_three.grid()
            password_review_lbl_four.grid()
            password_review_lbl_five.grid()
            password_rating_lbl.grid()
        
            # rating score system
            rating = 5
            rating_flags = [0,0,0,0,0] 
            
            # check length of password >= 8
            if len(password_check_inp.text) < 8:
                rating -= 3
                rating_flags[0] = 1

            # check if password contains letters and numbers
            number_detected = False
            for character in password_check_inp.text:
                if character.isdigit() == True:
                    number_detected = True
            for character in password_check_inp.text:
                if character.isalpha() == True:
                    char_detected = True
            if number_detected == False or char_detected == False:
                rating_flags[1] = 1
                rating -= 2

             # check if passwords continas special symbols
            special_characters = "!@#$%^&*()-+?_=,<>/"
            special_character_detected = False
            for character in password_check_inp.text:
                if character in special_characters:
                    special_character_detected = True
            if special_character_detected == False:
                rating_flags[2] = 1
                rating -= 1

            # check if password has been blacklisted
            blacklist_check = search_blacklisted_passwords("common_passwords.txt", password_check_inp.text)
            if blacklist_check == True:
                rating_flags[3] = 1
                rating -= 5

            password_check_string = password_check_inp.text
            # check if your password has been leaked online
            # Check a password to see if it has been disclosed in a public breach corpus
            resp = pw.is_password_breached(password_check_string)
            print(resp)
            if resp >0:
                rating_flags[4] = 1
                rating -=5

            
                

            # update the review area
            if rating_flags[0] == 1:
                password_review_lbl_one.text = "Password Length > 8 characters: ❌"
            else:
                password_review_lbl_one.text = "Password Length > 8 characters: ✅"

            if rating_flags[1] == 1:
                password_review_lbl_two.text = "Contains Letters and Numbers: ❌"
            else:
                password_review_lbl_two.text = "Contains Letters and Numbers: ✅"

            if rating_flags[2] == 1:
                password_review_lbl_three.text = "Contains Special Characters: ❌"
            else:
                password_review_lbl_three.text = "Contains Special Characters: ✅"

            if rating_flags[3] == 1:
                password_review_lbl_four.text = "Password is commonly used: ❌"
            else:
                password_review_lbl_four.text = "Password is not commonly used: ✅"                

            if rating_flags[4] == 1:
                password_review_lbl_five.text = "Password has been leaked "+str(resp)+ " ≠times: ❌"
            else:
                password_review_lbl_five.text = "Password has not been leaked: ✅"      

            # update the first label to display the password rating
            # if password is less than or equal to 2, then alert user
            if rating <= 2:
                password_rating_lbl.text = "⚠️"
            else:
                password_rating_lbl.text = "Your password score is: " + ("⭐" * rating)


# widgets
splash_img = gp.Image(app,'images/password_utility_splash_image_medium.png')
password_check_lbl = gp.Label(app, "Enter your password:")
password_check_inp = gp.Secret(app)
password_rating_lbl = gp.Label(app, "Password Rating: ")
password_check_btn = gp.Button(app,'Check Password',generate_password_rating)
password_review_lbl_title = gp.Label(app, "Your password review: ")
password_review_lbl_one = gp.Label(app, "Password Length > 8 characters: ")
password_review_lbl_two = gp.Label(app, "Contains number(s): ")
password_review_lbl_three = gp.Label(app, "Contains special symbol(s): ")
password_review_lbl_four = gp.Label(app, "Isn't a blacklisted word: ")
password_review_lbl_five = gp.Label(app, "Hasn't been breached: ")

# widget positioning
app.add(splash_img, 2, 1, align = 'center')
app.add(password_check_lbl, 3, 1, align ='center')
app.add(password_check_inp, 4, 1, align = 'center')
app.add(password_check_btn, 5, 1, align = 'center')
app.add(password_review_lbl_title, 6, 1, align ='left')
app.add(password_review_lbl_one, 7, 1, align = 'left')
app.add(password_review_lbl_two, 8, 1, align = 'left')
app.add(password_review_lbl_three, 9, 1, align = 'left')
app.add(password_review_lbl_four, 10, 1, align = 'left')
app.add(password_review_lbl_five, 11, 1, align = 'left')
app.add(password_rating_lbl, 12,1, align='left')
password_review_lbl_title.grid_remove()
password_review_lbl_one.grid_remove()
password_review_lbl_two.grid_remove()
password_review_lbl_three.grid_remove()
password_review_lbl_four.grid_remove()
password_review_lbl_five.grid_remove()
password_rating_lbl.grid_remove()

# column span
splash_img.grid(columnspan=3)
password_check_lbl.grid(columnspan=3)
password_check_inp.grid(columnspan=3)
password_check_btn.grid(columnspan=3)


# run application
app.run()

