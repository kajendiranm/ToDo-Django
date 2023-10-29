let timer;
const inputBox = document.getElementById("myInput");
const result = document.getElementById("result");
const btn = document.getElementById('add_btn')

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

inputBox.addEventListener("input", function() {
  // Clear any previous timers
  clearTimeout(timer);

    if(inputBox.value == ""){
        result.innerText = ''
    }
    else{
  timer = setTimeout(function() {
    $.ajax({
        type: "POST",
        url: '',
        data: {
            'name': inputBox.value,
            'csrfmiddlewaretoken': csrftoken,
        },
        success: response=>{
            if(response.avail){
                result.innerText = `The name ${response.name} is Available!`
                result.classList.remove('red')
                result.classList.add('green')
                btn.classList.remove('hide')
            }
            else{
                result.innerText = `The name ${response.name} is Already taken!`
                result.classList.remove('green')
                result.classList.add('red')
                btn.classList.add('hide')
            }
        },
        error: err=>{
            console.log(err)
        }
    })

  }, 1000);
}
});

btn.addEventListener('click',()=>{
    $.ajax({
        type: "POST",
        url: '/ajax/add',
        data: {
            'name': inputBox.value,
            'csrfmiddlewaretoken': csrftoken,
        },
        success: response=>{
            result.innerText = `The name ${response.name} is Added!`
            btn.classList.add('hide')
        },
        error: err=>{
            console.log(err)
        }
    })
})