let inner_title = document.querySelector('.input-title')
let inner_content = document.querySelector('.input-content')


function submit_it () {
  let form = document.querySelector('.form-box');
  if (inner_title.value == '' || inner_content.value == '') { 
    alert('입력하세여');
  } else {
    let edit_confirm = confirm('수정하시겠습니까?');
    if (!edit_confirm) {
      return false;
    } else {
      form.submit();
    }
  }
}
