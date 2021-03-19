+++
type = "question"
title = "Destination IP address when proxy server is configured"
description = '''I m new to Wireshark and have very limited knowledge on how proxy servers function. I ran Wireshark on a campus LAN where the PCs are configured with a proxy server (e.g. proxy.example.com and port 8000), and I am not sure about the type of proxy server used.  All the packets captured show the desti...'''
date = "2012-10-09T10:34:00Z"
lastmod = "2012-10-09T13:54:00Z"
weight = 14823
keywords = [ "ip", "proxy", "address" ]
aliases = [ "/questions/14823" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Destination IP address when proxy server is configured](/questions/14823/destination-ip-address-when-proxy-server-is-configured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14823-score" class="post-score" title="current number of votes">0</div><span id="post-14823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I m new to Wireshark and have very limited knowledge on how proxy servers function.</p><p>I ran Wireshark on a campus LAN where the PCs are configured with a proxy server (e.g. <a href="http://proxy.example.com">proxy.example.com</a> and port 8000), and I am not sure about the type of proxy server used. All the packets captured show the destination IP address as that of the proxy server, not of the real destination (e.g. <a href="http://www.yahoo.com">www.yahoo.com</a>, <a href="http://www.google.com">www.google.com</a>, etc). Is there any way I can figure out the real destination IP addresses from Wireshark's captures??</p><p>Similarly all the incoming packets carry the source IP address as that of the proxy server (not that of Yahoo, Google, etc). I wish to filter out packets from <a href="http://www.youtube.com">www.youtube.com</a>. Is it possible?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-proxy" rel="tag" title="see questions tagged &#39;proxy&#39;">proxy</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '12, 10:34</strong></p><img src="https://secure.gravatar.com/avatar/cdf60269b04f7d9d53c78ff540b017b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aaks&#39;s gravatar image" /><p><span>Aaks</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aaks has no accepted answers">0%</span></p></div></div><div id="comments-container-14823" class="comments-container"></div><div id="comment-tools-14823" class="comment-tools"></div><div class="clear"></div><div id="comment-14823-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14836"></span>

<div id="answer-container-14836" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14836-score" class="post-score" title="current number of votes">0</div><span id="post-14836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your HTTP client normally uses the host name part of the URL to do a DNS lookup to connect to the requested host. Then is sends an HTTP GET of the rest of the URL. The host name is also included in that request.</p><p>Now, if you've configured a HTTP proxy for your client it opens a connection to there and then sends the HTTP GET, with the complete URI, including the host name. The proxy then uses that information to setup its own connection with the intended host and forwards the HTTP GET. Any responses received are send back the the originating client.</p><p>So what you need to look at is the TCP connection and the host name part of the GET requests. These requests are send forward, and the responses come back the same way. So your endpoint tracking has raised from the network level to the session level.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '12, 13:54</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-14836" class="comments-container"></div><div id="comment-tools-14836" class="comment-tools"></div><div class="clear"></div><div id="comment-14836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

