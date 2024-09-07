<?php

use App\Http\Controllers\CourseController;
use App\Http\Controllers\StudentController;
use App\Http\Controllers\StudentCourseController;
use App\Http\Middleware\binary_decider;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

Route::post('/students/create', [StudentController::class, 'create']);

Route::post('/courses/create', [CourseController::class, 'create']);

Route::post('/student_course/create', [StudentCourseController::class, 'create']);

Route::get('/student/{id}/courses', [StudentCourseController::class, 'getStudentCourses']);

Route::get('/course/{id}/students', [StudentCourseController::class,'getCourseStudents']);

Route::get('/students/{id?}/{field?}', [StudentController::class,'read']);

Route::get('random_number', function (Request $request){
    return response()->json($request->all());
})->middleware([binary_decider::class]);

Route::middleware([binary_decider::class])->group(function () {
    Route::get('random_number_2', function (){
        return response("Hey you 2 !");
    });

    Route::get('random_number_3', function (){
        return response('Hey you 3');
    });
});