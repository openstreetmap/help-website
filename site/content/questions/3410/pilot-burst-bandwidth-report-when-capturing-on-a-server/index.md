+++
type = "question"
title = "Pilot burst bandwidth report when capturing on a server"
description = '''I installed WireShark on a streaming media server to perform a capture. This server is on its own switch port, but in a ip subnet that has other servers. So the streaming media server can see traffic intended for other servers, yet it is on its own 1Gigabit link to the switch.  So here’s my question...'''
date = "2011-04-09T14:13:00Z"
lastmod = "2011-04-19T16:29:00Z"
weight = 3410
keywords = [ "burst", "server", "pilot" ]
aliases = [ "/questions/3410" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Pilot burst bandwidth report when capturing on a server](/questions/3410/pilot-burst-bandwidth-report-when-capturing-on-a-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3410-score" class="post-score" title="current number of votes">0</div><span id="post-3410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I installed WireShark on a streaming media server to perform a capture. This server is on its own switch port, but in a ip subnet that has other servers. So the streaming media server can see traffic intended for other servers, yet it is on its own 1Gigabit link to the switch.</p><p>So here’s my question: when the burst bandwidth report (1ms) says the bandwidth in this capture is bursting to 1.4Gigabit, is that truly just for this link the server is on, or is that traffic not intended for this server that shows up in the reports muddling this result?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-burst" rel="tag" title="see questions tagged &#39;burst&#39;">burst</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-pilot" rel="tag" title="see questions tagged &#39;pilot&#39;">pilot</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '11, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/7df3f9a4b16eae9f77feb6eabe92919e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eelarry&#39;s gravatar image" /><p><span>eelarry</span><br />
<span class="score" title="36 reputation points">36</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eelarry has no accepted answers">0%</span></p></div></div><div id="comments-container-3410" class="comments-container"><span id="3624"></span><div id="comment-3624" class="comment"><div id="post-3624-score" class="comment-score"></div><div class="comment-text"><p>Riverbed: We can see the bandwidth reported on the 1ms views seem to exceed the linkspeed, which should not be possible.</p><p>In Windows, using a normal NIC, the OS handles time-stamping the arriving packets. Depending on what else the OS is handling, there can be some delay in the time-stamping process and several packets collected in the buffer may be recorded with the same time-stamp.<br />
</p><p>TurboCap capture card, when installed in a Linux box, time stamping can be made more accurate by assigning one of the CPU's processor This will result in much greater accuracy for the sub-second burst views.</p></div><div id="comment-3624-info" class="comment-info"><span class="comment-age">(19 Apr '11, 16:29)</span> <span class="comment-user userinfo">eelarry</span></div></div></div><div id="comment-tools-3410" class="comment-tools"></div><div class="clear"></div><div id="comment-3410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3411"></span>

<div id="answer-container-3411" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3411-score" class="post-score" title="current number of votes">1</div><span id="post-3411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="eelarry has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You're kind of in the wrong place to ask questions about "Pilot", this is the Wireshark Q&amp;A site. The "Burst bandwidth report" is pure Pilot functionality. You might want to contact Pilot support.</p><p>However, I'll give it a shot: Are you looking at the combined bandwidth (in and out)? If so, the maximum output that you can expect is 2Gbit/s on a full-duplex Gbit/s link. And since your on a switch, this should only be traffic to/from the streaming media server on which you are capturing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '11, 15:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></p></div></div><div id="comments-container-3411" class="comments-container"><span id="3412"></span><div id="comment-3412" class="comment"><div id="post-3412-score" class="comment-score"></div><div class="comment-text"><p>I agree--I thought I would only see traffic for this server, but I'm seeing many other conversations and I don't know why, unless this switch, which happens to be an HP 1800 with old firmware, is not doing its job.</p></div><div id="comment-3412-info" class="comment-info"><span class="comment-age">(09 Apr '11, 18:05)</span> <span class="comment-user userinfo">eelarry</span></div></div><span id="3414"></span><div id="comment-3414" class="comment"><div id="post-3414-score" class="comment-score"></div><div class="comment-text"><p>Okay, the traffic I'm seeing that should not be on this port is from a Microsoft load balancer, but I still don't know why it is seen there.</p></div><div id="comment-3414-info" class="comment-info"><span class="comment-age">(09 Apr '11, 20:30)</span> <span class="comment-user userinfo">eelarry</span></div></div><span id="3415"></span><div id="comment-3415" class="comment"><div id="post-3415-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answers" to "comments" as that's the way this site works best, see the FAQ)</p><p>Microsoft loadbalancing works by flooding all incoming traffic to all ports in the vlan. This is done by having a virtual mac-address that is used for only incoming traffic (the arp response gives out the address). Outgoing traffic never uses this mac-address and therefor the switch must flood the traffic.</p></div><div id="comment-3415-info" class="comment-info"><span class="comment-age">(10 Apr '11, 00:05)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="3421"></span><div id="comment-3421" class="comment"><div id="post-3421-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply and the forum tips! So MS load balancing is flooding to all ports in the vlan and making them process traffic they should not be seeing! Sounds like the reason this network is experiencing problems under even moderate loads.</p></div><div id="comment-3421-info" class="comment-info"><span class="comment-age">(10 Apr '11, 08:17)</span> <span class="comment-user userinfo">eelarry</span></div></div><span id="3424"></span><div id="comment-3424" class="comment"><div id="post-3424-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure if Microsoft also suggests this, but I would always put a Microsoft Network Loadbalancing cluster in a separate vlan to make sure no other systems will get all the incoming traffic.</p></div><div id="comment-3424-info" class="comment-info"><span class="comment-age">(10 Apr '11, 09:46)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-3411" class="comment-tools"></div><div class="clear"></div><div id="comment-3411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

