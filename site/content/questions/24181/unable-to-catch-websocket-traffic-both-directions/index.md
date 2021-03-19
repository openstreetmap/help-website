+++
type = "question"
title = "Unable to catch websocket traffic (both directions)"
description = '''Hello, I have a computer A:  - 192.168.0.1 (physical laptop)  - Glassfish server (websocket endpoint)   - Wireshark  and a computer B:  - VM inside Virtualbox, which A runs (network = bridged)  - 192.168.0.2 Now, when I try to catch websocket traffic (B opens a browser, connects to endpoint A and se...'''
date = "2013-08-29T22:39:00Z"
lastmod = "2013-08-30T02:15:00Z"
weight = 24181
keywords = [ "filter", "traffic", "websocket" ]
aliases = [ "/questions/24181" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Unable to catch websocket traffic (both directions)](/questions/24181/unable-to-catch-websocket-traffic-both-directions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24181-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a computer A:<br />
- 192.168.0.1 (physical laptop)<br />
- Glassfish server (websocket endpoint)<br />
- Wireshark<br />
</p><p>and a computer B:<br />
- VM inside Virtualbox, which A runs (network = bridged)<br />
- 192.168.0.2<br />
</p><p>Now, when I try to catch websocket traffic (B opens a browser, connects to endpoint A and sends text using JS. Server replies with some text), I can only see ws-traffic from A to B. However my glassfish server outputs the text that B sends, so it (A to B) must go along the 'wire' also.</p><p>Is there something wrong how I filter the traffic? I use ip-filter with value 192.168.0.2. It seems to catch tcp handshake ok and other traffic as well. But I can only see tcp from B to A and not websocket. Any ideas?</p><p>thanks, E<br />
</p></div><div id="question-tags" class="tags-container tags">filter traffic websocket</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '13, 22:39</strong></p><img src="https://secure.gravatar.com/avatar/30812c676e3ed3809e718b4ad8cedd6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ezte123&#39;s gravatar image" /><p>ezte123<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ezte123 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-24181" class="comments-container"></div><div id="comment-tools-24181" class="comment-tools"></div><div class="clear"></div><div id="comment-24181-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24189"></span>

<div id="answer-container-24189" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24189-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>VM inside Virtualbox,</p></blockquote><p>There have been other reports about problems with capturing data on <strong>bridged Virtualbox interfaces</strong>.</p><blockquote><p><a href="https://www.google.com/?q=site:ask.wireshark.org+virtualbox+bridge">https://www.google.com/?q=site:ask.wireshark.org+virtualbox+bridge</a></p></blockquote><p>Please run Wireshark in the virtual machine and capture the whole traffic there. That seems to work well.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '13, 02:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Aug '13, 02:16</p></div></div><div id="comments-container-24189" class="comments-container"><span id="24200"></span><div id="comment-24200" class="comment"><div id="post-24200-score" class="comment-score"></div><div class="comment-text"><p>Ok thanks, I'll try that.</p></div><div id="comment-24200-info" class="comment-info"><span class="comment-age">(30 Aug '13, 08:02)</span> ezte123</div></div></div><div id="comment-tools-24189" class="comment-tools"></div><div class="clear"></div><div id="comment-24189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

