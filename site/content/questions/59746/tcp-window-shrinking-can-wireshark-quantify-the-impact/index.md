+++
type = "question"
title = "TCP Window shrinking;  Can Wireshark quantify the impact?"
description = '''Hi y&#x27;all... I am analyzing why a new data replication process is taking longer – and generating lower throughput – than is expected / acceptable. I have looked at some packets, and I see the TCP Window on the “receiver” shrinking over time, and at times it shrinks effectively to zero, and the sender...'''
date = "2017-02-28T13:30:00Z"
lastmod = "2017-03-03T09:15:00Z"
weight = 59746
keywords = [ "tcp_window_update" ]
aliases = [ "/questions/59746" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TCP Window shrinking; Can Wireshark quantify the impact?](/questions/59746/tcp-window-shrinking-can-wireshark-quantify-the-impact)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59746-score" class="post-score" title="current number of votes">0</div><span id="post-59746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi y'all...</p><p>I am analyzing why a new data replication process is taking longer – and generating lower throughput – than is expected / acceptable.</p><p>I have looked at some packets, and I see the TCP Window on the “receiver” shrinking over time, and at times it shrinks effectively to zero, and the sender must wait until a TCP Window Update arrives, to resume sending. This occurs periodically.</p><p>So I know that the receiver is not able to “keep up” with the replication data being sent, which slows down the replication process.</p><p>What I do NOT know is: BY HOW MUCH??? If we are able to resolve this, would it improve throughput by 10%? 30%? 80%?</p><p>Does anyone have any suggestions on how I can use Wireshark's analysis capabilities to quantify the impact of this condition?</p><p>Thx all,</p><p>feenyman99</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp_window_update" rel="tag" title="see questions tagged &#39;tcp_window_update&#39;">tcp_window_update</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '17, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p><span>feenyman99</span><br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span></p></div></div><div id="comments-container-59746" class="comments-container"><span id="59747"></span><div id="comment-59747" class="comment"><div id="post-59747-score" class="comment-score"></div><div class="comment-text"><p>Faster hard disk, more CPU, reduce system load that is what you can try.</p></div><div id="comment-59747-info" class="comment-info"><span class="comment-age">(28 Feb '17, 13:47)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="59757"></span><div id="comment-59757" class="comment"><div id="post-59757-score" class="comment-score"></div><div class="comment-text"><p>Can you share us a trace. <a href="https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/#more-1468">https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/#more-1468</a></p></div><div id="comment-59757-info" class="comment-info"><span class="comment-age">(01 Mar '17, 03:49)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="59831"></span><div id="comment-59831" class="comment"><div id="post-59831-score" class="comment-score"></div><div class="comment-text"><p>The folks looking at the health of the receiving server tell me that CPU, Memory and Disk Utilization are all quite low during this data replication process. I am having someone take a second look to confirm this, but, as of now, there is no indication that the receiver is lacking capacity for this process.</p><p>Regarding sharing a trace... I will look at the link you provided (file sharing tutorial), as I'd like to know how to do this, but I must say that I'm in a VERY security-conscious industry sector, and I'm not sure I could share a trace file, even if I use a tool to modify/obscure the IP Addresses.<br />
</p><p>Thx!</p></div><div id="comment-59831-info" class="comment-info"><span class="comment-age">(03 Mar '17, 09:15)</span> <span class="comment-user userinfo">feenyman99</span></div></div></div><div id="comment-tools-59746" class="comment-tools"></div><div class="clear"></div><div id="comment-59746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59754"></span>

<div id="answer-container-59754" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59754-score" class="post-score" title="current number of votes">2</div><span id="post-59754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="feenyman99 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What you can do to get the theoretical throughput is to calculate the Bandwidth-delay product (BDP; see. <a href="https://www.switch.ch/de/network/tools/tcp_throughput/index.html">https://www.switch.ch/de/network/tools/tcp_throughput/index.html</a> ).</p><p>Take the max reported window size reported by the sender and the initial Round Trip Time as input values.</p><p>With this you can calculate the diff to your measured throughput.</p><p>Please be aware that other influences (e.g. packet loss) can change the throughput too.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '17, 00:06</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Mar '17, 00:07</strong> </span></p></div></div><div id="comments-container-59754" class="comments-container"></div><div id="comment-tools-59754" class="comment-tools"></div><div class="clear"></div><div id="comment-59754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

