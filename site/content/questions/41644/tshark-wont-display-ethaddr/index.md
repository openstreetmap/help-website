+++
type = "question"
title = "tshark won&#x27;t display eth.addr"
description = '''Here&#x27;s my command: tshark -i iface -o wlan.enable_decryption:TRUE -2 -R ip -T fields -e eth.dst -e ip.src -e ip.len  Actually the -R is &quot;ip &amp;amp;&amp;amp; !ip == 192.168.0.0/24&quot; but the code display here seems bent on replacing &#x27;&amp;amp;&#x27; with html entities. Anyway, I have WPA credentials in ~/.wireshark/8...'''
date = "2015-04-21T12:40:00Z"
lastmod = "2015-04-21T14:00:00Z"
weight = 41644
keywords = [ "eth.addr", "wlan", "tshark" ]
aliases = [ "/questions/41644" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [tshark won't display eth.addr](/questions/41644/tshark-wont-display-ethaddr)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41644-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Here's my command:</p><pre><code>tshark -i iface -o wlan.enable_decryption:TRUE -2 -R ip -T fields -e eth.dst -e ip.src -e ip.len</code></pre><p>Actually the -R is "ip &amp;&amp; !ip == 192.168.0.0/24" but the code display here seems bent on replacing '&amp;' with html entities.</p><p>Anyway, I have WPA credentials in <code>~/.wireshark/80211_keys</code> and this works for nodes that subsequently connect to the network, but the first field (<code>eth.dst</code>) is always blank. I've also tried <code>eth.addr</code>, same thing.</p><p>How can I get what I want here, namely, the destination MAC address, the IP source address, and the packet length?</p></div><div id="question-tags" class="tags-container tags">eth.addr wlan tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '15, 12:40</strong></p><img src="https://secure.gravatar.com/avatar/abf01b6006996f947014ff671ba4151b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mk27&#39;s gravatar image" /><p>mk27<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mk27 has no accepted answers">0%</span></p></div></div><div id="comments-container-41644" class="comments-container"></div><div id="comment-tools-41644" class="comment-tools"></div><div class="clear"></div><div id="comment-41644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41645"></span>

<div id="answer-container-41645" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41645-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but the first field (eth.dst) is always blank. I've also tried eth.addr, same thing.</p></blockquote><p>which is totally normal, if you are looking at wifi/wlan traffic, as it does not have an <strong>ethernet header</strong>.</p><p>Please try one of the following fields:</p><blockquote><p>-e wlan.addr -e wlan.ra -e wlan.sa -e wlan.ta -e wlan.da</p></blockquote><p>For more details, please check the following link:</p><blockquote><p><a href="https://www.wireshark.org/docs/dfref/w/wlan.html">https://www.wireshark.org/docs/dfref/w/wlan.html</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '15, 14:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-41645" class="comments-container"></div><div id="comment-tools-41645" class="comment-tools"></div><div class="clear"></div><div id="comment-41645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

