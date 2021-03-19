+++
type = "question"
title = "How to use libwireshark.dll (X64) in 64-bit windows project"
description = '''Hello all: When i use &quot;LoadLibrary(&quot;libwireshark.dll&quot;) in vs2010, loadlibrary failed with error 193, that is : &quot;1% is not a valid Win32 program&quot;. My project is in X64 mode, and libwireshark.dll is built in X64 too. Why?'''
date = "2013-03-24T18:33:00Z"
lastmod = "2013-03-25T06:45:00Z"
weight = 19790
keywords = [ "libwireshark", "loadlibrary" ]
aliases = [ "/questions/19790" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to use libwireshark.dll (X64) in 64-bit windows project](/questions/19790/how-to-use-libwiresharkdll-x64-in-64-bit-windows-project)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19790-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all: When i use "LoadLibrary("libwireshark.dll") in vs2010, loadlibrary failed with error 193, that is : "1% is not a valid Win32 program". My project is in X64 mode, and libwireshark.dll is built in X64 too. Why?</p></div><div id="question-tags" class="tags-container tags">libwireshark loadlibrary</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '13, 18:33</strong></p><img src="https://secure.gravatar.com/avatar/39efcf271888ff7393da0ae88c14a075?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunnymato&#39;s gravatar image" /><p>sunnymato<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunnymato has no accepted answers">0%</span></p></div></div><div id="comments-container-19790" class="comments-container"></div><div id="comment-tools-19790" class="comment-tools"></div><div class="clear"></div><div id="comment-19790-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19808"></span>

<div id="answer-container-19808" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19808-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What OS are you trying to run this on? Your build may default to a target OS such as Win 7, and then the dll is not valid for earlier versions of Windows.</p><p>Use <code>dumpbin /headers</code> on the dll to see the target version (shown as "subsystem version" in dumpbin output).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '13, 06:45</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-19808" class="comments-container"><span id="19989"></span><div id="comment-19989" class="comment"><div id="post-19989-score" class="comment-score"></div><div class="comment-text"><p>Thanks. The problem has been solved.</p></div><div id="comment-19989-info" class="comment-info"><span class="comment-age">(01 Apr '13, 07:33)</span> sunnymato</div></div><span id="19990"></span><div id="comment-19990" class="comment"><div id="post-19990-score" class="comment-score">1</div><div class="comment-text"><p>Can you tell everyone else how it was resolved, in case someone else runs into the issue?</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-19990-info" class="comment-info"><span class="comment-age">(01 Apr '13, 07:40)</span> grahamb ♦</div></div></div><div id="comment-tools-19808" class="comment-tools"></div><div class="clear"></div><div id="comment-19808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

