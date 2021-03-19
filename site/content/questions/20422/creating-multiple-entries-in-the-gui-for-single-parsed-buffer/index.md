+++
type = "question"
title = "Creating multiple entries in the GUI for single parsed buffer"
description = '''Hi, I am a newbie so please direct me to existing data if such exists (I was not succesful at finding). I am implementing a new proprietary protocolto view my company&#x27;s device traces. The protocol packets arrive packed in a buffer on a specific UDP port. My wish is to show each packet as a new entry...'''
date = "2013-04-15T08:00:00Z"
lastmod = "2013-04-15T21:19:00Z"
weight = 20422
keywords = [ "info", "gui", "subdissector", "sub-dissector", "proto_tree" ]
aliases = [ "/questions/20422" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Creating multiple entries in the GUI for single parsed buffer](/questions/20422/creating-multiple-entries-in-the-gui-for-single-parsed-buffer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20422-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am a newbie so please direct me to existing data if such exists (I was not succesful at finding).</p><p>I am implementing a new proprietary protocolto view my company's device traces. The protocol packets arrive packed in a buffer on a specific UDP port.</p><p>My wish is to show each packet as a new entry in the main GUI even though they arrive inside a single buffer. I have tried using subdissectors and even a new dissector via call_dissector() but all attempts fail to show in the main table, all I succeed is to have the packets show in the parent buffer tree (reasonable since I pass that tree in cal_dissector).</p><p>Is there any way to achieve this?</p><p>Many thanks</p></div><div id="question-tags" class="tags-container tags">info gui subdissector sub-dissector proto_tree</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '13, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/fa7c952ff82c858b325ae0c691090dc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amirix&#39;s gravatar image" /><p>amirix<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amirix has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Apr '13, 08:32</p></div></div><div id="comments-container-20422" class="comments-container"></div><div id="comment-tools-20422" class="comment-tools"></div><div class="clear"></div><div id="comment-20422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20442"></span>

<div id="answer-container-20442" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20442-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The packet list is designed to show a packet on a single row, changing that may be a significant amount of work.But since this question has come up a number of times recently ways of achiving that should perhaps be considered, the developers mailing list is a more apropriate place for that discussion.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '13, 21:19</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-20442" class="comments-container"><span id="20475"></span><div id="comment-20475" class="comment"><div id="post-20475-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick reply. I think this feature is worthwhile for unpacking. I'll visit the mailing list for updates</p></div><div id="comment-20475-info" class="comment-info"><span class="comment-age">(16 Apr '13, 09:08)</span> amirix</div></div><span id="20679"></span><div id="comment-20679" class="comment"><div id="post-20679-score" class="comment-score"></div><div class="comment-text"><p>I'm busting my head finding how to begin and estimate the amount of work needed for such a task. Is there any chance you are familiar with similar attempts or can point we a place in the code to begin digging from?</p><p>Many Thanks</p></div><div id="comment-20679-info" class="comment-info"><span class="comment-age">(21 Apr '13, 08:22)</span> amirix</div></div><span id="20681"></span><div id="comment-20681" class="comment"><div id="post-20681-score" class="comment-score"></div><div class="comment-text"><p>As I said starting a thread on dev is more apropriate as others might have ideas. It probably involves redesigning the packet list. Figuring out how the GUI display ought to look could be a first step. Doubles for packet numbers? e.g packet 100.1, 100.2 etc or perhaps there's a better way? Any way it might be a significant amount of work...</p></div><div id="comment-20681-info" class="comment-info"><span class="comment-age">(21 Apr '13, 10:34)</span> Anders ♦</div></div><span id="20963"></span><div id="comment-20963" class="comment"><div id="post-20963-score" class="comment-score"></div><div class="comment-text"><p>I found a way to do it that seems clean enough and will hopefully sustain the throughput needed and be easily ported to other OS: I altered the dumpcap code in a way that the fragmentation is made there, the original IP/UDP header is appended with needed changes and then forwarded to WS. I'll post this also in the development thread I opened.</p></div><div id="comment-20963-info" class="comment-info"><span class="comment-age">(05 May '13, 11:46)</span> amirix</div></div></div><div id="comment-tools-20442" class="comment-tools"></div><div class="clear"></div><div id="comment-20442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

