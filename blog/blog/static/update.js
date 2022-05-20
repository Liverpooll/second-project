


function move_url (pk) {
  location.href = `http://127.0.0.1:8000/blog/delete/${pk}`
}

function update_onclick (pk) {
  if (!confirm("정말 수정하시겠습니까?")) {
} else {
   move_url(pk)
}
}
