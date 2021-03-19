+++
type = "question"
title = "Capturing UDP packets from the same computer"
description = '''Hello, I&#x27;m writing a program in C# and I&#x27;m sending UDP messages to my own computer. I want Wireshark to capture those packets, but it doesn&#x27;t capture them. Maybe it&#x27;s because those packets are not transmitted at all through my network card? and if so how can I still capture them using Wireshark? Tha...'''
date = "2010-10-13T01:48:00Z"
lastmod = "2010-10-18T06:05:00Z"
weight = 500
keywords = [ "udp" ]
aliases = [ "/questions/500" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing UDP packets from the same computer](/questions/500/capturing-udp-packets-from-the-same-computer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-500-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm writing a program in C# and I'm sending UDP messages to my own computer. I want Wireshark to capture those packets, but it doesn't capture them. Maybe it's because those packets are not transmitted at all through my network card? and if so how can I still capture them using Wireshark? Thank you in advance, Hod</p></div><div id="question-tags" class="tags-container tags">udp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '10, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/e880605404a7ca5033988fbfbacabe53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hodwolff&#39;s gravatar image" /><p>hodwolff<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hodwolff has no accepted answers">0%</span></p></div></div><div id="comments-container-500" class="comments-container"></div><div id="comment-tools-500" class="comment-tools"></div><div class="clear"></div><div id="comment-500-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="502"></span>

<div id="answer-container-502" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-502-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Maybe it's because those packets are not transmitted at all through my network card?</p></blockquote><p>That is correct. What the capture driver doesn't see won't show up in Wireshark.</p><blockquote><p>and if so how can I still capture them using Wireshark?</p></blockquote><p>That very much depends, see <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">the Wiki</a> on loopback interfaces.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '10, 04:28</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-502" class="comments-container"></div><div id="comment-tools-502" class="comment-tools"></div><div class="clear"></div><div id="comment-502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="504"></span>

<div id="answer-container-504" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-504-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Can you rewrite the code to reference the local computers real IP instead of localhost or 127.0.0.1? That <em>should</em> force the traffic through the stack.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '10, 10:42</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p>GeonJay<br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-504" class="comments-container"><span id="506"></span><div id="comment-506" class="comment"><div id="post-506-score" class="comment-score"></div><div class="comment-text"><p>It probably won't since the stack is usually smart(?) enough to see that (one of) it's own interface addresses is used, hence can loopback before hitting the capture driver.</p></div><div id="comment-506-info" class="comment-info"><span class="comment-age">(14 Oct '10, 01:28)</span> Jaap ♦</div></div></div><div id="comment-tools-504" class="comment-tools"></div><div class="clear"></div><div id="comment-504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="525"></span>

<div id="answer-container-525" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-525-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm using Windows XP SP3 and writing in VS 2008. I've installed MS Loopback adapter on my copmuter but it still doesn't work. It seems like when I try to send a UDP packet I can't define the local IP address in that class - if I'm sending it to my network card or to the Loopback adapter the local address is the same as the remote address, so it doesn't work even when I'm sending to the loopback adapter. Can anyone help please? Thank you</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '10, 06:05</strong></p><img src="https://secure.gravatar.com/avatar/e880605404a7ca5033988fbfbacabe53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hodwolff&#39;s gravatar image" /><p>hodwolff<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hodwolff has no accepted answers">0%</span></p></div></div><div id="comments-container-525" class="comments-container"></div><div id="comment-tools-525" class="comment-tools"></div><div class="clear"></div><div id="comment-525-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

