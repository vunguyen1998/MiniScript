# 1. Auto download chương
## Web: `https://truyenyy.vip/manager`

```
so_chuong = document.getElementById('id_chap_num').value
ten_chuong = document.getElementById('id_chap_title').value
noi_dung_chuong = document.getElementById('id_chap_content').value
next_btn = document.getElementsByClassName('btn btn-secondary')[2]

var a = document.createElement("a");
a.href = window.URL.createObjectURL(new Blob(['Chương ' + so_chuong + ': ' + ten_chuong + '\n' + noi_dung_chuong], {type: "text/plain"}));
a.download = 'Chương ' + so_chuong + '.txt';
a.click();

next_btn.click();
```


## Web: `https://metruyencv.com/`
```
let title = document.getElementsByClassName('h1 mb-4 font-weight-normal nh-read__title')[0].innerText
let content = document.getElementById('js-read__content').innerText

var next_btn = document.getElementsByClassName('nh-read__action d-flex align-items-center h6 mb-0 ml-auto rounded-3 py-2 px-4')[0];


var a = document.createElement("a");
a.href = window.URL.createObjectURL(new Blob([content], {type: "text/plain"}));
a.download = title.split(':')[0] + '.txt';
a.click();

next_btn.click();
```

# 2. Hỗ trợ đăng chương trên TruyenYY
## Web: `https://truyenyy.vip/manager/novel/58760/chapter/add/`

```
so_chuong = document.getElementById('id_chap_num')
ten_chuong = document.getElementById('id_chap_title')
noi_dung_chuong = document.getElementById('id_chap_content')
is_vip = document.getElementById('id_is_vip')
tlt = document.getElementById('id_vip_stones')
btn_luu_nhap = document.querySelector("#btn_save_draft")
ten_truyen = document.querySelector("body > div.content-wrapper.py-3 > div > ol > li.breadcrumb-item.active")
url = window.location.pathname

if (url.search('chapter/add') > -1) {
    setTimeout(async()=>{
        txt = await window.navigator.clipboard.readText()
        title = txt.split("\n")[0]

        so_chuong.value = title.split(": ")[0].replace('Chương ','')
        ten_chuong.value = title.split(": ")[1]
        await window.navigator.clipboard.writeText(txt.replace(title, ''))
        is_vip.checked = true
        
        if (ten_truyen.innerText == 'Máy Móc Toàn Cầu Tiến Hóa (Dịch)' || ten_truyen.innerText == 'Lãnh Chúa Toàn Dân: Điểm Danh Nhận Giảm Giá Thần Khí (Dịch)' || ten_truyen.innerText == 'Lãnh Chúa Toàn Dân: Bắt Đầu Xây Dựng Tiên Vực Bất Hủ (Dịch)') || ten_truyen.innerText == 'Phản Phái Vô Địch: Mang Theo Đồ Đệ Đi Săn Khí Vận (Dịch)') {
            tlt.value = 30
        }
        else {
            tlt.value = 25
        }
    }, 200)
}

if (url.search('drafts') > -1 && url.search('edit') > -1) {
  currentDate = new Date().toJSON().slice(0, 10)
  hen_gio = document.getElementById('id_schedule_at')
  
  if (localStorage.getItem("gio_dang") == null || localStorage.getItem("gio_dang") == 24) {
    gio_dang = 16
  }
  
  else {
    gio_dang = localStorage.getItem("gio_dang")
  }
  hen_gio.value = currentDate + ' ' + gio_dang + ':01'
  // noi_dung_chuong.value = await window.navigator.clipboard.readText()

  // Khi bấm nút Lưu lại sẽ tự động save vào localStorage
  document.querySelector("#id_form > button.btn.btn-primary").addEventListener("click", save_local_store)
  function save_local_store() {
    // get Giờ từ hẹn lịch xuất bản
    gio_dang = parseInt(hen_gio.value.split(' ')[1].split(':')[0]) + 1
    // Set Item
    localStorage.setItem("gio_dang", gio_dang);
  }
}
```

## Code test
```
// if (url.search('https://truyenyy.vip/manager/novel/list/joined/') > -1) {
//   setTimeout(async()=>{
//     item = document.querySelector("#novel_42720 > h5")
//     href = item.children[0].href
//     // var request = new XMLHttpRequest();
//     // request.onreadystatechange = function() {
//     //   jsontext = request.responseText;
//     //   so_chuong = jsontext.split('<span class="badge badge-secondary">')[1].split('</span>')[0];
//     // }
//     // request.open("GET", href, true);
//     // request.send();
//     async function start() {
//       await fetch(href).then(res => res.text()).then(data => {
//        so_chuong = data.split('<span class="badge badge-secondary">')[1].split('</span>')[0]
//       })
//     }
//     start()
//     chuong = document.createElement('span')
//     chuong.innerText = 'Chương mới nhất: ' + so_chuong
//     item.appendChild(chuong)
//   }, 100)
// }
```