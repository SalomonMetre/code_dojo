<?php

namespace App\Http\Controllers;

use App\Models\Course;
use App\Models\Student;
use App\Models\StudentCourse;
use Illuminate\Http\Request;

class StudentCourseController extends Controller
{
    public function create(Request $request){
        $student_course = StudentCourse::create($request->all());
        return response()->json([
            "result" => $student_course ? "success" : "failure",
        ]);
    }

    public function getStudentCourses($id){
        $student = Student::find($id);
        return response()->json(["courses"=>$student->courses]);
    }

    public function getCourseStudents($id){
        $course = Course::find($id);
        return response()->json(["courses"=>$course->students]);
    }
}
