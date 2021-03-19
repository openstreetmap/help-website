+++
type = "question"
title = "Large rtt or packets lost factors,which affects tcp performance most?"
description = '''Usually,when we check one tcp flow traffic and evaluate if the packets lost or large rtt exit.If the two factors both exit,how to judge which effect the tcp throughput seriously? Does anybody know the good way to judge this?'''
date = "2012-12-22T01:12:00Z"
lastmod = "2012-12-22T04:34:00Z"
weight = 17156
keywords = [ "large", "rtt", "packets", "lost" ]
aliases = [ "/questions/17156" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Large rtt or packets lost factors,which affects tcp performance most?](/questions/17156/large-rtt-or-packets-lost-factorswhich-affects-tcp-performance-most)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17156-score" class="post-score" title="current number of votes">0</div><span id="post-17156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Usually,when we check one tcp flow traffic and evaluate if the packets lost or large rtt exit.If the two factors both exit,how to judge which effect the tcp throughput seriously? Does anybody know the good way to judge this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-large" rel="tag" title="see questions tagged &#39;large&#39;">large</span> <span class="post-tag tag-link-rtt" rel="tag" title="see questions tagged &#39;rtt&#39;">rtt</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-lost" rel="tag" title="see questions tagged &#39;lost&#39;">lost</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '12, 01:12</strong></p><img src="https://secure.gravatar.com/avatar/7fdbac8aac2e38813e1fc1da4c6efdf4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chinasan&#39;s gravatar image" /><p><span>chinasan</span><br />
<span class="score" title="0 reputation points">0</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chinasan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Dec '12, 03:03</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-17156" class="comments-container"></div><div id="comment-tools-17156" class="comment-tools"></div><div class="clear"></div><div id="comment-17156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17157"></span>

<div id="answer-container-17157" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17157-score" class="post-score" title="current number of votes">2</div><span id="post-17157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It depends on your application. An application like FTP usually doesn't care too much about the RTT when transferring <strong>large</strong> files since there is no request-reply-request-reply communication going back and forth all the time - there is one "give me the file"-request, followed by tons of response packets. If you're doing <strong>small</strong> transfers instead (like requesting thousands of tiny files) the RTT will hurt you a lot more since you're serializing requests one after the other.</p><p>So basically what you have to look at is this: how many requests are there that need to be executed one after the other, and how much data is returned each time? The smaller the data and the more requests you serialize, the more a large RTT will hurt you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '12, 02:03</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-17157" class="comments-container"><span id="17158"></span><div id="comment-17158" class="comment"><div id="post-17158-score" class="comment-score"></div><div class="comment-text"><p>Mostly we analyze application such as ftp or http streaming,no much requests.I have searched some classical tcp throughput formula(including rtt and lost ration ,MSS),very <a href="http://complicated.Is">complicated.Is</a> there any simple way to judge which factors effect seriously?</p></div><div id="comment-17158-info" class="comment-info"><span class="comment-age">(22 Dec '12, 02:46)</span> <span class="comment-user userinfo">chinasan</span></div></div><span id="17161"></span><div id="comment-17161" class="comment"><div id="post-17161-score" class="comment-score"></div><div class="comment-text"><p>I don't think there is a simple way, since too many factors come into play here. You need to look at the amount of requests, minimum bandwidth of the connection, RTT, TCP inital window size, window size adjustments made by the receiver (which might lead to window full issues), plus packet loss and recovery time penalties. Yikes! ;-)</p></div><div id="comment-17161-info" class="comment-info"><span class="comment-age">(22 Dec '12, 04:34)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-17157" class="comment-tools"></div><div class="clear"></div><div id="comment-17157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

