+++
type = "question"
title = "Ideas for configuring catpure for outgoing Internet traffic?"
description = '''At a site I monitor, the cable modem seems to go out often, and Comcast states the issue is  internal to our network. We&#x27;ve tried 3 modems throughout the year, all with same results, so I would like to try caputuring packets to see if there may be malformed packets causing the problem.  Cable modem ...'''
date = "2011-01-06T13:10:00Z"
lastmod = "2011-01-06T15:54:00Z"
weight = 1654
keywords = [ "capture", "remote", "external" ]
aliases = [ "/questions/1654" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Ideas for configuring catpure for outgoing Internet traffic?](/questions/1654/ideas-for-configuring-catpure-for-outgoing-internet-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1654-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>At a site I monitor, the cable modem seems to go out often, and Comcast states the issue is internal to our network. We've tried 3 modems throughout the year, all with same results, so I would like to try caputuring packets to see if there may be malformed packets causing the problem.<br />
</p><p>Cable modem -&gt; Passive HUB -&gt; WatchGuard X55 Edge firewall WAN1 port. LAN0 port -&gt; Dell Switch for internal network. I've setup a separate computer to act as the remote capture computer, and placed it on a hub between the cable modem and the firewall WAN0 port.<br />
</p><p>If this is the best method, what must I do on the firewall to reach that external PC? If it's set as DHCP client, will it interfere with the cabel modem picking up an IP from Comcast? I would like to run captures from a computer located on the internal LAN. Thanks for any help. Did not notice anything in docs discussing this.</p><p>Walt</p></div><div id="question-tags" class="tags-container tags">capture remote external</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '11, 13:10</strong></p><img src="https://secure.gravatar.com/avatar/ff818382a2364a0fbfca4e20fa26607b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Romseye&#39;s gravatar image" /><p>Romseye<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Romseye has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-1654" class="comments-container"></div><div id="comment-tools-1654" class="comment-tools"></div><div class="clear"></div><div id="comment-1654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1657"></span>

<div id="answer-container-1657" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1657-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The best thing to do in this case is to install second NIC on your monitoring PC and possibly plug that in to your firewall or DMZ. Then just VNC (for Linux) or Windows Remote Desktop to control that PC. That way your monitoring interface on your capture PC doesn't need to have an IP address, just on the management interface. (I use a USB-Ethernet dongle for this purpose quite often, and use the built-in Ethernet on my laptop for the packetcpature).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '11, 15:54</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-1657" class="comments-container"></div><div id="comment-tools-1657" class="comment-tools"></div><div class="clear"></div><div id="comment-1657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

