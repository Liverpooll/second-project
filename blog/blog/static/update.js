let inner_title = document.querySelector('.input-title')
let inner_content = document.querySelector('.input-content')


function update_url (pk) {
  location.href = `http://127.0.0.1:8000/blog/update/${pk}`
}

function delete_url (pk) {
  location.href = `http://127.0.0.1:8000/blog/delete/${pk}`
}

function update_onclick (pk) {
  if( inner_title == null ) {
    alert('제목을 입력해주세요') 
    } else {
      if (!confirm("정말 수정하시겠습니까?")) {
      } else {
         delete_url(pk);
      }
    }
  }

function init(title) {
  console.log(title.value)
}