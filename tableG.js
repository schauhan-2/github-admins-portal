const fs = require('fs');

function getTable() {
    fs.readFile('output.csv', 'utf8', function (err, data) {
        let collabratores = new Map();
        let tempArray = data.split('\n')
        tempArray.forEach(line => {
            let tempArray2 = line.split(',');
            if(!collabratores.has(tempArray2[0])){
                collabratores.set(tempArray2[0], tempArray2.slice(1,3));
            }
            else{
                collabratores.set(tempArray2[0], collabratores.get(tempArray2[0]).push(tempArray2.slice(1,3)));
            }
        })
                
        //Create a HTML Table element.
        var table = document.createElement("TABLE");
        table.border = "1";
         
        //Get the count of columns.
        var columnCount = collabratores[0].length;
         
        //Add the header row.
        var row = table.insertRow(-1);
        for (var i = 0; i < columnCount; i++) {
            var headerCell = document.createElement("TH");
            headerCell.innerHTML = collabratores[0][i];
            row.appendChild(headerCell);
        }
         
        //Add the data rows.
        for (var i = 1; i < customers.length; i++) {
            row = table.insertRow(-1);
            for (var j = 0; j < columnCount; j++) {
                var cell = row.insertCell(-1);
                cell.innerHTML = collabratores[i][j];
            }
        }
         
        var dvTable = document.getElementById("dvTable");
        dvTable.innerHTML = "";
        dvTable.appendChild(table);
    });
}