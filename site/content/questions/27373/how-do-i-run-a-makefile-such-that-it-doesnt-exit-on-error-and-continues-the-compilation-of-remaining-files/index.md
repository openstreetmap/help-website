+++
type = "question"
title = "How do I run a makefile such that it doesn&#x27;t exit on error and continues the compilation of remaining files?"
description = '''I have a makefile that I run and I do not want it to exit if there is an error during the compilation of a particular file. I want it to continue compiling other files. Is this possible? If yes how?'''
date = "2013-11-26T00:25:00Z"
lastmod = "2013-11-26T04:52:00Z"
weight = 27373
keywords = [ "make", "makefile", "build", "linux" ]
aliases = [ "/questions/27373" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I run a makefile such that it doesn't exit on error and continues the compilation of remaining files?](/questions/27373/how-do-i-run-a-makefile-such-that-it-doesnt-exit-on-error-and-continues-the-compilation-of-remaining-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27373-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a makefile that I run and I do not want it to exit if there is an error during the compilation of a particular file. I want it to continue compiling other files. Is this possible? If yes how?</p></div><div id="question-tags" class="tags-container tags">make makefile build linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '13, 00:25</strong></p><img src="https://secure.gravatar.com/avatar/0a3500d83a034d54be7470d7ed010604?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pysudhir&#39;s gravatar image" /><p>pysudhir<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pysudhir has no accepted answers">0%</span></p></div></div><div id="comments-container-27373" class="comments-container"><span id="27379"></span><div id="comment-27379" class="comment"><div id="post-27379-score" class="comment-score"></div><div class="comment-text"><p>A makefile for what? If this is for Wireshark, please give some more details, if not, then the question is not relevant for Ask Wireshark.</p></div><div id="comment-27379-info" class="comment-info"><span class="comment-age">(26 Nov '13, 01:47)</span> grahamb ♦</div></div></div><div id="comment-tools-27373" class="comment-tools"></div><div class="clear"></div><div id="comment-27373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27417"></span>

<div id="answer-container-27417" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27417-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Based on <a href="http://ask.wireshark.org/questions/27388/error-invalid-use-of-incomplete-type-tvbuff_t">your other question</a>, I assume this question is about building a Wireshark dissector.</p><p>If so, then the answer to your question is:</p><blockquote><p><code>man make</code></p></blockquote><p>which will tell you to run make with option -k:</p><pre><code>       -k, --keep-going
        Continue  as  much  as  possible after an error.  While the target
        that failed, and those that depend on it, cannot  be  remade,  the
        other dependencies of these targets can be processed all the same.</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Nov '13, 04:53</p></div></div><div id="comments-container-27417" class="comments-container"></div><div id="comment-tools-27417" class="comment-tools"></div><div class="clear"></div><div id="comment-27417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

