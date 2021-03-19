+++
type = "question"
title = "Unable to decode packets payload"
description = '''Hi, I&#x27;m using 2 RaspberryPi&#x27;s to communicate with each other over IP using netcat (Unencrypted and direct over IP messaging through port 555) using R.Pi#1: sudo nc -l 555 R.Pi#2: sudo nc 192.168.43.107 555. I checked, it works and it does not encrypt the packet&#x27;s payload, I can see the entire conver...'''
date = "2016-12-16T06:02:00Z"
lastmod = "2016-12-16T06:02:00Z"
weight = 58166
keywords = [ "llc", "decryption", "payload", "tcp", "arpspoofing" ]
aliases = [ "/questions/58166" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to decode packets payload](/questions/58166/unable-to-decode-packets-payload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58166-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm using 2 RaspberryPi's to communicate with each other over IP using netcat (Unencrypted and direct over IP messaging through port 555) using R.Pi#1: <code>sudo nc -l 555</code> R.Pi#2: <code>sudo nc 192.168.43.107 555</code>. I checked, it works and it does not encrypt the packet's payload, I can see the entire conversation on WireShark.</p><p>Then, im sniffing that conversation with a 3rd R.Pi running Kali-Linux using wireshark,but now I see the conversation under LLC protocl instead of TCP like I saw before, and I belive the data payload is now encrypted.I tried decrypt it through HEX to string converter or Binary to string converter, still its gibrish, How can i make it human-readable?</p><p>Here are some pictures:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/all_packets.jpg" alt="alt text" /></p><p>Packet 148 Data: <img src="https://osqa-ask.wireshark.org/upfiles/packet_148.jpg" alt="alt text" /></p><p>it's Payload is(Hex Stream): 2000000000277e5bf58848eb699738a8a50b1c8304f0963a64554e2b70881ab95bbb9353e66d81fc524d196ea014162b663b5b16dc</p><p>Packet 149: <img src="https://osqa-ask.wireshark.org/upfiles/packet_149.jpg" alt="alt text" /></p><p>it's Payload is(Hex Stream): 0000000066a402fe5551f063251d00745c97f7e34379265f60b8c412cd2221397afd1d5a04a5a09cf02d3208d4f3f8264666c0621383099b2e8715339ddda609c32363d1234d14a4a8edf8e0155ee91d6d4c9647</p><p>Packet 158: <img src="https://osqa-ask.wireshark.org/upfiles/packet_158.jpg" alt="alt text" /> it's Payload is(Hex Stream): 000000008641e14b03305a4f6e72921b0bfb3e9dd3febd24d005a67cc209a204cb40a0fe68b35e27810e410cc6800fdd1078998c8062f1594ab6dc0f95d3722398f21065c101c4b9c29af74820e64a7b3c6ec9f328</p><p>Before the arpspoofing: SENDING:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/withoutarp.jpg" alt="alt text" /> And RESPONSE:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/withoutarp1_YWNxHzW.jpg" alt="alt text" /></p><p>Any ideas please?</p></div><div id="question-tags" class="tags-container tags">llc decryption payload tcp arpspoofing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '16, 06:02</strong></p><img src="https://secure.gravatar.com/avatar/34e92c458583e7a88b7fc96fb424c50d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eyal360&#39;s gravatar image" /><p>eyal360<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eyal360 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-58166" class="comments-container"><span id="58167"></span><div id="comment-58167" class="comment"><div id="post-58167-score" class="comment-score"></div><div class="comment-text"><p>Sigh. As ever, a capture file is much more useful than some screenshots.</p><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, DropBox etc.?</p><p>Also can you explain your capture environment and where the captures were made, i.e. show the 3 RPI's, and the connections between them?</p></div><div id="comment-58167-info" class="comment-info"><span class="comment-age">(16 Dec '16, 06:22)</span> grahamb ♦</div></div><span id="58169"></span><div id="comment-58169" class="comment"><div id="post-58169-score" class="comment-score"></div><div class="comment-text"><p>yes, this is the Drive link :each for Rx and Tx messages <a href="https://drive.google.com/file/d/0B4dE5ujOQI6RN2JlLTFQTkozdGc/view?usp=sharing">https://drive.google.com/file/d/0B4dE5ujOQI6RN2JlLTFQTkozdGc/view?usp=sharing</a> <a href="https://drive.google.com/file/d/0B4dE5ujOQI6RSUd4X1RkU2tDcFU/view?usp=sharing">https://drive.google.com/file/d/0B4dE5ujOQI6RSUd4X1RkU2tDcFU/view?usp=sharing</a></p><p>Im capturing over my WLAN, all the R.Pi's are connected to the same WPA wifi.</p><p>Thanks for the quick reply.</p><p>p.s: its only showing the LLC packets because the others are unrelated ARP or other managment protocol packets so i've unselected them.</p></div><div id="comment-58169-info" class="comment-info"><span class="comment-age">(16 Dec '16, 06:45)</span> eyal360</div></div></div><div id="comment-tools-58166" class="comment-tools"></div><div class="clear"></div><div id="comment-58166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

