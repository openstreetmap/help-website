+++
type = "question"
title = "Capture WLAN-traffic using Wireshark"
description = '''I&#x27;m trying to understand how to capture traffic on my WLAN(WPA2) using Wireshark. I can see the traffic going to and from my Backtrack-PC and Wireshark is able to decrypt it (using the WPA-password and the four EAPOL Key msg), but I can&#x27;t see any traffic going from other clients on the network. If I...'''
date = "2012-08-18T03:10:00Z"
lastmod = "2012-08-20T05:00:00Z"
weight = 13713
keywords = [ "eapol", "wireshark" ]
aliases = [ "/questions/13713" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Capture WLAN-traffic using Wireshark](/questions/13713/capture-wlan-traffic-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13713-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to understand how to capture traffic on my WLAN(WPA2) using Wireshark. I can see the traffic going to and from my Backtrack-PC and Wireshark is able to decrypt it (using the WPA-password and the four EAPOL Key msg), but I can't see any traffic going from other clients on the network. If I deauth a client from my BT-PC I only get two EAPOL Key msg, 1/4 and 3/4, it's missing key 2/4 and 4/4. Why is that?</p><p>I've tried different approaches listening on both wlan0 and mon0 but no luck. It seems to me that Wireshark can only capture the WPA-handshake going from the client to the AP and not vice versa. I can't get any data-traffic (like http) from my clients.</p><p>Am I doing something wrong here or is it just impossible to capture traffic on WLAN encrypted with WPA2?</p><p>This is my config, BackTrack 5 R1 running on a PC with a Alfa AWUS036H (The computer running Wireshark). AP is a ASUS RT-N56U. Clients: one Laptop running BackTrack 5 R1 and one Android-Phone.</p><p>BT-tools used, Wireshark (sniffer) airmon-ng (to swith wlan0 into monitor mode) aireplay-ng (to deauth)</p></div><div id="question-tags" class="tags-container tags">eapol wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '12, 03:10</strong></p><img src="https://secure.gravatar.com/avatar/d822dafb338476cf58a60b0df6319000?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ziggemannen&#39;s gravatar image" /><p>Ziggemannen<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ziggemannen has no accepted answers">0%</span></p></div></div><div id="comments-container-13713" class="comments-container"></div><div id="comment-tools-13713" class="comment-tools"></div><div class="clear"></div><div id="comment-13713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13750"></span>

<div id="answer-container-13750" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13750-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>To verify that your capture setup is working please try the following setup:</p><ul><li>Make sure you're not using 802.11n since the AWUS036H isn't .n capable</li><li>Setup mon0 using airmon-ng</li><li>use airodump-ng on mon0 with '-c' for channel and with '--bssid' for the APs MAC address and write the output into a capture file with '-w'.</li></ul><p>Compare that trace with your prior tests, if there's more frames in it, you might have an issue with wireshark fiddling with the monitor mode. In any case try not to enable the "promiscuous mode" setting in wireshark when capturing from your mon0 interface and see if that helps.</p><p>The AWUS036H is perfectly capable of sniffing WPA2/AES traffic, that should not be an issue. Try to limit your AP to 802.11g for testing purposes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '12, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Aug '12, 05:01</p></div></div><div id="comments-container-13750" class="comments-container"><span id="13794"></span><div id="comment-13794" class="comment"><div id="post-13794-score" class="comment-score"></div><div class="comment-text"><p>Thank you! It was as simple as setting the AP to 802.11g. Now I can see my other clients traffic and after a successfull handshake capture, Wireshark can decrypt the packets.</p></div><div id="comment-13794-info" class="comment-info"><span class="comment-age">(21 Aug '12, 10:17)</span> Ziggemannen</div></div></div><div id="comment-tools-13750" class="comment-tools"></div><div class="clear"></div><div id="comment-13750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13714"></span>

<div id="answer-container-13714" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13714-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>WLAN is not my specialty, but keep in mind that the WiFi adapter basically works in half duplex mode, so if you're using it as a communication device (and not just as a passive capture card) your outgoing traffic will prevent reading other (incoming) packets at the same time - because the card can either receive <strong>or</strong> send data (not both). Have you tried removing all IP addresses from your WiFi NIC to see if it works as a capture-only card?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '12, 03:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Aug '12, 03:21</p></div></div><div id="comments-container-13714" class="comments-container"><span id="13716"></span><div id="comment-13716" class="comment"><div id="post-13716-score" class="comment-score"></div><div class="comment-text"><p>With BackTrack and the Alfa AWUS036H you can set the card into monitor-mode, that way it should listen to all traffic going through the air.</p></div><div id="comment-13716-info" class="comment-info"><span class="comment-age">(18 Aug '12, 03:33)</span> Ziggemannen</div></div><span id="13720"></span><div id="comment-13720" class="comment"><div id="post-13720-score" class="comment-score"></div><div class="comment-text"><p>I've just upgraded Wireshark to version 1.8.1 and now I occasionally get all four EAPOL packets when a client connects to the AP, but I still can't see any data traffic coming from the client in Wireshark. If I fire up a webbrowser and starts surfing on the client all Wireshark get is "Request-to-send" and "802.11 Block Ack".</p></div><div id="comment-13720-info" class="comment-info"><span class="comment-age">(18 Aug '12, 13:23)</span> Ziggemannen</div></div></div><div id="comment-tools-13714" class="comment-tools"></div><div class="clear"></div><div id="comment-13714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

