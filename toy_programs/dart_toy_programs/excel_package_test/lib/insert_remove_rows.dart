import 'dart:io';
import 'package:excel_dart/excel_dart.dart';

void main() {
  var file = "New_Excel_File.xlsx";
  var bytes = File(file).readAsBytesSync();
  var excel = Excel.decodeBytes(bytes);
  Sheet sheetObject = excel['Sheet1'];

  // Insert a new row at index 2
  sheetObject.insertRow(2);
  
  // Remove a row at index 3
  sheetObject.removeRow(3);

  var fileBytes = excel.save();
  File(file).writeAsBytesSync(fileBytes!); // Save the updated file

  print("Rows inserted and removed!");
}
