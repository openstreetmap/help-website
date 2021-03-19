+++
type = "question"
title = "Capturing Between Wireless Router &amp; Cable Modem Problem"
description = '''Hi. I am trying to capture packets bewtween my iPad and the Internet. Since I cannot capture directly from the iPad, I&#x27;m using the hub-and-laptop approach. I have placed a hub between my wireless router and my cable modem, and I have also attached my laptop to the hub, so I can use Wireshark to capt...'''
date = "2011-04-27T18:10:00Z"
lastmod = "2011-04-28T06:43:00Z"
weight = 3770
keywords = [ "ipad", "hub", "cable_modem" ]
aliases = [ "/questions/3770" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing Between Wireless Router & Cable Modem Problem](/questions/3770/capturing-between-wireless-router-cable-modem-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3770-score" class="post-score" title="current number of votes">0</div><span id="post-3770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi.</p><p>I am trying to capture packets bewtween my iPad and the Internet. Since I cannot capture directly from the iPad, I'm using the hub-and-laptop approach.</p><p>I have placed a hub between my wireless router and my cable modem, and I have also attached my laptop to the hub, so I can use Wireshark to capture all the traffic going through the hub. So far, so good... the iPad is still communicating successfully with the Internet, via the wireless router.</p><p>However, when I start capturing packets, I find that I'm only seeing packets in one direction!! It's obvious that packets are going in both directions, since, again, the iPad is communicating successfully.</p><p>Is there something fundamentally wrong with my setup?</p><p>Thx for any enlightenment.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ipad" rel="tag" title="see questions tagged &#39;ipad&#39;">ipad</span> <span class="post-tag tag-link-hub" rel="tag" title="see questions tagged &#39;hub&#39;">hub</span> <span class="post-tag tag-link-cable_modem" rel="tag" title="see questions tagged &#39;cable_modem&#39;">cable_modem</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '11, 18:10</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p><span>feenyman99</span><br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span></p></div></div><div id="comments-container-3770" class="comments-container"></div><div id="comment-tools-3770" class="comment-tools"></div><div class="clear"></div><div id="comment-3770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="3776"></span>

<div id="answer-container-3776" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3776-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3776-score" class="post-score" title="current number of votes">3</div><span id="post-3776-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Wireshark <a href="http://wiki.wireshark.org/HubReference">wiki</a> warns of dual-speed hubs:</p><blockquote><p>Note that "dual-speed" hubs that support both 10MBit and 100MBit ports might not send all unicast traffic between 10MBit and 100MBit ports; if so, you can only capture all traffic between hosts whose Ethernet interfaces are both running at the same speed as the Ethernet interface on the machine capturing traffic.</p></blockquote><p>Does the warning apply in your case?</p><p>You might also be interested in <a href="http://stackoverflow.com/questions/437061/how-do-you-monitor-network-traffic-on-the-iphone">this</a> and <a href="http://blog.jerodsanto.net/2009/06/sniff-your-iphones-network-traffic/">this</a>, which recommends using a WiFi proxy. Yet another alternative is to jailbreak your iPad and use tcpdump (installed from Cydia).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '11, 20:26</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-3776" class="comments-container"></div><div id="comment-tools-3776" class="comment-tools"></div><div class="clear"></div><div id="comment-3776-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3777"></span>

<div id="answer-container-3777" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3777-score" class="post-score" title="current number of votes">1</div><span id="post-3777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>or use a low cost, portable, <a href="http://www.lovemytool.com/blog/2010/04/review-of-dualcomm-5-port-pass-through-port-mirroring-switch-by-betty-dubois.html">port mirroring switch</a> between the AP and cable modem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '11, 22:11</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3777" class="comments-container"></div><div id="comment-tools-3777" class="comment-tools"></div><div class="clear"></div><div id="comment-3777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3784"></span>

<div id="answer-container-3784" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3784-score" class="post-score" title="current number of votes">0</div><span id="post-3784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hmmm... It <em>is</em> a 10/100 hub (Netgear dual speed hub DS104), so I guess this could be the problem, but I have used it many, many times before without any issues whatsoever. The only difference in this current configuration, from previous ones, is that the hub is between a wireless router (Linksys WRT54GS) and a cable modem (Arris TM502G) [on my home LAN]. In the past, I have typically used it between a workstation and its wall jack [at work].</p><p>I'm about to try something else... Instead of tapping into the hub with my laptop, I will use my desktop, to see if that makes a difference.</p><p>One more thing... When I had the laptop plugged into the hub, I did NOT give it an IP address - its IP address was 0.0.0.0. Could this be the problem? (I was reluctant to give it an IP address, because it's on the ISP's side of the router, in their IP space, rather than in my home LAN space.)</p><p>Thx again y'all.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '11, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p><span>feenyman99</span><br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span></p></div></div><div id="comments-container-3784" class="comments-container"></div><div id="comment-tools-3784" class="comment-tools"></div><div class="clear"></div><div id="comment-3784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

