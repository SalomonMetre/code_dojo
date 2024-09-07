<?php

namespace App\Http\Controllers;

use App\Models\Student;
use Illuminate\Http\Request;

class StudentController extends Controller
{
    public function create(Request $request)
    {
        $student = Student::create($request->all());
        $response = ["result" => $student ? "success" : "failure"];
        return response()->json($response);
    }

    public function read($id = null, $field = null)
    {
        if (empty($id) or $id == null) {
            return response()->json(["result" => "success", "data"=> Student::all()]);
        } else {
            $student = Student::find($id);
            if (empty($field) or $field == null) {
                echo "id empty";
                return response()->json(["result" => "success", "data" => $student ? $student->toArray() : []]);
            } else {
                switch ($field) {
                    case "name":
                        return response()->json(["result" => "success", "name" => $student->name]);
                    case "age":
                        return response()->json(["result" => "success", "age" => $student->age]);
                    case "updated_at":
                        return response()->json(["result" => "success", "updated_at" => $student->updated_at]);
                    default:
                        return response()->json(["result" => "success", "data" => $student->toArray()]);
                }
            }
        }
    }
}
