+++
type = "question"
title = "What is the tshark command to open previously captured pcap files?"
description = '''if we want to open pcap files in tshark is it possible?'''
date = "2015-03-26T04:38:00Z"
lastmod = "2015-03-26T05:15:00Z"
weight = 40881
keywords = [ "pcap", "tshark" ]
aliases = [ "/questions/40881" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What is the tshark command to open previously captured pcap files?](/questions/40881/what-is-the-tshark-command-to-open-previously-captured-pcap-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40881-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>if we want to open pcap files in tshark is it possible?</p></div><div id="question-tags" class="tags-container tags">pcap tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '15, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p>ankit<br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></div></div><div id="comments-container-40881" class="comments-container"></div><div id="comment-tools-40881" class="comment-tools"></div><div class="clear"></div><div id="comment-40881-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40883"></span>

<div id="answer-container-40883" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40883-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can always refer to the tshark manual page, of which a current version is available on <a href="https://www.wireshark.org/docs/man-pages/tshark.html">the Wireshark web site</a>.</p><p>As for your question: use the command line option <code>-r &lt;filename&gt;</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '15, 05:11</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-40883" class="comments-container"><span id="40928"></span><div id="comment-40928" class="comment"><div id="post-40928-score" class="comment-score"></div><div class="comment-text"><p>thanks man</p></div><div id="comment-40928-info" class="comment-info"><span class="comment-age">(26 Mar '15, 20:18)</span> ankit</div></div></div><div id="comment-tools-40883" class="comment-tools"></div><div class="clear"></div><div id="comment-40883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40885"></span>

<div id="answer-container-40885" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40885-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you looked at the <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark manual page</a> or tried the help output from tshark <code>tshark -h</code>?</p><p>Using either method you should see the -r &lt;infile&gt; option to read from a file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '15, 05:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Mar '15, 05:15</p></div></div><div id="comments-container-40885" class="comments-container"><span id="40927"></span><div id="comment-40927" class="comment"><div id="post-40927-score" class="comment-score"></div><div class="comment-text"><p>thanks man</p></div><div id="comment-40927-info" class="comment-info"><span class="comment-age">(26 Mar '15, 20:18)</span> ankit</div></div></div><div id="comment-tools-40885" class="comment-tools"></div><div class="clear"></div><div id="comment-40885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

