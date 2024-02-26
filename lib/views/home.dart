import 'package:flutter/material.dart';
import 'package:flutter_application_1/Views/Widgets/stadium_card.dart';
import 'package:flutter_application_1/models/studium.api.dart';
import 'package:flutter_application_1/models/studium.dart';
import 'package:flutter_application_1/views/stadium_detail.dart';

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {

  late List<Studium> _studiums;
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    getStudiums();
  }

  Future<void> getStudiums() async {
    _studiums = await Studiumapi.getStudium();
    setState(() {
      _isLoading = false;
    });
    print(_studiums);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(Icons.sports_soccer),
              SizedBox(width: 10),
              Text('Studiums'),
            ],
          ),
          shadowColor: Colors.black,
        ),
        body: _isLoading
        ? Center(child: CircularProgressIndicator())
        :ListView.builder(
                itemCount: _studiums.length,
                itemBuilder: (context, index) {
                  return GestureDetector(
                onTap: () {
                  Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => StudiumDetails(studium: _studiums[index]),
                            ),
                        );
                       },
                  child: StadiumCard(
                      title: _studiums[index].name, //to fix later : _studiums[index].name
                      location: _studiums[index].country + ", " + _studiums[index].city,//to fix later _studiums[index].country
                      thumbnailUrl: _studiums[index].picture.main,//to fix later _studiums[index].picture.toString()
                      ),
                      );
                },
              ));
  }
}
