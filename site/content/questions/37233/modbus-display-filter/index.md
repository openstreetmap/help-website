+++
type = "question"
title = "Modbus display filter"
description = '''When working on a bug in a modbus server implementation I nodiced that when the modbus display filter cannot decode the packet (due to a protocol error in the message) the remaining data is printed like: &#x27;Data: 0113feb0800000010000047b&#x27; However it is not made clear to me that this packet is actually...'''
date = "2014-10-21T05:29:00Z"
lastmod = "2014-10-21T08:00:00Z"
weight = 37233
keywords = [ "modbus", "display-filter" ]
aliases = [ "/questions/37233" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Modbus display filter](/questions/37233/modbus-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37233-score" class="post-score" title="current number of votes">0</div><span id="post-37233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When working on a bug in a modbus server implementation I nodiced that when the modbus display filter cannot decode the packet (due to a protocol error in the message) the remaining data is printed like:<br />
'Data: 0113feb0800000010000047b'</p><p>However it is not made clear to me that this packet is actually erroneous.</p><p>After solving the bug (the server was responding with more bytes than the client asked for) the modbus message was further decoded like:<br />
Register (0): 276<br />
Register (0): 65198<br />
Register (0): 32768<br />
</p><p>Wouldn't it be a good idea to use the display filter to mark packets with (clear) protocol errors?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-modbus" rel="tag" title="see questions tagged &#39;modbus&#39;">modbus</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '14, 05:29</strong></p><img src="https://secure.gravatar.com/avatar/2f668f5e18cf5b2dc4d4e221a3a9359d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kneh&#39;s gravatar image" /><p><span>kneh</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kneh has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-37233" class="comments-container"></div><div id="comment-tools-37233" class="comment-tools"></div><div class="clear"></div><div id="comment-37233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37241"></span>

<div id="answer-container-37241" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37241-score" class="post-score" title="current number of votes">1</div><span id="post-37241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Because there are proprietary (unpublished) extensions to the Modbus protocol, if the dissector comes across a function code it can't handle, then the dissector just calls the generic "data" dissector that generates the display you saw.</p><p>So with this dissector its a bit hard to definitively spot a protocol error.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '14, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></br></p></div></div><div id="comments-container-37241" class="comments-container"></div><div id="comment-tools-37241" class="comment-tools"></div><div class="clear"></div><div id="comment-37241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

