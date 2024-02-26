import 'package:flutter/material.dart';
import 'package:flutter_application_1/models/studium.dart';

class StudiumDetails extends StatelessWidget {
  final Studium studium;

  const StudiumDetails({Key? key, required this.studium}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(studium.name),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image.network(
              studium.picture.main,
              width: double.infinity,
              height: 200,
              fit: BoxFit.cover,
            ),
            const SizedBox(height: 16, width: 15,),
            const Text(
              'Description:',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            Text(
              studium.desc,
              style: TextStyle(fontSize: 16, color: Colors.black),
            ),
            Text('Name: ${studium.name}'),
           const Text(
              'Location:',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold,color: Colors.black),
            ),
            Text(
              '${studium.country}, ${studium.city}',
              style: TextStyle(fontSize: 16, color: Colors.black),
            ),
            // Add more details as needed
          ],
        ),
      ),
    );
  }
}
