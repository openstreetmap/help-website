+++
type = "question"
title = "Usb 3 Support"
description = '''Will there be usb 3 support?'''
date = "2016-07-21T23:30:00Z"
lastmod = "2016-07-22T00:26:00Z"
weight = 54232
keywords = [ "3", "usb" ]
aliases = [ "/questions/54232" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Usb 3 Support](/questions/54232/usb-3-support)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54232-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Will there be usb 3 support?</p></div><div id="question-tags" class="tags-container tags">3 usb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '16, 23:30</strong></p><img src="https://secure.gravatar.com/avatar/fccde3e506caa2409e5459164de2065d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peanut&#39;s gravatar image" /><p>Peanut<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peanut has no accepted answers">0%</span></p></div></div><div id="comments-container-54232" class="comments-container"></div><div id="comment-tools-54232" class="comment-tools"></div><div class="clear"></div><div id="comment-54232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54233"></span>

<div id="answer-container-54233" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54233-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="https://www.wireshark.org/faq.html#q1.11">Faq 1.11</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '16, 23:45</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-54233" class="comments-container"></div><div id="comment-tools-54233" class="comment-tools"></div><div class="clear"></div><div id="comment-54233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54234"></span>

<div id="answer-container-54234" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54234-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There <strong>is</strong> USB3 support, if you have in mind USBPcap on Windows. But the documentation is not really good. In the <a href="http://desowin.org/usbpcap/todo.html">TODO section of USBPcap's home page</a>, there is a description of the problem and solution. The fact that it prints using <del>stroked-out text</del> suggests that the problem has been solved. There is a link to a mailing list on the topic in the end of that text, but in that list there is still no clear statement how to switch on USB 3.0 support.</p><p>So you have to go to the command line, move to the directory where you have told the installer to put USBPcap, and run <code>USBPcapCMD.exe -I</code> . In my case, it looked the following way:</p><pre><code>c:\Program Files\USBPcap&gt;USBPcapCMD.exe -I

c:\Program Files\USBPcap&gt;Hardware ID: USB\ROOT_HUB30&amp;VID8086&amp;PID1E31&amp;REV0004
Hardware ID: USB\ROOT_HUB30&amp;VID8086&amp;PID1E31
Hardware ID: USB\ROOT_HUB30
RootHub does not have standard HWID! Added USB\ROOT_HUB30&amp;VID8086&amp;PID1E31&amp;REV0004 to non-standard list.
Hardware ID: USB\ROOT_HUB20&amp;VID8086&amp;PID1E26&amp;REV0004
Hardware ID: USB\ROOT_HUB20&amp;VID8086&amp;PID1E26
Hardware ID: USB\ROOT_HUB20
Found standard HWID
...</code></pre><p>After this, you can start Wireshark again. Either you'll see one more <em>USBPcapN</em> interface in the list, or the one on which you've never captured anything before will "come alive". Start the capture, insert your USB3.0 device and see the miracle happen.</p><p>The theory below is that USB3.0 is in fact a completely separate subsystem with its own root hub and its own electrical contacts on the connectors shared with the USB 1.1/2.0 root hub. So to capture a 3.0 device, you need to capture at a different <em>USBPcapN</em> interface than to capture a 2.0 device inserted to the same connector on your PC.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '16, 00:26</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-54234" class="comments-container"></div><div id="comment-tools-54234" class="comment-tools"></div><div class="clear"></div><div id="comment-54234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

