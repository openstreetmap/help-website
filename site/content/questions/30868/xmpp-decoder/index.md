+++
type = "question"
title = "XMPP decoder"
description = '''Hi! Please, help me!!! I can&#x27;t decode XMPP packets. It&#x27;s possible with wireshark? Thanks'''
date = "2014-03-16T19:43:00Z"
lastmod = "2014-03-16T20:04:00Z"
weight = 30868
keywords = [ "xmpp" ]
aliases = [ "/questions/30868" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [XMPP decoder](/questions/30868/xmpp-decoder)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30868-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi! Please, help me!!! I can't decode XMPP packets. It's possible with wireshark? Thanks</p></div><div id="question-tags" class="tags-container tags">xmpp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '14, 19:43</strong></p><img src="https://secure.gravatar.com/avatar/5a25948a102271ca98e2bc682d0917d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nataap&#39;s gravatar image" /><p>nataap<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nataap has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Mar '14, 20:01</p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-30868" class="comments-container"></div><div id="comment-tools-30868" class="comment-tools"></div><div class="clear"></div><div id="comment-30868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30869"></span>

<div id="answer-container-30869" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30869-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, it decodes XMPP. It assumes the TCP port for it is 5222, so if your server is using a different port you'll need to tell wireshark to decode your particular TCP packets as XMPP by using the "Decode As" feature (either through the Analyze menu, or by right-clicking one of the packets you want it to decode as XMPP). And of course if your XMPP communication is over encrypted SSL/TLS, then wireshark can't decode that unless you give it the key info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '14, 20:04</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30869" class="comments-container"><span id="30892"></span><div id="comment-30892" class="comment"><div id="post-30892-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much! I deactivated SSL/TLS on the OpenFire server and now i can see text of messages!</p></div><div id="comment-30892-info" class="comment-info"><span class="comment-age">(17 Mar '14, 09:44)</span> nataap</div></div><span id="37322"></span><div id="comment-37322" class="comment"><div id="post-37322-score" class="comment-score"></div><div class="comment-text"><p>Where can I the key my client (pidgin) is using? It's likely to be <a href="https://www.bock.nu/blog/decrypting-tls-with-wireshark">impossible</a>: <code>Unfortunately, this feature can only decrypt traffic that is transport-layer-encryted. If you have any traffic where encryption is implemented in the protocol itself (usually called "STARTTLS"), as with most SMTP or XMPP (Jabber) services, you can not decrypt the traffic like this at the moment.</code></p></div><div id="comment-37322-info" class="comment-info"><span class="comment-age">(23 Oct '14, 16:03)</span> x-yuri</div></div></div><div id="comment-tools-30869" class="comment-tools"></div><div class="clear"></div><div id="comment-30869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

