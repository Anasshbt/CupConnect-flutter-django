class Studium {
  final int id;
  final String name;
  final int capacity;
  final String city;
  final String country;
  final String desc;
  final int cost;
  final Picture picture;
  final String map;

  Studium({
    required this.id,
    required this.name,
    required this.capacity,
    required this.city,
    required this.country,
    required this.desc,
    required this.cost,
    required this.picture,
    required this.map,
  });

factory Studium.fromJson(dynamic json) {
  return Studium(
    id: json['id'] as int,
    name: json['name'] as String,
    capacity: json['capacity'] as int,
    city: json['city'] as String,
    country: json['country'] as String,
    desc: json['desc'] as String,
    cost: json['cost'] as int,
    picture: Picture(
      main: json['picture']['main'] as String,
      s1: json['picture']['s1'] as String,
      s2: json['picture']['s2'] as String,
      s3: json['picture']['s3'] as String,
      s4: json['picture']['s4'] as String,
    ),
    map: json['map'] as String,
  );
}
 static List<Studium> studiumsFromSnapshot(List snapshot) {
    return snapshot.map((data) {
      return Studium.fromJson(data);
    }).toList();
  }

}
class Picture {
  final String main;
  final String s1;
  final String s2;
  final String s3;
  final String s4;

  Picture({
    required this.main,
    required this.s1,
    required this.s2,
    required this.s3,
    required this.s4,
  });
}