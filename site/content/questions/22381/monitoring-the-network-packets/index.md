+++
type = "question"
title = "Monitoring the network packets"
description = '''I have a 2 questions-  1. I need to a write a C program through which I need to monitor the network packets of the Tshark, in the LINUX. How could I do this??  2. Is it possible to monitor the rate at which the packets are flowing in the network, if yes how could I do this. Please answer these quest...'''
date = "2013-06-26T18:03:00Z"
lastmod = "2013-06-27T08:12:00Z"
weight = 22381
keywords = [ "capture", "packet-capture" ]
aliases = [ "/questions/22381" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Monitoring the network packets](/questions/22381/monitoring-the-network-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22381-score" class="post-score" title="current number of votes">0</div><span id="post-22381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a 2 questions- 1. I need to a write a C program through which I need to monitor the network packets of the Tshark, in the LINUX. How could I do this?? 2. Is it possible to monitor the rate at which the packets are flowing in the network, if yes how could I do this.</p><p>Please answer these questions.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '13, 18:03</strong></p><img src="https://secure.gravatar.com/avatar/72bb467fdfcb864b343d591c407020f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rahuulbp&#39;s gravatar image" /><p><span>rahuulbp</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rahuulbp has no accepted answers">0%</span></p></div></div><div id="comments-container-22381" class="comments-container"></div><div id="comment-tools-22381" class="comment-tools"></div><div class="clear"></div><div id="comment-22381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22397"></span>

<div id="answer-container-22397" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22397-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22397-score" class="post-score" title="current number of votes">0</div><span id="post-22397-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark (and tshark) are packet analysers, not network traffic monitors. You are probably looking at the wrong tools for your task.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '13, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-22397" class="comments-container"><span id="22406"></span><div id="comment-22406" class="comment"><div id="post-22406-score" class="comment-score"></div><div class="comment-text"><p>Yes i understand, but I need to count the number of packets from the terminal window in the tshark and write a C program accordingly. My question is how can we count the number of packets of the tshark and connect/map that to the C program.</p></div><div id="comment-22406-info" class="comment-info"><span class="comment-age">(27 Jun '13, 07:50)</span> <span class="comment-user userinfo">rahuulbp</span></div></div><span id="22408"></span><div id="comment-22408" class="comment"><div id="post-22408-score" class="comment-score"></div><div class="comment-text"><p>Have a look at dumpcap. That outputs the packets seen as a count and unlike tshark won't run out of memory if capturing for an extended length of time.</p><p>I guess your C program could spawn dumpcap and grab the stdout to inspect the packet count.</p></div><div id="comment-22408-info" class="comment-info"><span class="comment-age">(27 Jun '13, 08:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-22397" class="comment-tools"></div><div class="clear"></div><div id="comment-22397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

