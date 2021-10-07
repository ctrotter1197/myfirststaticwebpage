<?php
$server = "christrottersqlserver.database.windows.net";
$username = "christrotter1197";
$password = "Chris1197";
$database_name = "ChrisTrotterDatabase";

$connection = mysqli_init();
mysqli_real_connect($connection, $server, $username, $password, $database_name, 3306);

    $studentID1 = $_POST["stID1"];
    $grade1 = $_POST["grade1"];
    $studentID2 = $_POST["stID2"];
    $grade2 = $_POST["grade2"];
    $studentID3 = $_POST["stID3"];
    $grade3 = $_POST["grade3"];

$query = mysqli_query($connection, "CREATE TABLE Grades(
            StudentID int,
            Grade int
            );

            INSERT INTO Grades (StudentID,Grade)
            VALUES ('.$stID1.','.$grade1.');

            INSERT INTO Grades (StudentID,Grade)
            VALUES ('.$stID2.', '.$grade2.');

            INSERT INTO Grades (StudentID,Grade)
            VALUES ('.$stID3.', '.$grade3.');

            SELECT AVG(Grade)
            FROM Grades;
            "));

if($outcomes = mysqli_multi_query($connection, $query))
{
    echo "The information inputted has been processed!";
    mysql_free_result($outcomes);
};

mysqli_close($connection);

?>
