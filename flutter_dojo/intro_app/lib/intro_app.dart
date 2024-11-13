import 'dart:convert';
import 'package:http/http.dart' as http;

class Package{
  final String name;
  final String latestVersion;
  final String? description;
  final String? publisher;

  Package(
    this.name,
    this.latestVersion,
    this.description,
    this.publisher,
  );

  @override
  String toString(){
    return "Package{name : $name, latestVersion : $latestVersion, description : $description, publisher : $publisher}";
  }
}

void main() async{
  final httpPackageUrl = Uri.https('dart.dev', '/f/packages/http.json');
  final httpPackageResponse = await http.get(httpPackageUrl);
  if(httpPackageResponse.statusCode != 200){
    print("Failed to retrive the http package !");
    return;
  }
  final json = jsonDecode(httpPackageResponse.body) as Map;
  final package = Package(json["name"], json["latestVersion"], json["description"], json["publisher"]);
  print(package);
}