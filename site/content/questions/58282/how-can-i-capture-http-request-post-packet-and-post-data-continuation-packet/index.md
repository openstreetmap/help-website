+++
type = "question"
title = "How Can I capture http request POST packet and POST data (Continuation) packet?"
description = '''I know that http POST packet is captured by tcp[((tcp[12:1] &amp;amp; 0xf0) &amp;gt;&amp;gt; 2):4] = 0x504f5354 BPF syntax. but, this syntax has a problem.  If the size of the http POST packet is large, the POST data is divided and transmitted.  (Info column has Continuation in the packet)  At that time, Wiresh...'''
date = "2016-12-21T17:05:00Z"
lastmod = "2016-12-22T00:41:00Z"
weight = 58282
keywords = [ "body", "http", "post", "request", "data" ]
aliases = [ "/questions/58282" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How Can I capture http request POST packet and POST data (Continuation) packet?](/questions/58282/how-can-i-capture-http-request-post-packet-and-post-data-continuation-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58282-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know that http POST packet is captured by <strong>tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x504f5354</strong> BPF syntax.</p><p>but, this syntax has a problem.</p><p>If the size of the http POST packet is large, the POST data is divided and transmitted. (Info column has Continuation in the packet)</p><p>At that time, Wireshark does not collect the divided packets.</p><p>How do I collect these separate http POST packets?</p><p>Which BPF filter should I use?</p></div><div id="question-tags" class="tags-container tags">body http post request data</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Dec '16, 17:05</strong></p><img src="https://secure.gravatar.com/avatar/d1212e2780b71f55779158446d700dbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cds0915&#39;s gravatar image" /><p>cds0915<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cds0915 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Dec '16, 23:49</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-58282" class="comments-container"></div><div id="comment-tools-58282" class="comment-tools"></div><div class="clear"></div><div id="comment-58282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58289"></span>

<div id="answer-container-58289" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58289-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think it's possible to apply capture filters that have to use dependencies on other packets. In your case you'd need something that captures frames that are follow-up frames of a POST frame. As far as I know there's no way to keep track of something like this during capture.</p><p>The only way to get it all is to capture HTTP completely I'm afraid.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '16, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-58289" class="comments-container"><span id="58293"></span><div id="comment-58293" class="comment"><div id="post-58293-score" class="comment-score"></div><div class="comment-text"><p>Filters (whether capture or display) can only operate on a single packet at a time, they decide whether the packet is in our out.</p><p>There is no "memory" of packets that have gone before.</p></div><div id="comment-58293-info" class="comment-info"><span class="comment-age">(22 Dec '16, 01:06)</span> grahamb ♦</div></div></div><div id="comment-tools-58289" class="comment-tools"></div><div class="clear"></div><div id="comment-58289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

