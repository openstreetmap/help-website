+++
type = "question"
title = "Fragmentation"
description = '''I&#x27;m troubleshooting an application across the WAN and want to know how to look in the trace to see if IP fragmentation could be an issue. The client trace file is captured directly from the NIC and the server trace is from port span. The network team claimed there&#x27;s fragmentation but it does do not ...'''
date = "2011-11-08T08:39:00Z"
lastmod = "2011-11-16T04:40:00Z"
weight = 7281
keywords = [ "fragmentation" ]
aliases = [ "/questions/7281" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Fragmentation](/questions/7281/fragmentation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7281-score" class="post-score" title="current number of votes">0</div><span id="post-7281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm troubleshooting an application across the WAN and want to know how to look in the trace to see if IP fragmentation could be an issue. The client trace file is captured directly from the NIC and the server trace is from port span. The network team claimed there's fragmentation but it does do not show when filtered with the "IP fragments" flag for the trace. The trace show there's no delay with the response time for the request and response. The majority of the delay seems to be the client when looking at the client and server side traces. I just want to rule out fragmentation is not an issue and not sure what else to check. Want to rule out the fragmentation is the cause of the delay.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fragmentation" rel="tag" title="see questions tagged &#39;fragmentation&#39;">fragmentation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '11, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/9d629f265392eaf7b61f921e25f9f730?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ws2006&#39;s gravatar image" /><p><span>ws2006</span><br />
<span class="score" title="1 reputation points">1</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ws2006 has no accepted answers">0%</span></p></div></div><div id="comments-container-7281" class="comments-container"></div><div id="comment-tools-7281" class="comment-tools"></div><div class="clear"></div><div id="comment-7281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7282"></span>

<div id="answer-container-7282" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7282-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7282-score" class="post-score" title="current number of votes">2</div><span id="post-7282-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Look for the ICMP message "fragmentation needed". The display filter <strong>icmp.type == 3 and icmp.code == 4</strong> reveals these messages.</p><p>Fragmentation might still be an issue if the ICMP message is blocked by a firewall, resulting in a "black hole router". Typical symptoms for a black hole router are</p><ul><li>The connection is properly set up (successful 3-way handshake)</li><li>Short packets go through, like the individual keystrokes of a telnet or ssh session</li><li>The application "freezes" when large segments are transmitted (authentication with username and password is okay, but large transfers fail)</li></ul><p>Good hunting!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '11, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-7282" class="comments-container"><span id="7470"></span><div id="comment-7470" class="comment"><div id="post-7470-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Did not see any ICMP messages.</p></div><div id="comment-7470-info" class="comment-info"><span class="comment-age">(16 Nov '11, 04:33)</span> <span class="comment-user userinfo">ws2006</span></div></div><span id="7471"></span><div id="comment-7471" class="comment"><div id="post-7471-score" class="comment-score"></div><div class="comment-text"><p>Do you see the initial 3-way handshake?</p><p>If yes: Do you see the delivery of small packets (e. g. authentication), while large packets are dropped?</p><p>The lack of ICMP messages can indicate the presence of a black hole router.</p></div><div id="comment-7471-info" class="comment-info"><span class="comment-age">(16 Nov '11, 04:40)</span> <span class="comment-user userinfo">packethunter</span></div></div></div><div id="comment-tools-7282" class="comment-tools"></div><div class="clear"></div><div id="comment-7282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

