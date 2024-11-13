import 'package:excel_dart/excel_dart.dart';
import 'dart:io';

void main() {
  var excel = Excel.createExcel(); // Automatically creates 1 empty sheet: Sheet1
  Sheet sheetObject = excel['Sheet1'];

  sheetObject.cell(CellIndex.indexByString("A1")).value = "Hello";
  sheetObject.cell(CellIndex.indexByString("B1")).value = "World";

  var fileBytes = excel.save(fileName: "New_Excel_File.xlsx");
  File("New_Excel_File.xlsx")
    ..createSync(recursive: true)
    ..writeAsBytesSync(fileBytes!);

  print("New Excel file created!");
}
