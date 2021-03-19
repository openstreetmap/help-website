+++
type = "question"
title = "Wireshark crashed when using the &quot;stop capture after&quot; feature"
description = '''Hi everybody, yesterday i made capture session with three wireshark machines and i used the &quot;stop capture&quot; and &quot;use multiple files&quot; option on all machines. At the end of the capture time, all machines were unuseable, wireshark shows &quot;closing file please wait&quot; and thats it. After killing wireshark th...'''
date = "2013-01-24T06:40:00Z"
lastmod = "2013-01-24T06:47:00Z"
weight = 17928
keywords = [ "program", "hangs" ]
aliases = [ "/questions/17928" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crashed when using the "stop capture after" feature](/questions/17928/wireshark-crashed-when-using-the-stop-capture-after-feature)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17928-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody,</p><p>yesterday i made capture session with three wireshark machines and i used the "stop capture" and "use multiple files" option on all machines. At the end of the capture time, all machines were unuseable, wireshark shows "closing file please wait" and that<code>s it. After killing wireshark the pc</code>s are working normal. I use the 1.8.4 version. Perhaps anybody knows or have seen this too? Thanks for help.</p><p>Mike</p></div><div id="question-tags" class="tags-container tags">program hangs</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '13, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/d6cab55f3f8d50d3a16c726d050325ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikethebandit31&#39;s gravatar image" /><p>mikethebandit31<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikethebandit31 has no accepted answers">0%</span></p></div></div><div id="comments-container-17928" class="comments-container"></div><div id="comment-tools-17928" class="comment-tools"></div><div class="clear"></div><div id="comment-17928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17929"></span>

<div id="answer-container-17929" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17929-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, that is probably the typical out-of-memory problem that happens when Wireshark runs for quite some time. You should do the capture by running the command line utility "dumpcap" instead (it's in the Wireshark directory), which is used by Wireshark to capture anyway. You can specify all the command line options necessary to make it do the same as if called by Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '13, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-17929" class="comments-container"><span id="17930"></span><div id="comment-17930" class="comment"><div id="post-17930-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot , i`ll try this option at the next time!!!</p></div><div id="comment-17930-info" class="comment-info"><span class="comment-age">(24 Jan '13, 06:53)</span> mikethebandit31</div></div></div><div id="comment-tools-17929" class="comment-tools"></div><div class="clear"></div><div id="comment-17929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

