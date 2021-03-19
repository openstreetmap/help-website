+++
type = "question"
title = "what is the purpose of tcp.pdu.size filter"
description = '''I am working with pdml format. I am trying to determine the octets of a frame using the nodes of a frame in pdml (field, proto). sometimes there is a field (filter) called tcp.pdu.size which value is the octets of the payload. Why this filed is not presented always if tcp contains any upper layer pr...'''
date = "2013-08-20T02:34:00Z"
lastmod = "2013-08-21T08:20:00Z"
weight = 23868
keywords = [ "pdml", "tcp", "display-filter" ]
aliases = [ "/questions/23868" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [what is the purpose of tcp.pdu.size filter](/questions/23868/what-is-the-purpose-of-tcppdusize-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23868-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am working with pdml format. I am trying to determine the octets of a frame using the nodes of a frame in pdml (field, proto). sometimes there is a field (filter) called tcp.pdu.size which value is the octets of the payload. Why this filed is not presented always if tcp contains any upper layer protocol? for example if tcp contains http, then tcp.pdu.size not presented, but in case of diameter it is. why does not this node have a hidden attribute?</p><pre><code>&lt;field name=&quot;tcp.pdu.size&quot; showname=&quot;PDU Size: 96&quot; size=&quot;96&quot; pos=&quot;70&quot; show=&quot;96&quot;   value=&quot;010000600000011800000000506af74f48c2f57d0000010c4000000c000007d10000010840000022696d7361735858582e696d7361732e6572696373736f6e2e736500000000012840000019696d7361732e6572696373736f6e2e7365000000&quot;/&gt;</code></pre></div><div id="question-tags" class="tags-container tags">pdml tcp display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '13, 02:34</strong></p><img src="https://secure.gravatar.com/avatar/0c7332e9fdd92b1e99d905c07ab4bdc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HiB&#39;s gravatar image" /><p>HiB<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HiB has no accepted answers">0%</span></p></div></div><div id="comments-container-23868" class="comments-container"></div><div id="comment-tools-23868" class="comment-tools"></div><div class="clear"></div><div id="comment-23868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23908"></span>

<div id="answer-container-23908" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23908-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The field is populated if the protocol runing atop of TCP uses tcp_dissect_pdus() metod of doing reassembly (see readme.dissectors 2.7 and 2.7.1). The field isn't hidden as it wouldn't be visible in the GUI if it was and use of hidden fields are generaly discurraged as you would have to know about them to be able to use them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '13, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-23908" class="comments-container"><span id="23912"></span><div id="comment-23912" class="comment"><div id="post-23912-score" class="comment-score"></div><div class="comment-text"><p>Thanks! then I need to find another way to able to determine the octets of a packet (I am struggling with padding octets)</p></div><div id="comment-23912-info" class="comment-info"><span class="comment-age">(21 Aug '13, 08:41)</span> HiB</div></div></div><div id="comment-tools-23908" class="comment-tools"></div><div class="clear"></div><div id="comment-23908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

