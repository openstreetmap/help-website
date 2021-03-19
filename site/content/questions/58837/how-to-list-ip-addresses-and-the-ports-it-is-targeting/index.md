+++
type = "question"
title = "How to list IP addresses and the ports it is targeting??"
description = '''Hi, I would like to list all the targeted ports of each IP address. I know that in wireshark we can filter destination IP address and Ports.(statitics-&amp;gt;ipv4-&amp;gt;destination and ports)  But How to get the statistics of which are all the ports, an IP address is targeting?? If that feature is not th...'''
date = "2017-01-17T06:50:00Z"
lastmod = "2017-01-17T07:55:00Z"
weight = 58837
keywords = [ "ip", "statistics", "ports" ]
aliases = [ "/questions/58837" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to list IP addresses and the ports it is targeting??](/questions/58837/how-to-list-ip-addresses-and-the-ports-it-is-targeting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58837-score" class="post-score" title="current number of votes">0</div><span id="post-58837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I would like to list all the targeted ports of each IP address.</p><p>I know that in wireshark we can filter destination IP address and Ports.(statitics-&gt;ipv4-&gt;destination and ports)</p><p>But How to get the statistics of which are all the ports, an IP address is targeting??</p><p>If that feature is not there in wireshark,could anybody suggest any method to do the same??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-ports" rel="tag" title="see questions tagged &#39;ports&#39;">ports</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '17, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/95e9674b7a67d58ada813e0c6bc38d84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="subinjp&#39;s gravatar image" /><p><span>subinjp</span><br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="subinjp has no accepted answers">0%</span></p></div></div><div id="comments-container-58837" class="comments-container"><span id="58838"></span><div id="comment-58838" class="comment"><div id="post-58838-score" class="comment-score"></div><div class="comment-text"><p>You'll need to define what you mean by "targeting"?</p><p>Do you mean you want a list of destination ports for all packets sourced from a specific IP address, regardless of the destination address?</p></div><div id="comment-58838-info" class="comment-info"><span class="comment-age">(17 Jan '17, 07:10)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="58839"></span><div id="comment-58839" class="comment"><div id="post-58839-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@grahamb</span> Yes.absolutely.Thats what I want.Btw Thanks for your reply.</p></div><div id="comment-58839-info" class="comment-info"><span class="comment-age">(17 Jan '17, 07:12)</span> <span class="comment-user userinfo">subinjp</span></div></div></div><div id="comment-tools-58837" class="comment-tools"></div><div class="clear"></div><div id="comment-58837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58841"></span>

<div id="answer-container-58841" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58841-score" class="post-score" title="current number of votes">0</div><span id="post-58841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="subinjp has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In the Destination and Ports dialog, "Display Filter" box enter a filter to limit the display to the source address, e.g. <code>ip.src == 1.2.3.4</code> and click the Apply button.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '17, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-58841" class="comments-container"><span id="58842"></span><div id="comment-58842" class="comment"><div id="post-58842-score" class="comment-score"></div><div class="comment-text"><p>Thank you.</p></div><div id="comment-58842-info" class="comment-info"><span class="comment-age">(17 Jan '17, 07:55)</span> <span class="comment-user userinfo">subinjp</span></div></div></div><div id="comment-tools-58841" class="comment-tools"></div><div class="clear"></div><div id="comment-58841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

