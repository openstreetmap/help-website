+++
type = "question"
title = "how to save logs in fully recognizable format?"
description = '''HI, I use wireshark and save logs, but part of each log is not recognizable like: &#x27;§őSPG ŕ ŕ %x PĆ( E Ňu TN…žŐŔ¨d ľHR&amp;lt;14&amp;gt;[172-10:00:55:950] 192.168.0.002 CallReportType:call_end, calling:555999333, called:101111000, origin:callout, answer: 0-00-00 00:00:00, end: 0-00-00 00:00:00, bill...'''
date = "2014-08-25T01:00:00Z"
lastmod = "2014-08-25T01:47:00Z"
weight = 35699
keywords = [ "log" ]
aliases = [ "/questions/35699" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to save logs in fully recognizable format?](/questions/35699/how-to-save-logs-in-fully-recognizable-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35699-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI,</p><p>I use wireshark and save logs, but part of each log is not recognizable like:</p><p>'§őSPG ŕ ŕ %?x PĆ(<code> E  Ňu</code> TN…žŐŔ¨d ľHR&lt;14&gt;[172-10:00:55:950] 192.168.0.002 CallReportType:call_end, calling:555999333, called:101111000, origin:callout, answer: 0-00-00 00:00:00, end: 0-00-00 00:00:00, billsec:0</p><p>Each line before marker &lt;14&gt; has this type of string.</p><p>Can You explain why or suggest how to configure to become logs recognizable like in wireshark window?</p></div><div id="question-tags" class="tags-container tags">log</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '14, 01:00</strong></p><img src="https://secure.gravatar.com/avatar/3690418a10f47a981a8999ff8bab8a9d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="invoso&#39;s gravatar image" /><p>invoso<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="invoso has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Aug '14, 01:20</p></div></div><div id="comments-container-35699" class="comments-container"></div><div id="comment-tools-35699" class="comment-tools"></div><div class="clear"></div><div id="comment-35699-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35700"></span>

<div id="answer-container-35700" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35700-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What means "recognizable" to you? Wireshark "logs" (usually called "traces" or "captures") are binary, not text, because ASCII text would lose too much information and can't be worked with regarding filters etc. Traces are supposed to be looked at in Wireshark or other Analyzers, not text editors.</p><p>If you need certain elements as text you can use the file -&gt; export menus to do that. But keep in mind that the capture always produces binary files first, so you cannot capture directly to text.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '14, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35700" class="comments-container"><span id="35702"></span><div id="comment-35702" class="comment"><div id="post-35702-score" class="comment-score"></div><div class="comment-text"><p>I mean that begin of each line looks not recognizable: '§őSPG ŕ ŕ %?x PĆ( E Ňu TN…žŐŔ¨d ľHR&lt;14&gt;</p><p>this data in Wireshark including No., time, source, destination, protocol. length and info but in logs data before &lt;14&gt; including characters not recognizable for me. (notepad++)</p></div><div id="comment-35702-info" class="comment-info"><span class="comment-age">(25 Aug '14, 02:24)</span> invoso</div></div><span id="35703"></span><div id="comment-35703" class="comment"><div id="post-35703-score" class="comment-score"></div><div class="comment-text"><p>of couse - it's stored in binary, not ASCII ;-)</p><p>If you need to have the packet list as text you can export it via</p><p>File -&gt; Export Packet Dissections -&gt; as CSV</p></div><div id="comment-35703-info" class="comment-info"><span class="comment-age">(25 Aug '14, 02:30)</span> Jasper ♦♦</div></div><span id="35704"></span><div id="comment-35704" class="comment"><div id="post-35704-score" class="comment-score"></div><div class="comment-text"><p>It works, but how to set in capture settings?</p><p>I need to be sure that wireshark storing data in realtime.</p><p>Or how to convert to ascii?</p></div><div id="comment-35704-info" class="comment-info"><span class="comment-age">(25 Aug '14, 03:23)</span> invoso</div></div><span id="35705"></span><div id="comment-35705" class="comment"><div id="post-35705-score" class="comment-score"></div><div class="comment-text"><p>Wireshark is storing data in realtime, and those life captures can <strong>only</strong> be stored as PCAP or PCAPng binary files.</p><p>You can convert existing files to other formats using the editcap command (comes with Wireshark; command line tool). The parameter you need is -F for specifying the output format. If you run "editcap -F" you'll get a list of all available formats.</p></div><div id="comment-35705-info" class="comment-info"><span class="comment-age">(25 Aug '14, 03:33)</span> Jasper ♦♦</div></div><span id="35899"></span><div id="comment-35899" class="comment"><div id="post-35899-score" class="comment-score"></div><div class="comment-text"><p>But part of logs are recognizable, those after &lt;14&gt; marker.</p></div><div id="comment-35899-info" class="comment-info"><span class="comment-age">(01 Sep '14, 01:37)</span> invoso</div></div><span id="35900"></span><div id="comment-35900" class="comment not_top_scorer"><div id="post-35900-score" class="comment-score"></div><div class="comment-text"><p>yes, because the packet contains ASCII content. This means that the network packet transported readable text, and is displayed as such. The packet and frame headers are binary though, which you can't read.</p><p>BTW, pls use comments instead of answers; I converted them for you now for a number of times.</p></div><div id="comment-35900-info" class="comment-info"><span class="comment-age">(01 Sep '14, 01:43)</span> Jasper ♦♦</div></div></div><div id="comment-tools-35700" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-35700-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

