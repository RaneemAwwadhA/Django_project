
  // Add product to cart
  function addcart(productId, quantity) {
    $.ajax({
      url: '/addtocart/',  
      type: 'get',
      data: {
        'id': productId,  
        'quantity': quantity 
      },
      success: function(result) {
        console.log(result.cart_count);
        $('.cart-count').text(result.cart_count);  
        
      
        Swal.fire({
          title: 'Yay! It\'s in Your Cart 💖',
          text: 'The product has been added successfully.',
          icon: 'success',
          iconColor: '#c48ec7',
          background: 'linear-gradient(135deg, #fef9ff, #f8e7f9, #eef2fc)',
          color: '#4a4a4a',
          confirmButtonText: 'Got it!',
          timer: 4000,
          timerProgressBar: true,
          customClass: {
            popup: 'rounded-5 shadow-sm',
            title: 'fw-semibold',
            confirmButton: 'sweet-confirm-btn'
          }
        });
      }
    });
  }




  