+++
type = "question"
title = "tcpdump -ni utun0  doesn&#x27;t capture traffic"
description = '''Hi there! I&#x27;m using OS X 10.9 and standard apple ipsec connection. After connection I see utun0 interface is active. But when I use command &quot;tcpdump -ni utun0&quot; i haven&#x27;t see any captured traffic. If I use standard L2TP connection and interface ppp0, I see a traffic and it&#x27;s work perfect. Why it does...'''
date = "2013-12-10T21:25:00Z"
lastmod = "2014-03-09T03:20:00Z"
weight = 27986
keywords = [ "utun0" ]
aliases = [ "/questions/27986" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tcpdump -ni utun0 doesn't capture traffic](/questions/27986/tcpdump-ni-utun0-doesnt-capture-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27986-score" class="post-score" title="current number of votes">0</div><span id="post-27986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there! I'm using OS X 10.9 and standard apple ipsec connection. After connection I see utun0 interface is active. But when I use command "tcpdump -ni utun0" i haven't see any captured traffic. If I use standard L2TP connection and interface ppp0, I see a traffic and it's work perfect. Why it doesn't work with tunnel interfaces?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-utun0" rel="tag" title="see questions tagged &#39;utun0&#39;">utun0</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '13, 21:25</strong></p><img src="https://secure.gravatar.com/avatar/315d509a4273e13a41351d52d3a3c2f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yevgeniy%20Luchshikov&#39;s gravatar image" /><p><span>Yevgeniy Luc...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yevgeniy Luchshikov has no accepted answers">0%</span></p></div></div><div id="comments-container-27986" class="comments-container"><span id="30600"></span><div id="comment-30600" class="comment"><div id="post-30600-score" class="comment-score"></div><div class="comment-text"><p>I have this problem too running OSX 10.9.2, no traffic seen on utun0. I've checked with other Mac users I work with and they also cannot capture on utun0 running Mavericks.</p></div><div id="comment-30600-info" class="comment-info"><span class="comment-age">(08 Mar '14, 06:03)</span> <span class="comment-user userinfo">CiscoMac</span></div></div></div><div id="comment-tools-27986" class="comment-tools"></div><div class="clear"></div><div id="comment-27986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30607"></span>

<div id="answer-container-30607" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30607-score" class="post-score" title="current number of votes">0</div><span id="post-30607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>see the other question about utun0.</p><blockquote><p><a href="http://ask.wireshark.org/questions/4812/on-mac-osx-i-cant-capture-packets-sent-over-a-vpn">http://ask.wireshark.org/questions/4812/on-mac-osx-i-cant-capture-packets-sent-over-a-vpn</a><br />
</p></blockquote><p>Apparently Apple did not fix that 'problem'. So, please check the status of Apple Bug-ID: 9699332 (the other user filed that bug report).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '14, 03:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-30607" class="comments-container"></div><div id="comment-tools-30607" class="comment-tools"></div><div class="clear"></div><div id="comment-30607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

