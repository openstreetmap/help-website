+++
type = "question"
title = "Filtering: Bitwise-and is leading to linker error"
description = '''Hello, I have tried to put bitwise-and(&amp;amp;) into the display filter Dialog box&#x27;s sources, made proper and necessary changes that are required (like calling the bitwise-and related function (ftype_can_bitwise_and) from ftypes/ftypes.c same as the other operator functions are called). There are no c...'''
date = "2011-10-07T00:18:00Z"
lastmod = "2011-10-07T01:15:00Z"
weight = 6768
keywords = [ "filter" ]
aliases = [ "/questions/6768" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Filtering: Bitwise-and is leading to linker error](/questions/6768/filtering-bitwise-and-is-leading-to-linker-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6768-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have tried to put bitwise-and(&amp;) into the display filter Dialog box's sources, made proper and necessary changes that are required (like calling the bitwise-and related function (ftype_can_bitwise_and) from ftypes/ftypes.c same as the other operator functions are called). There are no compile-time errors but at the end I'm facing a linker error called :</p><pre><code>Linking wireshark.exe
        link @C:\DOCUME~1\admin\LOCALS~1\Temp\nm1C1.tmp
libui.lib(dfilter_expr_dlg.obj) : error LNK2019: unresolved external symbol _ftype_can_trig referenced in function _show_relations
wireshark.exe : fatal error LNK1120: 1 unresolved externals
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN\link.EXE&quot;&#39; : return code &#39;0x460&#39;
Stop.</code></pre><p>Please help.</p></div><div id="question-tags" class="tags-container tags">filter</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '11, 00:18</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p>Terrestrial ...<br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Oct '11, 05:25</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-6768" class="comments-container"></div><div id="comment-tools-6768" class="comment-tools"></div><div class="clear"></div><div id="comment-6768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6773"></span>

<div id="answer-container-6773" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6773-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>As I can't find the symbol <code>ftype_can_trig</code> anywhere in the svn tree for trunk nor in the function <code>show_relations</code>, I'm assuming this is something you've added.</p><p>If this is the case you will also need to add it to the list of exported functions in epan\libwireshark.def so that code outside of libwireshark can use it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '11, 01:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Oct '11, 01:16</p></div></div><div id="comments-container-6773" class="comments-container"><span id="6775"></span><div id="comment-6775" class="comment"><div id="post-6775-score" class="comment-score"></div><div class="comment-text"><p>thanks Grahamb. Im trying to put triggers so i have defined a function called ftype_can_trig but it didnt allow. I have tried to add bitwise and as it is already present but not activated. Finally i made the code little messy.</p></div><div id="comment-6775-info" class="comment-info"><span class="comment-age">(07 Oct '11, 01:23)</span> Terrestrial ...</div></div><span id="6778"></span><div id="comment-6778" class="comment"><div id="post-6778-score" class="comment-score"></div><div class="comment-text"><p>I have also include one of my variable from epan/ftypes/ftypes.h into the libwireshark.def but this isn't working. I followed the rules presented in that def file.</p><p>Code in ftypes.h typedef struct _a_b { int r; gint64 t; int tr; gint64 tri; }a_b;</p><p>WS_VAR_IMPORT a_b ab_struct;</p><hr /><p>Appended text in the libwireshark.def is</p><p>ab_struct DATA</p><p>Please Help!!</p></div><div id="comment-6778-info" class="comment-info"><span class="comment-age">(07 Oct '11, 04:11)</span> Terrestrial ...</div></div><span id="6779"></span><div id="comment-6779" class="comment"><div id="post-6779-score" class="comment-score"></div><div class="comment-text"><p>I guess it's a linker error again about unresolved externals?</p><p>Are you sure you've rebuilt libwireshark as what you've done seems correct to me?</p></div><div id="comment-6779-info" class="comment-info"><span class="comment-age">(07 Oct '11, 05:30)</span> grahamb ♦</div></div><span id="6799"></span><div id="comment-6799" class="comment"><div id="post-6799-score" class="comment-score"></div><div class="comment-text"><p>I have distcleaned and compiled it but this time there are no linker errors. Instead, I got the errors like:</p><p>ftype-integer.c</p><p>ftype-integer.c(258) : error C2037: left of 'tri' specifies undefined struct/union 'a_b'</p><p>ftype-integer.c(259) : error C2037: left of 'r' specifies undefine d struct/union 'a_b'</p><p>etc kind of Compile time errors.</p></div><div id="comment-6799-info" class="comment-info"><span class="comment-age">(07 Oct '11, 23:30)</span> Terrestrial ...</div></div><span id="6800"></span><div id="comment-6800" class="comment"><div id="post-6800-score" class="comment-score">1</div><div class="comment-text"><p>Basic c syntax errors then. This is probably better handled on the dev mailing list rather than the Q&amp;A site. Post the relevant code and errors there. See <a href="http://www.wireshark.org/lists/">here</a> for more details</p></div><div id="comment-6800-info" class="comment-info"><span class="comment-age">(08 Oct '11, 00:08)</span> grahamb ♦</div></div><span id="6802"></span><div id="comment-6802" class="comment not_top_scorer"><div id="post-6802-score" class="comment-score"></div><div class="comment-text"><p>should i mail to [email protected] from my gmail account?</p></div><div id="comment-6802-info" class="comment-info"><span class="comment-age">(08 Oct '11, 00:57)</span> Terrestrial ...</div></div></div><div id="comment-tools-6773" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-6773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

