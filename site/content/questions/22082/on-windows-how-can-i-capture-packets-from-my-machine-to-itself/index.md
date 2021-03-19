+++
type = "question"
title = "On Windows, how can I capture packets from my machine to itself?"
description = '''Hello all, I want to capture sntp packets from system(windows 8) running as both server and client(using a tool). my question is how can i capture ntp packets from this tool using wireshark in other system(windows xp) while server client tool(both as server and client) is synchronizing time in unica...'''
date = "2013-06-15T00:09:00Z"
lastmod = "2013-06-17T17:23:00Z"
weight = 22082
keywords = [ "windows", "loopback" ]
aliases = [ "/questions/22082" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [On Windows, how can I capture packets from my machine to itself?](/questions/22082/on-windows-how-can-i-capture-packets-from-my-machine-to-itself)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22082-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I want to capture sntp packets from system(windows 8) running as both server and client(using a tool). my question is how can i capture ntp packets from this tool using wireshark in other system(windows xp) while server client tool(both as server and client) is synchronizing time in unicast mode.</p><p>thankfully monisha</p></div><div id="question-tags" class="tags-container tags">windows loopback</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '13, 00:09</strong></p><img src="https://secure.gravatar.com/avatar/767dcd7d6261caeaff96971a2356a682?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sana&#39;s gravatar image" /><p>sana<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sana has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jun '13, 16:33</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-22082" class="comments-container"></div><div id="comment-tools-22082" class="comment-tools"></div><div class="clear"></div><div id="comment-22082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22088"></span>

<div id="answer-container-22088" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22088-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>see the answer to a similar question:</p><blockquote><p><code>http://ask.wireshark.org/questions/21912/sntp-packet-cannot-be-captured</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '13, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-22088" class="comments-container"><span id="22112"></span><div id="comment-22112" class="comment"><div id="post-22112-score" class="comment-score"></div><div class="comment-text"><p>hi ,</p><p>Gone through the link. Can I use same system as client and server to capture those packets in other system? if so what are all the settings required in wireshark or how can i do that?</p><p>thanks for ur time sana</p></div><div id="comment-22112-info" class="comment-info"><span class="comment-age">(16 Jun '13, 23:57)</span> sana</div></div><span id="22116"></span><div id="comment-22116" class="comment"><div id="post-22116-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Can I use <strong>same system</strong> as client and server to capture those packets in <strong>other system</strong>?</p></blockquote><p>??? <strong>same</strong> system or <strong>other</strong> system?</p></div><div id="comment-22116-info" class="comment-info"><span class="comment-age">(17 Jun '13, 06:20)</span> Kurt Knochner ♦</div></div><span id="22125"></span><div id="comment-22125" class="comment"><div id="post-22125-score" class="comment-score"></div><div class="comment-text"><p>ya like single system(system 1)works as both server and client and one more system(system 2) to capture packets(from system 1) using wireshark</p></div><div id="comment-22125-info" class="comment-info"><span class="comment-age">(17 Jun '13, 22:12)</span> sana</div></div><span id="22126"></span><div id="comment-22126" class="comment"><div id="post-22126-score" class="comment-score"></div><div class="comment-text"><blockquote><p>ya like single system(system 1)works as both server and client and one more system(system 2) to capture packets(from system 1) using wireshark</p></blockquote><p>Can't work and won't work. System 1 is communicating with system 1 (i.e., with itself) over an internal connection within the operating system software, <em>NOT</em> over an Ethernet or Wi-Fi network or anything else to which system 2 has any access whatsoever, and, unfortunately, unlike many UN*Xes, that internal network can't be sniffed using the same mechanism that is used to sniff external networks, so Wireshark can't see the traffic even on system 1 itself.</p><p>See my answer.</p></div><div id="comment-22126-info" class="comment-info"><span class="comment-age">(17 Jun '13, 23:04)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-22088" class="comment-tools"></div><div class="clear"></div><div id="comment-22088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22124"></span>

<div id="answer-container-22124" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22124-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the same computer is being used as both a client and a server, and that computer is using itself as a server, so that all the messages are sent from the computer to itself, you cannot capture them by using some other system; those packets are <em>NOT</em> transmitted on <em>ANY</em> network, much less a network that some other computer can sniff on.</p><p>On Windows, about all you can do in that case is run <a href="http://www.netresec.com/?page=RawCap">RawCap</a> and have it write out to a file, and then read the file in Wireshark (or TShark or tcpdump/WinDump or...).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '13, 17:23</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-22124" class="comments-container"></div><div id="comment-tools-22124" class="comment-tools"></div><div class="clear"></div><div id="comment-22124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

