+++
type = "question"
title = "how to capture the traffic of devices interacting in our network"
description = '''using ethernet on my laptop (192.168.1.23), which is installed wireshare, would like to capture the traffic from ip camera (192.168.1.63) to network vdieo recorder (192.168.1.245). i have tried by putting this &quot;ip.src==192.168.1.63 and ip.dst==192.168.1.245&quot; but nothing appear in wireshark.'''
date = "2017-04-20T00:29:00Z"
lastmod = "2017-04-20T01:11:00Z"
weight = 60905
keywords = [ "packet" ]
aliases = [ "/questions/60905" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to capture the traffic of devices interacting in our network](/questions/60905/how-to-capture-the-traffic-of-devices-interacting-in-our-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60905-score" class="post-score" title="current number of votes">0</div><span id="post-60905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>using ethernet on my laptop (192.168.1.23), which is installed wireshare, would like to capture the traffic from ip camera (192.168.1.63) to network vdieo recorder (192.168.1.245).</p><p>i have tried by putting this "ip.src==192.168.1.63 and ip.dst==192.168.1.245" but nothing appear in wireshark.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '17, 00:29</strong></p><img src="https://secure.gravatar.com/avatar/1b0fe9b52b986885797a87b0d0ef7b41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NICK007&#39;s gravatar image" /><p><span>NICK007</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NICK007 has no accepted answers">0%</span></p></div></div><div id="comments-container-60905" class="comments-container"></div><div id="comment-tools-60905" class="comment-tools"></div><div class="clear"></div><div id="comment-60905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60907"></span>

<div id="answer-container-60907" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60907-score" class="post-score" title="current number of votes">2</div><span id="post-60907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="NICK007 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Likely because you're on a switched network with all three items connected to that switch so your laptop won't see the traffic between the camera and the recorder.</p><p>See the Wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet Capturing Setup</a> for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '17, 00:35</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-60907" class="comments-container"><span id="60912"></span><div id="comment-60912" class="comment"><div id="post-60912-score" class="comment-score"></div><div class="comment-text"><p>I got it! thanks for your help!!</p></div><div id="comment-60912-info" class="comment-info"><span class="comment-age">(20 Apr '17, 01:11)</span> <span class="comment-user userinfo">NICK007</span></div></div></div><div id="comment-tools-60907" class="comment-tools"></div><div class="clear"></div><div id="comment-60907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

