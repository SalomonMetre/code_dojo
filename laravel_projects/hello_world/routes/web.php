<?php

use App\Http\Controllers\BookController;
use App\Http\Controllers\RandomController;
use App\Http\Controllers\StudentController;
use Illuminate\Support\Facades\Route;
use Illuminate\Http\Request;


Route::get('/', function () {
    return view('welcome');
});

Route::get('/graveyard', function () {
    return 'Welcome to this page!';
});

Route::get('/names', function () {
    return response()->json([
        'names' => ['salomon', 'joseph', 'benedicte']
    ]);
});

Route::get('/send_message', function (Request $request) {
    echo 'You want to send the message: {$request->message}';
});

Route::get(
    'send_name/{name}',
    [RandomController::class, "sendName"]
);

Route::get('/books/create', [BookController::class, 'getCreateBookView']);

Route::post('/books/create', [BookController::class,'createBook']);


