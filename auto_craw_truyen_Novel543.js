(function() {
    'use strict';

    // --- CẤU HÌNH SELECTOR ---
    const SELECTORS = {
        title: "#chapterWarp > div.chapter-content.px-3 > h1",
        content: "#chapterWarp > div.chapter-content.px-3 > div",
        nextBtn: "#read > div > div.warp.my-5.foot-nav > a:nth-child(5)"
    };

    // --- CÁC HÀM HỖ TRỢ ---

    // 1. Hàm làm sạch tiêu đề (Bỏ (1/2), (2/2)...)
    function cleanTitle(rawTitle) {
        if (!rawTitle) return "";
        // Xóa các chuỗi dạng (số/số) ở cuối
        return rawTitle.replace(/\s*\(\d+\/\d+\)$/, '').trim();
    }

    // 2. Hàm tải file về máy
    function downloadFile(filename, text) {
        const element = document.createElement('a');
        element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
        element.setAttribute('download', filename + ".txt");
        element.style.display = 'none';
        document.body.appendChild(element);
        element.click();
        document.body.removeChild(element);
    }

    // 3. Hàm hiển thị trạng thái trên màn hình
    function showStatus(msg, color = 'green') {
        let box = document.getElementById('crawl-status-box');
        if (!box) {
            box = document.createElement('div');
            box.id = 'crawl-status-box';
            box.style.position = 'fixed';
            box.style.bottom = '10px';
            box.style.right = '10px';
            box.style.padding = '10px';
            box.style.background = 'rgba(0,0,0,0.8)';
            box.style.color = 'white';
            box.style.zIndex = '9999';
            box.style.borderRadius = '5px';
            box.style.fontFamily = 'Arial, sans-serif';
            document.body.appendChild(box);
        }
        box.style.border = `2px solid ${color}`;
        box.innerHTML = msg;
    }

    // --- LOGIC CHÍNH ---

    // Kiểm tra xem tool có đang chạy không
    const isRunning = localStorage.getItem('crawler_running') === 'true';

    if (!isRunning) {
        // TRẠNG THÁI 1: CHƯA CHẠY -> HIỆN NÚT START
        const btn = document.createElement('button');
        btn.innerText = "▶ BẮT ĐẦU CRAWL TỪ ĐÂY";
        btn.style.position = "fixed";
        btn.style.top = "10px";
        btn.style.right = "10px";
        btn.style.zIndex = "9999";
        btn.style.padding = "15px";
        btn.style.backgroundColor = "red";
        btn.style.color = "white";
        btn.style.border = "none";
        btn.style.cursor = "pointer";
        btn.style.fontSize = "16px";
        btn.style.fontWeight = "bold";

        btn.onclick = function() {
            localStorage.setItem('crawler_running', 'true');
            // Xóa dữ liệu cũ nếu có
            localStorage.removeItem('crawler_saved_title');
            localStorage.removeItem('crawler_saved_content');
            alert("Đã bắt đầu! Trang sẽ tự reload và tải truyện.");
            location.reload();
        };
        document.body.appendChild(btn);

    } else {
        // TRẠNG THÁI 2: ĐANG CHẠY -> TỰ ĐỘNG XỬ LÝ
        
        // Tạo nút dừng khẩn cấp
        const stopBtn = document.createElement('button');
        stopBtn.innerText = "⏹ DỪNG LẠI";
        stopBtn.style.position = "fixed";
        stopBtn.style.top = "10px";
        stopBtn.style.right = "10px";
        stopBtn.style.zIndex = "10000";
        stopBtn.style.backgroundColor = "gray";
        stopBtn.style.color = "white";
        stopBtn.onclick = function() {
            localStorage.setItem('crawler_running', 'false');
            alert("Đã dừng crawler.");
            location.reload();
        };
        document.body.appendChild(stopBtn);

        // Lấy DOM
        const titleEl = document.querySelector(SELECTORS.title);
        const contentEl = document.querySelector(SELECTORS.content);
        const nextBtnEl = document.querySelector(SELECTORS.nextBtn);

        if (!titleEl || !contentEl) {
            showStatus("❌ Không tìm thấy nội dung. Dừng lại.", "red");
            localStorage.setItem('crawler_running', 'false');
            return;
        }

        const rawTitle = titleEl.innerText.trim();
        const currentTitle = cleanTitle(rawTitle);
        const currentText = contentEl.innerText.trim(); // Dùng innerText để giữ xuống dòng

        // Lấy dữ liệu đã lưu trong LocalStorage (Của phần trước)
        const savedTitle = localStorage.getItem('crawler_saved_title');
        let savedContent = localStorage.getItem('crawler_saved_content') || "";

        showStatus(`⏳ Đang xử lý: ${currentTitle}...`, "yellow");

        // LOGIC GỘP CHƯƠNG
        if (savedTitle === currentTitle) {
            // Trường hợp: Đây là phần tiếp theo (2/2) của chương trước
            console.log("Phát hiện phần tiếp theo của chương cũ. Đang gộp...");
            savedContent += "\n\n" + currentText; // Nối thêm nội dung
            
            // Cập nhật lại bộ nhớ
            localStorage.setItem('crawler_saved_content', savedContent);
        } else {
            // Trường hợp: Đây là chương MỚI hoàn toàn
            
            // 1. Nếu có chương cũ trong bộ nhớ -> Tải xuống ngay
            if (savedTitle) {
                console.log("Chương mới phát hiện. Đang lưu chương cũ...");
                downloadFile(savedTitle, savedContent);
            }

            // 2. Lưu chương hiện tại vào bộ nhớ (để chờ xem có phần 2/2 không)
            const newContentFormat = `${currentTitle}\n\n${currentText}`;
            localStorage.setItem('crawler_saved_title', currentTitle);
            localStorage.setItem('crawler_saved_content', newContentFormat);
        }

        // CHUYỂN TRANG
        if (nextBtnEl && nextBtnEl.href && !nextBtnEl.href.includes("javascript")) {
            setTimeout(() => {
                showStatus("➡ Đang sang trang kế...", "blue");
                nextBtnEl.click();
            }, 2000); // Đợi 2 giây rồi bấm (để tránh bị chặn hoặc tải chưa xong)
        } else {
            // HẾT TRUYỆN
            // Tải nốt chương cuối cùng đang nằm trong bộ nhớ
            const finalTitle = localStorage.getItem('crawler_saved_title');
            const finalContent = localStorage.getItem('crawler_saved_content');
            if (finalTitle) {
                downloadFile(finalTitle, finalContent);
            }
            
            showStatus("✅ Đã crawl xong toàn bộ!", "green");
            localStorage.setItem('crawler_running', 'false');
            alert("Hoàn tất!");
        }
    }
})();
