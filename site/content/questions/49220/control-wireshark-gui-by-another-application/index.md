+++
type = "question"
title = "Control Wireshark GUI by another application"
description = '''I&#x27;m writing an application that analyzes network traffic. This app launches Wireshark GUI with the captured data and filters. Now, I want to jump to certain packets, change filters, what ever.., or control that already running instance of Wireshark. Is that possible? And if, how can it be done in ge...'''
date = "2016-01-14T09:26:00Z"
lastmod = "2016-01-14T09:31:00Z"
weight = 49220
keywords = [ "wireshark" ]
aliases = [ "/questions/49220" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Control Wireshark GUI by another application](/questions/49220/control-wireshark-gui-by-another-application)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49220-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing an application that analyzes network traffic. This app launches Wireshark GUI with the captured data and filters.</p><p>Now, I want to jump to certain packets, change filters, what ever.., or <strong>control that already running instance</strong> of Wireshark. Is that possible? And if, how can it be done in general?</p><p><strong>Some details:</strong><br />
I'm working with Mono under Windows and Linux. While it would be nice to have a solution for both, I could also write a solution for a dedicated environment.</p><p>It could be that <a href="https://ask.wireshark.org/questions/30169/control-wireshark-with-my-application">this Question</a> had the same intent but if so, it seems misunderstood.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '16, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/b6e4be0989ca25bb9d59ba5840d2cb24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DuStellstFragen&#39;s gravatar image" /><p>DuStellstFragen<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DuStellstFragen has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jan '16, 09:28</p></div></div><div id="comments-container-49220" class="comments-container"></div><div id="comment-tools-49220" class="comment-tools"></div><div class="clear"></div><div id="comment-49220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49221"></span>

<div id="answer-container-49221" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49221-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is a command line parameter "-g" to open Wireshark and have it jump to a specific packet. E.g.</p><pre><code>wireshark -g 111 test.pcapng</code></pre><p>opens the file "test.pcapng" and jumps to packet 111.</p><p>Other than that, check this question:</p><p><a href="https://ask.wireshark.org/questions/47107/go-to-packet-via-an-api">https://ask.wireshark.org/questions/47107/go-to-packet-via-an-api</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '16, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-49221" class="comments-container"><span id="49223"></span><div id="comment-49223" class="comment"><div id="post-49223-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jasper for your reply. I don't want to launch another instance of Wireshark. But the last answer by Kurt Knochner in the thread you mentioned seems interesting. Thanks!</p></div><div id="comment-49223-info" class="comment-info"><span class="comment-age">(14 Jan '16, 10:45)</span> DuStellstFragen</div></div></div><div id="comment-tools-49221" class="comment-tools"></div><div class="clear"></div><div id="comment-49221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

