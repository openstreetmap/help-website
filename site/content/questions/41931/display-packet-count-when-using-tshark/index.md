+++
type = "question"
title = "Display packet count when using tshark"
description = '''I&#x27;m using dumpcap to capture packets. Typically looks like this: $ dumpcap -i eth0 -a duration:1 -w test.pcap Capturing on mon0 File: test.pcap Packets captured: 63 Packets received/dropped on interface mon0: 63/0 (100.0%)  I put this into a script and would like to save the number of captured packe...'''
date = "2015-04-28T19:38:00Z"
lastmod = "2015-04-28T20:30:00Z"
weight = 41931
keywords = [ "dumpcap", "tshark" ]
aliases = [ "/questions/41931" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Display packet count when using tshark](/questions/41931/display-packet-count-when-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41931-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using dumpcap to capture packets. Typically looks like this:</p><pre><code>$ dumpcap -i eth0 -a duration:1 -w test.pcap
Capturing on mon0
File: test.pcap
Packets captured: 63
Packets received/dropped on interface mon0: 63/0 (100.0%)</code></pre><p>I put this into a script and would like to save the number of captured packets (63 in the example above) to a file. I can do it by using for example tshark, but that's not what I'm after. Just looking for something like wc -l that gives me the count of captured packets in the pcap file.</p><p>Any suggestions? Thanks!</p><p>/Z</p></div><div id="question-tags" class="tags-container tags">dumpcap tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '15, 19:38</strong></p><img src="https://secure.gravatar.com/avatar/c19324dc35615378dc81ba8a3d71b0b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SamA&#39;s gravatar image" /><p>SamA<br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SamA has no accepted answers">0%</span></p></div></div><div id="comments-container-41931" class="comments-container"></div><div id="comment-tools-41931" class="comment-tools"></div><div class="clear"></div><div id="comment-41931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41933"></span>

<div id="answer-container-41933" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41933-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you <strong>only</strong> want the packet count, after <code>dumpcap</code> completes, your script could run "<a href="https://www.wireshark.org/docs/man-pages/capinfos.html"><code>capinfos</code></a> <code>-Trc test.pcap</code>". If you don't want the filename displayed before the count value, you could further pipe the output to <code>sed</code> to remove the filename using an appropriate substitution string.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '15, 20:30</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-41933" class="comments-container"><span id="41942"></span><div id="comment-41942" class="comment"><div id="post-41942-score" class="comment-score"></div><div class="comment-text"><p>Thanks cmaynard. Useful!</p></div><div id="comment-41942-info" class="comment-info"><span class="comment-age">(29 Apr '15, 05:17)</span> SamA</div></div></div><div id="comment-tools-41933" class="comment-tools"></div><div class="clear"></div><div id="comment-41933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41932"></span>

<div id="answer-container-41932" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41932-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just found the answer myself:</p><p>capinfos test.pcap</p><p>does the trick!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '15, 20:13</strong></p><img src="https://secure.gravatar.com/avatar/c19324dc35615378dc81ba8a3d71b0b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SamA&#39;s gravatar image" /><p>SamA<br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SamA has no accepted answers">0%</span></p></div></div><div id="comments-container-41932" class="comments-container"></div><div id="comment-tools-41932" class="comment-tools"></div><div class="clear"></div><div id="comment-41932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

