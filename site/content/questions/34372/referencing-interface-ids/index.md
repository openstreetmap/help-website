+++
type = "question"
title = "referencing interface id&#x27;s"
description = '''Hello, How is it possible to dereference interface-ids (0,1,2,3...) in a pcapng trace to the real interface names? thx for hints, steffen'''
date = "2014-07-03T00:20:00Z"
lastmod = "2014-07-03T00:41:00Z"
weight = 34372
keywords = [ "interfaces", "ids" ]
aliases = [ "/questions/34372" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [referencing interface id's](/questions/34372/referencing-interface-ids)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34372-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>How is it possible to dereference interface-ids (0,1,2,3...) in a pcapng trace to the real interface names?</p><p>thx for hints, steffen</p></div><div id="question-tags" class="tags-container tags">interfaces ids</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '14, 00:20</strong></p><img src="https://secure.gravatar.com/avatar/bee49869be792a7d6aee203210f9892e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Discovery&#39;s gravatar image" /><p>Discovery<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Discovery has no accepted answers">0%</span></p></div></div><div id="comments-container-34372" class="comments-container"></div><div id="comment-tools-34372" class="comment-tools"></div><div class="clear"></div><div id="comment-34372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34373"></span>

<div id="answer-container-34373" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34373-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>PCAPng stores interface name and description, but depending on your OS it may still not be easy to dereference them.</p><p>Linux should store the interface name like "eth0" in the interface name value, which makes it easy to find. Just open the summary statistics window to see it.</p><p>Under Windows you'll see GUIDs for interface names, and you'll need access to the original capture PC to match them against the NICs. To do that, open the Summary statistics of a PCAPng file, which will list the capture interfaces. Then run "dumpcap -D" on a command line to get a list of capture interfaces, and match the GUID string from the summary to see what string matches which interface.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '14, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-34373" class="comments-container"><span id="34378"></span><div id="comment-34378" class="comment"><div id="post-34378-score" class="comment-score"></div><div class="comment-text"><p>thx for your very helpful answer. To be shure beeing right: is interface index number (as seen in the trace) order starting with 0 the same as the listed order by "dumpcap -D" starting with 1 or summary tab with missing number - so you can reference using the order?</p></div><div id="comment-34378-info" class="comment-info"><span class="comment-age">(03 Jul '14, 02:35)</span> Discovery</div></div><span id="34379"></span><div id="comment-34379" class="comment"><div id="post-34379-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately, no. The interfaces in the file are starting at 0 for the first interface that was actually used in the capture. So if you see 3 interfaces in dumpcap but use interface 1 and 3 they will appear as interface 0 and 1 in the trace.</p><p>You have to match them by name to the "dumpcap -D" output, not by index.</p></div><div id="comment-34379-info" class="comment-info"><span class="comment-age">(03 Jul '14, 02:37)</span> Jasper ♦♦</div></div></div><div id="comment-tools-34373" class="comment-tools"></div><div class="clear"></div><div id="comment-34373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

