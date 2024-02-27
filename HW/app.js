function finalGrade(exam, projects) {
    if (exam > 90 || projects > 10) return 100;
    if (exam > 75 && projects >= 5) return 90;
    if (exam > 50 && projects >= 2) return 75;
    return 0;
}


// console.log(finalGrade(85, 7));
function finalGrade2(exam, projects) {
    if (exam > 90 || projects > 10) {
        console.log(1);
    }
    else if (exam > 75 && projects >= 5) {
        console.log(2);
    }
    else if (exam > 50 && projects >= 2) {
        console.log(3);
    }else{ console.log(4);
    }
}

finalGrade2(85, 7);

