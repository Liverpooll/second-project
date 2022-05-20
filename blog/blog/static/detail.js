


function move_url (pk) {
  location.href = `http://127.0.0.1:8000/blog/delete/${pk}`
}

function delete_onclick (pk) {
  if (!confirm("정말 삭제하시겠습니까?")) {
} else {
   move_url(pk)
}
}



