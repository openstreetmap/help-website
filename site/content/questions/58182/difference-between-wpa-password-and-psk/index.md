+++
type = "question"
title = "Difference between WPA-password and PSK"
description = '''Hi forum as i understand in a preshared-key network, the PSK (which is actually the PMK) can be derived from the WPA-password and the SSID... Questions: If a user would like to join an AP and he is asked to enter a password, is this password called the WPA-password or is this the PSK?  Thank you ver...'''
date = "2016-12-17T06:00:00Z"
lastmod = "2016-12-17T06:27:00Z"
weight = 58182
keywords = [ "and", "psk", "difference", "wpa-password", "between" ]
aliases = [ "/questions/58182" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Difference between WPA-password and PSK](/questions/58182/difference-between-wpa-password-and-psk)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58182-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi forum</p><p>as i understand in a preshared-key network, the PSK (which is actually the PMK) can be derived from the WPA-password and the SSID...</p><p>Questions: If a user would like to join an AP and he is asked to enter a password, is this password called the WPA-password or is this the PSK?</p><p>Thank you very much for any clarifications!</p><p>Joe</p></div><div id="question-tags" class="tags-container tags">and psk difference wpa-password between</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '16, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/c08acf577aad3b14e932ee8f48cf7d20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joseph123&#39;s gravatar image" /><p>joseph123<br />
<span class="score" title="11 reputation points">11</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joseph123 has no accepted answers">0%</span></p></div></div><div id="comments-container-58182" class="comments-container"></div><div id="comment-tools-58182" class="comment-tools"></div><div class="clear"></div><div id="comment-58182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58183"></span>

<div id="answer-container-58183" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58183-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not really a Wireshark question, but anyway here is a view.</p><p>WiFi Alliance refers to it this way:</p><ul><li>Enable WPA2-Personal (aka WPA2-PSK) with AES encryption</li></ul><p>So 'Personal' would take a passphrase or password and derive a PSK through a process with example code given in 802.11-2012 Annex M.4, also loosely described in the wikipedia reference below. An example implementation is the <a href="https://www.wireshark.org/tools/wpa-psk.html">Wireshark online calculator</a>. I prefer the way they refer to it:</p><ul><li>The Wireshark WPA Pre-shared Key Generator provides an easy way to convert a WPA passphrase and SSID to the 256-bit pre-shared ("raw") key used for key derivation.</li></ul><p>The PSK would be the PMK in this case. In addition, 802.11-2012 describes how to use these:</p><ul><li>4.10.3.3 AKM Operations with a Password or PSK (and other places in the standard)</li></ul><p>So to answer your specific question, I prefer to call it a passphrase. I like the term passphrase because from a security context, a passphrase is usually better than a password, but both are better than PSK because PSK is derived from this along with the SSID. But you will see all variants described in different ways.</p><p>In WPA2-Enterprise, the PMK is transferred from the RADIUS server after authentication and delivered to both the AP and the wireless client for use so there is no offline calculator. It makes decryption very difficult as well, because we need the four way handshake and the PMK from the authentication step; the PMK usually changes every session timeout period, which can be short (e.g. adjustable, but commonly 30 minutes or sometimes a few hours).</p><p>Some references:</p><p><a href="https://en.wikipedia.org/wiki/IEEE_802.11i-2004">https://en.wikipedia.org/wiki/IEEE_802.11i-2004</a> <a href="https://standards.ieee.org/about/get/802/802.11.html">802.11-2012 specification</a> (see IEEE website, it is free) <a href="http://www.wi-fi.org/node/7924">http://www.wi-fi.org/node/7924</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '16, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Dec '16, 06:34</p></div></div><div id="comments-container-58183" class="comments-container"></div><div id="comment-tools-58183" class="comment-tools"></div><div class="clear"></div><div id="comment-58183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

