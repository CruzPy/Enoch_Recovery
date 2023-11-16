# Enoch_Recovery Features:
```
# Clone repo in working directory and open terminal
pipenv shell
pipenv install dev

# Ensure MySQL DB is correctly configured as well as settings.py 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Features
1. New Gmail (EnochRecoveryDDP@gmail.com) for google/youtube business
- TODO: Before going online: Must submit application to google to approve external functionality

2. Interactive About Page expresses engaging mission with clear call to action
- Simple and incentivizing for client to submit orientation form

3. State of the art testimonial video
- Smooth Transitions + Blurring + Captioning (a lot more!)

4. Blurred photos to conserve private identities while promoting business 
- Identities have been blurred in the interest of maintaining personal integrity

5. Stylish webpage consisting of appealing & modern visuals
- Dynamic interaction and styles bringing the website to life

6. Orientation form allows client to submit appointment request
- Strategically tab input form that encourages client submission

7. Litigation protection allows for transperency when collecting user information
- Clear statement showing client what their data will be used for
- TODO: Could be enhanced with privacy policy

8. Elegant client form confirmation page with automated orientation 
- Interactable confirmation page stylishly displaying key appointment info

9. Customized database securely stores client information 
- Database safely stores client name, phone #, email & appointment details

10.Two seamless ways to interact with client data (read, create, update, delete)
- Admin portal: /admin --> Easy to use extension to manage site
- API: /api/orientation --> Method of enhancing the website for future development

11. Automated Email notification system
- Client orientation info is sent to enoch's business email address 
- Seperate email notification to client confirming appointment details
