import 'dart:io';
import 'package:excel_dart/excel_dart.dart';

void main() {
  var file = "New_Excel_File.xlsx";
  var bytes = File(file).readAsBytesSync();
  var excel = Excel.decodeBytes(bytes);
  Sheet sheetObject = excel['Sheet1'];

  // Merge cells from A1 to C1
  sheetObject.merge(CellIndex.indexByString("A1"), CellIndex.indexByString("C1"), customValue: "Merged Cells");

  var fileBytes = excel.save();
  File(file).writeAsBytesSync(fileBytes!); // Save the updated file

  print("Cells merged!");
}
