+++
type = "question"
title = "Multiple IPs in X-Forwarded-For field"
description = '''Hi All,  Like the title says, I have a packets that have multiple IPs in the X-Forwarded-For field. Our public facing IPs and sites are behind Akamai and some of the IPs are from them. This is expected. There are others for another business partner and a few unknowns. However, occasionally I&#x27;ll see ...'''
date = "2017-06-12T15:17:00Z"
lastmod = "2017-06-13T00:50:00Z"
weight = 61963
keywords = [ "x-forwarded-for" ]
aliases = [ "/questions/61963" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple IPs in X-Forwarded-For field](/questions/61963/multiple-ips-in-x-forwarded-for-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61963-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61963-score" class="post-score" title="current number of votes">0</div><span id="post-61963-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>Like the title says, I have a packets that have multiple IPs in the X-Forwarded-For field. Our public facing IPs and sites are behind Akamai and some of the IPs are from them. This is expected. There are others for another business partner and a few unknowns. However, occasionally I'll see packets with 2 or even 3 IPs in that field.</p><p>What does that mean?</p><p>My first thought was routing before or after Akamai, but I don't think that is correct.</p><p>Thanks in advance!</p><p>Rk.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-x-forwarded-for" rel="tag" title="see questions tagged &#39;x-forwarded-for&#39;">x-forwarded-for</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '17, 15:17</strong></p><img src="https://secure.gravatar.com/avatar/ff945b794cf3186f696dc75bec792743?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rkwarner2&#39;s gravatar image" /><p><span>rkwarner2</span><br />
<span class="score" title="4 reputation points">4</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rkwarner2 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jun '17, 18:41</strong> </span></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span></p></div></div><div id="comments-container-61963" class="comments-container"></div><div id="comment-tools-61963" class="comment-tools"></div><div class="clear"></div><div id="comment-61963-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61967"></span>

<div id="answer-container-61967" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61967-score" class="post-score" title="current number of votes">0</div><span id="post-61967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="https://en.wikipedia.org/wiki/X-Forwarded-For">this Wikipedia article</a>, which discusses how the X-Forwarded-For header is used to keep a proxy server from also turning into an anonymizing service. The article states that:</p><p>"The general format of the field is:"</p><pre><code>X-Forwarded-For: client, proxy1, proxy2</code></pre><p>"where the value is a comma+space separated list of IP addresses, the left-most being the original client, and each successive proxy that passed the request adding the IP address where it received the request from. In this example, the request passed through proxy1, proxy2, and then proxy3 (not shown in the header). proxy3 appears as [the] remote address of the request."</p><p>So it looks like the packets with multiple IP addresses in the X-Forwarded-For header are going through multiple proxies or load balancers before reaching the web server.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '17, 18:37</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-61967" class="comments-container"><span id="61968"></span><div id="comment-61968" class="comment"><div id="post-61968-score" class="comment-score"></div><div class="comment-text"><p>Awesome! Thank you. That answers my question.</p></div><div id="comment-61968-info" class="comment-info"><span class="comment-age">(12 Jun '17, 19:36)</span> <span class="comment-user userinfo">rkwarner2</span></div></div><span id="61976"></span><div id="comment-61976" class="comment"><div id="post-61976-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-61976-info" class="comment-info"><span class="comment-age">(13 Jun '17, 00:50)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-61967" class="comment-tools"></div><div class="clear"></div><div id="comment-61967-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

