+++
type = "question"
title = "Wireless capture"
description = '''OK, I don&#x27;t know if I&#x27;m doing this wrong or if what I&#x27;m trying to do is even supported. What I&#x27;m trying to do is monitor packets on my WEP network. I am connected via wireless and I can pass traffic with no issues via wlan0.  I start Wireshark in promiscuous mode on wlan0 and all I can see is broadc...'''
date = "2012-04-27T23:13:00Z"
lastmod = "2012-04-28T05:11:00Z"
weight = 10494
keywords = [ "question", "wlan", "help", "capture" ]
aliases = [ "/questions/10494" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireless capture](/questions/10494/wireless-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10494-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>OK, I don't know if I'm doing this wrong or if what I'm trying to do is even supported. What I'm trying to do is monitor packets on my WEP network. I am connected via wireless and I can pass traffic with no issues via wlan0. I start Wireshark in promiscuous mode on wlan0 and all I can see is broadcast, multicast and my (to/from) traffic. It's just like I'm on a switched network. I added the WEP key to the protocols options sections under IEEE 802.11, still just the same. I have tested my wireless card with airmon-ng and it works fine (injection, capture and monitor mode). The card has the z1211b chipset using the using the z1211RW driver and firmware on Backtrack 5 r2.<br />
So, my question is: Should I be able to see all traffic on the wireless network doing this? Do I need to put the card in monitor mode and capture on mon0, instead to make this work? Am I possibly having an issue with my wireless card that is causing the issue?</p></div><div id="question-tags" class="tags-container tags">question wlan help capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '12, 23:13</strong></p><img src="https://secure.gravatar.com/avatar/0bc1dabd3011386b6e8cb72c7a41a58f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deets52&#39;s gravatar image" /><p>deets52<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deets52 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-10494" class="comments-container"></div><div id="comment-tools-10494" class="comment-tools"></div><div class="clear"></div><div id="comment-10494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10496"></span>

<div id="answer-container-10496" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10496-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Correct, you have to put your card into monitor mode and capture on mon0 to see all packets instead of just broadcast+own traffic. Being connected to your own wireless network might also give you issues when capturing, so better make sure that you are just using plain monitor mode.</p><p>Stick to <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">http://wiki.wireshark.org/CaptureSetup/WLAN</a> for more details if needed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '12, 05:11</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-10496" class="comments-container"><span id="10500"></span><div id="comment-10500" class="comment"><div id="post-10500-score" class="comment-score"></div><div class="comment-text"><p>First of all, thank you very much for your answer. I am confused by it, however. I did read the wiki that you linked to (several times) and that is one of the reasons I asked the question. The part I don't understand is:<br />
<br />
<strong>Promiscuous mode</strong> <font><br />
In promiscuous mode the MAC address filter mentioned above is disabled and all packets of the currently joined 802.11 network (with a specific SSID and channel) are captured, just as in traditional Ethernet.</font></p><p><font> </font></p><p><font>This seems to work on Linux and various BSDs, including Mac OS X. On Windows, putting 802.11 adapters into promiscuous mode is usually crippled, see the Windows section below.</font></p><font> </font><p><font>Promiscuous mode can be enabled in the Wireshark Capture Options.</font></p><p>Are you saying I can't do it or that I can do it, but you don't recommend it?<br />
I thought monitor mode pick up all traffic of the given channel regardless of network or SSID. I will do more testing with monitor mode captures but the limited test I did yesterday yielded very similar results.</p></div><div id="comment-10500-info" class="comment-info"><span class="comment-age">(28 Apr '12, 10:09)</span> deets52</div></div><span id="10508"></span><div id="comment-10508" class="comment"><div id="post-10508-score" class="comment-score"></div><div class="comment-text"><p>You can try to use wireshark's builtin option to enable promiscuous mode but for wireless capturing I never really got this to work except with dedicated WiFi capture cards. I'm not saying it never works, just IF there are problems (like in your case) pre-enable monitor mode (not exactly the same as promiscuous mode) with airmon-ng and specify the right channel.</p><p>After that you can start wireshark without setting promisc. mode (trying to set it might corrupt with mon. mode from airmon-ng with certain drivers)</p></div><div id="comment-10508-info" class="comment-info"><span class="comment-age">(29 Apr '12, 13:04)</span> Landi</div></div><span id="10510"></span><div id="comment-10510" class="comment"><div id="post-10510-score" class="comment-score"></div><div class="comment-text"><p>Not really the answer I wanted, but that works for me. I was thinking that there was a problem with the card (drivers, firmware, etc) since it is a z1211b card using the z1211RW drivers. I guess I will just need to work on the filters. The main reason I did not want to have to do that is because there are several "noisy" neighbors (wifi speaking) and to let the packet capture run too long creates too much overhead. Even though I can filter out what I don't want to see, it is still in the main capture file that grows way too large too quick.<br />
Thank you for taking the time to look at this and answer - I do appreciate your time. Keep up the good work and have a beer on me (or because of me) - I'll be having one as well.<br />
CHEERS!</p></div><div id="comment-10510-info" class="comment-info"><span class="comment-age">(29 Apr '12, 14:01)</span> deets52</div></div></div><div id="comment-tools-10496" class="comment-tools"></div><div class="clear"></div><div id="comment-10496-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

