+++
type = "question"
title = "Passwords and personal info"
description = '''I work at a University and one of the professors wants IT to install Wireshark in one of the teaching labs for a class. We are concerned that the students will take this opportunity to sniff out password packets and other personal information. When packets are captured, can the contents actually be ...'''
date = "2013-02-06T06:47:00Z"
lastmod = "2013-02-06T09:58:00Z"
weight = 18360
keywords = [ "passwords" ]
aliases = [ "/questions/18360" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Passwords and personal info](/questions/18360/passwords-and-personal-info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18360-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I work at a University and one of the professors wants IT to install Wireshark in one of the teaching labs for a class. We are concerned that the students will take this opportunity to sniff out password packets and other personal information.</p><p>When packets are captured, can the contents actually be viewed, or are they encrypted?</p></div><div id="question-tags" class="tags-container tags">passwords</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '13, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/fdd2ea9c272794c9383d84eec3bbaca6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rfcomm2k&#39;s gravatar image" /><p>rfcomm2k<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rfcomm2k has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Feb '13, 06:50</p></div></div><div id="comments-container-18360" class="comments-container"><span id="18367"></span><div id="comment-18367" class="comment"><div id="post-18367-score" class="comment-score">1</div><div class="comment-text"><p>IMHO you have it slightly backwards. You should intentionally introduce fake passwords and personal information on the wire. It would teach an important lesson about the importance of data encryption and likely make the lab more fun an interesting.</p></div><div id="comment-18367-info" class="comment-info"><span class="comment-age">(06 Feb '13, 08:36)</span> Gerald Combs ♦♦</div></div><span id="18374"></span><div id="comment-18374" class="comment"><div id="post-18374-score" class="comment-score"></div><div class="comment-text"><blockquote><p>We are concerned that the students will take this opportunity to sniff out password packets and other personal information.</p></blockquote><p>I bet some of them are doing exactly that right now, you just did not know yet ;-)) Just check how many of them connect to your network with their own laptop...</p></div><div id="comment-18374-info" class="comment-info"><span class="comment-age">(06 Feb '13, 12:36)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-18360" class="comment-tools"></div><div class="clear"></div><div id="comment-18360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="18361"></span>

<div id="answer-container-18361" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18361-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Any encryption depends on the protocol used by the password packets, Wireshark just displays what is captured from the interfaces.</p><p>Note that encrypted info can be decrypted by Wireshark, given sufficient extra information that isn't available purely by capturing traffic, e.g. encrypted WiFi traffic given the connection password, or even TLS\SSL traffic given the server secret key.</p><p>Depending on the network setup, e.g. switched ethernet, the available traffic to capture will be restricted to that available from the switch port which will limit the opportunities for misbehaviour.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Feb '13, 07:36</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-18361" class="comments-container"><span id="18362"></span><div id="comment-18362" class="comment"><div id="post-18362-score" class="comment-score"></div><div class="comment-text"><p>Of course some encryption schemes, WEP for example, can be easily cracked.</p></div><div id="comment-18362-info" class="comment-info"><span class="comment-age">(06 Feb '13, 07:59)</span> cmaynard ♦♦</div></div><span id="18364"></span><div id="comment-18364" class="comment"><div id="post-18364-score" class="comment-score"></div><div class="comment-text"><p>Dos anyone still consider WEP an encryption scheme these days? It's more an obfuscation than anything else.</p></div><div id="comment-18364-info" class="comment-info"><span class="comment-age">(06 Feb '13, 08:10)</span> grahamb ♦</div></div><span id="18365"></span><div id="comment-18365" class="comment"><div id="post-18365-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately, some people are still using WEP. WPA has also been cracked though.</p></div><div id="comment-18365-info" class="comment-info"><span class="comment-age">(06 Feb '13, 08:21)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-18361" class="comment-tools"></div><div class="clear"></div><div id="comment-18361-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18370"></span>

<div id="answer-container-18370" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18370-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Depending upon the class, using Wireshark can be entirely appropriate. See <a href="http://ask.wireshark.org/questions/6423/wireshark-on-university-network?page=1&amp;focusedAnswerId=6424#6424">this question</a> for another discussion of this issue, from the teacher's point of view.</p><p>Regardless, I bet you've got some technically knowledgeable students who have already figured out how to capture traffic on your network. Rather than trying to keep Wireshark off the network, I'd focus more on ensuring that sensitive network traffic is appropriately encrypted.</p><p>I would think that your IT staff should already be using Wireshark in the course of maintaining the network, and they should be aware of what traffic crosses the network unencrypted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Feb '13, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-18370" class="comments-container"></div><div id="comment-tools-18370" class="comment-tools"></div><div class="clear"></div><div id="comment-18370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18363"></span>

<div id="answer-container-18363" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18363-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>One way to mitigate this worry is to limit the users that can actually capture traffic.</p><p>Assuming sufficiently controlled installations and permissions you can limit the access to the capture engine (dumpcap (U*IX) or WinPcap (Windows)), or not install the capture engines at all. This way the labs still can use the dissection capabilities of Wireshark, but using previously captured files only, not life traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Feb '13, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-18363" class="comments-container"></div><div id="comment-tools-18363" class="comment-tools"></div><div class="clear"></div><div id="comment-18363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

