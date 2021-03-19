+++
type = "question"
title = "Capturing all the traffic"
description = '''Hello guys, i decided to come here as my very last resort. I searched maybe the entire google for about 1 week, this is driving me insane. So here&#x27;s the issue:  I own a very small company, and i want to check if my employees are playing farmville or using facebook or whatever sites of that kind, ins...'''
date = "2011-02-08T07:54:00Z"
lastmod = "2011-02-08T10:23:00Z"
weight = 2228
keywords = [ "wireshark" ]
aliases = [ "/questions/2228" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing all the traffic](/questions/2228/capturing-all-the-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2228-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello guys, i decided to come here as my very last resort. I searched maybe the entire google for about 1 week, this is driving me insane. So here's the issue: I own a very small company, and i want to check if my employees are playing farmville or using facebook or whatever sites of that kind, instead of working. So, i'm not going to install remote software, because those are their computers, and i don't want to break that privacy of course. Some friends told me about this program. Here's what i did:</p><p>1 - Installed wireshark and winpcap on my computer 2 - started the scan on my wlan interface</p><p>I did enter on some sites, and it's awesome, i can see what's going on. But soon i realized...that's my own traffic only. I can't see nothing about my employees traffic. So as i was searching google, i found out about the promiscuous mode. Well, i tried both ways, turned it on and off. doesn't help.</p><p>So i got other friend that said: Hey that sucks on windows, try booting into "backtrack linux dist" , it comes with wireshark and sure will work. Funny thing, i tried backtrack and i can see the computer names on my network, some stuff going on, but that's it. I still can't see any "http" traffic from them. I want to make sure if it's my computer problem, my NIC problem or whatever, so i can buy a proper card or maybe a usb network card? what you guys think? thanks in advance</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '11, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/83ba468800427c6b7992b4d7ddb46583?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JackLopez&#39;s gravatar image" /><p>JackLopez<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JackLopez has no accepted answers">0%</span></p></div></div><div id="comments-container-2228" class="comments-container"></div><div id="comment-tools-2228" class="comment-tools"></div><div class="clear"></div><div id="comment-2228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="2230"></span>

<div id="answer-container-2230" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2230-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sometimes switch can be the problem. Once an intelligent switch senses the best rout to send traffic, you could be left out of the so called "loop".</p><p>Check out "Port Mirroring" switches like this one: NetGear GS108T</p><p>Just a thought</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '11, 08:17</strong></p><img src="https://secure.gravatar.com/avatar/a2c36e0535e33d86a1738e74e85101fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="drewcrewof2&#39;s gravatar image" /><p>drewcrewof2<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="drewcrewof2 has no accepted answers">0%</span></p></div></div><div id="comments-container-2230" class="comments-container"><span id="2233"></span><div id="comment-2233" class="comment"><div id="post-2233-score" class="comment-score"></div><div class="comment-text"><p>He's trying to capture wireless traffic, as in "no cable" -&gt; no switch - you might want to re-read his problem description ;-)</p></div><div id="comment-2233-info" class="comment-info"><span class="comment-age">(08 Feb '11, 10:20)</span> Jasper ♦♦</div></div></div><div id="comment-tools-2230" class="comment-tools"></div><div class="clear"></div><div id="comment-2230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2232"></span>

<div id="answer-container-2232" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2232-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks so much. Since i got your reply, i've been reading a lot on that matter. yeah, i will never get anything with my router. i'm gonna check the prices on that one, thanks!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '11, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/83ba468800427c6b7992b4d7ddb46583?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JackLopez&#39;s gravatar image" /><p>JackLopez<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JackLopez has no accepted answers">0%</span></p></div></div><div id="comments-container-2232" class="comments-container"><span id="2235"></span><div id="comment-2235" class="comment"><div id="post-2235-score" class="comment-score"></div><div class="comment-text"><p>I don't think buying a switch will help unless you force your employees to use it by shutting down WLAN for them and having them use a cable connection to that switch. Which is a valid strategy of course, but not a very subtle one if you want to avoid their attention to what you're trying to do ;-)</p></div><div id="comment-2235-info" class="comment-info"><span class="comment-age">(08 Feb '11, 10:38)</span> Jasper ♦♦</div></div></div><div id="comment-tools-2232" class="comment-tools"></div><div class="clear"></div><div id="comment-2232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2234"></span>

<div id="answer-container-2234" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2234-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're stumbling over the typical WiFi capture problem - on Windows you can't capture WLAN with Wireshark unless using a special USB capture adapter ("AirPCAP") sold by CaceTech. Check the answer Landi gave on this question: <a href="http://ask.wireshark.org/questions/1048/cant-capture-network-traffic?page=1#1057">can't capture network traffic</a></p><p>Regarding backtrack: it should work, but you still might have to enable monitor mode on the wireless card for Wireshark to see all frames.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '11, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2234" class="comments-container"></div><div id="comment-tools-2234" class="comment-tools"></div><div class="clear"></div><div id="comment-2234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

