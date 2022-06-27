async function PostApi() {
    const data = {buy_order: "ordenCompra12345678",
                    session_id: "sesion1234557545",
                    amount: 10000,
                    return_url: "http://www.comercio.cl/webpay/retorno"
                }
    const url= `/rswebpaytransaction/api/webpay/v1.2/transactions`
    await fetch(url,{
        method: 'POST',
        body: JSON.stringify(data),
        
        headers:{
            'Content-Type': 'application/json',
            'Tbk-Api-Key-Id': '597055555532',
            'Tbk-Api-Key-Secret': '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C'
          }
    }.then(res => console.log(res.url)));
  }

  /* {
    "buy_order": "ordenCompra12345678",
    "session_id": "sesion1234557545",
    "amount": 10000,
    "return_url": "http://www.comercio.cl/webpay/retorno"
   } */