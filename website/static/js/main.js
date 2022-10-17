
// Automatic dismiss alerts
if (document.querySelector('.js-alert')) {
    document.querySelectorAll('.js-alert').forEach(function ($el) {
        setTimeout(() => {
            $el.classList.remove('show');
        }, 5000);
    });
}

function deleteNote(noteId){
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId })
    }).then(_res => {
        window.location.href = "/"
    })
}

function editNote(noteId){
    console.log(noteId)
}