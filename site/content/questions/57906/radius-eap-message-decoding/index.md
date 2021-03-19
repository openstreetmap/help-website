+++
type = "question"
title = "radius eap message decoding"
description = '''I have server sertificate and key. I made dump. Key installed in wireshark preferences. I see Secure Socket Layer, TLS, Sertificates, but Encrypted Application Data still encrypted. &#x27;Follow SSL&#x27; stream not works : tcp.stream eq 4369 in filter is wrong - radius uses udp. How to extract and decode EAP...'''
date = "2016-12-06T07:48:00Z"
lastmod = "2016-12-08T03:05:00Z"
weight = 57906
keywords = [ "eap", "eap-peap", "radius", "ssl", "ssl_decrypt" ]
aliases = [ "/questions/57906" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [radius eap message decoding](/questions/57906/radius-eap-message-decoding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57906-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have server sertificate and key. I made dump. Key installed in wireshark preferences.</p><p>I see Secure Socket Layer, TLS, Sertificates, but Encrypted Application Data still encrypted.</p><p>'Follow SSL' stream not works : <code>tcp.stream eq 4369</code> in filter is wrong - radius uses udp.</p><p>How to extract and decode EAP messages?</p></div><div id="question-tags" class="tags-container tags">eap eap-peap radius ssl ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '16, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/7eaafb57af2725f3efbe529861bab43a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eri&#39;s gravatar image" /><p>eri<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eri has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Dec '16, 07:49</p></div></div><div id="comments-container-57906" class="comments-container"></div><div id="comment-tools-57906" class="comment-tools"></div><div class="clear"></div><div id="comment-57906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="57909"></span>

<div id="answer-container-57909" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57909-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I couldn't get this to work either, maybe someone can point us in the right direction. Until then, here are some links:</p><p><a href="https://wiki.freeradius.org/guide/stats-with-radsniff">https://wiki.freeradius.org/guide/stats-with-radsniff</a> <a href="https://supportforums.cisco.com/blog/154046">https://supportforums.cisco.com/blog/154046</a> <a href="http://security.stackexchange.com/questions/70981/decoding-tunnel-bytes-in-eap-tls-or-eap-ttls-using-wireshark">http://security.stackexchange.com/questions/70981/decoding-tunnel-bytes-in-eap-tls-or-eap-ttls-using-wireshark</a></p><p>I use radsniff now to get at the primary master keys for 802.11/WPA2 when using Enterprise authentication. It doesn't directly address what you wanted, decryption of the TLS tunnel, but it provides what I needed so maybe you would get lucky too. The Cisco link walks through a way to decrypt the tunnel in Radius packets, assuming you are not using DH.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '16, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></p></div></div><div id="comments-container-57909" class="comments-container"></div><div id="comment-tools-57909" class="comment-tools"></div><div class="clear"></div><div id="comment-57909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57954"></span>

<div id="answer-container-57954" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57954-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="https://supportforums.cisco.com/blog/154046">https://supportforums.cisco.com/blog/154046</a> very useful</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '16, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/7eaafb57af2725f3efbe529861bab43a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eri&#39;s gravatar image" /><p>eri<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eri has no accepted answers">0%</span></p></div></div><div id="comments-container-57954" class="comments-container"></div><div id="comment-tools-57954" class="comment-tools"></div><div class="clear"></div><div id="comment-57954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

