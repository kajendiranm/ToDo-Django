let timer;
const inputBox = document.getElementById("id_username");
const result = document.getElementById("result");
console.log("kaja")

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
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
        result.classList.add('hide')
    }
    else{
  timer = setTimeout(function() {
    $.ajax({
        type: "POST",
        url: '/todo/namechecker',
        data: {
            'name': inputBox.value,
            'csrfmiddlewaretoken': csrftoken,
        },
        success: response=>{
            if(response.avail){
                result.innerText = `Username ${response.name} is Available!`
                result.classList.remove('hide')
                result.classList.add('green')
                result.classList.remove('red')
            }
            else{
                result.innerText = `Username ${response.name} is Already taken!`
                result.classList.remove('green')
                result.classList.add('red')
                result.classList.remove('hide')

            }
        },
        error: err=>{
            console.log(err)
        }
    })

  }, 1000);
}
});