const SERVER = 'http://ubuntu.sovanreach.com:10025';
// const SERVER = 'http://localhost:9001';

const API_URL = `${SERVER}/api/restaurant`;
$(document).ready(_ => {
    console.log('aa')
    scrap_page();
})

function scrap_page() {
    $.ajax({
        url: API_URL,
        dataType: 'json',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        success: function(data) {
            const students = data.student;
            const professors = data.professor;
            updateUI(students, 'tab1primary');
            updateUI(professors, 'tab2primary')
        },
        error: function(error) {
            console.log(error)
        }
   });
}

function updateUI(food_data , tab_name){
    const card_divs = $(`#${tab_name} > div`)
    const foods = food_data['food'];
    const images = food_data['image'];
    foods.forEach((data, index) => {
        $(card_divs[index]).find('.card-title').text(data)
        $(card_divs[index]).find('img').attr('src',`/img/${images[index]}.jpg`);
    })
}
