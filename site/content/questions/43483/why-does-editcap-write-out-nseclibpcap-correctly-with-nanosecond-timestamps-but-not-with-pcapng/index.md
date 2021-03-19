+++
type = "question"
title = "Why does editcap write out nseclibpcap correctly with nanosecond timestamps, but not with pcapng?"
description = '''I have a pcap file with nanosecond timestamps. I have used a hex editor to make sure the magic number in the header is correct, and Wireshark does interpret the timestamps correctly. I run the following command to convert it to pcapng: editcap -F pcapng input.pcap output.pcapng  And editcap writes o...'''
date = "2015-06-23T14:04:00Z"
lastmod = "2015-06-24T15:28:00Z"
weight = 43483
keywords = [ "nseclibpcap", "editcap", "nanosecond" ]
aliases = [ "/questions/43483" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Why does editcap write out nseclibpcap correctly with nanosecond timestamps, but not with pcapng?](/questions/43483/why-does-editcap-write-out-nseclibpcap-correctly-with-nanosecond-timestamps-but-not-with-pcapng)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43483-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a pcap file with nanosecond timestamps. I have used a hex editor to make sure the magic number in the header is correct, and Wireshark does interpret the timestamps correctly. I run the following command to convert it to pcapng:</p><pre><code>editcap -F pcapng input.pcap output.pcapng</code></pre><p>And editcap writes out a file with only microsecond resolution. This is concerning, because several tools that rely on WinPcap incorrectly interpret nanosecond timestamps as microsecond -- which leads to out of order packets downstream -- and I was concerned editcap might be doing the same thing. Out of curiosity, I tried the following command, to see what would happen:</p><pre><code>editcap -F nseclibpcap input.pcap output.pcap</code></pre><p>And as output, got a pcap with nanosecond timestamps!</p><p>I am hoping someone can explain what is going on here. Are there essentially two "errors" dealing with nanosecond pcaps that are cancelling each other out in the 2nd case (i.e. keeps the ts_usec field is kept unaltered in the process)? In the first case, is it interpreting the ts_usec field correctly and truncating, or is it interpreting it as microsecond and timestamps will be inaccurate? Does editcap use winpcap at all?</p></div><div id="question-tags" class="tags-container tags">nseclibpcap editcap nanosecond</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '15, 14:04</strong></p><img src="https://secure.gravatar.com/avatar/bc7ef38c9fb207c34f2903fe2876744d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chuu&#39;s gravatar image" /><p>Chuu<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chuu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jun '15, 14:25</p></div></div><div id="comments-container-43483" class="comments-container"></div><div id="comment-tools-43483" class="comment-tools"></div><div class="clear"></div><div id="comment-43483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43525"></span>

<div id="answer-container-43525" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43525-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Editcap does not WinPcap. Instead it has its own code to handle the various formats conversion. As you noticed, right now pcapng export only supports the default microseconds timestamp but it properly truncates the value so you do not have any corruption (as Wireshark stores all timestamps internally with nano seconds definition by default).</p><p>Edit: I'm adding the ability to keep nanosecond timestamp resolution when converting to pcapng format in Wireshark 1.99.8. The corresponding review can be found here: <a href="https://code.wireshark.org/review/#/c/9111/">https://code.wireshark.org/review/#/c/9111/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '15, 15:28</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jun '15, 17:13</p></div></div><div id="comments-container-43525" class="comments-container"></div><div id="comment-tools-43525" class="comment-tools"></div><div class="clear"></div><div id="comment-43525-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

