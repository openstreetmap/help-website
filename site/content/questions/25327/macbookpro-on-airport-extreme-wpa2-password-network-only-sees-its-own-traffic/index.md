+++
type = "question"
title = "MacBookPro on Airport Extreme WPA2 Password Network Only Sees Its Own Traffic"
description = '''Hi, I have a MacBookPro3,1 (OS X 10.8.5) on an Airport Extreme network. I am running Wireshark 1.10.2. The problem I have is that I only see traffic directed to/from my system, despite the fact I know that there is other traffic on the WiFi network (such as from an identical MBP next to the one runn...'''
date = "2013-09-27T19:45:00Z"
lastmod = "2013-09-28T02:04:00Z"
weight = 25327
keywords = [ "captureproblems", "macbookpro", "airportextreme", "wpa2password" ]
aliases = [ "/questions/25327" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MacBookPro on Airport Extreme WPA2 Password Network Only Sees Its Own Traffic](/questions/25327/macbookpro-on-airport-extreme-wpa2-password-network-only-sees-its-own-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25327-score" class="post-score" title="current number of votes">0</div><span id="post-25327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a MacBookPro3,1 (OS X 10.8.5) on an Airport Extreme network. I am running Wireshark 1.10.2. The problem I have is that I only see traffic directed to/from my system, despite the fact I know that there is other traffic on the WiFi network (such as from an identical MBP next to the one running WireShark and streaming traffic to Apple TV). I will qualify that by saying that I see broadcast and multicast traffic from other devices (ARP, MDNS, etc.), but no point-to-point traffic.</p><p>The network is secured with WPA2 password. The laptop's wireless interface (en1) is in promiscuous mode. But, I only see my own traffic. All devices are on the 5GHz network.</p><p>Any idea what I may be doing wrong?</p><p>TIA!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-captureproblems" rel="tag" title="see questions tagged &#39;captureproblems&#39;">captureproblems</span> <span class="post-tag tag-link-macbookpro" rel="tag" title="see questions tagged &#39;macbookpro&#39;">macbookpro</span> <span class="post-tag tag-link-airportextreme" rel="tag" title="see questions tagged &#39;airportextreme&#39;">airportextreme</span> <span class="post-tag tag-link-wpa2password" rel="tag" title="see questions tagged &#39;wpa2password&#39;">wpa2password</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '13, 19:45</strong></p><img src="https://secure.gravatar.com/avatar/17657d1bd0b14e8a1f519b1d158e7185?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Human31&#39;s gravatar image" /><p><span>Human31</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Human31 has no accepted answers">0%</span></p></div></div><div id="comments-container-25327" class="comments-container"><span id="25328"></span><div id="comment-25328" class="comment"><div id="post-25328-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The laptop's wireless interface (en1) is in promiscuous mode</p></blockquote><p>Is it in <em>monitor</em> mode? (If the traffic you're capturing has Ethernet headers, it's <em>not</em> in monitor mode.)</p></div><div id="comment-25328-info" class="comment-info"><span class="comment-age">(27 Sep '13, 23:33)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-25327" class="comment-tools"></div><div class="clear"></div><div id="comment-25327-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25330"></span>

<div id="answer-container-25330" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25330-score" class="post-score" title="current number of votes">0</div><span id="post-25330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have tried enabling monitor mode, and it simply adds to the mix the AP's broadcast frames, and my MPB's layer 2 traffic (protocol 802.11).</p><p>If I filter on wlan.addr for my MAC, I get all my traffic, both IP and layer 2.</p><p>If I filter on the MAC for any other system on the network that is actively sending/receiving, I only get the IP broadcast or multicast traffic that originates from those systems. I see none of their layer 2 traffic and none of their other IP traffic.</p><p>Bottom line: For some reason it is acting as if my wireless interface is not getting set to promiscuous mode. However, the interface clearly thinks it is in promiscuous mode:</p><p><strong>$ ifconfig en1</strong></p><p><strong>en1: flags=8963 UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST mtu 1500</strong></p><p>Any other ideas? PLEASE!!</p><p>I should add that I never had problems under Snow Leopard, that it only started after an upgrade to Mt. Lion (a year ago?) and I have ignored the problem until now, but I'm desperate to get it working to help debug some other aving.</p><p>TIA!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '13, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/17657d1bd0b14e8a1f519b1d158e7185?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Human31&#39;s gravatar image" /><p><span>Human31</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Human31 has no accepted answers">0%</span></p></div></div><div id="comments-container-25330" class="comments-container"></div><div id="comment-tools-25330" class="comment-tools"></div><div class="clear"></div><div id="comment-25330-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

