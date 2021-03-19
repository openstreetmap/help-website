+++
type = "question"
title = "Calculate throughput using WireShark and compare to theoretical bandwidth"
description = '''hi, I would like to know how to solve this problem using wireshark. Problem Download big file and calculate throughput, compare to theoretical bandwidth - Theoretical: Transmission time (in seconds) = Size of file (in bits) / Bandwidth (in bits/second) and Throughput: Throughput (in bits) = Size of ...'''
date = "2012-10-28T06:13:00Z"
lastmod = "2012-10-28T15:25:00Z"
weight = 15320
keywords = [ "using", "throughput", "wireshark" ]
aliases = [ "/questions/15320" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Calculate throughput using WireShark and compare to theoretical bandwidth](/questions/15320/calculate-throughput-using-wireshark-and-compare-to-theoretical-bandwidth)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15320-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, I would like to know how to solve this problem using wireshark. <strong>Problem</strong> Download big file and calculate throughput, compare to theoretical bandwidth - Theoretical: Transmission time (in seconds) = Size of file (in bits) / Bandwidth (in bits/second) and Throughput: Throughput (in bits) = Size of file (in bits) / Transmission time (in seconds).</p></div><div id="question-tags" class="tags-container tags">using throughput wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '12, 06:13</strong></p><img src="https://secure.gravatar.com/avatar/4642f0134e630332b2d9d100882e2bb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amar&#39;s gravatar image" /><p>Amar<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amar has no accepted answers">0%</span></p></div></div><div id="comments-container-15320" class="comments-container"><span id="15321"></span><div id="comment-15321" class="comment"><div id="post-15321-score" class="comment-score"></div><div class="comment-text"><p>if I understand this correctly, simply so to Statistics-&gt; I/O graphs -&gt; and change your Y axis units to Bits/Tick</p></div><div id="comment-15321-info" class="comment-info"><span class="comment-age">(28 Oct '12, 06:35)</span> thetechfirm</div></div><span id="15322"></span><div id="comment-15322" class="comment"><div id="post-15322-score" class="comment-score"></div><div class="comment-text"><p>That is probably not exact enough, and doesn'twork well when the throughput is not constant but goes faster and slower over time...</p></div><div id="comment-15322-info" class="comment-info"><span class="comment-age">(28 Oct '12, 07:44)</span> Jasper ♦♦</div></div></div><div id="comment-tools-15320" class="comment-tools"></div><div class="clear"></div><div id="comment-15320-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15324"></span>

<div id="answer-container-15324" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15324-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>My approach would be: find the TCP session in which the transfer takes place, and calculate the throughput. Usually this is simple in test traces, because the download is the only large transfer and thus easily spotted. Open the conversation statistics and look for the largest TCP conversation. Filter on it (popup menu, A &lt;-&gt; B), set a time reference on the SYN packet, go to the last packet, read relative time and cummulative bytes (you might need to add the according colum first). After that you can use your formula. Or you just look at the throughput in the Summary statistics after filtering the flow. Homework assignment complete.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '12, 15:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-15324" class="comments-container"></div><div id="comment-tools-15324" class="comment-tools"></div><div class="clear"></div><div id="comment-15324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

