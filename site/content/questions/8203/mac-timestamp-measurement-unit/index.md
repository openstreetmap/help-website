+++
type = "question"
title = "MAC Timestamp measurement Unit"
description = '''Hi guys, Hope you can help me with this one : We have this 9-digits MAC Timestamp in the Radio Header Section, what is the measurement unit for that? Wireshark defines it as &quot;Value in microseconds of the MAC&#x27;s Time Synchronizations Function timer when the first bit of the MPDU arrived at the MAC&quot; bu...'''
date = "2012-01-03T02:08:00Z"
lastmod = "2012-01-03T18:17:00Z"
weight = 8203
keywords = [ "timestamp", "mac", "radioheader" ]
aliases = [ "/questions/8203" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [MAC Timestamp measurement Unit](/questions/8203/mac-timestamp-measurement-unit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8203-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, Hope you can help me with this one :</p><p>We have this 9-digits MAC Timestamp in the Radio Header Section, what is the measurement unit for that? Wireshark defines it as "Value in microseconds of the MAC's Time Synchronizations Function timer when the first bit of the MPDU arrived at the MAC" but I kind of not sure about that. Does it mean it took like about 974538712 usec for a Packet to reach my WLAN card? or The unit is somehow not directly Microseconds and some how needs conversion.</p><p>Thank you in advance,</p><p>A.G</p></div><div id="question-tags" class="tags-container tags">timestamp mac radioheader</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jan '12, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/559f374efd2eaeaafac5616bbec62008?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AminGho&#39;s gravatar image" /><p>AminGho<br />
<span class="score" title="51 reputation points">51</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AminGho has no accepted answers">0%</span></p></div></div><div id="comments-container-8203" class="comments-container"></div><div id="comment-tools-8203" class="comment-tools"></div><div class="clear"></div><div id="comment-8203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8213"></span>

<div id="answer-container-8213" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8213-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The MAC timestamp field in radiotap headers is <a href="http://www.radiotap.org/defined-fields/TSFT">as defined by radiotap.org</a>; the Wireshark definition directly quotes the radiotap spec. The timing synchronization function is discussed by <a href="http://en.wikipedia.org/wiki/Timing_Synchronization_Function_(TSF)">the Wikipedia page for it</a>. It has nothing to do with the time it takes for the packet to reach your WLAN card over the air - there's just a timer, running with microsecond resolution, in all stations, and the time stamp value represents the value of the timer at the time the first bit of the MAC-layer packet arrived at the card. You can't use it to determine much in the way of useful timing information for a single packet.</p><p>See section 11 of <a href="http://standards.ieee.org/getieee802/download/802.11-2007.pdf">the IEEE 802.11-2007 specification</a> for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '12, 18:17</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8213" class="comments-container"><span id="8253"></span><div id="comment-8253" class="comment"><div id="post-8253-score" class="comment-score"></div><div class="comment-text"><p>Thanks Harris, Actually I read most of these pages before and that's exactly why I posted this question, cuz I am confused about the definitions. The fact is it's not clear to me what is this 9-Digit number. If you don't mind please answer my questions below to help me make it clear :</p><p>1- This 9-digit number it's not Microsecond so We can not say 978654345 usec! Right?</p><p>2-Is it Time Tick? base on Wikipedia TSF is based on 1-Mhz Clock and "ticks" in Microseconds. Does this mean each tick is equal to 1usec? if It's a tick they gotta be a way to convert it to a more understandable unit like millisecond or microsecond.</p><p>Thank you in advance.</p></div><div id="comment-8253-info" class="comment-info"><span class="comment-age">(06 Jan '12, 06:27)</span> AminGho</div></div><span id="8262"></span><div id="comment-8262" class="comment"><div id="post-8262-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>This 9-digit number it's not Microsecond so We can not say 978654345 usec! Right?</p></blockquote><p>Wrong. It <em>is</em> microseconds, as per the 802.11 spec. It's only 978.654345 seconds, which is substantially less than an hour, and I certainly <em>hope</em> your Wi-Fi access point, for example, can keep running for at least that long.</p><blockquote><p>base on Wikipedia TSF is based on 1-Mhz Clock and "ticks" in Microseconds. Does this mean each tick is equal to 1usec?</p></blockquote><p>Yes. Each tick is 1 microsecond - that's what a 1 MHz clock does (1 megahertz = 1 million per second = each one is a millionth of a second, i.e. a microsecond).</p></div><div id="comment-8262-info" class="comment-info"><span class="comment-age">(06 Jan '12, 11:57)</span> Guy Harris ♦♦</div></div><span id="8263"></span><div id="comment-8263" class="comment"><div id="post-8263-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot Harris, It's way more clear now. One more thing, when the timer reaches 999999999 does it go back to 000000000 or it goes to 10-digits and so on? And is this true that the 000000000 state is when the WLAN card just started and connected to an AP or an ad-hoc?</p><p>Once again thanks a lot for your great help. I really appreciate it.</p></div><div id="comment-8263-info" class="comment-info"><span class="comment-age">(06 Jan '12, 23:24)</span> AminGho</div></div><span id="8266"></span><div id="comment-8266" class="comment"><div id="post-8266-score" class="comment-score">1</div><div class="comment-text"><p>The timer is a <em>binary</em> timer, so 999999999 is not a special value - it's just 0x000000003B9AC9FF - so its decimal display value would go to 10 digits. (It's a 64-bit timer, so it's not going to roll over as a binary timer any time soon.)</p><p>I don't see anything obvious in section 11 of the 802.11 spec to say what value the TSF timer has before a STA has seen any beacons. If it doesn't specify, they probably, in practice, would start at 0.</p></div><div id="comment-8266-info" class="comment-info"><span class="comment-age">(07 Jan '12, 11:51)</span> Guy Harris ♦♦</div></div><span id="8274"></span><div id="comment-8274" class="comment"><div id="post-8274-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much again. You explained it great. I will try the zero state and I will let you know if that's the case. I might come back with more question regarding this. Thanks again for your great help.</p></div><div id="comment-8274-info" class="comment-info"><span class="comment-age">(08 Jan '12, 05:34)</span> AminGho</div></div></div><div id="comment-tools-8213" class="comment-tools"></div><div class="clear"></div><div id="comment-8213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

