+++
type = "question"
title = "Persistent connection from questionable IP address on port 443"
description = '''For a small business setup, I have a Windows 2008 server acting as AD domain controller and Exchange 2007 server. I&#x27;ve recently begun to look further into all network activity and notice something unusual to me involving this server. There is a persistent connection between it and a Verizon wireless...'''
date = "2013-04-03T09:28:00Z"
lastmod = "2013-04-03T11:44:00Z"
weight = 20061
keywords = [ "443", "traffic" ]
aliases = [ "/questions/20061" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Persistent connection from questionable IP address on port 443](/questions/20061/persistent-connection-from-questionable-ip-address-on-port-443)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20061-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20061-score" class="post-score" title="current number of votes">0</div><span id="post-20061-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For a small business setup, I have a Windows 2008 server acting as AD domain controller and Exchange 2007 server. I've recently begun to look further into all network activity and notice something unusual to me involving this server. There is a persistent connection between it and a Verizon wireless IP address (174.254.24.191, 174.240.0.73, 174.254.1.124 to name a few) always geolocated in Las Vegas. This connection uses port 443 on my server. The service name being used is "SYSTEM". This connection is using the same public IP address as our MX record. I do use Exchange active-sync for a few users. Any suggestions as to further identify EXACTLY what this IP address is doing with my server? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-443" rel="tag" title="see questions tagged &#39;443&#39;">443</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '13, 09:28</strong></p><img src="https://secure.gravatar.com/avatar/8ffcd15398891e5456e1d7c0585fd7f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steveg&#39;s gravatar image" /><p><span>steveg</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steveg has no accepted answers">0%</span></p></div></div><div id="comments-container-20061" class="comments-container"></div><div id="comment-tools-20061" class="comment-tools"></div><div class="clear"></div><div id="comment-20061-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20066"></span>

<div id="answer-container-20066" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20066-score" class="post-score" title="current number of votes">0</div><span id="post-20066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, if you want to know EXACTLY what these IP's are doing on your server, you can use the private key of the server to decrypt the traffic in Wireshark and see which HTTPS requests they are sending. My guess would indeed be that it is Exchange active-sync traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '13, 10:26</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20066" class="comments-container"><span id="20067"></span><div id="comment-20067" class="comment"><div id="post-20067-score" class="comment-score"></div><div class="comment-text"><p>OK, thanks for your advice. Unfortunately, due to my lack of experience, I don't know how to do what you suggest. I'd appreciate further instructions, or your pointing me to exact instructions as to how to accomplish this. Thanks again.</p></div><div id="comment-20067-info" class="comment-info"><span class="comment-age">(03 Apr '13, 11:44)</span> <span class="comment-user userinfo">steveg</span></div></div></div><div id="comment-tools-20066" class="comment-tools"></div><div class="clear"></div><div id="comment-20066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

