<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create New Book</title>
</head>
<body>
    <h2>Create New Book</h2>
    <form method="POST" action="/books/create">
        
        <input name="_token" value="{{ csrf_token() }}" >

        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title" placeholder="Enter book title"><br>

        <label for="type">Genre:</label><br>
        <input type="text" id="type" name="type" placeholder="Enter book genre"><br>

        <label for="year_edition">Year of Edition:</label><br>
        <input type="number" id="year_edition" name="year_edition" placeholder="Enter year of edition"><br>

        <input type="submit" value="Create New Book">
    </form>
</body>
</html>
