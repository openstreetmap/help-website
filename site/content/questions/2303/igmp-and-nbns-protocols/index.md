+++
type = "question"
title = "IGMP and NBNS protocols"
description = '''Hi I am trying to do packet analysis of my network. I have directly connected my computer with my home router. At the wireshark capture, the first 6 packets are sent through the NBNS protocol (source IP: 192.168.1.255 and destination IP: 192.168.1.255) whereas the 7th packet is sent through the IGMP...'''
date = "2011-02-13T09:03:00Z"
lastmod = "2011-02-14T23:10:00Z"
weight = 2303
keywords = [ "nbns", "protocols", "igmp" ]
aliases = [ "/questions/2303" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IGMP and NBNS protocols](/questions/2303/igmp-and-nbns-protocols)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2303-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am trying to do packet analysis of my network. I have directly connected my computer with my home router.</p><p>At the wireshark capture, the first 6 packets are sent through the NBNS protocol (source IP: 192.168.1.255 and destination IP: 192.168.1.255) whereas the 7th packet is sent through the IGMP protocol (source IP: 192.168.1.1 and destination IP: 224.0.0.12). Is this normal?</p><p>then I open the internet explorer to connect with wwww.microsoft.com and it does the TCP handshake with 6 different IP addresses. Is this normal? some of these TCP handshakes connect with msn and microsoft IP but some other connect to some IP like bnetfile or autonomy or hpvmm control kwdb-commn (according to the Info Tab of the of the packet list pane)</p><p>thanks in advance</p></div><div id="question-tags" class="tags-container tags">nbns protocols igmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '11, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/e15247a28980167b64a8419f60a71e7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stefi&#39;s gravatar image" /><p>Stefi<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stefi has no accepted answers">0%</span></p></div></div><div id="comments-container-2303" class="comments-container"></div><div id="comment-tools-2303" class="comment-tools"></div><div class="clear"></div><div id="comment-2303-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2337"></span>

<div id="answer-container-2337" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2337-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The first time I looked at the network traffic being sent by my PC, I was pretty amazed at all the stuff that goes on "under the covers" and the number of sites contacted by my browser. :)</p><p>What you describe doesn't particularly sound strange, although I can't speak to the destinations being contacted by IE.</p><p>Delving into the network traffic in &amp; out of your PC can be a great learning experience, but it can also be a bit overwhelming since there's a lot of different protocols which normally get used:</p><p>E.G., Everything from HTTP (hyper text transfer protocol) to DNS (domain name system) to NTP (network time protocol) to NBNS (netbios naming service) to IGMP (internet group management protocol) to ....</p><p>Welcome to the world of networking !</p><p>Is there a particular issue that you want to address by doing the packet analysis ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '11, 23:10</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-2337" class="comments-container"></div><div id="comment-tools-2337" class="comment-tools"></div><div class="clear"></div><div id="comment-2337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

