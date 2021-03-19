+++
type = "question"
title = "Approved/Recommended Dual NICs"
description = '''We have captured using an old Netgear GA511 for many years. Using Netoptics taps, we capture to both the laptop onboard NIC and the GA511. We occasionally experience minor timestamp differences between them, but nothing we can&#x27;t deal with. We were never sure if it was due to the NICs or the two inst...'''
date = "2012-10-05T11:48:00Z"
lastmod = "2012-10-08T11:06:00Z"
weight = 14738
keywords = [ "nic", "dual-nic" ]
aliases = [ "/questions/14738" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Approved/Recommended Dual NICs](/questions/14738/approvedrecommended-dual-nics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14738-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have captured using an old Netgear GA511 for many years. Using Netoptics taps, we capture to both the laptop onboard NIC and the GA511. We occasionally experience minor timestamp differences between them, but nothing we can't deal with. We were never sure if it was due to the NICs or the two instances of Wireshark that were running. With the advantages of 1.8, we are re-visiting our configuration, and are interested in the possibility of a dual-NIC PC card.<br />
</p><p>Long ago, there was a list of compatible/recommended NICs on the Wireshark (or maybe Ethereal or WinpCap) site. I can't seem to find any such list. Is there a list any more? Do all NICs support promiscuous mode now?<br />
</p><p>Any recommendations for dual-NIC PC cards from the field? Any known problems?</p></div><div id="question-tags" class="tags-container tags">nic dual-nic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Oct '12, 11:48</strong></p><img src="https://secure.gravatar.com/avatar/27f9a3366649276c114a10cbb7a7b277?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bmcmanus&#39;s gravatar image" /><p>bmcmanus<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bmcmanus has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-14738" class="comments-container"></div><div id="comment-tools-14738" class="comment-tools"></div><div class="clear"></div><div id="comment-14738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14779"></span>

<div id="answer-container-14779" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14779-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As far as I know, there is no official list of recommended NICs, neither for Wireshark nor for WinPcap. Both systems are built to work (basically) with every ethernet adapter (and others). However, we all know there are several issues with NIC drivers (Offloading, TCP Chimney, etc.) that make it hard to choose the right one. Even worse, with every driver update problems can shift (one problem fixed, two new added ;-)).</p><p>So, basically, you can just rely on the "recommendation" of people who actually have used one specific adapter.</p><p>Let's see which NICs will be named here. I would name the Intel PRO/1000 PT Dual Port Server Adapter.</p><p>Maybe you want to take a look a TurboCap, a dual/quad port NIC especially built for packet capturing.</p><blockquote><p><code>http://www.riverbed.com/us/products/cascade/wireshark_enhancements/turbocap.php</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '12, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-14779" class="comments-container"><span id="14812"></span><div id="comment-14812" class="comment"><div id="post-14812-score" class="comment-score"></div><div class="comment-text"><p>Kurt - Thanks for the info. The turbocap looks like a great device. We are looking for PC card dual NICs for our analysis laptops, however. Any suggestions from users with those devices?</p></div><div id="comment-14812-info" class="comment-info"><span class="comment-age">(09 Oct '12, 04:27)</span> bmcmanus</div></div><span id="14821"></span><div id="comment-14821" class="comment"><div id="post-14821-score" class="comment-score"></div><div class="comment-text"><p>Oops, I did not see the "PC card" part.</p><p>I know only one ExpressCard with a dual port nic:</p><blockquote><p><code>http://eu.startech.com/Networking-IO/Adapter-Cards/Dual-Port-ExpressCard-Gigabit-Laptop-Ethernet-NIC-Network-Adapter-Card~EC2000S</code><br />
</p></blockquote><p>No experience at all with that card!</p><p>I doubt, that there is any dual port nic with a "PC card" interface.</p><p>Maybe it's time for better/new equipment ;-))</p></div><div id="comment-14821-info" class="comment-info"><span class="comment-age">(09 Oct '12, 10:12)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-14779" class="comment-tools"></div><div class="clear"></div><div id="comment-14779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

