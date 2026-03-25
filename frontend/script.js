
const API = "http://127.0.0.1:8000/products"


// CREATE
async function createProduct(){

const data={
sku:Math.random().toString(36).substring(7),
name:document.getElementById("c_name").value,
description:"Created from UI",
category:document.getElementById("c_category").value,
brand:document.getElementById("c_brand").value,
price:parseFloat(document.getElementById("c_price").value),
currency:"INR",
discount_percent:0,
stock:parseInt(document.getElementById("c_stock").value),
is_active:true,
rating:4.5,
tags:["new"],
image_urls:[document.getElementById("c_image").value],
dimensions_cm:{length:10,width:10,height:5},
seller:{
seller_id:crypto.randomUUID(),
name:"Web Seller",
email:"seller@test.com",
website:"https://example.com"
}
}

await fetch(API,{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify(data)
})

alert("Product Created")
getProducts()
}



// GET ALL
async function getProducts(){

const res=await fetch(API)
const data=await res.json()

const list=document.getElementById("productList")

list.innerHTML=""

data.items.forEach(p=>{

const image=p.image_urls?.[0] || "https://via.placeholder.com/200"

const div=document.createElement("div")
div.className="product"

div.innerHTML=`

<img src="${image}">

<h4>${p.name}</h4>

<p>${p.brand}</p>

<p>₹ ${p.price}</p>

<p>Stock: ${p.stock}</p>

<p>ID: ${p.id}</p>

`

list.appendChild(div)

})

}



// GET BY ID
async function getProductById(){

const id=document.getElementById("searchId").value

const res=await fetch(`${API}/${id}`)
const p=await res.json()

const list=document.getElementById("productList")

list.innerHTML=""

const div=document.createElement("div")
div.className="product"

div.innerHTML=`

<h3>${p.name}</h3>
<p>${p.brand}</p>
<p>₹ ${p.price}</p>
<p>Stock ${p.stock}</p>
<p>${p.id}</p>

`

list.appendChild(div)

}



// UPDATE
async function updateProduct(){

const id=document.getElementById("u_id").value

const payload={
price:parseFloat(document.getElementById("u_price").value),
stock:parseInt(document.getElementById("u_stock").value)
}

await fetch(`${API}/${id}`,{
method:"PUT",
headers:{"Content-Type":"application/json"},
body:JSON.stringify(payload)
})

alert("Product Updated")

getProducts()

}



// DELETE
async function deleteProduct(){

const id=document.getElementById("d_id").value

await fetch(`${API}/${id}`,{
method:"DELETE"
})

alert("Product Deleted")

getProducts()

}