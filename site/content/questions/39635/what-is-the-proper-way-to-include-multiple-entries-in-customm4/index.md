+++
type = "question"
title = "What is the proper way to include multiple entries in Custom.m4?"
description = '''The Custom.m4.example file only includes one custom dissector. I thought that this would work: m4_define([_CUSTOM_AC_OUTPUT_], [plugins/foo/Makefile, plugins/bar/Makefile, plugins/baz/Makefile]  but this causes aclocal to exit with an error and halt the build during ./autogen.sh. aclocal -I ./acloca...'''
date = "2015-02-04T05:58:00Z"
lastmod = "2015-02-04T06:11:00Z"
weight = 39635
keywords = [ "custom.m4", "development", "autotools", "build", "plugin" ]
aliases = [ "/questions/39635" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What is the proper way to include multiple entries in Custom.m4?](/questions/39635/what-is-the-proper-way-to-include-multiple-entries-in-customm4)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39635-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The Custom.m4.example file only includes one custom dissector. I thought that this would work:</p><pre><code>m4_define([_CUSTOM_AC_OUTPUT_], [plugins/foo/Makefile, plugins/bar/Makefile, plugins/baz/Makefile]</code></pre><p>but this causes aclocal to exit with an error and halt the build during <code>./autogen.sh</code>.</p><pre><code>aclocal -I ./aclocal-fallback
/usr/bin/m4:configure.ac:2976: Warning: excess arguments to builtin `define&#39; ignored
/usr/bin/m4:configure.ac:2976: Warning: excess arguments to builtin `ifdef&#39; ignored
autom4te: /usr/bin/m4 failed with exit status: 1
aclocal: error: echo failed with exit status: 1</code></pre><p>Clearly I have the syntax wrong. What is the correct construct to include multiple custom dissectors in Custom.m4?</p></div><div id="question-tags" class="tags-container tags">custom.m4 development autotools build plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '15, 05:58</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-39635" class="comments-container"></div><div id="comment-tools-39635" class="comment-tools"></div><div class="clear"></div><div id="comment-39635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39636"></span>

<div id="answer-container-39636" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39636-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The format is</p><p><code>define(_CUSTOM_AC_OUTPUT_,  foo/bar/Makefile  foo1/bar1/Makefile )dnl</code></p><p>That is each entry on a separate line and no commas.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '15, 06:11</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Feb '15, 10:31</p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-39636" class="comments-container"></div><div id="comment-tools-39636" class="comment-tools"></div><div class="clear"></div><div id="comment-39636-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

