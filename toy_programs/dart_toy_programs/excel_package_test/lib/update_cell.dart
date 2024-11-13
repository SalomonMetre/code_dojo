import 'dart:io';
import 'package:excel_dart/excel_dart.dart';

void main() {
  var file = "New_Excel_File.xlsx";
  var bytes = File(file).readAsBytesSync();
  var excel = Excel.decodeBytes(bytes);
  Sheet sheetObject = excel['Sheet1'];

  var cell = sheetObject.cell(CellIndex.indexByString("A1"));
  cell.value = "Updated Value"; // Update cell value
  cell.cellStyle = CellStyle(fontFamily: getFontFamily(FontFamily.Calibri), bold: true);

  var fileBytes = excel.save();
  File(file).writeAsBytesSync(fileBytes!); // Save the updated file

  print("Cell updated!");
}
