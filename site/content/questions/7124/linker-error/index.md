+++
type = "question"
title = "Linker error"
description = '''Hello, I have a function called catch_first_filtered_pkt() inside main_filter_toolbar.c. This should be called from inside wireshark/epan/dfilter/dfvm.c &#x27;s any_test(dfilter_t *df, FvalueCmpFunc cmp, int reg1, int reg2) function block. I&#x27;ve encountered a Linker error LINK2019:unresolved external symb...'''
date = "2011-10-27T21:52:00Z"
lastmod = "2011-10-27T23:56:00Z"
weight = 7124
keywords = [ "gtk", "linker", "dfilter", "error" ]
aliases = [ "/questions/7124" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Linker error](/questions/7124/linker-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7124-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a function called <code>catch_first_filtered_pkt()</code> inside <code>main_filter_toolbar.c</code>. This should be called from inside wireshark/epan/dfilter/dfvm.c 's <code>any_test(dfilter_t *df, FvalueCmpFunc cmp, int reg1, int reg2)</code> function block. I've encountered a Linker error <code>LINK2019:unresolved external symbol _catch_first_filtered_pkt inside dfilter.lib</code>. How can i solve this error? Please Help.</p></div><div id="question-tags" class="tags-container tags">gtk linker dfilter error</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '11, 21:52</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p>Terrestrial ...<br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div></div><div id="comments-container-7124" class="comments-container"><span id="7126"></span><div id="comment-7126" class="comment"><div id="post-7126-score" class="comment-score"></div><div class="comment-text"><p><code>Creating library libwireshark.lib and object libwireshark.exp dfilter.lib(dfvm.obj) : error LNK2019: unresolved external symbol _catch_first_filtered_pkt r eferenced in function _any_test libwireshark.dll : fatal error LNK1120: 1 unresolved externals NMAKE : fatal error U1077: '"C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN \link.EXE"' : return code '0x460' Stop. NMAKE : fatal error U1077: '"C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN \nmake.exe"' : return code '0x2' Stop.</code></p></div><div id="comment-7126-info" class="comment-info"><span class="comment-age">(27 Oct '11, 23:11)</span> Terrestrial ...</div></div></div><div id="comment-tools-7124" class="comment-tools"></div><div class="clear"></div><div id="comment-7124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7127"></span>

<div id="answer-container-7127" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7127-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hurray!! I have resolved this by myself!!(though solution is somewhat silly ;-))</p><p>I have created a structure called <code>xyz</code> which has a function pointer called <code>fp_catch_first_pkt</code> inside epan/dfilter/dfvm.h.I have exported it using <code>WS_VAR_IMPORT</code>. I have assigned the address of <code>catch_first_filtered_pkt()</code> to it inside main_filter_toolbar.c file. Finally, i'm able to call the function this way:</p><p><code>xyz.fp_catch_first_pkt();</code></p></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '11, 23:56</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p>Terrestrial ...<br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Oct '11, 23:57</p></div></div><div id="comments-container-7127" class="comments-container"><span id="7132"></span><div id="comment-7132" class="comment"><div id="post-7132-score" class="comment-score"></div><div class="comment-text"><p>I presume that if xyz.fp_catch_first_pkt is null you don't call through it?</p><p>Otherwise, this will probably crash in TShark, which includes libwireshark (hence the code in epan/dfilter/dfvm.c) but does <em>NOT</em> have any toolbars (hence doesn't have gtk/main_filter_toolbar.c).</p></div><div id="comment-7132-info" class="comment-info"><span class="comment-age">(28 Oct '11, 02:16)</span> Guy Harris ♦♦</div></div><span id="7135"></span><div id="comment-7135" class="comment"><div id="post-7135-score" class="comment-score"></div><div class="comment-text"><p>Ok! What would be the good solution to solve this linker error?</p></div><div id="comment-7135-info" class="comment-info"><span class="comment-age">(28 Oct '11, 02:51)</span> Terrestrial ...</div></div><span id="7137"></span><div id="comment-7137" class="comment"><div id="post-7137-score" class="comment-score"></div><div class="comment-text"><p>That depends on what the ultimate purpose of these changes is, especially if it's something that'd be useful in TShark as well.</p></div><div id="comment-7137-info" class="comment-info"><span class="comment-age">(28 Oct '11, 03:01)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-7127" class="comment-tools"></div><div class="clear"></div><div id="comment-7127-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

