+++
type = "question"
title = "autostop based on time least packet received?"
description = '''Hi, I&#x27;ve been reading the docs here:  https://www.wireshark.org/docs/man-pages/tshark.html trying to find a way to stop a capture if no packet has been received for at least X seconds I know I can put an absolute timeout in place using the &quot;-a duration&quot; flags...but ideally I would be able to run:  t...'''
date = "2016-10-25T10:11:00Z"
lastmod = "2016-10-25T15:38:00Z"
weight = 56652
keywords = [ "autostop", "timeout" ]
aliases = [ "/questions/56652" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [autostop based on time least packet received?](/questions/56652/autostop-based-on-time-least-packet-received)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56652-score" class="post-score" title="current number of votes">0</div><span id="post-56652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I've been reading the docs here:</p><p><a href="https://www.wireshark.org/docs/man-pages/tshark.html">https://www.wireshark.org/docs/man-pages/tshark.html</a></p><p>trying to find a way to stop a capture if no packet has been received for at least X seconds</p><p>I know I can put an absolute timeout in place using the "-a duration" flags...but ideally I would be able to run:</p><p>tshark host &lt;source_ip&gt; -w dump.pcap</p><p>Such that the capture stopped when no traffic from that source IP had been received for X seconds. Any ideas....?<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-autostop" rel="tag" title="see questions tagged &#39;autostop&#39;">autostop</span> <span class="post-tag tag-link-timeout" rel="tag" title="see questions tagged &#39;timeout&#39;">timeout</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '16, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/ed56b38042032c7d46130c321dbcbd7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dbrb2&#39;s gravatar image" /><p><span>dbrb2</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dbrb2 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-56652" class="comments-container"><span id="56655"></span><div id="comment-56655" class="comment"><div id="post-56655-score" class="comment-score"></div><div class="comment-text"><p>Just wondering, what's the use case?</p></div><div id="comment-56655-info" class="comment-info"><span class="comment-age">(25 Oct '16, 11:09)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="56662"></span><div id="comment-56662" class="comment"><div id="post-56662-score" class="comment-score"></div><div class="comment-text"><p>I'm checking comms on a number of video streams. I can start each stream, and tshark, in parallel - but the stream may take a few seconds to join - so Ineed to capture with tshark for long enough to get a representative sample of packets, but not so long I'm wasting time...</p></div><div id="comment-56662-info" class="comment-info"><span class="comment-age">(25 Oct '16, 15:38)</span> <span class="comment-user userinfo">dbrb2</span></div></div><span id="56663"></span><div id="comment-56663" class="comment"><div id="post-56663-score" class="comment-score"></div><div class="comment-text"><p>I think I will do this by combining packet count with duration...</p></div><div id="comment-56663-info" class="comment-info"><span class="comment-age">(25 Oct '16, 15:38)</span> <span class="comment-user userinfo">dbrb2</span></div></div></div><div id="comment-tools-56652" class="comment-tools"></div><div class="clear"></div><div id="comment-56652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56653"></span>

<div id="answer-container-56653" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56653-score" class="post-score" title="current number of votes">0</div><span id="post-56653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately that's not currently supported.</p><p>You could raise an enhancement request on the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a> (if there isn't a similar one already).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '16, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-56653" class="comments-container"><span id="56654"></span><div id="comment-56654" class="comment"><div id="post-56654-score" class="comment-score"></div><div class="comment-text"><p>I might do that, thanks</p><p>Another option - not quite the same, but in my case with a similar outcome, would be to combine a packet limit -c with a duration</p><p>That would presumably quit either when X matching packets were received, or when the duration was hit, whichever came first...</p></div><div id="comment-56654-info" class="comment-info"><span class="comment-age">(25 Oct '16, 11:02)</span> <span class="comment-user userinfo">dbrb2</span></div></div></div><div id="comment-tools-56653" class="comment-tools"></div><div class="clear"></div><div id="comment-56653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

