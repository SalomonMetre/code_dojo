<?php

namespace App\Http\Controllers;

use App\Models\Book;
use Illuminate\Http\Request;
use Illuminate\Routing\Controller;

class BookController extends Controller{

    public function getCreateBookView(){
        return view('books/create');
    }

    public function createBook(Request $request){
        $book = Book::create($request->all());
        echo "Book saved !";
    }
}