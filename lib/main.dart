import 'package:flutter/material.dart';
import 'package:flutter_application_1/Views/home.dart';
import 'package:flutter_application_1/views/Login.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'CupConnect',
      theme: ThemeData(
        primarySwatch: Colors.deepOrange,
        primaryColor: Color.fromARGB(255, 202, 96, 96),
        textTheme: const TextTheme(
          bodyMedium: TextStyle(color: Colors.white),
       ),
      ),
      
      home: const SignInPage(),

    );
  }
}
