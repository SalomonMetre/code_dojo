<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Course extends Model
{
    use HasFactory;

    protected $table = "courses";
    protected $fillable = ['name'];

    public function students(){
        return $this->belongsToMany(Student::class, "student_course","course_id","student_id");
    }
}
