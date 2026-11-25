// Behaviour for the static preview: mobile nav, FAQ accordion, contact form,
// cookie banner. The live site posts the form to PocketBase — this preview has
// no backend, so the submit hands the same data to WhatsApp instead.
(() => {
  const WA = "6281388244662";

  // ---- mobile nav
  const toggle = document.querySelector(".mobile-toggle");
  const mobileNav = document.querySelector(".mobile-nav");
  if (toggle && mobileNav) {
    toggle.addEventListener("click", () => {
      const open = mobileNav.hasAttribute("hidden");
      mobileNav.toggleAttribute("hidden", !open);
      toggle.setAttribute("aria-expanded", String(open));
      toggle.setAttribute("aria-label", open ? "Tutup navigasi" : "Buka navigasi");
      toggle.innerHTML = open
        ? '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>'
        : '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>';
    });
    mobileNav.addEventListener("click", (ev) => {
      if (ev.target.closest("a")) toggle.click();
    });
  }

  // ---- FAQ accordion (one open at a time, like the live site)
  const items = [...document.querySelectorAll(".faq-item")];
  items.forEach((item) => {
    const button = item.querySelector(".faq-question");
    button.addEventListener("click", () => {
      const isOpen = item.classList.contains("is-open");
      items.forEach((other) => {
        other.classList.remove("is-open");
        other.querySelector(".faq-question").setAttribute("aria-expanded", "false");
        other.querySelector(".faq-answer")?.remove();
      });
      if (isOpen) return;
      item.classList.add("is-open");
      button.setAttribute("aria-expanded", "true");
      const p = document.createElement("p");
      p.className = "faq-answer";
      p.textContent = button.dataset.answer;
      item.appendChild(p);
    });
  });

  // ---- contact form -> WhatsApp handoff
  const form = document.querySelector("[data-lead-form]");
  if (form) {
    const error = form.querySelector(".contact-form-error");
    form.addEventListener("submit", (ev) => {
      ev.preventDefault();
      const data = new FormData(form);
      const name = String(data.get("name") || "").trim();
      const whatsapp = String(data.get("whatsapp") || "").trim();
      const area = String(data.get("area") || "").trim();
      const needs = String(data.get("needs") || "").trim();
      if (!name || !whatsapp || !area) {
        error.textContent = "Nama, nomor WhatsApp, dan area pemasangan wajib diisi.";
        error.hidden = false;
        return;
      }
      error.hidden = true;
      const message =
        `Halo, saya ${name}.\n` +
        `Nomor WhatsApp: ${whatsapp}\n` +
        `Area pemasangan: ${area}\n` +
        (needs ? `Kebutuhan: ${needs}\n` : "") +
        "Mohon informasi ketersediaan jaringan dan pendaftaran WiFi XL Home.";
      window.open(`https://wa.me/${WA}?text=${encodeURIComponent(message)}`, "_blank", "noopener");
      form.innerHTML =
        '<div class="contact-form-success">' +
        '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>' +
        `<h3>Terima kasih, ${name.replace(/[<>&]/g, "")}!</h3>` +
        "<p>Permintaan Anda sudah dibuka di WhatsApp. Kirim pesannya agar admin kami bisa melanjutkan konsultasi.</p>" +
        "</div>";
    });
  }

  // ---- cookie banner (visual only: no trackers on this static preview)
  const KEY = "cc_cookie";
  const banner = document.createElement("section");
  banner.className = "cookie-banner";
  banner.setAttribute("role", "dialog");
  banner.setAttribute("aria-label", "Pilihan cookie");
  banner.hidden = true;
  banner.innerHTML =
    "<div><h2>Privasi Anda, pilihan Anda.</h2><p>Cookie penting mendukung fungsi situs. Cookie opsional hanya digunakan dengan izin Anda.</p></div>" +
    '<div class="cookie-actions">' +
    '<button type="button" data-cookie="reject">Tolak opsional</button>' +
    '<button type="button" data-cookie="customize">Sesuaikan</button>' +
    '<button type="button" class="cookie-accept" data-cookie="accept">Terima semua</button>' +
    "</div>";
  document.body.appendChild(banner);

  const hasConsent = () => document.cookie.split("; ").some((c) => c.startsWith(KEY + "="));
  const save = () => {
    document.cookie = `${KEY}=${encodeURIComponent(
      JSON.stringify({ categories: ["necessary"], consentTimestamp: new Date().toISOString() })
    )}; max-age=15724800; path=/; SameSite=Lax`;
    banner.hidden = true;
  };
  if (!hasConsent()) banner.hidden = false;
  banner.addEventListener("click", (ev) => {
    const btn = ev.target.closest("[data-cookie]");
    if (!btn) return;
    save();
  });
  document.querySelector("[data-cookie-settings]")?.addEventListener("click", () => {
    banner.hidden = false;
  });
})();
