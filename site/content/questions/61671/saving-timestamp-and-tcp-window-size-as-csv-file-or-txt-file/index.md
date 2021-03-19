+++
type = "question"
title = "Saving timestamp and tcp window size as CSV file or txt file"
description = '''Hello Is that possible to save only timestamp and TCP window size from a capture file (PCAP file)? How can I do it?'''
date = "2017-05-28T07:00:00Z"
lastmod = "2017-05-28T07:05:00Z"
weight = 61671
keywords = [ "wireshark", "tcpwindowsize" ]
aliases = [ "/questions/61671" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Saving timestamp and tcp window size as CSV file or txt file](/questions/61671/saving-timestamp-and-tcp-window-size-as-csv-file-or-txt-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61671-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>Is that possible to save only timestamp and TCP window size from a capture file (PCAP file)?</p><p>How can I do it?</p></div><div id="question-tags" class="tags-container tags">wireshark tcpwindowsize</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '17, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/5e26585f104939e9d0d1045d25254f1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="foxmodem&#39;s gravatar image" /><p>foxmodem<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="foxmodem has no accepted answers">0%</span></p></div></div><div id="comments-container-61671" class="comments-container"></div><div id="comment-tools-61671" class="comment-tools"></div><div class="clear"></div><div id="comment-61671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61672"></span>

<div id="answer-container-61672" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61672-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>On a command line you can use tshark to do that for you, e.g.</p><pre><code>tshark -r &quot;sample.pcap&quot; -Tfields -e frame.time -e tcp.window_size_value</code></pre><p>-TFields tells tshark to print field values, and the -e parameters specify the display filter name of the field you want.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '17, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61672" class="comments-container"><span id="61673"></span><div id="comment-61673" class="comment"><div id="post-61673-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I will try!</p><p>How can I plot a graphic of timestamp X TCP window size? Wireshark can do it?</p></div><div id="comment-61673-info" class="comment-info"><span class="comment-age">(28 May '17, 07:15)</span> foxmodem</div></div><span id="61674"></span><div id="comment-61674" class="comment"><div id="post-61674-score" class="comment-score"></div><div class="comment-text"><p>Try Statistics - TCP Stream Graphs - Window Scaling</p></div><div id="comment-61674-info" class="comment-info"><span class="comment-age">(28 May '17, 07:18)</span> Jasper ♦♦</div></div></div><div id="comment-tools-61672" class="comment-tools"></div><div class="clear"></div><div id="comment-61672-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

