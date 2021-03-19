+++
type = "question"
title = "Topology map, GUI or otherwise"
description = '''I have a rogue computer on our network somewhere that is attempting to send out spoofed packets using an IP that is not even part of our domain. I see it trying to get out at the firewall because the packets are being rejected. We use a 10 network and the packets are from a 192 IP. I&#x27;m looking for a...'''
date = "2010-09-21T10:56:00Z"
lastmod = "2010-09-21T11:16:00Z"
weight = 249
keywords = [ "identify", "spoofed", "packets", "computer" ]
aliases = [ "/questions/249" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Topology map, GUI or otherwise](/questions/249/topology-map-gui-or-otherwise)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-249-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a rogue computer on our network somewhere that is attempting to send out spoofed packets using an IP that is not even part of our domain. I see it trying to get out at the firewall because the packets are being rejected. We use a 10 network and the packets are from a 192 IP. I'm looking for a way that wireshark might be able to help me identify which switch the computer doing these dastardly deeds might be located so I can narrow down where to look. Does anyone have any suggestions? Thanks!</p></div><div id="question-tags" class="tags-container tags">identify spoofed packets computer</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '10, 10:56</strong></p><img src="https://secure.gravatar.com/avatar/d66f6e2dbd00a0f3185506ae378fd243?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kbirecki&#39;s gravatar image" /><p>kbirecki<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kbirecki has no accepted answers">0%</span></p></div></div><div id="comments-container-249" class="comments-container"></div><div id="comment-tools-249" class="comment-tools"></div><div class="clear"></div><div id="comment-249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="250"></span>

<div id="answer-container-250" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-250-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That totally depends on the network infrastructure. If it's a pure switched network with no routers (other that the firewall), you can use wireshark to capture the packets just before the firewall. Look at the source mac-address of the packets and use the mac-address forwarding tables of your switches to work out on which port this system is attached.</p><p>When other routers are involved, the steps are basically the same, but you will have to work through the steps for each routing hop (as the mac-address that you see on the firewall is the mac-address of the first router on the way to the rogue system).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '10, 11:16</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-250" class="comments-container"><span id="251"></span><div id="comment-251" class="comment"><div id="post-251-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the suggestions. I'm pretty confident it is in one particular office because I only see the denied traffic on one firewall, so I'll see if I can find the MAC address from the firewall or a capture from wireshark. This was very helpful, and a quick response! Thanks!</p></div><div id="comment-251-info" class="comment-info"><span class="comment-age">(21 Sep '10, 11:21)</span> kbirecki</div></div><span id="437"></span><div id="comment-437" class="comment"><div id="post-437-score" class="comment-score"></div><div class="comment-text"><p>I agree with SYNbit and would add that a lot of firewalls today allow you to do captures directly on them. You might try that first as it will be less disruptive to production traffic.</p></div><div id="comment-437-info" class="comment-info"><span class="comment-age">(06 Oct '10, 06:47)</span> blacknight</div></div></div><div id="comment-tools-250" class="comment-tools"></div><div class="clear"></div><div id="comment-250-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

