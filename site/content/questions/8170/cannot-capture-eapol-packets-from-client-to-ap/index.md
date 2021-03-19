+++
type = "question"
title = "Cannot capture EAPOL packets from client to AP"
description = '''Hi, I&#x27;m new to wireshark, and I&#x27;ve spent many hours searching online and troubleshooting this peculiar behavior. I have a simple topology, just two computers wirelessly connected to a router, using WPA encryption. I&#x27;ve set up my wireshark to decrypt packets, by going into the IEEE 802.11 protocol se...'''
date = "2011-12-31T11:38:00Z"
lastmod = "2011-12-31T11:38:00Z"
weight = 8170
keywords = [ "decryption", "eapol", "wpa" ]
aliases = [ "/questions/8170" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot capture EAPOL packets from client to AP](/questions/8170/cannot-capture-eapol-packets-from-client-to-ap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8170-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm new to wireshark, and I've spent many hours searching online and troubleshooting this peculiar behavior. I have a simple topology, just two computers wirelessly connected to a router, using WPA encryption. I've set up my wireshark to decrypt packets, by going into the IEEE 802.11 protocol setting and enabling decryption with the key wpa-pwd:password:SSID, as explained in <a href="http://wiki.wireshark.org/HowToDecrypt802.11">here</a></p><p>With one computer I'm trying to capture the packets exchanged between the other computer and the router. However, regardless of which computer I use to capture the packets (I have wireshark installed on both) I cannot capture all four of the EAPOL handshake packets. Instead, I can only capture those EAPOL packets going from access point to client (packets 1/4 and 3/4). I'm pretty sure this has nothing to do with the wireless strength of my client, because my computers are right next to each other and they ARE receiving broadcast packets from one another. Furthermore if I turn off the encryption, then they can capture one another's packets just fine. Also, everybody's on channel 11 and using 802.11b so I've ruled that out as well. Does anyone have any idea of what else I should try to do to figure out what's going on? I really appreciate your help!</p></div><div id="question-tags" class="tags-container tags">decryption eapol wpa</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '11, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/0b145a77e0aaa86fbb591f5c639c42a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bhh1988&#39;s gravatar image" /><p>bhh1988<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bhh1988 has no accepted answers">0%</span></p></div></div><div id="comments-container-8170" class="comments-container"><span id="9947"></span><div id="comment-9947" class="comment"><div id="post-9947-score" class="comment-score"></div><div class="comment-text"><p>I am also facing the same issue. not able to see packets 1/4 and 3/4 from the 4 way handshake during <a href="http://WPA2.Is">WPA2.Is</a> there any resolution for this? Is this a bug or a hardware limitation. I have a professional sniffer, Omnipeek. I was able to capture all packets using it. I am using Ubiquiti sr71x wlan interface, wireshark 1.4.6, ubuntu 11.04.</p></div><div id="comment-9947-info" class="comment-info"><span class="comment-age">(04 Apr '12, 19:47)</span> mohit</div></div></div><div id="comment-tools-8170" class="comment-tools"></div><div class="clear"></div><div id="comment-8170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

