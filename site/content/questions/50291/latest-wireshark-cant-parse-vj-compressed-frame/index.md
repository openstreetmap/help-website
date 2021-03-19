+++
type = "question"
title = "Latest Wireshark can&#x27;t parse VJ compressed frame"
description = '''For the same packet within the same PCAP file, By using different version of Wireshark tool, I can see different log view. Issue is not seen on Wireshark Version 1.10.0 but seen on recent version such as latest 2.0.1 Example: // Wireshark Version 2.0.1 20 24.0 DTE DCE 0x002d 12 PPP Van Jacobson Comp...'''
date = "2016-02-17T21:46:00Z"
lastmod = "2016-02-18T05:23:00Z"
weight = 50291
keywords = [ "ppp" ]
aliases = [ "/questions/50291" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Latest Wireshark can't parse VJ compressed frame](/questions/50291/latest-wireshark-cant-parse-vj-compressed-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50291-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For the <em>same</em> packet within the <em>same</em> PCAP file, By using different version of Wireshark tool, I can see different log view. Issue is not seen on Wireshark Version 1.10.0 but seen on recent version such as latest 2.0.1</p><p>Example:</p><p>// Wireshark Version 2.0.1</p><p>20 24.0 DTE DCE 0x002d 12 PPP Van Jacobson Compressed TCP/IP (0x002d)</p><p>// Wireshark Version 1.10.0, this is good</p><p>20 2016-02-17 10:01:18.6 14.31.22.16 121.15.143.92 12 TCP 35075 &gt; hbci [PSH, ACK] Seq=1 Ack=1 Win=16384 [TCP CHECKSUM INCORRECT] Len=7</p><p>Can you please let me know if there is any settings relate to this.</p><p>I checked Edit -&gt; Preference -&gt; Protocols -&gt; PPP, &lt;decompressed vj-compressed="" frames=""&gt; is already checked</p></div><div id="question-tags" class="tags-container tags">ppp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '16, 21:46</strong></p><img src="https://secure.gravatar.com/avatar/17f76e7d25aed56f038d848bafe6f881?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephennnuaa&#39;s gravatar image" /><p>stephennnuaa<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephennnuaa has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Feb '16, 21:47</p></div></div><div id="comments-container-50291" class="comments-container"></div><div id="comment-tools-50291" class="comment-tools"></div><div class="clear"></div><div id="comment-50291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50297"></span>

<div id="answer-container-50297" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50297-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please file a bug on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a> and attach the capture to the file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '16, 00:24</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-50297" class="comments-container"><span id="50299"></span><div id="comment-50299" class="comment"><div id="post-50299-score" class="comment-score"></div><div class="comment-text"><p>Thanks Harris, I will file the bug report shortly</p></div><div id="comment-50299-info" class="comment-info"><span class="comment-age">(18 Feb '16, 01:26)</span> stephennnuaa</div></div></div><div id="comment-tools-50297" class="comment-tools"></div><div class="clear"></div><div id="comment-50297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50303"></span>

<div id="answer-container-50303" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50303-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The code to handle Van Jacobson compression was removed from Wireshark, starting with the 1.12 release, due to concerns about its license. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12138">bug 12138</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '16, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-50303" class="comments-container"></div><div id="comment-tools-50303" class="comment-tools"></div><div class="clear"></div><div id="comment-50303-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

