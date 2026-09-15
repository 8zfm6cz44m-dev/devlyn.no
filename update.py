#!/usr/bin/env python3
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Uppdatera meta description
content = re.sub(
    r'content="Devlyn hjelper norske restauranter og lokale bedrifter.*?"',
    r'content="Devlyn leverer digitale løsninger som gjør små og mellomstore bedrifter konkurransedyktige online."',
    content
)

# 2. Uppdatera H1
content = re.sub(
    r'<h1>Vi bygger nettsider som selger, ikke bare ligger der\.</h1>',
    r'<h1>Nettsider som faktisk jobber for deg.</h1>',
    content
)

# 3. Uppdatera lead-tekst
content = re.sub(
    r'<p class="lead">Devlyn hjelper norske restauranter og lokale bedrifter med nettsider, bestillingsløsninger, SEO og AI-drevet synlighet — fra første analyse til lansering\.</p>',
    r'<p class="lead">Vi kombinerer solid digital erfaring med moderne webutvikling for å gjøre små og mellomstore bedrifter synlige og valgte på nett.</p>',
    content
)

# 4. Ta bort "Slik jobber vi"-sektionen
content = re.sub(
    r'<section id="slik-vi-jobber">.*?</section>\n\n',
    '',
    content,
    flags=re.DOTALL
)

# 5. Uppdatera "Nettsider · SEO"-teksten
content = re.sub(
    r'<div><b>Nettsider · SEO</b><span>Hovedfokus: norske restauranter og lokale SMB-er</span></div>',
    r'<div><b>Nettsider · SEO</b><span>For bedrifter som vil bli funnet og valgt online</span></div>',
    content
)

# 6. Flytta section-sub närmare h2 for Tjenester
# Leta efter "Tjenester" och dess section-sub
content = re.sub(
    r'(<h2>Tjenester</h2>)\n\s*<p class="section-sub">Alt en liten eller mellomstor bedrift trenger for å bli funnet og valgt på nett\.</p>',
    r'\1\n      <p class="section-sub">Alt en bedrift trenger for å bli funnet og valgt.</p>',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Alla ändringar gjorda!")
