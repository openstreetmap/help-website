+++
type = "question"
title = "Remote RTP monitor of second Tomato router using dual nics"
description = '''My setup: One cable modem (assigned two IP Addresses) to an HP Procurve 1410-8G switch. IP Address 1 to E4200 Tomato router and home network computers. IP Address 2 to E3000 Tomato and IP Phones; Panasonic KX-TGP550T04 base unit plus 3 TPA50 remotes (no computers permanently attached). QoS and bandw...'''
date = "2012-05-20T02:35:00Z"
lastmod = "2012-05-20T13:44:00Z"
weight = 11151
keywords = [ "remote-monitoring", "dual-nic" ]
aliases = [ "/questions/11151" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Remote RTP monitor of second Tomato router using dual nics](/questions/11151/remote-rtp-monitor-of-second-tomato-router-using-dual-nics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11151-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My setup:</p><p>One cable modem (assigned two IP Addresses) to an HP Procurve 1410-8G switch. IP Address 1 to E4200 Tomato router and home network computers. IP Address 2 to E3000 Tomato and IP Phones; Panasonic KX-TGP550T04 base unit plus 3 TPA50 remotes (no computers permanently attached). QoS and bandwidth caps keep things in order.</p><p>I have successfully used Wireshark to run a remote capture of RTP and SIP streams from the Panasonic phones on the VOIP network by attaching a netbook running Wireshark to the E3000, and I have also monitored the streams from the home network softphone using Wireshark on one of the home network computers.</p><p>I would like to monitor the voip network for a while since this is a new setup, but I don't have the luxury of leaving the netbook attached to the E3000.</p><p>Since my main computer on the home network has dual nics, I was wondering if it is possible to connect the unused nic to the voip network to monitor the Panasonic phones on the E3000 without messing up the home network, and how this might be accomplished?</p><p>The E4200 and E3000 have different network addresses (eg 192.168.1.1 and 192.168.2.1) and both act as DHCP servers.</p></div><div id="question-tags" class="tags-container tags">remote-monitoring dual-nic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '12, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/0ed1956853a31a5f01e3b400574dedf9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="semiarid&#39;s gravatar image" /><p>semiarid<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="semiarid has no accepted answers">0%</span></p></div></div><div id="comments-container-11151" class="comments-container"></div><div id="comment-tools-11151" class="comment-tools"></div><div class="clear"></div><div id="comment-11151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11164"></span>

<div id="answer-container-11164" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11164-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I have successfully used Wireshark to run a remote capture of RTP and SIP streams from the Panasonic phones on the VOIP network by attaching a netbook running Wireshark to the E3000</p></blockquote><p>repeat exactly that with your home PC. Connect the unused 2nd nic to the E3000 in the same way you did with the netbook. I just wonder how you captured the traffic, as the switch you mentioned, has no port mirroring features. Is that a feature of the E3000? Could you please comment on this?</p><p>To prevent the PC from getting an IP address from the E300 (DHCP), either disable the "TCP/IP binding" on that nic (nic settings), or give it an arbitrary static IP address (without default gateway). Then start sniffing on that 2nd nic with wireshark, as you did with the laptop.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '12, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-11164" class="comments-container"></div><div id="comment-tools-11164" class="comment-tools"></div><div class="clear"></div><div id="comment-11164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

