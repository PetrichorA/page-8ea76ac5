fetch(document.head.querySelector("#resource").href).then((e=>e.json())).then((e=>Object.values(e).map((e=>{const t=document.createElement("img");t.src="https://coldcdn.com/api/cdn/arweave/"+e,t.addEventListener("error",(()=>{t.src.startsWith("https://coldcdn.com/")?t.src="https://dist.arweave.net/"+e:t.src="https://coldcdn.com/api/cdn/arweave/"+e})),document.body.appendChild(t)}))));