+++
type = "question"
title = "How can I capture HTTP on WLAN with AirPCap?"
description = '''Hello all, I am using WireShark 1.12.0 and an AirPCap from Riverbed to analyze communication between a Wi-Fi device (it&#x27;s an RN-171-EK, so I&#x27;ll call it an RN-171 from here on out) and a server. I am not a network admin, so I am looking for some remedial assistance (read: I don&#x27;t know what I&#x27;m doing)...'''
date = "2014-09-10T05:51:00Z"
lastmod = "2014-09-10T08:32:00Z"
weight = 36158
keywords = [ "1.12.0", "airpcap", "http", "wifi" ]
aliases = [ "/questions/36158" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How can I capture HTTP on WLAN with AirPCap?](/questions/36158/how-can-i-capture-http-on-wlan-with-airpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36158-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I am using WireShark 1.12.0 and an AirPCap from Riverbed to analyze communication between a Wi-Fi device (it's an RN-171-EK, so I'll call it an RN-171 from here on out) and a server. I am not a network admin, so I am looking for some remedial assistance (read: I don't know what I'm doing).</p><p>I can capture some traffic between my RN-171 and my wireless router because I can see the MAC addresses of each in the source and destination fields. These packets are all categorized as "802.11" in the protocol field and the info in all of the packets are either QoS Data or Probe Request.</p><p>What I was expecting (hoping, really) to see was IP addresses in the source and destination fields and "HTTP" in the protocol field, with the actual calls to the web service and the response from the server in the Info field.</p><p>The RN-171 reports which channel it is using when it associates with my wireless network, so I adjust the channel I am monitoring appropriately. I have tried toggling the promiscuous mode and the "capture packets in pcap-ng format" settings, but I find I am blindly making changes because I don't know how to configure the WireShark/AirPCap combo appropriately to see the actual HTTP traffic.</p><p>Can anyone help me with how to configure the settings to see HTTP traffic?</p><p>Thank you,</p><p>-Ted</p></div><div id="question-tags" class="tags-container tags">1.12.0 airpcap http wifi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '14, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/e3d1246c6effdb644f67dab8a2c9c08a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fiasco&#39;s gravatar image" /><p>Fiasco<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fiasco has no accepted answers">0%</span></p></div></div><div id="comments-container-36158" class="comments-container"><span id="36164"></span><div id="comment-36164" class="comment"><div id="post-36164-score" class="comment-score">1</div><div class="comment-text"><p>Is the WLAN encrypted? If it is, you won't see anything useful like HTTP before decrypting it with the Decryption key.</p></div><div id="comment-36164-info" class="comment-info"><span class="comment-age">(10 Sep '14, 06:23)</span> Jasper ♦♦</div></div><span id="36165"></span><div id="comment-36165" class="comment"><div id="post-36165-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jasper.<br />
</p><p>The WLAN is indeed encrypted. I entered the SSID and Passphrase via the Decryption Keys Management window. I have double-checked the SSID and Passphrase and they are correct. And now triple-checked, just to make sure. I also have "Wireshark" selected as the decryption mode.<br />
</p><p>I should have mentioned this in the original post. I'm sure I've not mentioned much more, but I don't know what is important to take note of. Does it matter the version of winpcap (4.1.3) installed alongside the AirPCap software (also 4.1.3)?</p></div><div id="comment-36165-info" class="comment-info"><span class="comment-age">(10 Sep '14, 06:41)</span> Fiasco</div></div><span id="36167"></span><div id="comment-36167" class="comment"><div id="post-36167-score" class="comment-score"></div><div class="comment-text"><p>Ok, I have to admit my WLAN analysis skills are quite limited - if everything works fine you should see decrypted traffic. If you don't there may be something wrong, but I'm no expert in troubleshooting WLAN traffic. Maybe someone else can help out here.</p><p>I think winpcap and AirPCap versions are fine.</p></div><div id="comment-36167-info" class="comment-info"><span class="comment-age">(10 Sep '14, 06:51)</span> Jasper ♦♦</div></div><span id="36168"></span><div id="comment-36168" class="comment"><div id="post-36168-score" class="comment-score"></div><div class="comment-text"><p>Okay, thanks for trying Jasper.</p></div><div id="comment-36168-info" class="comment-info"><span class="comment-age">(10 Sep '14, 06:53)</span> Fiasco</div></div></div><div id="comment-tools-36158" class="comment-tools"></div><div class="clear"></div><div id="comment-36158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36175"></span>

<div id="answer-container-36175" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36175-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>In encrypted (AES/TKIP) scenarios you have have the handshake from your wireless client with the accesspoint inside the capture, because it contains random values which will be unique for the encryption key generation from the PSK.</p><p>Did you start your capture before connecting to the wireless network? Otherwise there is no way of decrypting the traffic. You can check by searching for EAPOL packets within the trace file hinting for the key exchange.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '14, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span> </br></br></p></div></div><div id="comments-container-36175" class="comments-container"><span id="36178"></span><div id="comment-36178" class="comment"><div id="post-36178-score" class="comment-score"></div><div class="comment-text"><p>Brilliant, Landi. That appears to have been my problem. I "thumbs up"ed your answer, but I don't see how to mark it as the solution.</p><p>Now that I've taken your advice, I think I remember reading that somewhere early on, but it slipped through the cracks with all the new information I was taking in at the time.</p><p>Thank you for setting me straight.</p><p>-Ted</p></div><div id="comment-36178-info" class="comment-info"><span class="comment-age">(10 Sep '14, 10:58)</span> Fiasco</div></div><span id="36180"></span><div id="comment-36180" class="comment"><div id="post-36180-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I "thumbs up"ed your answer, but I don't see how to mark it as the solution.</p></blockquote><p>That's because it <em>wasn't</em> an answer, it was just a comment. I've converted it to an answer (and moved your comment on it to be a comment on the answer), so you can now mark it as the solution.</p></div><div id="comment-36180-info" class="comment-info"><span class="comment-age">(10 Sep '14, 11:30)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-36175" class="comment-tools"></div><div class="clear"></div><div id="comment-36175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

