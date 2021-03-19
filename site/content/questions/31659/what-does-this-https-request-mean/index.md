+++
type = "question"
title = "What does this HTTPS request mean?"
description = '''When I make an HTTPS request (for example, GET https://http2katanatest.cloudapp.net:8443/root/index.html, I capture the following data on wireshark: 16 03 01 00 ef 01 00 00 eb 03 03 30 84 c4 29 f2 20 c6 80 97 91 89 c1 78 ... What is this? This does not seem like HEADER frames. Is it compressed data?...'''
date = "2014-04-08T23:08:00Z"
lastmod = "2014-04-09T01:08:00Z"
weight = 31659
keywords = [ "https" ]
aliases = [ "/questions/31659" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What does this HTTPS request mean?](/questions/31659/what-does-this-https-request-mean)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31659-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I make an HTTPS request (for example, GET <a href="https://http2katanatest.cloudapp.net:8443/root/index.html,">https://http2katanatest.cloudapp.net:8443/root/index.html,</a> I capture the following data on wireshark:</p><p>16 03 01 00 ef 01 00 00 eb 03 03 30 84 c4 29 f2 20 c6 80 97 91 89 c1 78 ...</p><p>What is this? This does not seem like HEADER frames. Is it compressed data?</p></div><div id="question-tags" class="tags-container tags">https</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '14, 23:08</strong></p><img src="https://secure.gravatar.com/avatar/2a56bba405cf39f0c9c108ad57156ade?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sufi&#39;s gravatar image" /><p>sufi<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sufi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Apr '14, 13:47</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-31659" class="comments-container"></div><div id="comment-tools-31659" class="comment-tools"></div><div class="clear"></div><div id="comment-31659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31662"></span>

<div id="answer-container-31662" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31662-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That is a SSL Handshake Client Hello</p><p>Use the Decode As Function to tell wireshark to interpret those as SSL</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '14, 01:08</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-31662" class="comments-container"><span id="31686"></span><div id="comment-31686" class="comment"><div id="post-31686-score" class="comment-score"></div><div class="comment-text"><p>Or add port 8443 to the list of SSL ports</p><blockquote><p>Edit -&gt; Preferences -&gt; Protocols -&gt; HTTP -&gt; SSL/TLS ports</p></blockquote><p>Add 8443 to that list, like this: 443,8443</p></div><div id="comment-31686-info" class="comment-info"><span class="comment-age">(09 Apr '14, 13:45)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-31662" class="comment-tools"></div><div class="clear"></div><div id="comment-31662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

