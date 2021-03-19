+++
type = "question"
title = "When I capture ping test in Wireshark, I only see the Reply  and no Request, why?"
description = '''I was doing a connectivity test by sending ping from a host to a destination IP@. I was only seeing the Reply to the ping but not the Request in Wireshark. Is this normal? I was expecting to see a line for the ping Request and another line for the ping Reply'''
date = "2012-04-21T08:29:00Z"
lastmod = "2012-04-25T07:52:00Z"
weight = 10377
keywords = [ "ping" ]
aliases = [ "/questions/10377" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [When I capture ping test in Wireshark, I only see the Reply and no Request, why?](/questions/10377/when-i-capture-ping-test-in-wireshark-i-only-see-the-reply-and-no-request-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10377-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was doing a connectivity test by sending ping from a host to a destination [email protected] I was only seeing the Reply to the ping but not the Request in Wireshark. Is this normal? I was expecting to see a line for the ping Request and another line for the ping Reply</p></div><div id="question-tags" class="tags-container tags">ping</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '12, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/ca47e779dd1311b9d9d63eb8c3ad2a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="redeem314&#39;s gravatar image" /><p>redeem314<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="redeem314 has no accepted answers">0%</span></p></div></div><div id="comments-container-10377" class="comments-container"><span id="10449"></span><div id="comment-10449" class="comment"><div id="post-10449-score" class="comment-score"></div><div class="comment-text"><p>was there any display or capture filter in place (Display: ip.src / ip.dst Capture: src / dst)?</p></div><div id="comment-10449-info" class="comment-info"><span class="comment-age">(25 Apr '12, 17:00)</span> Kurt Knochner ♦</div></div><span id="14485"></span><div id="comment-14485" class="comment"><div id="post-14485-score" class="comment-score"></div><div class="comment-text"><p>I have a similar problem. I have a WLAN interface and a VPN interface. On the WLAN I can see both requests and replies. But on the VPN interface I can only see replies.</p></div><div id="comment-14485-info" class="comment-info"><span class="comment-age">(24 Sep '12, 13:06)</span> Michael Closson</div></div><span id="15412"></span><div id="comment-15412" class="comment"><div id="post-15412-score" class="comment-score"></div><div class="comment-text"><p>Hi I am having the same problem. I am seeing the reply packets but not the request packets. Any ideas as to what the problem can be?</p><p>[I am running Wireshark v1.8.3 on Windows 7]</p></div><div id="comment-15412-info" class="comment-info"><span class="comment-age">(31 Oct '12, 02:59)</span> tcal0005</div></div><span id="15415"></span><div id="comment-15415" class="comment"><div id="post-15415-score" class="comment-score"></div><div class="comment-text"><p>I have solved my problem - my firewall was blocking the packets.</p></div><div id="comment-15415-info" class="comment-info"><span class="comment-age">(31 Oct '12, 03:31)</span> tcal0005</div></div><span id="40449"></span><div id="comment-40449" class="comment"><div id="post-40449-score" class="comment-score"></div><div class="comment-text"><p>I can't see the reply packets instead.</p></div><div id="comment-40449-info" class="comment-info"><span class="comment-age">(10 Mar '15, 13:27)</span> cbehling</div></div></div><div id="comment-tools-10377" class="comment-tools"></div><div class="clear"></div><div id="comment-10377-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10439"></span>

<div id="answer-container-10439" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10439-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should see the icmp request also. It all depends on where your packet capture point is. Are there multiple paths between the two hosts in question? It's possible the icmp request went one path while the reply was returned over a different path. How are your Wireshark filters setup? Can you see bi-directional traffic from both hosts your interested in?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '12, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/a00c3e32ea96f4989d9360937a93c73f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeoffP&#39;s gravatar image" /><p>GeoffP<br />
<span class="score" title="40 reputation points">40</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeoffP has no accepted answers">0%</span></p></div></div><div id="comments-container-10439" class="comments-container"></div><div id="comment-tools-10439" class="comment-tools"></div><div class="clear"></div><div id="comment-10439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

