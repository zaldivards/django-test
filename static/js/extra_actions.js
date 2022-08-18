const urls_ = Object.freeze({
    movie_delete: '/movies/delete',
    movie_edit: '/movies/edit',
    lend_delete: '/movies/remove-lend',
    lend_edit: '/movies/lends/edit'
})

async function delete_record(url) {
    let token = Cookies.get('csrftoken')
    const res = await fetch(url, {
        method: "DELETE",
        headers: { 'X-CSRFToken': token }
    })
    return res
}

function notificate(text, clazz, clazzToRemove) {
    element = document.querySelector('#notification')
    element.classList.remove(clazzToRemove)
    element.classList.add(clazz)
    document.querySelector("#notification p").textContent = text
    $("#notification").fadeIn("slow");
}


$(document).ready(() => {
    $('#myTable').DataTable();
});

$(".edit_marker").click((e) => {
    if (e.target !== e.currentTarget) return;
    let id_str = e.target.parentNode.getAttribute('movie-id')

    if (id_str === null) {
        id_str = e.target.parentNode.getAttribute('lend-id')
        location.href = `${urls_.lend_edit}/${id_str}`
    }
    else {
        location.href = `${urls_.movie_edit}/${id_str}`
    }
})

$(".close").click(() => $("#notification").fadeOut("slow"));

$('.remove_marker').click(async (e) => {
    if (e.target !== e.currentTarget) return;
    if (confirm('Are you sure you want to delete this record?')) {
        
        let res = Object()
        let id_str = e.target.parentNode.getAttribute('movie-id')
        let id = -1

        if (id_str === null) {
            id_str = e.target.parentNode.getAttribute('lend-id')
            res = await delete_record(`${urls_.lend_delete}/${id_str}`)
        }
        else {
            res = await delete_record(`${urls_.movie_delete}/${id_str}`)
        }

        if (res.status === 204) {
            e.target.parentNode.remove()
            notificate('Successfully removed!', 'alert-success', 'alert-danger')
        }
        else {
            console.log(await res.json());
            notificate('Error trying to remove the record', 'alert-danger', 'alert-success')
        }

    }
})
