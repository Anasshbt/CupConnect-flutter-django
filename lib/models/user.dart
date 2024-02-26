class User{
  int? id;
  String? username,email,password,gender, phone, country, token;

  User({
    this.id,
    this.username,
    this.email,
    this.password,
    this.gender,
    this.phone,
    this.country
  });


  factory User.fromJson(json) {
    return User(
      id: json["id"] as int,
      username: json["username"]as String,
      email: json["email"]as String,
      password: json["password"]as String,
      gender: json["gender"]as String,
      phone: json["phone"]as String,
      country: json["country"]as String,
    );
  }
}
