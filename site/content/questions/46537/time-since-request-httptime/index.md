+++
type = "question"
title = "Time Since Request (http.time)"
description = '''Hi, I am trying to get time since request(http.time) value from another application. So I am wondering if that is a standard function on winpcap, or does wireshark calculate it by itself? (and how does it calculate?) Thanks,'''
date = "2015-10-13T16:23:00Z"
lastmod = "2015-10-14T06:38:00Z"
weight = 46537
keywords = [ "http.time", "since", "request", "time" ]
aliases = [ "/questions/46537" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Time Since Request (http.time)](/questions/46537/time-since-request-httptime)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46537-score" class="post-score" title="current number of votes">0</div><span id="post-46537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to get time since request(http.time) value from another application. So I am wondering if that is a standard function on winpcap, or does wireshark calculate it by itself? (and how does it calculate?)</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http.time" rel="tag" title="see questions tagged &#39;http.time&#39;">http.time</span> <span class="post-tag tag-link-since" rel="tag" title="see questions tagged &#39;since&#39;">since</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '15, 16:23</strong></p><img src="https://secure.gravatar.com/avatar/3ecc320b89cb973693e1f8c30f51dd68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tarik&#39;s gravatar image" /><p><span>tarik</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tarik has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Oct '15, 16:24</strong> </span></p></div></div><div id="comments-container-46537" class="comments-container"></div><div id="comment-tools-46537" class="comment-tools"></div><div class="clear"></div><div id="comment-46537-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46551"></span>

<div id="answer-container-46551" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46551-score" class="post-score" title="current number of votes">3</div><span id="post-46551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tarik has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>http.time is, as Christian said, calculated by Wireshark, but it is calculated in different ways, depending on your preference settings.</p><p>The client sends a request, let's say a GET request, and for the sake of simplicity, let's assume that the GET request fits in one packet.</p><p>The server sends a response, hopefully a "200 OK" response, followed by the data that was requested. The OK response will be in the first packet from the server, followed immediately, in the same packet, by however much of the data will fit. The rest of the data follows in additional packets. So occasionally, the 200 OK and all of the data will be in one packet, but usually the response will span multiple packets with the OK in the first one.</p><p>If the TCP preference "Allow subdissector to reassemble TCP streams" is <em>off</em>, the http.time will be the time between the GET request and the <em>first</em> packet of the response, the one containing the OK.</p><p>If "Allow subdissector to reassemble TCP streams" is <em>on</em> and the HTTP reassembly preferences have been left at their defaults (on), http.time will be the time between the GET request and the <em>last</em> packet of the response.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '15, 06:38</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-46551" class="comments-container"></div><div id="comment-tools-46551" class="comment-tools"></div><div class="clear"></div><div id="comment-46551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46538"></span>

<div id="answer-container-46538" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46538-score" class="post-score" title="current number of votes">1</div><span id="post-46538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It is calculated by Wireshark. A value which is calculated by Wireshark itsself could be identified by the brackets <code>[]</code><br />
For example <code>[TCP Segment Len: 1438]</code><br />
If you scroll over this field with your mouse than you can see in the status bar the real field name. In this case <code>tcp.len</code><br />
This string <code>tcp.len</code> could be used as an display filter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '15, 16:29</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></br></p></div></div><div id="comments-container-46538" class="comments-container"></div><div id="comment-tools-46538" class="comment-tools"></div><div class="clear"></div><div id="comment-46538-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

