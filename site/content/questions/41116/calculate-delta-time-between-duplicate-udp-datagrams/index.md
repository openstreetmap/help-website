+++
type = "question"
title = "Calculate delta time between duplicate UDP Datagrams"
description = '''Hi Everyone,  I hope there is a solution for this. I have a packet capture from a device&#x27;s interface that is receiving UDP packets and sending them back out the same interface (there is no physical difference in the payload but there is in the L2 header because the MACs change). I need a report on h...'''
date = "2015-04-01T22:45:00Z"
lastmod = "2015-04-02T02:25:00Z"
weight = 41116
keywords = [ "calculatedelta" ]
aliases = [ "/questions/41116" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Calculate delta time between duplicate UDP Datagrams](/questions/41116/calculate-delta-time-between-duplicate-udp-datagrams)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41116-score" class="post-score" title="current number of votes">0</div><span id="post-41116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Everyone,</p><p>I hope there is a solution for this. I have a packet capture from a device's interface that is receiving UDP packets and sending them back out the same interface (there is no physical difference in the payload but there is in the L2 header because the MACs change). I need a report on how much time it takes to my device to process these packets and send them back.</p><p>This means I need a feature that can identify the duplicate packets on my file and then calculate the time difference between them. There is a feature called "editcap" that can work with duplicate packets but the only option I see is to delete the duplicates which obviously is not useful to me.</p><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-calculatedelta" rel="tag" title="see questions tagged &#39;calculatedelta&#39;">calculatedelta</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '15, 22:45</strong></p><img src="https://secure.gravatar.com/avatar/235b5871af658a44e1321fb015784d86?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ds3010&#39;s gravatar image" /><p><span>ds3010</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ds3010 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Apr '15, 23:21</strong> </span></p></div></div><div id="comments-container-41116" class="comments-container"></div><div id="comment-tools-41116" class="comment-tools"></div><div class="clear"></div><div id="comment-41116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41125"></span>

<div id="answer-container-41125" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41125-score" class="post-score" title="current number of votes">0</div><span id="post-41125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>This means I need a feature that can identify the duplicate packets on my file and then calculate the time difference between them.</p></blockquote><p>There is no automatism in Wireshark to do that, however you can use tshark together with a script to do the calculation yourself.</p><p>First capture the traffic and store it in traffic.pcap.</p><p>Run tshark:</p><blockquote><p>tshark -nr traffic.pcap -Y "port xxxx" -T fields -e frame.number -e frame.time_epoch -e ip.src -e ip.dst -e ip.id -E separator=, -E header=y &gt; output.txt</p></blockquote><p>Then use a script (or a spreadsheet software) to calculate the time delta of frames with the same IP ID.</p><p><strong>However</strong>: Be aware, that the time stamps in the frames will only reflect the time when the OS (kernel or NIC driver) has seen the frames, so the time delta contains the following parts: <strong>dt(application) + dt(IP stack)</strong> and you can't determine the value of <strong>dt(IP stack)</strong>. If the difference to <strong>dt(application)</strong> is large enough, it won't matter, but if your application is really fast, it could be a problem, as you are then measuring the performance of the IP stack instead of your application.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '15, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-41125" class="comments-container"></div><div id="comment-tools-41125" class="comment-tools"></div><div class="clear"></div><div id="comment-41125-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

