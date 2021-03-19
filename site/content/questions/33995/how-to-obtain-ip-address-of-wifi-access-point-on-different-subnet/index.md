+++
type = "question"
title = "How to obtain IP address of wifi access point on different subnet?"
description = '''So my laptop is connected to a wifi access point that has no security configured. It is setup on a different subnet and the person that setup it&#x27;s IP address can no longer remember what he did. The simplest answer would be reset the AP to factory default but for the sake of argument lets assume that...'''
date = "2014-06-20T09:19:00Z"
lastmod = "2014-06-23T10:19:00Z"
weight = 33995
keywords = [ "wifi", "accesspoint" ]
aliases = [ "/questions/33995" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to obtain IP address of wifi access point on different subnet?](/questions/33995/how-to-obtain-ip-address-of-wifi-access-point-on-different-subnet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33995-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So my laptop is connected to a wifi access point that has no security configured. It is setup on a different subnet and the person that setup it's IP address can no longer remember what he did. The simplest answer would be reset the AP to factory default but for the sake of argument lets assume that isn't an option and set that aside. It seems like there should be a way to figure out the IP address of the AP. I even have its MAC address that I got off of the bottom of the unit. Is there a way that I can about doing this?</p><p>BTW it is my customer's AP here so there is no hacking or troublemaking going on, just trying educate myself.</p></div><div id="question-tags" class="tags-container tags">wifi accesspoint</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '14, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/cc6c871b710016ea3ba7c30fdb3ab6e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aaron%20Hartley&#39;s gravatar image" /><p>Aaron Hartley<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aaron Hartley has no accepted answers">0%</span></p></div></div><div id="comments-container-33995" class="comments-container"></div><div id="comment-tools-33995" class="comment-tools"></div><div class="clear"></div><div id="comment-33995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="34024"></span>

<div id="answer-container-34024" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34024-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way that I can about doing this?</p></blockquote><p>O.K. I assume the device is configured to work as a real <strong>AP</strong> and not as a <strong>router</strong>. If it was a router, it will be the default gateway for all connected clients, so the IP of the AP would be your default gateway (DOS box: route print) as soon as you are connected to the device.</p><p><strong>However</strong> you said <strong>AP</strong>, so here we go:</p><ul><li>Connect the AP network interface (LAN) to a switch</li><li>Connect your sniffer PC to the same switch (same VLAN)</li><li>Start Wireshark</li><li>power-cycle the AP</li></ul><p>Now look for ARP (gratuitous), broadcasts, other frames. If you're lucky, the AP reveals it's IP address in one of those frames.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '14, 17:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34024" class="comments-container"></div><div id="comment-tools-34024" class="comment-tools"></div><div class="clear"></div><div id="comment-34024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="34085"></span>

<div id="answer-container-34085" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34085-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Kurt thanks for responding. You draw an important distinction that I forgot to mention. The AP isn't really an AP but a wireless router, a linksys wrt54g. <strong><em>However</em></strong>, the wrt54g is <strong>not</strong> the gateway for the network, which is a comcast device. I'm assuming the router's DHCP has also been turned off because otherwise the network would be going bonkers (aside from not knowing the IP address of the wrt54g and having unsecured wifi the network otherwise works fine). Aside from scanning the network I also ran IP scan against the default IP for that device, 192.168.1.1 and it turned up nothing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '14, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/cc6c871b710016ea3ba7c30fdb3ab6e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aaron%20Hartley&#39;s gravatar image" /><p>Aaron Hartley<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aaron Hartley has no accepted answers">0%</span></p></div></div><div id="comments-container-34085" class="comments-container"></div><div id="comment-tools-34085" class="comment-tools"></div><div class="clear"></div><div id="comment-34085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

