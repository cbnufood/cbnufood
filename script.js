const API_URL = 'http://ubuntu.sovanreach.com:10025/api/restaurant';
// const API_URL = 'http://localhost:9001/api/restaurant';
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
    food_data.forEach((data, index) => {
        $(card_divs[index]).find('.card-title').text(data)
        const newImgName=encodeURIComponent(data);
        $(card_divs[index]).find('img').attr('src',`/img/${newImgName}.jpg`);
    })
}
