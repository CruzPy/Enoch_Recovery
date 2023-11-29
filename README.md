# Enoch_Recovery Features:

## This webapp is to provide information to clients looking to enroll in Enoch Recovery DDP program. Here they can find business and contact information. There is an orientation form which users can use to submit information to request an appointment, it is connected to Gmail API which triggers an email sent to the client confirming appointment information.

## To run this locally:
```
// Clone repo in working directory and open terminal
pipenv shell
pipenv install // Install dependencies

// Per settings.py, locally configure MySQL DB (enochrecovery), and user (etorres) with pass (admin)
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Enoch Recovery DDP Website Features:
1. Stylish webpage consisting of appealing & modern visuals
- Dynamic interaction and styles bringing the website to life
- ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/f2cd5ba6-a4b3-47e8-a281-4b059440cda9)

2. Created new Gmail account (EnochRecoveryDDP@gmail.com) for Google/YouTube business
- ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/1b98aba1-b8db-40c1-b86e-1a508ba2e0f7)

3. Interactive About Page expresses engaging mission with clear call to action
- Simple and incentivizing for client to submit orientation form
 ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/91f79769-8e40-46c7-a681-3832674157ed)

4. Produced state of the art testimonial video
- Smooth Transitions + Blurring + Captioning + Background Music
 ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/49fd055c-2573-4723-ae33-5efa533489d1)

5. Blurred photos to conserve private identities while promoting business 
- Identities have been blurred in the interest of maintaining personal integrity
 ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/c32d53e2-8fd2-4014-aadf-db23a9d7832d)

6. Orientation form allows client to submit appointment request
- Strategically tab input form that encourages client submission
- ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/d24464bb-1e43-4fab-a236-acaa841f4b93)


7. Developed privacy policy as a means of litigation protection
- Clear statement showing client what their data will be used for
- ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/66782c23-c1d2-4c4d-8219-b8e8eb6222fb)

8. Elegant client form confirmation page with automated orientation 
- Interactable confirmation page stylishly displaying key appointment info
- ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/db2a00b3-08a5-42ec-9add-b4d825b5b6ff)

9. Customized database securely stores client information (Not in use, data is not saved - client's request)
- Database safely stores client name, phone #, email & appointment details
- Providing easy to use platform to modify records
- ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/a034b7e9-098e-4737-8eff-c1590d9f2d6a)

10. Two seamless ways to interact with client data (read, create, update, delete) (Not in use, data is not saved - client's request)
- Admin portal: /admin --> Easy to use extension to manage site
- ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/4acda341-130f-474e-8621-5efaf58f0a58)

-	Admin portal can be used to view, update, or delete orientation appointments (Not in use, data is not saved - client's request)
-	![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/43dcbf47-9c99-4ac6-9501-93cb93fe39f1)

- API: /api/orientation --> Method of enhancing the website for future development 
- ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/693ddf6b-94d2-486a-ae2a-7970bab21009)

11. Automated Email notification system
- Client contact info is sent to Enoch’s business email address
- ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/14ff69aa-4de7-4f3d-a294-e7836c8655eb)

- Separate email notification to client confirming appointment details
- ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/44f54bc9-90d7-43a1-87c1-94c36ad8124e)

12. ‘Save to Google Calendar’ button transports the orientation details for an easy reminder for clients
- ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/9adfa488-2459-4bfc-b71e-3c12c45d6579)

13. Mobile Support
- ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/518eac85-c320-46c7-84a0-6ef25673b93d)
- ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/114ceff4-7629-4689-a4c6-4f384b199f03)

14. Error checks & validation 
- Can only choose valid name, telephone, email & orientation hours on the form
- ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/1da6aabb-0bf9-41aa-b982-68591bb18c32)

- Cannot use the same email address or phone # to sign up for a free orientation
- ![image](https://github.com/CruzPy/Enoch_Recovery/assets/18451622/4a49069b-12fe-4792-9e5b-a932c084a8b3)

