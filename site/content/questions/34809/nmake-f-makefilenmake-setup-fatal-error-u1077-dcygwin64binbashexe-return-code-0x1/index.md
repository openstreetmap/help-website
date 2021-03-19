+++
type = "question"
title = "nmake -f Makefile.nmake setup fatal error U1077: “d:&#92;cygwin64&#92;bin&#92;bash.EXE”: Return Code “0x1”"
description = '''  I follow the Step-by-Step Guide,when i go to the step&quot;nmake -f Makefile.nmake setup&quot;,i catch &quot;fatal error U1077: “d:&#92;cygwin64&#92;bin&#92;bash.EXE”: 返回代码Return Code “0x1”&quot;,any one who can help me will be appreciated.'''
date = "2014-07-21T22:10:00Z"
lastmod = "2014-07-22T03:01:00Z"
weight = 34809
keywords = [ "u1077", "0x1", "fatal", "error" ]
aliases = [ "/questions/34809" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [nmake -f Makefile.nmake setup fatal error U1077: “d:\\cygwin64\\bin\\bash.EXE”: Return Code “0x1”](/questions/34809/nmake-f-makefilenmake-setup-fatal-error-u1077-dcygwin64binbashexe-return-code-0x1)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34809-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="http://tianyinsoft.com/mytest/w1.jpg" alt="alt text" /></p><p><img src="http://tianyinsoft.com/mytest/w2.jpg" alt="alt text" /></p><p>I follow the Step-by-Step Guide,when i go to the step"nmake -f Makefile.nmake setup",i catch "fatal error U1077: “d:\cygwin64\bin\bash.EXE”: <del><a href="https://translate.google.com/#auto/en/%E8%BF%94%E5%9B%9E%E4%BB%A3%E7%A0%81">返回代码</a></del><strong>Return Code</strong> “0x1”",any one who can help me will be appreciated.</p></div><div id="question-tags" class="tags-container tags">u1077 0x1 fatal error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '14, 22:10</strong></p><img src="https://secure.gravatar.com/avatar/18906e9d1f4f10dc9f4930601c167910?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zhunanhui&#39;s gravatar image" /><p>zhunanhui<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zhunanhui has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jul '14, 02:25</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></img></div></div><div id="comments-container-34809" class="comments-container"></div><div id="comment-tools-34809" class="comment-tools"></div><div class="clear"></div><div id="comment-34809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34816"></span>

<div id="answer-container-34816" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34816-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks as though something is up with your build environment, particularly around the calls to winxx-setup.sh. The makefile calls the wrapper script winxx-setup.sh, where xx is 32 or 64 depending on how you've set your environment, yours looks like 32, and then the wrapper script exports some variables and calls the main setup script win-setup.sh, passing on the same parameters it was called with.</p><p>The fact that the usage message is printed implies win-setup.sh is being called with incorrect parameters, even though the appverify invocation does run. I don't understand why the missing QT error message is displayed, that only comes from the <code>process_libs</code> target which is run after the <code>verify_tools</code> target. Your output implies a failed invocation, the <code>verify_tools</code> target, then the <code>clean_setup</code> target, then another failed invocation</p><p>Have you made any changes at all to the source files? If so, please revert them and try to build a plain vanilla build first before making changes.</p><p>FYI, a Google translation into English of the Japanese text 返回代码 gives "Return Codes".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '14, 03:01</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-34816" class="comments-container"><span id="34825"></span><div id="comment-34825" class="comment"><div id="post-34825-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much, I also suspect the error may be I've changed the code, I revert the latest source code, now has been successfully compiled</p></div><div id="comment-34825-info" class="comment-info"><span class="comment-age">(22 Jul '14, 05:47)</span> zhunanhui</div></div></div><div id="comment-tools-34816" class="comment-tools"></div><div class="clear"></div><div id="comment-34816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

