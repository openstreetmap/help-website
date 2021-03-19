+++
type = "question"
title = "Filter packets between two devices in a capture"
description = '''Hello, I want to filter communication between two devices in a capture, regardless if the device is sender or receiver of a packet. Device 1 has the IP-Address 192.168.12.160 and device 2 has 192.168.12.161. How can I do that? Thanks. Darius'''
date = "2016-05-18T06:24:00Z"
lastmod = "2016-07-13T03:53:00Z"
weight = 52719
keywords = [ "capture-filters" ]
aliases = [ "/questions/52719" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Filter packets between two devices in a capture](/questions/52719/filter-packets-between-two-devices-in-a-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52719-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52719-score" class="post-score" title="current number of votes">0</div><span id="post-52719-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I want to filter communication between two devices in a capture, regardless if the device is sender or receiver of a packet. Device 1 has the IP-Address 192.168.12.160 and device 2 has 192.168.12.161. How can I do that? Thanks.</p><p>Darius</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filters" rel="tag" title="see questions tagged &#39;capture-filters&#39;">capture-filters</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '16, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/aa79cc5d06f12ca6e9f588ac7e6bd288?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Darius&#39;s gravatar image" /><p><span>Darius</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Darius has no accepted answers">0%</span></p></div></div><div id="comments-container-52719" class="comments-container"><span id="52725"></span><div id="comment-52725" class="comment"><div id="post-52725-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the quick answers.</p></div><div id="comment-52725-info" class="comment-info"><span class="comment-age">(18 May '16, 07:14)</span> <span class="comment-user userinfo">Darius</span></div></div></div><div id="comment-tools-52719" class="comment-tools"></div><div class="clear"></div><div id="comment-52719-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52720"></span>

<div id="answer-container-52720" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52720-score" class="post-score" title="current number of votes">0</div><span id="post-52720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>ip.addr== 192.168.12.160 and ip.addr==192.168.12.161</p><p>The "ip.addr" checks if either source or destination field match, so if you force both with "and" you'll only get conversations between those two.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 May '16, 06:29</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-52720" class="comments-container"><span id="54024"></span><div id="comment-54024" class="comment"><div id="post-54024-score" class="comment-score"></div><div class="comment-text"><p>Doesn't work for me.</p><p>I'm also trying to capture traffic between a router and a Phone (VOIP)</p><p>I have Wireshark 2.0.4 network is a IP-VPN</p><p>pc with wireshark have ip 10.11.7.20 router ip 10.11.27.254 Phone ip 10.11.27.7</p><p>I can ping from 10.11.7.20 to 10.11.27.254 and 10.11.27.7</p><p>When i set the display filter; ip.addr==10.11.27.254 and ip.addr==10.11.27.7 traffic is not shown.</p><p>What am i doing wrong?</p></div><div id="comment-54024-info" class="comment-info"><span class="comment-age">(13 Jul '16, 02:33)</span> <span class="comment-user userinfo">George Bonset</span></div></div><span id="54025"></span><div id="comment-54025" class="comment"><div id="post-54025-score" class="comment-score"></div><div class="comment-text"><p>Be more specific on the exact hardware interconnection you use. E.g. if your capturing PC is connected to a normal port of a switch to which the ip phone and the router are connected too, the traffic you are interested in never reaches the switch port to which your PC is connected, hence you cannot capture it. See <a href="https://wiki.wireshark.org/CaptureSetup">Wireshark Wiki on capture setup</a> for details.</p></div><div id="comment-54025-info" class="comment-info"><span class="comment-age">(13 Jul '16, 02:52)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="54026"></span><div id="comment-54026" class="comment"><div id="post-54026-score" class="comment-score"></div><div class="comment-text"><p>so, you can not use wireshark on a remote pc then. Even if it's in a ip-vpn network</p></div><div id="comment-54026-info" class="comment-info"><span class="comment-age">(13 Jul '16, 03:05)</span> <span class="comment-user userinfo">George Bonset</span></div></div><span id="54028"></span><div id="comment-54028" class="comment"><div id="post-54028-score" class="comment-score"></div><div class="comment-text"><p>That depends on what exactly means remote. You haven't provided your topology, but I assume that your PC has a normal internet connection and a VPN interface which gets an address from the 10.11.7.0/24 subnet while the devices you wish to capture are in 10.11.27.0/24 subnet. In this case, your chances for direct capture are very low because there is a routing between the two subnets.</p><p>If, however, both your PC's VPN address and the two remote devices are in 10.11.0.0/16 subnet, your chances are higher if you can convince the virtual switch at the remote end to send a copy of the traffic between the two devices to your VPN interface's virtual MAC address.</p><p>It may also be possible to run a capture directly on the router and let it store it into a file (many of them allow this, albeit most of them have storage space limitation so you can only capture short periods of time) or, instead, to send you a copy of the traffic matching a capture filter encapsulated into UDP packets with a special header (this is what e.g. Mikrotik routers can do).</p><p>If the router is linux-based, you may run tcpdump on it, saving the capture to a file and download the file for opening in Wireshark on your PC, or pipe it to the PC if storage space is small (see other Questions on this site for a howto).</p><p>For capturing at one of the devices involved in the captured communication (the router) one way or another, it is not important whether your PC's VPN interface shares a subnet with the captured devices' interfaces or not.</p></div><div id="comment-54028-info" class="comment-info"><span class="comment-age">(13 Jul '16, 03:53)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-52720" class="comment-tools"></div><div class="clear"></div><div id="comment-52720-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52721"></span>

<div id="answer-container-52721" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52721-score" class="post-score" title="current number of votes">0</div><span id="post-52721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at using ip.addr in your address filter. It is created for both source and destination IPv4 address. You can find more info <a href="https://wiki.wireshark.org/DisplayFilters">in the Wiki</a> and <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html">in the Users Guide</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 May '16, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-52721" class="comments-container"></div><div id="comment-tools-52721" class="comment-tools"></div><div class="clear"></div><div id="comment-52721-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

