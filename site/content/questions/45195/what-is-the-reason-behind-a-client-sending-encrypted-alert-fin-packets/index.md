+++
type = "question"
title = "what is the reason behind a client sending Encrypted Alert &amp; FIN Packets?"
description = '''Hi, We are facing application disconnection issue for an Oracle Application. It is a client software based application, not a web based. From the packet capture we observed that at the time of disconnection, client sends an &quot;Encrypted Alert&quot; packet following the FIN packet.   I would like to know at...'''
date = "2015-08-18T04:18:00Z"
lastmod = "2015-08-18T04:22:00Z"
weight = 45195
keywords = [ "tls", "disconnection" ]
aliases = [ "/questions/45195" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [what is the reason behind a client sending Encrypted Alert & FIN Packets?](/questions/45195/what-is-the-reason-behind-a-client-sending-encrypted-alert-fin-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45195-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We are facing application disconnection issue for an Oracle Application. It is a client software based application, not a web based. From the packet capture we observed that at the time of disconnection, client sends an "Encrypted Alert" packet following the FIN packet.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Disconnection.png" alt="alt text" /></p><p>I would like to know at what scenario, a client sends an "Encrypted Alert" &amp; FIN Packets. It doesn't seems abnormal as it happened 100 times during a session from 8:54AM to 11:23AM, but <strong>client got disconnected only one time</strong>, around 11:15AM <strong>with the below error.</strong></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Network_Error_today_17th_Aug_-_Direct_Connection.jpg" alt="alt text" /></p><p>Hope if someone can explain it in my basic knowledge level.</p><p>Thank You.</p><p>Regards, Shanavas Abdul Rahman</p></div><div id="question-tags" class="tags-container tags">tls disconnection</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '15, 04:18</strong></p><img src="https://secure.gravatar.com/avatar/504e3d5403a6be850ec620e030a75d92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shanavaska&#39;s gravatar image" /><p>shanavaska<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shanavaska has no accepted answers">0%</span></p></img></div></div><div id="comments-container-45195" class="comments-container"><span id="45196"></span><div id="comment-45196" class="comment"><div id="post-45196-score" class="comment-score"></div><div class="comment-text"><p>Full Packet Capture at <a href="https://protect-eu.mimecast.com/redirect/eNpdjMFOxSAURP-F9bMtFAS60vgbbC6XW9ukQAPULoz_LiYujMuZOWc-WcGzsYXVDRJ8QB3Ah-sosEVIL5FgCHukVPecAjQYMEf2YCdgV96UeJ17wqu2HKlgDvSnPvfAFvFghd673Yez5EbYnugaYj9FqO337ypH37fWzrq40Y33fQ83tQKprlR-IDeGfKcjQ6hulF7IYDU9k7Jm1SoIbtGSFKCQw-rFxNVkuJmkkJN246zBchOMUJ78BLw7fkWjDbdGWW3_8zBzRGJf35ymWMI">https://protect-eu.mimecast.com/redirect/eNpdjMFOxSAURP-F9bMtFAS60vgbbC6XW9ukQAPULoz_LiYujMuZOWc-WcGzsYXVDRJ8QB3Ah-sosEVIL5FgCHukVPecAjQYMEf2YCdgV96UeJ17wqu2HKlgDvSnPvfAFvFghd673Yez5EbYnugaYj9FqO337ypH37fWzrq40Y33fQ83tQKprlR-IDeGfKcjQ6hulF7IYDU9k7Jm1SoIbtGSFKCQw-rFxNVkuJmkkJN246zBchOMUJ78BLw7fkWjDbdGWW3_8zBzRGJf35ymWMI</a></p></div><div id="comment-45196-info" class="comment-info"><span class="comment-age">(18 Aug '15, 04:22)</span> shanavaska</div></div></div><div id="comment-tools-45195" class="comment-tools"></div><div class="clear"></div><div id="comment-45195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45197"></span>

<div id="answer-container-45197" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45197-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>See the answer to <a href="https://ask.wireshark.org/questions/38050/tlsv1-record-layer-encrypted-alert">this</a> question.</p><p>Basically an "Encrypted Alert" is a TLS notification, in your case the notification is likely that the session is stopping.</p><p>See also <a href="http://blog.fourthbit.com/2014/12/23/traffic-analysis-of-an-ssl-slash-tls-session">Analysis of a TLS Session</a> for a reasonable explanation of what's happening in a TLS session from start to end.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '15, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 18 Aug '15, 04:26</p></div></div><div id="comments-container-45197" class="comments-container"><span id="45359"></span><div id="comment-45359" class="comment"><div id="post-45359-score" class="comment-score"></div><div class="comment-text"><p>Hi Graham,</p><p>Thank you for your response.</p><p>From the explanation I can understand that "Encrypted Alert" is a "Close Notify" message to initialize the closure of a SSL/TLS session. This will be sent by Server. But in our case, client is sending the "Encrypted Alert" and don't know the reason behind. Is it because of application designed to work in this way or due to some abnormal TCP behavior client is initiating SSL shutdown?</p><p>Appreciate your quick response.</p><p>Thank You.</p></div><div id="comment-45359-info" class="comment-info"><span class="comment-age">(26 Aug '15, 01:30)</span> shanavaska</div></div><span id="45361"></span><div id="comment-45361" class="comment"><div id="post-45361-score" class="comment-score"></div><div class="comment-text"><p>From the error message it would appear that the application on the client had some sort of network issue, and subsequently closed the session.</p><p>You'll need to work with the application vendor to find out more.</p></div><div id="comment-45361-info" class="comment-info"><span class="comment-age">(26 Aug '15, 02:43)</span> grahamb ♦</div></div></div><div id="comment-tools-45197" class="comment-tools"></div><div class="clear"></div><div id="comment-45197-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

