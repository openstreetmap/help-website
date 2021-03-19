+++
type = "question"
title = "Change compiler and linker"
description = '''Hi All, After building wireshark successfully using Microsoft Compiler on windows, I was trying to build the application using Intel Compiler. I changed the value of CC and LD in RootFolder&#92; Makefile.nmake, but build was still using the MS compiler. Then I started changing the makefile.nmake in each...'''
date = "2015-07-31T12:01:00Z"
lastmod = "2015-08-01T09:31:00Z"
weight = 44707
keywords = [ "makefile.nmake", "build", "compiler" ]
aliases = [ "/questions/44707" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Change compiler and linker](/questions/44707/change-compiler-and-linker)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44707-score" class="post-score" title="current number of votes">0</div><span id="post-44707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>After building wireshark successfully using Microsoft Compiler on windows, I was trying to build the application using Intel Compiler.</p><p>I changed the value of CC and LD in RootFolder\ Makefile.nmake, but build was still using the MS compiler.</p><p>Then I started changing the makefile.nmake in each sub-folders. But, the problem is now I want to change the CFLAGS.</p><p>Is there any particular file from where I can change CC, LD and CFLAGS values globally??</p><p>Thanks,</p><p>Mitul</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-makefile.nmake" rel="tag" title="see questions tagged &#39;makefile.nmake&#39;">makefile.nmake</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-compiler" rel="tag" title="see questions tagged &#39;compiler&#39;">compiler</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '15, 12:01</strong></p><img src="https://secure.gravatar.com/avatar/4412232c71bd780e3a4bdd5e7f125e7e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MJS&#39;s gravatar image" /><p><span>MJS</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MJS has no accepted answers">0%</span></p></div></div><div id="comments-container-44707" class="comments-container"></div><div id="comment-tools-44707" class="comment-tools"></div><div class="clear"></div><div id="comment-44707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44723"></span>

<div id="answer-container-44723" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44723-score" class="post-score" title="current number of votes">0</div><span id="post-44723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think you may run into lots of issues using the nmake build system which is pretty specific to MS Visual C. I don't know of anyone else attempting to build Wireshark with the Intel Compiler, especially now VS Express Desktop is free.</p><p>If you're building off master you may want to try the CMake build (see <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=README.cmake">README.cmake</a> in the root of the source tree), although there is no generator specifically for the Intel Compiler, <a href="http://stackoverflow.com/questions/27623110/how-to-generate-a-visual-studio-project-that-uses-the-intel-compiler-using-cmake">this</a> SO answer shows how to set CMake to use the Intel Compiler.</p><p>Please report back on your results, the <a href="https://www.wireshark.org/lists/">dev</a> mailing list is probably the best place for this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '15, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-44723" class="comments-container"></div><div id="comment-tools-44723" class="comment-tools"></div><div class="clear"></div><div id="comment-44723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

