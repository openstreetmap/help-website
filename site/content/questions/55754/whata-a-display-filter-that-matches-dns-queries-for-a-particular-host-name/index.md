+++
type = "question"
title = "What&#x27;a a display filter that matches DNS queries for a particular host name?"
description = '''Hi,  If I want to filter for DNS queues sent by my machine to ANY DNS server for www.petenetlive.com what is the filter for that? Ive been searching google of 35 minutes. Why is that so hard to find :-/ Pete'''
date = "2016-09-22T07:43:00Z"
lastmod = "2016-09-22T08:01:00Z"
weight = 55754
keywords = [ "filter", "dns" ]
aliases = [ "/questions/55754" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What'a a display filter that matches DNS queries for a particular host name?](/questions/55754/whata-a-display-filter-that-matches-dns-queries-for-a-particular-host-name)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55754-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>If I want to filter for DNS queues sent by my machine to ANY DNS server for www.petenetlive.com what is the filter for that? Ive been searching google of 35 minutes. Why is that so hard to find :-/</p><p>Pete</p></div><div id="question-tags" class="tags-container tags">filter dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '16, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/4c300f2df527aceec0bd396e4c812fed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pete%20Long&#39;s gravatar image" /><p>Pete Long<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pete Long has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Sep '16, 12:31</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-55754" class="comments-container"></div><div id="comment-tools-55754" class="comment-tools"></div><div class="clear"></div><div id="comment-55754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55755"></span>

<div id="answer-container-55755" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55755-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The filter for that is <code>dns.qry.name == "www.petenetlive.com"</code>.</p><p>If you take any DNS query packet you happen to find (use just <code>dns</code> as a display filter first), and click through the packet dissection down to the "Name" item inside the "Query", you can right-click the line with the name and choose the <code>Apply as Filter -&gt; Selected</code> option. Then, you would change the name in the display filter field from the original one to "www.petenetlive.com" which you really want.</p><p>Why is it hard - because the generic question is "how do I filter for field X of protocol Y" and there are hundreds of protocols with hundreds of fields each. So there is no chance to have a tutorial for each, so finding a packet of the protocol you want and localizing the field of interest inside it is the most efficient way.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '16, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-55755" class="comments-container"><span id="55757"></span><div id="comment-55757" class="comment"><div id="post-55757-score" class="comment-score"></div><div class="comment-text"><p>Perfect, just what I needed</p><p>Regards</p><p>Pete</p></div><div id="comment-55757-info" class="comment-info"><span class="comment-age">(22 Sep '16, 08:08)</span> Pete Long</div></div></div><div id="comment-tools-55755" class="comment-tools"></div><div class="clear"></div><div id="comment-55755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

