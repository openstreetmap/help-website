+++
type = "question"
title = "Wireshark Crashes"
description = '''Hi All, Whenever I try to perform a Statistics / Service Response Time / DCE-RPC, Wireshark crashes. Has anyone had this issue before or any thoughts on how to resolve this? I have uninstalled and re-installed but the same issue occurs. Performing the capture on a Win 2012R2 Server with Wireshark Ve...'''
date = "2017-10-25T20:02:00Z"
lastmod = "2017-10-26T02:51:00Z"
weight = 64207
keywords = [ "dcerpc" ]
aliases = [ "/questions/64207" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Crashes](/questions/64207/wireshark-crashes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64207-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>Whenever I try to perform a Statistics / Service Response Time / DCE-RPC, Wireshark crashes. Has anyone had this issue before or any thoughts on how to resolve this? I have uninstalled and re-installed but the same issue occurs.</p><p>Performing the capture on a Win 2012R2 Server with Wireshark Ver 2.4.2</p><p>Regards,</p><p>Gaz</p></div><div id="question-tags" class="tags-container tags">dcerpc</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '17, 20:02</strong></p><img src="https://secure.gravatar.com/avatar/62402e431c539a6671a0f2dfba2638c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grummangy&#39;s gravatar image" /><p>Grummangy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grummangy has no accepted answers">0%</span></p></div></div><div id="comments-container-64207" class="comments-container"><span id="64209"></span><div id="comment-64209" class="comment"><div id="post-64209-score" class="comment-score"></div><div class="comment-text"><p>This is the Error information available at the time of the crash:</p><p><code> Problem signature:   Problem Event Name:   APPCRASH   Application Name: Wireshark.exe   Application Version:  2.4.2.0   Application Timestamp:    59dd16b8   Fault Module Name:    StackHash_8321   Fault Module Version: 6.3.9600.18821   Fault Module Timestamp:   59ba86db   Exception Code:   c0000374   Exception Offset: PCH_10_FROM_ntdll+0x0000000000090C8A   OS Version:   6.3.9600.2.0.0.272.7   Locale ID:    3081   Additional Information 1: 8321   Additional Information 2: 8321b13b1ccac4a9ff8e67c98304d83b   Additional Information 3: 37bc   Additional Information 4: 37bce00cb63062d26e97eb7dbe85b102</code></p></div><div id="comment-64209-info" class="comment-info"><span class="comment-age">(25 Oct '17, 20:42)</span> Grummangy</div></div></div><div id="comment-tools-64207" class="comment-tools"></div><div class="clear"></div><div id="comment-64207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64219"></span>

<div id="answer-container-64219" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64219-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Possibly a bug. How big is your capture?</p><p>Please raise an entry on the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a> and attach the capture causing the issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '17, 02:51</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-64219" class="comments-container"></div><div id="comment-tools-64219" class="comment-tools"></div><div class="clear"></div><div id="comment-64219-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

