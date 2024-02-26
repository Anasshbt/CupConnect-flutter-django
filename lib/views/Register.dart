import 'package:flutter/material.dart';
import 'package:flutter_application_1/views/Login.dart';
import 'package:flutter_application_1/views/Widgets/fields.dart';
import 'package:flutter_application_1/views/Widgets/texxt_button.dart';
import 'package:flutter_application_1/views/theme.dart';


class SignUpPage extends StatelessWidget {
  const SignUpPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: bgColor,
      body: ListView(
        padding: EdgeInsets.symmetric(
          horizontal: defaultMargin,
        ),
        children: [
          Container(
            margin: EdgeInsets.only(top: 100),
            child: Text(
              "Welcome to CupConnect!\n SignUp ",
              style: whiteTextStyle.copyWith(
                fontSize: 20,
                fontWeight: semiBold,
              ),
              textAlign: TextAlign.center,
            ),
          ),
          SizedBox(
            height: 5,
          ),
          CustomField(
            iconUrl: '',
            hint: 'username',
          ),
          CustomField(
            iconUrl: '',
            hint: 'Email',
          ),
            CustomField(
            iconUrl: '',
            hint: 'Phone',
          ),
           CustomField(
            iconUrl: '',
            hint: 'Gender',
          ),
          CustomField(
            iconUrl: '',
            hint: 'Password',
          ),
          CustomField(
            iconUrl: '',
            hint: 'virify Password',
          ),
          CustomTextButton(
            title: 'Register',
            margin: EdgeInsets.only(top: 50),
          ),
          Container(
            margin: EdgeInsets.only(
              top: 40,
              bottom: 74,
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                TextButton(
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => SignInPage()),
                    );
                  },
                  child: Text(
                    "Already have an Account ? try Signin",
                    style: whiteTextStyle.copyWith(
                      fontSize: 16,
                      fontWeight: semiBold,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
