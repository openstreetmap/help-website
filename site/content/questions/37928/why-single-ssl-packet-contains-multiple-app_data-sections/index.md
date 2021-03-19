+++
type = "question"
title = "why single SSL packet contains multiple app_data sections"
description = '''Hi there,  While troubleshooting a SSLVPN slowness issue, I noticed the Retransmitted SSL packets contains multiple app_data sections. I don&#x27;t see this kind of pattern in pcap files from other locations. The VPN Server has Nagle&#x27;s algorithm turned on, could this be the cause?  The following is an ex...'''
date = "2014-11-17T20:17:00Z"
lastmod = "2014-11-17T20:17:00Z"
weight = 37928
keywords = [ "ssl", "retransmission" ]
aliases = [ "/questions/37928" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [why single SSL packet contains multiple app\_data sections](/questions/37928/why-single-ssl-packet-contains-multiple-app_data-sections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37928-score" class="post-score" title="current number of votes">0</div><span id="post-37928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,<br />
</p><p>While troubleshooting a SSLVPN slowness issue, I noticed the Retransmitted SSL packets contains multiple app_data sections. I don't see this kind of pattern in pcap files from other locations. The VPN Server has Nagle's algorithm turned on, could this be the cause?<br />
</p><p>The following is an excerpt from the actual capture and in the SAME TCP stream. (For security reasons, the server's public IP is replaced with A.A.A.A). The server was trying to resend TCP Seq 32132 in packet 274, 277 and 281. Notice in each of those packet, there are 3 or 4 "Application Data section"? And also each packet's Next Sequence number is different. Why is that?</p><pre><code>274 11:45:14.796000 A.A.A.A 192.168.0.101   **32132**   32282   3923    TLSv1   208 1   [TCP Retransmission] Application Data, Application Data, Application Data, Application Data, Application Data   274

277 11:45:14.830000 A.A.A.A 192.168.0.101   **32132**   32312   3923    TLSv1   238 1   [TCP Retransmission] Application Data, Application Data, Application Data, Application Data, Application Data, Application Data 277

281 11:45:14.858000 A.A.A.A 192.168.0.101   **32132**   32312   3950    TLSv1   238 1   [TCP Out-Of-Order] Application Data, Application Data, Application Data, Application Data, Application Data, Application Data   281</code></pre><p>Hope someone could kindly clarify. Thanks! ~</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '14, 20:17</strong></p><img src="https://secure.gravatar.com/avatar/c448f4b70047cb832524825bc6af9dfc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Timbit&#39;s gravatar image" /><p><span>Timbit</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Timbit has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-37928" class="comments-container"></div><div id="comment-tools-37928" class="comment-tools"></div><div class="clear"></div><div id="comment-37928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

