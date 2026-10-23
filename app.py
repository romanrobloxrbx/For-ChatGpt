from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#fff7ed">
  <title>Meet Max — The 100-Year-Old Cat</title>
  <style>
    :root { --ink: #34251f; --muted: #78665c; --orange: #f28b50; --cream: #fff7ed; --pink: #ffe4dc; }
    * { box-sizing: border-box; }
    body { margin: 0; min-height: 100vh; font-family: Inter, ui-rounded, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: var(--ink); background: radial-gradient(circle at 12% 12%, #ffe2d3 0, transparent 28%), radial-gradient(circle at 90% 80%, #ffe7a8 0, transparent 25%), var(--cream); }
    .wrap { width: min(1080px, calc(100% - 36px)); margin: 0 auto; }
    header { display: flex; align-items: center; justify-content: space-between; padding: 24px 0; }
    .brand { font-weight: 850; letter-spacing: -.04em; font-size: 1.2rem; }
    .brand span { margin-right: 8px; }
    .tag { border: 1px solid #f3c7ad; border-radius: 999px; padding: 9px 14px; color: #92512f; background: #fffaf5; font-size: .85rem; font-weight: 700; }
    main { display: grid; grid-template-columns: 1.05fr .95fr; gap: 46px; align-items: center; padding: 52px 0 70px; }
    .eyebrow { color: #b55c2d; text-transform: uppercase; letter-spacing: .15em; font-size: .76rem; font-weight: 850; }
    h1 { font-size: clamp(2.7rem, 6vw, 5.3rem); line-height: .98; letter-spacing: -.07em; margin: 16px 0 22px; }
    h1 em { color: #e8753d; font-style: normal; }
    .intro { font-size: 1.15rem; line-height: 1.75; color: var(--muted); max-width: 490px; }
    .facts { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 30px; }
    .fact { background: rgba(255,255,255,.78); border: 1px solid #f5dfd0; border-radius: 20px; padding: 20px; box-shadow: 0 10px 30px rgba(100,60,30,.05); }
    .fact .icon { font-size: 1.5rem; }
    .fact small { display: block; color: var(--muted); margin-top: 12px; font-weight: 700; }
    .fact strong { display: block; font-size: 1.35rem; margin-top: 3px; }
    .cat-card { position: relative; border-radius: 36px; padding: 24px; background: linear-gradient(145deg, #ffd9c2, #ffedb9); min-height: 430px; display: grid; place-items: center; overflow: hidden; box-shadow: 0 24px 70px rgba(133,79,43,.15); }
    .sun { position: absolute; width: 250px; height: 250px; border-radius: 50%; background: rgba(255,255,255,.42); top: 38px; right: 25px; }
    .paw { position: absolute; font-size: 2.5rem; opacity: .35; }
    .paw.one { top: 35px; left: 32px; transform: rotate(-20deg); }
    .paw.two { bottom: 42px; right: 28px; transform: rotate(20deg); }
    .cat-emoji { position: relative; font-size: clamp(9rem, 20vw, 15rem); filter: drop-shadow(0 18px 8px rgba(111,62,34,.13)); animation: float 4s ease-in-out infinite; }
    .caption { position: absolute; bottom: 24px; left: 24px; right: 24px; text-align: center; font-weight: 800; color: #79462e; }
    .note { margin: 0 0 60px; border-radius: 22px; padding: 22px 24px; background: rgba(255,255,255,.7); border: 1px solid #f5dfd0; color: var(--muted); line-height: 1.7; }
    .note strong { color: var(--ink); }
    footer { border-top: 1px solid #efd9c9; padding: 22px 0 30px; color: var(--muted); font-size: .9rem; display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap; }
    @keyframes float { 0%,100% { transform: translateY(0) rotate(-2deg); } 50% { transform: translateY(-10px) rotate(2deg); } }
    @media (max-width: 760px) { main { grid-template-columns: 1fr; padding-top: 28px; gap: 30px; } .cat-card { min-height: 320px; } header { gap: 12px; } .tag { font-size: .75rem; } }
    @media (prefers-reduced-motion: reduce) { .cat-emoji { animation: none; } }
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="brand"><span>🐾</span>Max's Story</div>
      <div class="tag">A remarkable discovery</div>
    </header>
    <main>
      <section>
        <div class="eyebrow">Meet the cat everyone is talking about</div>
        <h1>Meet Max,<br>the <em>100-Year-Old</em> Cat!</h1>
        <p class="intro">Yesterday, scientists found out that a cat called Max lived 100 years. Here's the little story behind that remarkable discovery.</p>
        <div class="facts">
          <div class="fact"><div class="icon">🐱</div><small>NAME</small><strong>Max</strong></div>
          <div class="fact"><div class="icon">🎂</div><small>AGE</small><strong>100 years</strong></div>
        </div>
      </section>
      <section class="cat-card" aria-label="Illustration of a cat">
        <div class="sun"></div><div class="paw one">🐾</div><div class="paw two">🐾</div>
        <div class="cat-emoji" role="img" aria-label="Cat">🐈</div>
        <div class="caption">Max's extraordinary story ✨</div>
      </section>
    </main>
    <section class="note"><strong>🔎 The discovery</strong><br>Scientists found out yesterday that Max lived 100 years. That's all the information currently included on this page.</section>
    <footer><span>🐾 A little page about Max</span><span>Made with Python and Flask</span></footer>
  </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
