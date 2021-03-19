+++
type = "question"
title = "Wireshark 1.6 ,1.8. 1.8 RC2 generating a runtime library error (Terminal in a unusual way...)"
description = '''Hi there, Could anyone let me know if you encountered this issue where Wireshark is capturing packets fine for few minutes and then crash with the following Microsoft Virtual C++ runtime library error: This application has requested the runtime to terminate it in an unusual way. ... I am running win...'''
date = "2012-09-28T08:28:00Z"
lastmod = "2012-09-28T08:40:00Z"
weight = 14599
keywords = [ "runtime", "library", "error" ]
aliases = [ "/questions/14599" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.6 ,1.8. 1.8 RC2 generating a runtime library error (Terminal in a unusual way...)](/questions/14599/wireshark-16-18-18-rc2-generating-a-runtime-library-error-terminal-in-a-unusual-way)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14599-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>Could anyone let me know if you encountered this issue where Wireshark is capturing packets fine for few minutes and then crash with the following Microsoft Virtual C++ runtime library error:</p><p>This application has requested the runtime to terminate it in an unusual way. ...</p><p>I am running windows 2008 R2 x64 SP1 + all the latest patches and tried it over 3 different servers and with Wireshark V1.6.10, 1.8 and 1.8RC2 and got the same result.</p><p>Please let me know if you have any idea on how to resolve this.</p><p>Thanks !</p></div><div id="question-tags" class="tags-container tags">runtime library error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '12, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/377841780ef7abcccbc8b4c26efe2412?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="system_engineer_mtl&#39;s gravatar image" /><p>system_engin...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="system_engineer_mtl has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Sep '12, 08:47</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-14599" class="comments-container"></div><div id="comment-tools-14599" class="comment-tools"></div><div class="clear"></div><div id="comment-14599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14600"></span>

<div id="answer-container-14600" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14600-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What sort of interfaces are you capturing on, and what level of traffic is occurring on those interfaces? Are you setting any capture filters? It's possible that you are capturing so much data that Wireshark is simply <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">running out of memory</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '12, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-14600" class="comments-container"></div><div id="comment-tools-14600" class="comment-tools"></div><div class="clear"></div><div id="comment-14600-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

