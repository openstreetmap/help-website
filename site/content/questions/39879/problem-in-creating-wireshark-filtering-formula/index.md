+++
type = "question"
title = "problem in creating wireshark filtering formula"
description = '''I am stuck at creating wireshark filter to remove all these from showing up. The current filter that I have is below, and i no idea how to further enhance it. http.request.method == &quot;POST&quot; || http.request.method == &quot;PUT&quot; || http.request.method == &quot;GET&quot; How to filter out these?   a. TCP Retransmissio...'''
date = "2015-02-15T23:35:00Z"
lastmod = "2015-02-16T06:08:00Z"
weight = 39879
keywords = [ "filter", "capture", "wireshark" ]
aliases = [ "/questions/39879" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [problem in creating wireshark filtering formula](/questions/39879/problem-in-creating-wireshark-filtering-formula)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39879-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am stuck at creating wireshark filter to remove all these from showing up.</p><p>The current filter that I have is below, and i no idea how to further enhance it.</p><p>http.request.method == "POST" || http.request.method == "PUT" || http.request.method == "GET"</p><p>How to filter out these?</p><pre><code>  a. TCP Retransmission  
  b. TCP Spurious Retransmission  
  c. TCP Out-of-Order  
  d. with content ending IGD.xml  
  e. GET / HTTP/1.0 without query string url.  
</code></pre><p>Photo attached.</p><p><img src="http://s9.postimg.org/sier6l88f/aaa.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">filter capture wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '15, 23:35</strong></p><img src="https://secure.gravatar.com/avatar/0d97beabda7e8d8fb96270f60d829058?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packetguy&#39;s gravatar image" /><p>packetguy<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packetguy has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 16 Feb '15, 06:08</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-39879" class="comments-container"></div><div id="comment-tools-39879" class="comment-tools"></div><div class="clear"></div><div id="comment-39879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39886"></span>

<div id="answer-container-39886" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39886-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try this:</p><blockquote><p>http.request and not (tcp.analysis.flags or http contains "GET / HTTP/1" or http contains "IGD.xml HTTP/1")</p></blockquote><p><strong>http.request</strong> (without method) because you listed the most common requests anyway.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '15, 06:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-39886" class="comments-container"></div><div id="comment-tools-39886" class="comment-tools"></div><div class="clear"></div><div id="comment-39886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

