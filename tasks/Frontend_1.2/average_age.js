let persons = [
    {
        id: 1,
        name: "Jan Kowalski"
    }, {
        id: 2,
        name: "John Doe"
    }, {
        id: 3,
        name: "Jarek Kaczka"
    }
]

let ages = [
    {
        person: 1,
        age: 18
    }, {
        person: 2,
        age: 24
    }, {
        person: 3,
        age: 666
    }
]
 
let locations = [
    {
        person: 1,
        country: "Poland"
    }, {
        person: 3,
        country: "Poland"
    }, {
        person: 1,
        country: "USA"
    }
]

function find_person_from_poland() {
    var id_persons = []
    for (var i in locations) {
        var table = locations[i];
        if (table['country'] == "Poland")
        id_persons.push(table['person'])
    }
        return id_persons    
  }

function age_of_persons_from_poland(id_array) {
    var sum_age = []
    for (var i in ages) {
        var table = ages[i];
        if(id_array.includes(table['person']))
            sum_age.push(table['age'])
      }
    return sum_age
  }

function calculate_medium_age(age_array) {
    let sum = 0; 
    for (let i = 0; i < age_array. length; i++) { 
        sum += age_array[i]; 
    }
    result = sum / persons_age.length;
    return result.toFixed(2)
}

var id_persons = find_person_from_poland();
var persons_age = age_of_persons_from_poland(id_persons);
document.write("Medium age: " + calculate_medium_age(persons_age) + "<br>");