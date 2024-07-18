        }
        else if (moves[i] == 'L') {
            h--
        }
        else if (moves[i] == 'U') {
            v++
        }
        else if (moves[i] == 'D') {
            v--
        }
        else {
            continue;
        }
    for (let i = 0; i <= l; i++) {
        if (moves[i] == 'R') {
            h++
    }
    return h === 0 && v === 0;

};
"
