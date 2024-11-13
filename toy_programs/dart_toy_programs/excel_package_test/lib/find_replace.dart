import 'dart:io';
import 'package:excel_dart/excel_dart.dart';

void main() {
  var file = "New_Excel_File.xlsx";
  var bytes = File(file).readAsBytesSync();
  var excel = Excel.decodeBytes(bytes);
  Sheet sheetObject = excel['Sheet1'];

  // Find and replace "OldValue" with "NewValue"
  int replacedCount = sheetObject.findAndReplace('OldValue', 'NewValue');

  var fileBytes = excel.save();
  File(file).writeAsBytesSync(fileBytes!); // Save the updated file

  print("Replaced $replacedCount occurrences!");
}
