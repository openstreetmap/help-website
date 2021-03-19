+++
type = "question"
title = "Multiple packets in the same plugin"
description = '''Hi, I have an issue. I have made a plugin for a protocol names View Change Messages. It is working fine. These messages can be seen on TCP port 7002. Now in response to these view messages, view accept and view reject messages are seen which are also on TCP port 7002. So I made a plugin (separate pl...'''
date = "2011-08-03T02:19:00Z"
lastmod = "2011-08-03T03:28:00Z"
weight = 5419
keywords = [ "plugins" ]
aliases = [ "/questions/5419" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple packets in the same plugin](/questions/5419/multiple-packets-in-the-same-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5419-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have an issue. I have made a plugin for a protocol names View Change Messages. It is working fine. These messages can be seen on TCP port 7002. Now in response to these view messages, view accept and view reject messages are seen which are also on TCP port 7002. So I made a plugin (separate plugin) for view accept.</p><p>However, now since two of my plugins detect packets on TCP port 7002, only one plugins decodes packets.</p><p>So how to take care of different messages which work on top of same protocol and on the same port??</p><p>Regards, Sidharth</p></div><div id="question-tags" class="tags-container tags">plugins</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '11, 02:19</strong></p><img src="https://secure.gravatar.com/avatar/dbf35370bedfda8272cbf9e044a6cf1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sidharth&#39;s gravatar image" /><p>sidharth<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sidharth has no accepted answers">0%</span></p></div></div><div id="comments-container-5419" class="comments-container"></div><div id="comment-tools-5419" class="comment-tools"></div><div class="clear"></div><div id="comment-5419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5423"></span>

<div id="answer-container-5423" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5423-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Surely these extra messages are part of the same protocol, and your single dissector should handle all of them? Why do you think that you need a separate dissector for each message?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '11, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-5423" class="comments-container"><span id="5427"></span><div id="comment-5427" class="comment"><div id="post-5427-score" class="comment-score"></div><div class="comment-text"><p>i realize that now. But all these messages have different packet structures.!!! So how to deal with that??</p></div><div id="comment-5427-info" class="comment-info"><span class="comment-age">(03 Aug '11, 04:04)</span> sidharth</div></div><span id="5428"></span><div id="comment-5428" class="comment"><div id="post-5428-score" class="comment-score">1</div><div class="comment-text"><p>In your dissector add handlers for each message type, hopefully your protocol has some form of message type indicator in a common header that the code can use. Most dissectors obtain that value and then use a <code>switch()</code> to handle the separate cases.</p></div><div id="comment-5428-info" class="comment-info"><span class="comment-age">(03 Aug '11, 04:38)</span> grahamb ♦</div></div></div><div id="comment-tools-5423" class="comment-tools"></div><div class="clear"></div><div id="comment-5423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

