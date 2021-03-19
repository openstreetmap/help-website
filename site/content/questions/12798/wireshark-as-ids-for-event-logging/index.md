+++
type = "question"
title = "wireshark as IDS for event logging?"
description = '''Dear Developer&#x27;s and User&#x27;s of Wireshark, Wireshark is a great application for network monitoring and sniffing. It can decode almost all protocols available from Ethernet,IP even to the WSN&#x27;s protocols such as 802.15.4,6LOWPAN .. etc.  In order to find an attack, we need to monitor the network ( src...'''
date = "2012-07-17T06:13:00Z"
lastmod = "2012-07-17T15:32:00Z"
weight = 12798
keywords = [ "detect", "attack", "plugin", "ids", "wireshark" ]
aliases = [ "/questions/12798" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [wireshark as IDS for event logging?](/questions/12798/wireshark-as-ids-for-event-logging)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12798-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Developer's and User's of Wireshark,</p><p>Wireshark is a great application for network monitoring and sniffing. It can decode almost all protocols available from Ethernet,IP even to the WSN's protocols such as 802.15.4,6LOWPAN .. etc.</p><p>In order to find an attack, we need to monitor the network ( src, dest address and the invalid packets nature ). So is it possible for an application or plugin developed for wireshark, to use it for detecting attack event's?</p><p>And possibly develop an low-level Intrusion Detection System?? Does it exist in some or other way?</p><p>I just need to monitor the src address, and if it's flooding or not!</p></div><div id="question-tags" class="tags-container tags">detect attack plugin ids wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '12, 06:13</strong></p><img src="https://secure.gravatar.com/avatar/f3d738bff0414eeb08274b0152607e76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="prabhakaran&#39;s gravatar image" /><p>prabhakaran<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="prabhakaran has no accepted answers">0%</span></p></div></div><div id="comments-container-12798" class="comments-container"></div><div id="comment-tools-12798" class="comment-tools"></div><div class="clear"></div><div id="comment-12798-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12808"></span>

<div id="answer-container-12808" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12808-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Note that Wireshark (and TShark) both keep data structures used in the dissection process, to keep track of requests and matching responses (for example, some protocols don't carry enough information in a response to decode the response, so you need to find the request to which it's a response to get information such as the request code), do packet reassembly, and so on.</p><p>This means that the memory requirements of Wireshark and TShark increase as more packets are captured or read, so the memory used by Wireshark and TShark will increase over time.</p><p>They also do a very detailed dissection of packets, which might be more than is needed for an IDS.</p><p>This makes it not ideal as an intrusion detection system; that's not a function for which it was designed. It might be better to use programs designed to act as intrusion detection systems for that purpose, such as as <a href="http://www.snort.org/">Snort</a> and <a href="http://bro-ids.org/">Bro</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '12, 13:57</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-12808" class="comments-container"><span id="12811"></span><div id="comment-12811" class="comment"><div id="post-12811-score" class="comment-score"></div><div class="comment-text"><p>@Guy Harris : Thank you for your answer. I think it's appropriate.</p><p>In the existing IDS, they support very limited protocols. And they follow their own data structure's such that, we cannot use the existing wireshark protocol dissector's with them. And I wanted to develop an IDS for WSN's. That's why i wanted to know whether any plugins have been developed keeping this in mind.</p><p>Anyway thanks for your response. If someone got some idea. please dont wait to post your opinion!</p></div><div id="comment-12811-info" class="comment-info"><span class="comment-age">(17 Jul '12, 14:12)</span> prabhakaran</div></div></div><div id="comment-tools-12808" class="comment-tools"></div><div class="clear"></div><div id="comment-12808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12815"></span>

<div id="answer-container-12815" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12815-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I just need to monitor the src address, and if it's flooding or not!</p></blockquote><p>if you need just that, wireshark would be kind of "overkill", as you spend a lot of CPU time dissecting packets while you just want the src ip and a summary about the packet rate within a defined timeslice.</p><p>If you really need just that, I recommend some tutorials about libpcap programming. With that knowledge you can write your own little tool that does exactly what you need, without the "hassle" of dissecting packets (but also without the benefit of it).</p><blockquote><p><code>http://www.tcpdump.org/pcap.html</code><br />
<code>http://undergraduate.csse.uwa.edu.au/units/CITS3231/reading/libpcap-programming.pdf</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '12, 15:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jul '12, 16:18</p></div></div><div id="comments-container-12815" class="comments-container"><span id="12825"></span><div id="comment-12825" class="comment"><div id="post-12825-score" class="comment-score"></div><div class="comment-text"><p>@Kurt : Thanks for your Opinion. I will have a look at it. The libpcap programming document was very good! thanks for sharing.</p></div><div id="comment-12825-info" class="comment-info"><span class="comment-age">(18 Jul '12, 05:40)</span> prabhakaran</div></div><span id="12829"></span><div id="comment-12829" class="comment"><div id="post-12829-score" class="comment-score"></div><div class="comment-text"><p>you're welcome. Good luck.</p></div><div id="comment-12829-info" class="comment-info"><span class="comment-age">(18 Jul '12, 07:03)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12815" class="comment-tools"></div><div class="clear"></div><div id="comment-12815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

