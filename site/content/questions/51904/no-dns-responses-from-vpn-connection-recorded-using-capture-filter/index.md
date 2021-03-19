+++
type = "question"
title = "No DNS Responses from VPN Connection Recorded using Capture Filter"
description = '''When I use the simple &quot;Port 53&quot; capture filter on my main ethernet interface I correctly see all of the DNS queries and their corresponding responses. However, when I use this same filter against an OpenVPN interface on this same machine I see only the DNS queries and none of the responses. They are...'''
date = "2016-04-23T16:12:00Z"
lastmod = "2016-04-26T04:01:00Z"
weight = 51904
keywords = [ "winpcap", "capture-filter", "dns" ]
aliases = [ "/questions/51904" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [No DNS Responses from VPN Connection Recorded using Capture Filter](/questions/51904/no-dns-responses-from-vpn-connection-recorded-using-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51904-score" class="post-score" title="current number of votes">0</div><span id="post-51904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I use the simple "Port 53" capture filter on my main ethernet interface I correctly see all of the DNS queries and their corresponding responses. However, when I use this same filter against an OpenVPN interface on this same machine I see only the DNS queries and none of the responses.</p><p>They are there, however, because if I capture all traffic against this interface and then use the simple "DNS" display filter, I see all queries and all responses as expected. It appears something is amiss with WinPCAP but I am unable to troubleshoot it.</p><p>Any help appreciated!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '16, 16:12</strong></p><img src="https://secure.gravatar.com/avatar/396bc1cfc1caa8872a79c11b450010b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jxdomb&#39;s gravatar image" /><p><span>jxdomb</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jxdomb has no accepted answers">0%</span></p></div></div><div id="comments-container-51904" class="comments-container"></div><div id="comment-tools-51904" class="comment-tools"></div><div class="clear"></div><div id="comment-51904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51955"></span>

<div id="answer-container-51955" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51955-score" class="post-score" title="current number of votes">0</div><span id="post-51955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please try Npcap, a fork of WinPcap but more advanced:</p><p><a href="https://github.com/nmap/npcap/releases/">https://github.com/nmap/npcap/releases/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '16, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/0f8ec58f46e4af3a67f768675c20aac8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yang%20Luo&#39;s gravatar image" /><p><span>Yang Luo</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yang Luo has one accepted answer">4%</span></p></div></div><div id="comments-container-51955" class="comments-container"></div><div id="comment-tools-51955" class="comment-tools"></div><div class="clear"></div><div id="comment-51955-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

