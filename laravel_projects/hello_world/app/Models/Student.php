<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Casts\Attribute;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Student extends Model
{
    use HasFactory;

    protected $table = "students";
    protected $fillable = ['name', 'age'];


    public function courses(){
        return $this->belongsToMany(Course::class, "student_course","student_id","course_id");
    }

    public function name(): Attribute{
        return Attribute::make(
            get: fn (string $name) => strtolower($name),
        );
    }
}
