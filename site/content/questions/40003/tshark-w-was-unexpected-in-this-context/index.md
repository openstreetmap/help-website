+++
type = "question"
title = "tshark: &quot;-w&quot; was unexpected in this context."
description = '''Hello, I wrote a filter like that:  -r &quot;c:&#92;&#92;temp&#92;&#92;test1.pcap&quot; tcp.stream eq 17 -w &quot;c:&#92;&#92;temp&#92;&#92;output&#92;&#92;tcp-stream17.pcap&quot;  However, it says that &quot;-w&quot; was unexpected in this context. Any idea what is wrong? Thank you all. '''
date = "2015-02-21T03:32:00Z"
lastmod = "2015-02-21T10:26:00Z"
weight = 40003
keywords = [ "tshark" ]
aliases = [ "/questions/40003" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tshark: "-w" was unexpected in this context.](/questions/40003/tshark-w-was-unexpected-in-this-context)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40003-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I wrote a filter like that:</p><pre><code>-r &quot;c:\\temp\\test1.pcap&quot; tcp.stream eq 17 -w &quot;c:\\temp\\output\\tcp-stream17.pcap&quot;</code></pre><p>However, it says that "-w" was unexpected in this context. Any idea what is wrong? Thank you all.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '15, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/18b564e64b58aeced67f48ae0c9b51dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maayan%20Cohen&#39;s gravatar image" /><p>Maayan Cohen<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maayan Cohen has no accepted answers">0%</span></p></div></div><div id="comments-container-40003" class="comments-container"></div><div id="comment-tools-40003" class="comment-tools"></div><div class="clear"></div><div id="comment-40003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40007"></span>

<div id="answer-container-40007" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40007-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Simply quoting the filter string doesn't work, you're mixing positional parameter use and explicit named parameter use. Either move the (positional) filter to the end:</p><p><code>-r C:\Temp\test1.pcap -w C:\temp\output\tcp-stream17.pcap tcp.stream eq 17</code></p><p>or add the -Y parameter to indicate it's a display filter (and quote the filter):</p><p><code>-r C:\Temp\test1.pcap -Y "tcp.stream eq 17" -w C:\temp\output\tcp-stream17.pcap</code></p><p>Also note that you don't need to escape the backslashes and as the paths don't have spaces you don't need to quote them either.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '15, 10:26</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Feb '15, 10:27</p></div></div><div id="comments-container-40007" class="comments-container"></div><div id="comment-tools-40007" class="comment-tools"></div><div class="clear"></div><div id="comment-40007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40004"></span>

<div id="answer-container-40004" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40004-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use quotes around your filter expression.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '15, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40004" class="comments-container"></div><div id="comment-tools-40004" class="comment-tools"></div><div class="clear"></div><div id="comment-40004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

