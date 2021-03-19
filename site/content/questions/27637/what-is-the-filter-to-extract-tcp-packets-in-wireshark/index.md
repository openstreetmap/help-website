+++
type = "question"
title = "What is the filter to extract TCP packets? (in wireshark)"
description = '''Anyone knows, please tell me. Your help is highly appreciated.'''
date = "2013-12-01T22:10:00Z"
lastmod = "2013-12-02T02:59:00Z"
weight = 27637
keywords = [ "tcppackets", "tshark", "tcp", "wireshark" ]
aliases = [ "/questions/27637" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What is the filter to extract TCP packets? (in wireshark)](/questions/27637/what-is-the-filter-to-extract-tcp-packets-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27637-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Anyone knows, please tell me. Your help is highly appreciated.</p></div><div id="question-tags" class="tags-container tags">tcppackets tshark tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '13, 22:10</strong></p><img src="https://secure.gravatar.com/avatar/f6794f3ef18ab7a1ad2e4f56711db6f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eliza%20Rana&#39;s gravatar image" /><p>Eliza Rana<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eliza Rana has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Dec '13, 22:19</p></div></div><div id="comments-container-27637" class="comments-container"></div><div id="comment-tools-27637" class="comment-tools"></div><div class="clear"></div><div id="comment-27637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27656"></span>

<div id="answer-container-27656" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27656-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use tshark as following on Linux/OSX:</p><pre><code>tshark -R &quot;tcp&quot; -r [path-to-file]</code></pre><p>or if your on Windwos and tshark is not in your path open <em>Command Prompt</em> aka <em>CMD</em>:</p><pre><code>cd C:\Program Files\Wireshark
tshark.exe -R &quot;tcp&quot; -r [path-to-file]</code></pre><p>You can view all options of <em>tshark</em> command with -h:</p><pre><code>tshark -h</code></pre><p>Let us know.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '13, 02:59</strong></p><img src="https://secure.gravatar.com/avatar/57dca282828fcb7b6086c0a77af93ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Edmond&#39;s gravatar image" /><p>Edmond<br />
<span class="score" title="181 reputation points">181</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Edmond has 2 accepted answers">33%</span></p></div></div><div id="comments-container-27656" class="comments-container"><span id="27665"></span><div id="comment-27665" class="comment"><div id="post-27665-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your help, Edmond. I would like to ask you one more question.</p><p>Here is my assignment: Plot time-series graph for number of TCP packets per 1 second.</p><p>I am plotting this graph using R programming in Windows. And I have to read csv file(that is transformed from pcap file) into R and then plot the time-series graph. In order to plot a graph, there must be 2 values x and y. So I consider x as frame.time. And the y must be the number of TCP packet per 1 second, but I don't know what it is and how to calculate it.</p><p>So could you help me please?</p></div><div id="comment-27665-info" class="comment-info"><span class="comment-age">(02 Dec '13, 08:30)</span> Eliza Rana</div></div></div><div id="comment-tools-27656" class="comment-tools"></div><div class="clear"></div><div id="comment-27656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27654"></span>

<div id="answer-container-27654" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27654-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>All the info you need for tshark can be found on the <a href="http://www.wireshark.org/docs/man-pages/tshark.html">man page</a>, or a summary by giving tshark a <code>-h</code> parameter.</p><p>For filters, you need to look at <a href="http://wiki.wireshark.org/CaptureFilters">Capture Filters</a> and <a href="http://wiki.wireshark.org/DisplayFilters">Display Filters</a>. Which one to use depends on your task and environment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '13, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Dec '13, 02:52</p></div></div><div id="comments-container-27654" class="comments-container"></div><div id="comment-tools-27654" class="comment-tools"></div><div class="clear"></div><div id="comment-27654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

