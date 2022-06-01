function add_to_cart(id) {
    fetch('/add_to_cart/'+id, 
        {method: 'POST'}
    )
}