import 'package:flutter_application_1/models/studium.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class Studiumapi {
  static Future<List<Studium>> getStudium() async {
    var uri = Uri.https('devjam.onrender.com', 'api/stadium/',
        {"limit": "18", "start": "0", "tag": "list.stadium"});

    final response = await http.get(uri);

if (response.statusCode == 200) {
    List<dynamic> data = jsonDecode(response.body);
      List<Studium> studiums = [];

      for (var item in data) {
        Studium studium = Studium.fromJson(item);
        studiums.add(studium);
      }

      return studiums;}
      return [];

  }
}