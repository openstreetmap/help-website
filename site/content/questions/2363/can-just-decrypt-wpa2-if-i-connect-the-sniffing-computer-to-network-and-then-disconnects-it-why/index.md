+++
type = "question"
title = "Can just decrypt WPA2 if I connect the sniffing computer to network and then disconnects it, why?"
description = '''Can somebody explain this: I am trying to decrypt the traffic in my own wireless network encrypted with WPA2. I have two laptops, let´s call them A and B where A is the computer with Wireshark installed.  I have specified the network key in Wireshark like: wpa-pwd:MyPassword:MySSID Then, if I start ...'''
date = "2011-02-16T01:56:00Z"
lastmod = "2011-02-17T09:31:00Z"
weight = 2363
keywords = [ "decrypt", "eapol", "wpa2" ]
aliases = [ "/questions/2363" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can just decrypt WPA2 if I connect the sniffing computer to network and then disconnects it, why?](/questions/2363/can-just-decrypt-wpa2-if-i-connect-the-sniffing-computer-to-network-and-then-disconnects-it-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2363-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can somebody explain this:</p><p>I am trying to decrypt the traffic in my own wireless network encrypted with WPA2. I have two laptops, let´s call them A and B where A is the computer with Wireshark installed.</p><p>I have specified the network key in Wireshark like: wpa-pwd:MyPassword:MySSID</p><p>Then, if I start the capturing and then connect computer B to the network (computer A is disconnected from network), just two EAPOL packets are captured and the traffic is not decrypted.</p><p>Then I disconnect computer B and connect computer A to the network and immediately disconnects computer A. I reconnect computer B and then I am able to see the encrypted data.</p><p>So:</p><ol><li><p>Computer B is connected and A is not --&gt; Cannot decrypt data<br />
</p></li><li><p>Computer A and B are connected --&gt; Cannot decrypt data</p></li><li><p>Computer A is connected to the network and immediately disconnected, then B connects and I am able to read the data.</p></li></ol><p>Why does just step 3 work? I think step 2 also should work.</p></div><div id="question-tags" class="tags-container tags">decrypt eapol wpa2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '11, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/b40d415d5a5ed5142e38ad841b2e176a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rox&#39;s gravatar image" /><p>Rox<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rox has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Feb '11, 02:00</p></div></div><div id="comments-container-2363" class="comments-container"></div><div id="comment-tools-2363" class="comment-tools"></div><div class="clear"></div><div id="comment-2363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2382"></span>

<div id="answer-container-2382" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2382-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't fully understand the exact scenario - but maybe I can bring some light into this:</p><p>Question: With which NIC do you capture the wireless traffic on computer A ? Because if you're capturing with the same NIC used for the wireless connection, chances are high you don't get all the packets transmitted by computer A over the wireless network, because your NIC works half duplex, meaning it can only capture or send packets.</p><p>Supposed you are using wireshark to capture with your internal NIC on computer A, wou would have to have a valid association to your AP in order to be able to capture any data on computer A (without using airpcap adapter or similar under windows)</p><p>That would be a hint, why you can only decrypt computer Bs traffic, since you only get the complete 3 or 4 EAPol packets when capturing Bs authentication from computer A.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '11, 10:45</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-2382" class="comments-container"></div><div id="comment-tools-2382" class="comment-tools"></div><div class="clear"></div><div id="comment-2382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2402"></span>

<div id="answer-container-2402" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2402-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don´t know if I got it. =/</p><p>I am using the internal wireless NIC on computer A. Since it is a wireless NIC I suppose it is just capturing on the wireless channel?</p><p>So you are saying that when A is connected to the wireless network, then the NIC both sends and receives packets but just in half duplex, and when I am not connected to network, the NIC just receives packets, and that is why I can read all four EAPol packets?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '11, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/b40d415d5a5ed5142e38ad841b2e176a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rox&#39;s gravatar image" /><p>Rox<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rox has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Feb '11, 09:32</p></div></div><div id="comments-container-2402" class="comments-container"><span id="2413"></span><div id="comment-2413" class="comment"><div id="post-2413-score" class="comment-score"></div><div class="comment-text"><p>Almost what I was meaning... What I'm saying is that at least from my experience - it is usual that you have problems with capturing data frames you SEND while the capture is running, at least if you're capturing with the same NIC, with which you are connected to the network. Might be that there are other problems as well, but that's my major path to follow, especially when capturing other computers traffic works fine.</p></div><div id="comment-2413-info" class="comment-info"><span class="comment-age">(18 Feb '11, 01:18)</span> Landi</div></div></div><div id="comment-tools-2402" class="comment-tools"></div><div class="clear"></div><div id="comment-2402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

