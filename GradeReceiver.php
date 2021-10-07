
<?php
    $studentID1 = $_GET["studentID1"];
    $grade1 = $_GET["grade1"];
    $studentID2 = $_GET["studentID2"];
    $grade2 = $_GET["grade2"];
    $studentID3 = $_GET["studentID3"];
    $grade3 = $_GET["grade3"];

    echo "Student 1: $studentID1  Grade: $grade1";
    echo "Student 2: $studentID2  Grade: $grade2";
    echo "Student 3: $studentID3  Grade: $grade3";

    $sum = $grade1 + $grade2 + $grade3;
    $average = $sum/3;

    echo "The cumulative average of the grades is $average";
?>
