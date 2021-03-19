+++
type = "question"
title = "Capturing handshake packets"
description = '''Hi to all! I&#x27;m using Wireshark in BackTrack, with an Alfa AWUS036H as wireless interface, put in monitor mode. I&#x27;m trying to analyze the traffic in my wireless network: if there&#x27;s no protection, I can capture the packets and analyze them; if the network is protected with WPA, following this guide: h...'''
date = "2012-04-08T13:31:00Z"
lastmod = "2012-04-08T13:31:00Z"
weight = 10016
keywords = [ "handshake", "packets" ]
aliases = [ "/questions/10016" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing handshake packets](/questions/10016/capturing-handshake-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10016-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi to all! I'm using Wireshark in BackTrack, with an Alfa AWUS036H as wireless interface, put in monitor mode. I'm trying to analyze the traffic in my wireless network: if there's no protection, I can capture the packets and analyze them; if the network is protected with WPA, following this guide: <a href="http://wiki.wireshark.org/HowToDecrypt802.11">http://wiki.wireshark.org/HowToDecrypt802.11</a></p><p>I added the wpa-psk in the preferences. So, I can capture the packets, but I can't decrypt them. Then, I discovered that I need 4 handshake packets, so I disconnected and reconnected a client to the AP to get them, but still can't decrypt the packets. Analyzing the traffic using as filter "eapol", I can see several packets, named: Key (msg 1/4) Key (msg 2/4) Key (Group msg 1/2) Key (Group msg 2/2)</p><p>My question is: since I need 4 handshake packets and I can see only Key (msg 1/4) and Key (msg 2/4) (I don't know about Group msg... - maybe broadcast packet?), this means I'm missing Key (msg 3/4) and Key (msg 4/4)? Or I have another problem that doesn't allow me to decrypt packets?</p><p>Many thanks in advance for your help! :)</p></div><div id="question-tags" class="tags-container tags">handshake packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '12, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/7be5d0dc6efe68ffb885d38f456f38e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mr%20Wolf&#39;s gravatar image" /><p>Mr Wolf<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mr Wolf has no accepted answers">0%</span></p></div></div><div id="comments-container-10016" class="comments-container"></div><div id="comment-tools-10016" class="comment-tools"></div><div class="clear"></div><div id="comment-10016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

