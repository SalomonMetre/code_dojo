import 'dart:io';
import 'package:path/path.dart';
import 'package:excel_dart/excel_dart.dart';

void main() {
  // ==========================
  // Configuration
  // ==========================

  // Path to the existing Excel file
  // Replace this with the actual path to your Excel file
  String existingFilePath = join(Directory.current.path, 'New_Excel_File.xlsx');

  // Name of the new sheet to add
  String newSheetName = 'NewSheet3';

  // ==========================
  // Reading the Existing Excel File
  // ==========================

  // Check if the file exists
  File existingFile = File(existingFilePath);
  if (!existingFile.existsSync()) {
    print("The file at path '$existingFilePath' does not exist.");
    return;
  }

  // Read the existing Excel file as bytes
  List<int> fileBytes = existingFile.readAsBytesSync();

  // Decode the Excel file
  Excel excel = Excel.decodeBytes(fileBytes);

  // ==========================
  // Adding a New Sheet
  // ==========================

  // Check if the sheet already exists
  if (excel.tables.containsKey(newSheetName)) {
    print("Sheet '$newSheetName' already exists in the Excel file.");
  } else {
    // Create a new sheet by accessing it via the sheet name
    Sheet newSheet = excel[newSheetName];

    // Add data to the new sheet
    newSheet.cell(CellIndex.indexByString("A1")).value = "This is a new sheet!";
    newSheet.cell(CellIndex.indexByString("A2")).value = 12345;

    print("New sheet '$newSheetName' created and data added.");
  }

  // ==========================
  // Saving the Updated Excel File
  // ==========================

  // Save the Excel file as bytes
  List<int>? updatedFileBytes = excel.save();

  if (updatedFileBytes == null) {
    print("Failed to save the Excel file.");
    return;
  }

  // Write the updated bytes back to the original file
  existingFile.writeAsBytesSync(updatedFileBytes, flush: true);

  print("Excel file saved successfully with the new sheet.");
}
