+++
type = "question"
title = "I think I&#x27;m being ARP spoofed or poisoned. How can I know for sure using Wireshark?"
description = '''I believe my router is infected since I recently had malware on my PC. I have since reinstalled Windows 7. After getting rid of the malware/virus from my PC, my network is acting weird (certain pages loading slowly or not at all on all computers) and I notice that the gateway mac address I am connec...'''
date = "2015-04-10T15:38:00Z"
lastmod = "2015-04-11T05:51:00Z"
weight = 41365
keywords = [ "arp", "poisoning", "malware", "arpspoofing", "xarp" ]
aliases = [ "/questions/41365" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [I think I'm being ARP spoofed or poisoned. How can I know for sure using Wireshark?](/questions/41365/i-think-im-being-arp-spoofed-or-poisoned-how-can-i-know-for-sure-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41365-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I believe my router is infected since I recently had malware on my PC. I have since reinstalled Windows 7. After getting rid of the malware/virus from my PC, my network is acting weird (certain pages loading slowly or not at all on all computers) and I notice that the gateway mac address I am connected to does not match the mac address on my router. It is off by one number. Is this normal?</p><p>Also, Xarp has warned me that ARP attacks have been detected, but I don't the next step from there. Can someone point me in the right direction. This is driving me crazy. Thanks.</p></div><div id="question-tags" class="tags-container tags">arp poisoning malware arpspoofing xarp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '15, 15:38</strong></p><img src="https://secure.gravatar.com/avatar/401ff91bb48fa5c615498711594a70a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="billyunaire&#39;s gravatar image" /><p>billyunaire<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="billyunaire has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Apr '15, 15:39</p></div></div><div id="comments-container-41365" class="comments-container"><span id="41374"></span><div id="comment-41374" class="comment"><div id="post-41374-score" class="comment-score">1</div><div class="comment-text"><p>You make some assumptions without much evidence. How are you determining the "gateway mac address"?</p><p>You state you have a "network of computers", how large is this, how are they connected to your internet router, and what type of internet connection do you have?</p></div><div id="comment-41374-info" class="comment-info"><span class="comment-age">(11 Apr '15, 02:10)</span> grahamb ♦</div></div></div><div id="comment-tools-41365" class="comment-tools"></div><div class="clear"></div><div id="comment-41365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41381"></span>

<div id="answer-container-41381" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41381-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>and I notice that the gateway mac address I am connected to does not match the mac address on my router. It is off by one number. Is this normal?</p></blockquote><p>I don't know if that's normal (could be a result of your router firmware). Anyway, you can figure out if there is ARP spoofing on the network, by doing this:</p><ul><li>start Wirshark on your client</li><li>Clear the ARP cache on your client (arp -f ; might need admin privileges i.e. elevated DOS box)</li><li>ping the default gateway IP</li><li>stop Wireshark</li><li>Apply the following filter: arp</li><li>Check if there are two ARP replies for the same request.</li></ul><p>If so, there is either something broken in your network (like one system having the same IP address as your default gateway) or there is really some ARP spoofing going on. In either case: switch off all your systems one by one and repeat the test until the duplicate ARP replies stop. Now you know which system caused them and you can further investigate what's wrong with that system.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '15, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-41381" class="comments-container"></div><div id="comment-tools-41381" class="comment-tools"></div><div class="clear"></div><div id="comment-41381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41366"></span>

<div id="answer-container-41366" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41366-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is this a modem or wireless router? If it's a wireless router I think someone is logged onto your your wifi and is doing a man in the middle attack on your network. I would change your wifi password and make it stronger, WPA2 over 20 chars and turn off WPS, plus make sure the firmware is up to date.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '15, 15:53</strong></p><img src="https://secure.gravatar.com/avatar/7c34b5795df1aaa486754544342bfc1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zer0day&#39;s gravatar image" /><p>zer0day<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zer0day has 3 accepted answers">60%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Apr '15, 16:03</p></div></div><div id="comments-container-41366" class="comments-container"><span id="41367"></span><div id="comment-41367" class="comment"><div id="post-41367-score" class="comment-score"></div><div class="comment-text"><p>It is a 2wire 3801HGV Router/Modem from ATT. I am currently using default settings for it. I will change the Password.</p><p>Would it help to clear devices connected to the router and enable mac filtering?</p></div><div id="comment-41367-info" class="comment-info"><span class="comment-age">(10 Apr '15, 16:26)</span> billyunaire</div></div><span id="41368"></span><div id="comment-41368" class="comment"><div id="post-41368-score" class="comment-score"></div><div class="comment-text"><p>Would it help to clear devices connected to the router and enable mac filtering? No it wouldn't. (4) important things, all of them are important....All</p><ol><li><p>Change password, consists of 20 characters or more having lowercase, uppercase, numbers, and special characters.</p></li><li><p>Encryption type is WPA2 w/ AES, not WPA or WEP</p></li><li><p>Turn off Wifi Protected Setup or WPS, with this on someone can crack your wifi password in 10 hours or less regardless of the length and complexity. This time frame now can differ depending if the AP has rate-limiting on pin challenges.</p></li><li><p>Make sure you have the latest firmware, having the latest most of the time improves security by adding additional layers of protection or patching holes in old ones.</p></li></ol></div><div id="comment-41368-info" class="comment-info"><span class="comment-age">(10 Apr '15, 19:57)</span> zer0day</div></div></div><div id="comment-tools-41366" class="comment-tools"></div><div class="clear"></div><div id="comment-41366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

