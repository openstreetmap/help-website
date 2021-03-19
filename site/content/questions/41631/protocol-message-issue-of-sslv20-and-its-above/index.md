+++
type = "question"
title = "Protocol message issue of SSLv2.0 and its above"
description = '''Dear all, When I click &quot;SSLv2&quot; item only in browser configuration page and the protocol label of client_hello shows as &quot;SSLv2&quot; such as attache file, sslv2i.jpg But when I change another protocol above SSLv2(e.g. SSLv3, TLSv1.0, TLSv1.1, and TLSv1.2 respectively), how come the protocol label always s...'''
date = "2015-04-21T06:41:00Z"
lastmod = "2015-04-22T03:47:00Z"
weight = 41631
keywords = [ "3202" ]
aliases = [ "/questions/41631" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Protocol message issue of SSLv2.0 and its above](/questions/41631/protocol-message-issue-of-sslv20-and-its-above)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41631-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear all,</p><p>When I click "SSLv2" item only in browser configuration page and the protocol label of client_hello shows as "SSLv2" such as attache file, sslv2i.jpg But when I change another protocol above SSLv2(e.g. SSLv3, TLSv1.0, TLSv1.1, and TLSv1.2 respectively), how come the protocol label always shows as "SSL" even if the version field of packet shows the correct real version such as attached file, tls1.0i.jpg?</p><p>Thanks in advance for your help.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/sslv2i.jpg" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/tls1.0i.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">3202</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '15, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/a7a151378898a3991d1e91899fada3ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Donald&#39;s gravatar image" /><p>Donald<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Donald has no accepted answers">0%</span></p></img></div></div><div id="comments-container-41631" class="comments-container"><span id="41635"></span><div id="comment-41635" class="comment"><div id="post-41635-score" class="comment-score"></div><div class="comment-text"><p>What is your OS and which version and what is your Wireshark version?</p></div><div id="comment-41635-info" class="comment-info"><span class="comment-age">(21 Apr '15, 07:35)</span> Jaap ♦</div></div><span id="41652"></span><div id="comment-41652" class="comment"><div id="post-41652-score" class="comment-score"></div><div class="comment-text"><p>My OS is Win7 and Wireshark version is 1.1.3, thanks.</p></div><div id="comment-41652-info" class="comment-info"><span class="comment-age">(21 Apr '15, 19:01)</span> Donald</div></div><span id="41655"></span><div id="comment-41655" class="comment"><div id="post-41655-score" class="comment-score"></div><div class="comment-text"><p>Wireshark 1.1.3? I kinda doubt that.</p></div><div id="comment-41655-info" class="comment-info"><span class="comment-age">(21 Apr '15, 23:28)</span> Jaap ♦</div></div></div><div id="comment-tools-41631" class="comment-tools"></div><div class="clear"></div><div id="comment-41631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41670"></span>

<div id="answer-container-41670" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41670-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See my answer to a very similar question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/15995/ssl-dissector-tlsv1-versus-ssl">https://ask.wireshark.org/questions/15995/ssl-dissector-tlsv1-versus-ssl</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '15, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div></div><div id="comments-container-41670" class="comments-container"></div><div id="comment-tools-41670" class="comment-tools"></div><div class="clear"></div><div id="comment-41670-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

