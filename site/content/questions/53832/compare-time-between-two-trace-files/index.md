+++
type = "question"
title = "compare time between two trace files"
description = '''hello, if I get two capture files from two different systems how can I make sure that both were captured simultaneously ?  I can see in the Frame details section provide by Wireshark:  But the other trace file shows :  So there&#x27;s at least 6 minutes difference. Is this information reliable ? Can it b...'''
date = "2016-07-05T06:24:00Z"
lastmod = "2016-07-05T07:31:00Z"
weight = 53832
keywords = [ "tls" ]
aliases = [ "/questions/53832" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [compare time between two trace files](/questions/53832/compare-time-between-two-trace-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53832-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello,</p><p>if I get two capture files from two different systems how can I make sure that both were captured simultaneously ?</p><p>I can see in the Frame details section provide by Wireshark:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/arrival_time.JPG" alt="alt text" /></p><p>But the other trace file shows :</p><p><img src="https://osqa-ask.wireshark.org/upfiles/222.JPG" alt="alt text" /></p><p>So there's at least 6 minutes difference. Is this information reliable ? Can it be caused by perhaps different time settings on both hosts ?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">tls</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '16, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p>adasko<br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></img></div></div><div id="comments-container-53832" class="comments-container"></div><div id="comment-tools-53832" class="comment-tools"></div><div class="clear"></div><div id="comment-53832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53836"></span>

<div id="answer-container-53836" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53836-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Time stamping is very much depending on the capture host clock and then some. So if there are no measures in place to sync the capture points and you have no measure of their clock difference there is little you can depend on.</p><p>If you do have a measure of their difference you can use <a href="https://www.wireshark.org/docs/man-pages/editcap.html">editcap</a> to manipulate the time stamps in one of the capture files to bring them back together. Still this won't compensate for clock drift in unsynchronized capture hosts, but could be a start. It will never be accurate though.</p><p>Further reading:</p><ul><li><a href="https://www.wireshark.org/docs/wsug_html_chunked/ChAdvTimestamps.html">User Guide: time stamps</a></li><li><a href="https://www.winpcap.org/docs/docs_40_2/html/group__NPF.html">NPF driver internals</a></li><li><a href="https://www.elvidence.com.au/understanding-time-stamps-in-packet-capture-data-pcap-files/">Understanding time stamps in packet capture data</a></li><li><a href="http://www.winpcap.org/docs/default.htm">WinPcap documentation</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '16, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></img></div></div><div id="comments-container-53836" class="comments-container"></div><div id="comment-tools-53836" class="comment-tools"></div><div class="clear"></div><div id="comment-53836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

