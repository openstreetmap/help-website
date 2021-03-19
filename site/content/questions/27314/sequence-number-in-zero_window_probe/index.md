+++
type = "question"
title = "sequence number in zero_window_probe"
description = '''Hello, need to have some experts look at this trace snippet showing a server sending a zero-window and the client sending probes with a 1 byte &#x27;garbage&#x27;.  I wonder whether the client sends a &#x27;correct&#x27; tcp.seq in its probes.  Here&#x27;s the trace: zero_window_probe.pcapng '''
date = "2013-11-24T10:01:00Z"
lastmod = "2013-11-25T08:17:00Z"
weight = 27314
keywords = [ "sequencenumber", "zero-window", "tcp", "garbage", "zerowindowprobe" ]
aliases = [ "/questions/27314" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [sequence number in zero\_window\_probe](/questions/27314/sequence-number-in-zero_window_probe)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27314-score" class="post-score" title="current number of votes">0</div><span id="post-27314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, need to have some experts look at this trace snippet showing a server sending a zero-window and the client sending probes with a 1 byte 'garbage'.</p><p>I wonder whether the client sends a 'correct' tcp.seq in its probes.</p><p>Here's the trace: <a href="http://cloudshark.org/captures/732cc9bc8d24">zero_window_probe.pcapng</a> <img src="https://osqa-ask.wireshark.org/upfiles/zero_window_probe.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sequencenumber" rel="tag" title="see questions tagged &#39;sequencenumber&#39;">sequencenumber</span> <span class="post-tag tag-link-zero-window" rel="tag" title="see questions tagged &#39;zero-window&#39;">zero-window</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-garbage" rel="tag" title="see questions tagged &#39;garbage&#39;">garbage</span> <span class="post-tag tag-link-zerowindowprobe" rel="tag" title="see questions tagged &#39;zerowindowprobe&#39;">zerowindowprobe</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '13, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-27314" class="comments-container"></div><div id="comment-tools-27314" class="comment-tools"></div><div class="clear"></div><div id="comment-27314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27316"></span>

<div id="answer-container-27316" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27316-score" class="post-score" title="current number of votes">1</div><span id="post-27316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mrEEde has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks pretty normal to me. Some operating systems use the last byte already acknowledged for Window probes (which would be a real "garbage byte"), others use the next byte to come for the same purpose.</p><p>This one seems to use the "next in line" byte to probe the window. Nothing unusual here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '13, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-27316" class="comments-container"><span id="27355"></span><div id="comment-27355" class="comment"><div id="post-27355-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your comment!</p></div><div id="comment-27355-info" class="comment-info"><span class="comment-age">(25 Nov '13, 08:17)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-27316" class="comment-tools"></div><div class="clear"></div><div id="comment-27316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

