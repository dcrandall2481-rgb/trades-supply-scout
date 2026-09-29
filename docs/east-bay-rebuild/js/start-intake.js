/**
 * Sends the homepage "Start a job" request (name, email, phone, ZIP, trade, notes)
 * to the intake inbox before site.js moves the visitor to the draft job file.
 * Load after config.js and before site.js.
 */
(function () {
  "use strict";
  var C = window.EBS_CONFIG || {};
  var action = C.formAction || "";
  var form = document.getElementById("start-form");
  if (!form || !/^https?:\/\//i.test(action)) return;

  function val(name) {
    var el = form.querySelector('[name="' + name + '"]');
    return el ? String(el.value || "").trim() : "";
  }

  form.addEventListener("submit", function () {
    var zip = val("zip").replace(/\D/g, "").slice(0, 5);
    var trade = val("trade");
    var email = val("email");
    if (!/^\d{5}$/.test(zip) || !trade || !email) return;

    var waitEmail = document.getElementById("waitlist-email");
    if (waitEmail && !waitEmail.value) waitEmail.value = email;

    var body = new URLSearchParams({
      _subject: "East Bay Services — Start a job (" + zip + ")",
      _template: "table",
      _captcha: "false",
      _replyto: email,
      form_type: "start_request",
      name: val("name"),
      email: email,
      phone: val("phone"),
      zip: zip,
      trade: trade,
      notes: val("notes"),
      page: window.location.pathname
    });

    try {
      fetch(action, {
        method: "POST",
        keepalive: true,
        headers: {
          Accept: "application/json",
          "Content-Type": "application/x-www-form-urlencoded"
        },
        body: body.toString()
      }).catch(function () {});
    } catch (e) {}
  });
})();
