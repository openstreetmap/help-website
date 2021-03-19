+++
type = "question"
title = "Wireshark display increasing trace file"
description = '''I have a trace file which is keep growing till trace stops. My requirement is to display the growing trace file in Wireshrk so that user can get the real time packet capturing experience. I have Wireshark Version 1.6.0rc2. How can I achieve this using command line parameters? Please suggest.'''
date = "2012-11-07T20:17:00Z"
lastmod = "2012-11-08T06:01:00Z"
weight = 15674
keywords = [ "rtp" ]
aliases = [ "/questions/15674" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark display increasing trace file](/questions/15674/wireshark-display-increasing-trace-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15674-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a trace file which is keep growing till trace stops. My requirement is to display the growing trace file in Wireshrk so that user can get the real time packet capturing experience. I have Wireshark Version 1.6.0rc2. How can I achieve this using command line parameters? Please suggest.</p></div><div id="question-tags" class="tags-container tags">rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '12, 20:17</strong></p><img src="https://secure.gravatar.com/avatar/97e620804d00012d2cec1885d6422a13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manojdeoli&#39;s gravatar image" /><p>manojdeoli<br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manojdeoli has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Nov '12, 20:18</p></div></div><div id="comments-container-15674" class="comments-container"></div><div id="comment-tools-15674" class="comment-tools"></div><div class="clear"></div><div id="comment-15674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15685"></span>

<div id="answer-container-15685" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15685-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>By default, Wireshark updates the packet list while capturing in GUI mode. The following options will change that behaviour:</p><blockquote><p><code>Edit -&gt; Preferences -&gt; Capture -&gt; Update list of packets in real time</code><br />
<code>Edit -&gt; Preferences -&gt; Capture -&gt; Automatic scrolling in live capture</code><br />
<code>Edit -&gt; Preferences -&gt; Capture -&gt; Hide capture info dialog</code><br />
</p></blockquote><p>Please try them to see the difference. You can set these option on the commandline</p><blockquote><p><code>wireshark -o capture.real_time_update:FALSE -o capture.auto_scroll:TRUE -o capture.show_info:FALSE</code><br />
</p></blockquote><p>TRUE enables the option and FLASE disables the option.</p><p>If you capture at the commandline (with tshark), tshark will show the packets as well and if you use option -w (write capture file) it will count the packets and show that counter.</p><p>If your Wireshark version does not work like this, I recommend to use the latest released version 1.8.3.</p><p>If I misunderstood your question, please add some details.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '12, 00:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-15685" class="comments-container"></div><div id="comment-tools-15685" class="comment-tools"></div><div class="clear"></div><div id="comment-15685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15713"></span>

<div id="answer-container-15713" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15713-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you're saying that some other process is creating the capture file and you want Wireshark to read from that file like it was a live capture; is that correct?</p><p>In that case: Wireshark doesn't do that yet. There is a bug request asking for the functionality: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5982">bug 5982</a> but it hasn't been implemented yet.</p><p>Also: 1.6.0rc2 is a Release Candidate for 1.6.0. 1.6.0 (the official release) has long since been released and the current 1.6 version is 1.6.11...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '12, 06:01</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span> </br></br></p></div></div><div id="comments-container-15713" class="comments-container"></div><div id="comment-tools-15713" class="comment-tools"></div><div class="clear"></div><div id="comment-15713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

