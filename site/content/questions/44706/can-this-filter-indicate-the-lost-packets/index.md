+++
type = "question"
title = "[closed] can this filter indicate the lost packets?"
description = '''I guess using a filter like: tcp.analysis.lost_segment &amp;amp;&amp;amp; tcp.analysis.ack_lost_segment could display the packets that are not in the capture file nor in the wire. The receiver doesn&#x27;t have them at all. '''
date = "2015-07-31T11:44:00Z"
lastmod = "2015-07-31T16:34:00Z"
weight = 44706
keywords = [ "filter", "packets", "lost", "wireshark" ]
aliases = [ "/questions/44706" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] can this filter indicate the lost packets?](/questions/44706/can-this-filter-indicate-the-lost-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44706-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I guess using a filter like: tcp.analysis.lost_segment &amp;&amp; tcp.analysis.ack_lost_segment could display the packets that are not in the capture file nor in the wire. The receiver doesn't have them at all.</p></div><div id="question-tags" class="tags-container tags">filter packets lost wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '15, 11:44</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p>flora<br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>closed 04 Aug '15, 06:55</p></div></div><div id="comments-container-44706" class="comments-container"></div><div id="comment-tools-44706" class="comment-tools"></div><div class="clear"></div><div id="comment-44706-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question" by flora 04 Aug '15, 06:55

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44713"></span>

<div id="answer-container-44713" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44713-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Easily said no. But this can indicate missing packets:<br />
</p><pre><code>tcp.analysis.lost_segment or tcp.analysis.ack_lost_segment</code></pre><p><strong>tcp.analysis.lost_segment</strong> is telling you just that the frame is not in capture file. One probably reason can be indeed that the frame was not on the wire at the capture point another reason can be for example that the frame was not captured correctly.</p><p><strong>tcp.analysis.ack_lost_segment</strong> is telling you that the corresponding segment is not in the tracefile but the correct answer for the missing segment is in the tracefile. The most likely reason for that is that the endpoint has seen the missing segment and acknowledged it correctly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '15, 16:34</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></p></div></div><div id="comments-container-44713" class="comments-container"></div><div id="comment-tools-44713" class="comment-tools"></div><div class="clear"></div><div id="comment-44713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

