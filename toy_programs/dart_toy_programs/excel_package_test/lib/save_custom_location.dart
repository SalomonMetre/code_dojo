import 'package:excel_dart/excel_dart.dart';
import 'dart:io';
import 'package:path/path.dart';

void main() {
  var excel = Excel.createExcel(); // Automatically creates 1 empty sheet: Sheet1
  Sheet sheetObject = excel['Sheet1'];

  sheetObject.cell(CellIndex.indexByString("A1")).value = "Hello";
  sheetObject.cell(CellIndex.indexByString("B1")).value = "World";

  var directory = Directory.current; // Gets the current directory
  var fileBytes = excel.save(fileName: "My_Custom_Location_Excel_File.xlsx");
  File(join(directory.path, "My_Custom_Location_Excel_File.xlsx"))
    ..createSync(recursive: true)
    ..writeAsBytesSync(fileBytes!);
  print("Excel file saved to custom location!");
}
