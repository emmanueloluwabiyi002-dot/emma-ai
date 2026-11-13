
from groq import Groq
from flask import Flask, request, jsonify
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
app = Flask(__name__)

HTML = """
<html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>
<style>body{margin:0;font-family:sans-serif;background:#ece5dd}#top{background:#ff4d6d;color:white;padding:12px;display:flex;gap:10px;align-items:center;position:fixed;top:0;left:0;right:0}#ava{width:40px;height:40px;background:white;color:#ff4d6d;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:bold}#msgs{padding:65px 10px 80px}.m{background:white;padding:10px;border-radius:10px;margin:8px 0;max-width:85%;white-space:pre-wrap}.moi{background:#dcf8c6;margin-left:auto}#bar{position:fixed;bottom:0;left:0;right:0;background:#ece5dd;display:flex;padding:8px;gap:5px}#t{flex:1;padding:12px;border-radius:20px;border:none}#b{background:#ff4d6d;border:none;color:white;border-radius:50%;width:50px;height:50px}</style>
</head><body><div id='top'><div id='ava'>E</div><div><b>Emma AI</b><br><small>La VRAIE Emma - By Boss</small></div></div><div id='msgs'><div class='m'>Bonjour ! Je suis Emma AI, la vraie AI de mon Boss. Pose-moi tout.</div></div><div id='bar'><input id='t' placeholder='Parle à Emma...'><button id='b' onclick='go()'>➤</button></div>
<script>
async function go(){
 var i=document.getElementById('t'); var v=i.value.trim(); if(!v) return;
 var d=document.createElement('div'); d.className='m moi'; d.innerText=v; document.getElementById('msgs').appendChild(d); i.value='';
 var r=document.createElement('div'); r.className='m'; r.innerText='Emma réfléchit...'; document.getElementById('msgs').appendChild(r);
 let res=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({msg:v})});
 let j=await res.json(); r.innerText=j.reply; window.scrollTo(0,document.body.scrollHeight);
}
</script></body></html>
"""

@app.route("/")
def home(): return HTML

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("msg","")
    c = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role":"system","content":"Tu es Emma AI, assistante intelligente, gentille, qui parle français simple comme une copine en Guinée. Tu aides pour cours, devoirs, vie."},{"role":"user","content":msg}])
    return jsonify({"reply": c.choices[0].message.content})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
