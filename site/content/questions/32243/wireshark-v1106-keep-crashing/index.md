+++
type = "question"
title = "wireshark v1.10.6 - keep crashing"
description = '''Hi, Wireshark was run with capturing files in multiple mode (to keep 200 files of 20MB each = max of ~4GB disk size) It runs for 30 minutes and after that it crashes. OS detials: windows 2008 server with latest SP;--64bit OS Trying to pull the crash dump from the remote system; Regards'''
date = "2014-04-28T03:33:00Z"
lastmod = "2014-04-28T03:54:00Z"
weight = 32243
keywords = [ "v1.10.6" ]
aliases = [ "/questions/32243" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark v1.10.6 - keep crashing](/questions/32243/wireshark-v1106-keep-crashing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32243-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Wireshark was run with capturing files in multiple mode (to keep 200 files of 20MB each = max of ~4GB disk size) It runs for 30 minutes and after that it crashes. OS detials: windows 2008 server with latest SP;--64bit OS Trying to pull the crash dump from the remote system; Regards</p></div><div id="question-tags" class="tags-container tags">v1.10.6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '14, 03:33</strong></p><img src="https://secure.gravatar.com/avatar/874b7628ad99a5242e04072733c437b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mws&#39;s gravatar image" /><p>mws<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mws has no accepted answers">0%</span></p></div></div><div id="comments-container-32243" class="comments-container"></div><div id="comment-tools-32243" class="comment-tools"></div><div class="clear"></div><div id="comment-32243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32245"></span>

<div id="answer-container-32245" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32245-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Likely to be running out of memory. See the Wiki page on this issue <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">here</a> and @Jaspers blog entry on the issue <a href="http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">here</a>, and the numerous similar questions on this site. In short, use dumpcap to make the captures.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '14, 03:54</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-32245" class="comments-container"></div><div id="comment-tools-32245" class="comment-tools"></div><div class="clear"></div><div id="comment-32245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

