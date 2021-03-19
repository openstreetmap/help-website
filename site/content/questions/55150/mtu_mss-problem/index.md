+++
type = "question"
title = "MTU_MSS Problem"
description = '''Ok, I&#x27;m oficially stumped. I have a corporate campus location with a couple of thousand users and all hell broke lose last week. Multiple applications and multiple users affected and the issue was very sporadic. We could find nothing wrong with the local network or WAN but then realized that none of...'''
date = "2016-08-28T14:58:00Z"
lastmod = "2016-08-29T06:04:00Z"
weight = 55150
keywords = [ "mtu" ]
aliases = [ "/questions/55150" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [MTU\_MSS Problem](/questions/55150/mtu_mss-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55150-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ok, I'm oficially stumped. I have a corporate campus location with a couple of thousand users and all hell broke lose last week. Multiple applications and multiple users affected and the issue was very sporadic. We could find nothing wrong with the local network or WAN but then realized that none of the Network Engineers were having any issues and the only difference between the Network Engineers other employees is that the Network Engineers have the Cisco VPN client installed with automatically lowers the NIC MTUs to 1300 bytes. On a hunch, we added ip tcp adjust-mss 1300 to the WAN routers and the problems instantly ceased for all users. So now we need to figure out what the hell happened. We have taken a capture from a workstation at an affected site and don't really see too much to worry about. There are some zero windows, but nothing to drastic. So my question is, does anyone have recommandations of what to look for in the capture files? We have already ruled out any WAN issues, so this is looking like a problem in the Data Center. Any thoughts would be greatly apprciated.</p></div><div id="question-tags" class="tags-container tags">mtu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '16, 14:58</strong></p><img src="https://secure.gravatar.com/avatar/1644e3ecddbd85b98d19853797a62751?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill7710&#39;s gravatar image" /><p>Bill7710<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill7710 has no accepted answers">0%</span></p></div></div><div id="comments-container-55150" class="comments-container"></div><div id="comment-tools-55150" class="comment-tools"></div><div class="clear"></div><div id="comment-55150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55163"></span>

<div id="answer-container-55163" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55163-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You won't see anything useful from a single capture file. You need to create, between the server and client machines which suffer from the issue in their regular communication, a TCP session which attempts to make use of the available MTU (like a ftp transfer of a large file) and see it fail after you disable the adjust-mss rule on that path. After that, you'll have to capture in two points, first at the server and at the client, and see the long packet to be sent from one of them but not reach the other. Then, you would keep one capturing point at the source and move the other one to the middle of the path to destination, and repeat the test to see whether the large packet has made it to the middle point or not. By repeating these steps while moving the capture points along the path, you should be able to isolate the section of the path which causes the issue.</p><p>The issue may be a misconfiguration of the MTU itself or too thorough filtering of icmp, preventing the MSS auto-detection from working by filtering icmp segmentation requests.</p><p>If the issue appears only sometimes even for file transfers, which normally do make use of the MSS available, there may be some dynamic routing in your network, causing the problematic section to be used in some transfers but not in others.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '16, 06:04</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-55163" class="comments-container"></div><div id="comment-tools-55163" class="comment-tools"></div><div class="clear"></div><div id="comment-55163-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

