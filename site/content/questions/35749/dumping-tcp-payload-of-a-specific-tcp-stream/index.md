+++
type = "question"
title = "Dumping TCP Payload of a Specific TCP Stream"
description = '''I would like to create a program using python &amp;lt;2.7 to be able to dump the whole data section of a TCP packet. I have tried parsing a PDML file, which worked when the packet has a &quot;fake-field-wrapper&quot; but proved difficult when the TCP packet contained application layer data. What would be the best...'''
date = "2014-08-26T03:30:00Z"
lastmod = "2014-08-26T08:31:00Z"
weight = 35749
keywords = [ "python", "capture", "payload", "tcp", "parsing" ]
aliases = [ "/questions/35749" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Dumping TCP Payload of a Specific TCP Stream](/questions/35749/dumping-tcp-payload-of-a-specific-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35749-score" class="post-score" title="current number of votes">0</div><span id="post-35749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to create a program using python &lt;2.7 to be able to dump the whole data section of a TCP packet.</p><p>I have tried parsing a PDML file, which worked when the packet has a "fake-field-wrapper" but proved difficult when the TCP packet contained application layer data.</p><p>What would be the best capture format to parse using python to achieve this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-payload" rel="tag" title="see questions tagged &#39;payload&#39;">payload</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '14, 03:30</strong></p><img src="https://secure.gravatar.com/avatar/5f3cd9d744398542caac634e2f608a61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WireTshark&#39;s gravatar image" /><p><span>WireTshark</span><br />
<span class="score" title="5 reputation points">5</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WireTshark has no accepted answers">0%</span></p></div></div><div id="comments-container-35749" class="comments-container"></div><div id="comment-tools-35749" class="comment-tools"></div><div class="clear"></div><div id="comment-35749-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35752"></span>

<div id="answer-container-35752" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35752-score" class="post-score" title="current number of votes">2</div><span id="post-35752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="WireTshark has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What happens if you disable the application layer protocols that seem to be causing problems for you? If you're in possession of the original capture file, maybe you can try exporting the data again and then reparsing the PDML?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '14, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-35752" class="comments-container"><span id="35756"></span><div id="comment-35756" class="comment"><div id="post-35756-score" class="comment-score"></div><div class="comment-text"><p>This worked perfectly. Thank you, something relatively simple but I could not get my head around it. That's great</p></div><div id="comment-35756-info" class="comment-info"><span class="comment-age">(26 Aug '14, 08:31)</span> <span class="comment-user userinfo">WireTshark</span></div></div></div><div id="comment-tools-35752" class="comment-tools"></div><div class="clear"></div><div id="comment-35752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

