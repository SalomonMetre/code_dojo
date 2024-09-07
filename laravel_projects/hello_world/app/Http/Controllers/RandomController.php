<?php

namespace App\Http\Controllers;

use Illuminate\Http\JsonResponse;
use Illuminate\Routing\Controller;
use Illuminate\Support\Facades\Request;

class RandomController extends Controller
{
    public function sendName($name): JsonResponse
    {
        return response()->json([
            'result' => "hey $name",
            'is_secure' => request()->isSecure(),
        ]);
    }
}
