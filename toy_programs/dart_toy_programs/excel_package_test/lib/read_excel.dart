import 'dart:io';
import 'package:excel_dart/excel_dart.dart';

void main() {
  var file = "/home/smonk/Downloads/base.xlsx";
  var bytes = File(file).readAsBytesSync();
  var excel = Excel.decodeBytes(bytes);

  for (var table in excel.tables.keys) {
    print(table); // Sheet Name
    print('Max Columns: ${excel.tables[table]?.maxCols}');
    print('Max Rows: ${excel.tables[table]?.maxRows}');
    for (var row in excel.tables[table]!.rows) {
      print("\nNew row\n");
      for(var data in row){
        print(data!.value);
      }
    }
  }
}
