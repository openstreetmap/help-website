+++
type = "question"
title = "I&#x27;m seeing ICMP traffic that I did not commence"
description = '''I&#x27;m the only one on my local network and I&#x27;m seeing ICMP traffic (destination unreachable) on my network....Why is this? I don&#x27;t believe that any ICMP traffic besides redirect traffic is good especially if you are not the one initiating it. For some odd reason, my default gateway is attempting to pi...'''
date = "2014-10-01T20:25:00Z"
lastmod = "2014-10-01T22:02:00Z"
weight = 36767
keywords = [ "destination", "icmp", "unreachable" ]
aliases = [ "/questions/36767" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [I'm seeing ICMP traffic that I did not commence](/questions/36767/im-seeing-icmp-traffic-that-i-did-not-commence)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36767-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm the only one on my local network and I'm seeing ICMP traffic (destination unreachable) on my network....Why is this? I don't believe that any ICMP traffic besides redirect traffic is good especially if you are not the one initiating it. For some odd reason, my default gateway is attempting to ping my client as shown in the screenshot.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/oddpackets_on_LAN.PNG" alt="alt text" /></p><p>Can anyone tell me why this is occurring?</p></div><div id="question-tags" class="tags-container tags">destination icmp unreachable</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '14, 20:25</strong></p><img src="https://secure.gravatar.com/avatar/4784c5fb1a0142030d51a339706a456c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beldum&#39;s gravatar image" /><p>Beldum<br />
<span class="score" title="49 reputation points">49</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beldum has no accepted answers">0%</span></p></img></div></div><div id="comments-container-36767" class="comments-container"></div><div id="comment-tools-36767" class="comment-tools"></div><div class="clear"></div><div id="comment-36767-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36771"></span>

<div id="answer-container-36771" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36771-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You (or some application on your Windows System) were trying to send TCP packets to <a href="http://www.ip-adress.com/whois/30.7.159.198">30.7.159.198</a> and your gateway 172.200.20.1 didn't know how to get there (Host unreachable: The target host should be adjacent but isn't) If you want to find out who is trying to connect, you might use an <a href="http://support.sasktel.com/app/answers/detail/a_id/11365/~/using-netstat-to-find-programs-using-up-internet-bandwidth-in-windows-xp,">elevated netstat -o</a> and figure out which application is trying to connect.</p><p>Regards Matthias,<br />
who thinks that most ICMP packets are good and "redirects" are not among those ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Oct '14, 22:02</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Oct '14, 23:01</p></div></div><div id="comments-container-36771" class="comments-container"><span id="36772"></span><div id="comment-36772" class="comment"><div id="post-36772-score" class="comment-score"></div><div class="comment-text"><p>Hello, How is it that you know from the information provided that something on my Windows System was trying to send TCP packets to 30.7.159.198? Where did you find that information? Thanks for your assistance.</p></div><div id="comment-36772-info" class="comment-info"><span class="comment-age">(01 Oct '14, 22:56)</span> Beldum</div></div><span id="36773"></span><div id="comment-36773" class="comment"><div id="post-36773-score" class="comment-score"></div><div class="comment-text"><p>The ICMP packet contains the original IP packet that triggered this 'error message'. so in the hexadecimal part of the packet you see another 4500 which is the start of the IP packet 001C is the length (28 bytes) 7F06 says it's a TCP packet and the TTL when the packet was seen is 127. With the initial TTL of windows being 128 this means that only 1 router had routed this packet (= decremented the TTL) .</p><p>It would have been easier to spot if you had captured the full packets ;-)</p></div><div id="comment-36773-info" class="comment-info"><span class="comment-age">(01 Oct '14, 23:04)</span> mrEEde</div></div><span id="36805"></span><div id="comment-36805" class="comment"><div id="post-36805-score" class="comment-score"></div><div class="comment-text"><p>Gosh I wish I knew how to use this wireshark tool as well as you. Thanks mrEEde!</p></div><div id="comment-36805-info" class="comment-info"><span class="comment-age">(02 Oct '14, 12:21)</span> Beldum</div></div></div><div id="comment-tools-36771" class="comment-tools"></div><div class="clear"></div><div id="comment-36771-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

