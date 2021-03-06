from django import forms
from django.core import validators


# Function for Validation
#def start_with_d(value):
    #if value[0].isalpha != True: #for only name should be in alphabet symbols
   # if value[0].lower() != 'd':
        #raise forms.ValidationError('Name should be start with d')

#def gmail_verification(value):
    #if value[len(value)-9:] != 'gmail.com':
        #raise forms.ValidationError('Must be gmail')
#---------------------------------------------------------------------------------------------------------------
class FeedBackForm(forms.Form):
    #name = forms.CharField(validators=[start_with_d])
    name = forms.CharField()
    roll_no = forms.IntegerField()
    #email = forms.EmailField(validators=[gmail_verification])
    email = forms.EmailField()
    password= forms.CharField(widget=forms.PasswordInput)
    rpassword_again = forms.CharField(widget=forms.PasswordInput)
    feedback = forms.CharField(widget=forms.Textarea,
               validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
    bot_handler = forms.CharField(required=False,widget=forms.HiddenInput)
#---------------------------------------------------------------------------------------------------------------

# clean method for total form validations
    def clean(self):
        print("Total form validations")
        cleaned_data = super().clean()

        #For Bot Handler
        bot_handler_value = cleaned_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError('Bot Validation!!!')

        #Password
        inputpassword = cleaned_data['password']
        inputrpassword_again = cleaned_data['rpassword_again']
        if inputpassword != inputrpassword_again:
            raise forms.ValidationError('Password Not Matched.')
        #Name
        inputname=cleaned_data['name']
        if len(inputname) < 10:
            raise forms.ValidationError('Name should compulsory contains minimum 10 characters')
        #ROll No.
        inputroll_no = cleaned_data['roll_no']
        if len(str(inputroll_no)) != 3:
            raise forms.ValidationError('Roll no. should compulsory contains exactly 3 digits')
#---------------------------------------------------------------------------------------------------------

# clean method for single form validations

    #def clean_roll_no(self):
       # input_roll_no=self.cleaned_data['roll_no']
       # print('Validating Rollno.')
       # return input_roll_no

    #def clean_email(self):
    #    input_email=self.cleaned_data['email']
    #    print('Validating Email.')
    #    return input_email

    #def clean_feedback(self):
    #    input_feedback=self.cleaned_data['feedback']
    #    print('Validating Feedback.')
    #    return input_feedback
#---------------------------------------------------------------------------------------------------------------