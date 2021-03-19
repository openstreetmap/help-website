+++
type = "question"
title = "how to generate dsp file in VS2008EE by Wireshark&#x27;s source codes?"
description = '''i want to debug the Wireshark&#x27;s source codes in VS2008EE, but there are only makefile, not dsp file. how to generate dsp file in VS2008EE by Wireshark&#x27;s source codes?'''
date = "2011-09-14T01:59:00Z"
lastmod = "2011-09-14T13:32:00Z"
weight = 6350
keywords = [ "windows", "debug", "generate", "dsp", "wireshark" ]
aliases = [ "/questions/6350" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to generate dsp file in VS2008EE by Wireshark's source codes?](/questions/6350/how-to-generate-dsp-file-in-vs2008ee-by-wiresharks-source-codes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6350-score" class="post-score" title="current number of votes">0</div><span id="post-6350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i want to debug the Wireshark's source codes in VS2008EE, but there are only makefile, not dsp file.</p><p>how to generate dsp file in VS2008EE by Wireshark's source codes?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-debug" rel="tag" title="see questions tagged &#39;debug&#39;">debug</span> <span class="post-tag tag-link-generate" rel="tag" title="see questions tagged &#39;generate&#39;">generate</span> <span class="post-tag tag-link-dsp" rel="tag" title="see questions tagged &#39;dsp&#39;">dsp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '11, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/a5a3214300b3b17fc46c3b656b7bed01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ylda_ljm0620&#39;s gravatar image" /><p><span>ylda_ljm0620</span><br />
<span class="score" title="31 reputation points">31</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ylda_ljm0620 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Sep '11, 12:31</strong> </span></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-6350" class="comments-container"></div><div id="comment-tools-6350" class="comment-tools"></div><div class="clear"></div><div id="comment-6350-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6365"></span>

<div id="answer-container-6365" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6365-score" class="post-score" title="current number of votes">1</div><span id="post-6365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To debug Wireshark on Windows:</p><ol><li><p>Build Wireshark on Windows from the commandline using the Wireshark nmakefile with VS2008EE in the normal manner (as described in <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">the Developers Guide</a>).</p></li><li><p>Start the VC2008EE GUI.</p></li><li><p>Do File ! Open ! Project/Solution on wireshark-gtk2\wireshark.exe</p></li></ol><p>You'll be able to do debugging of Wireshark in the normal manner with source code viewing, breakpoints &amp; etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '11, 12:06</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Sep '11, 12:28</strong> </span></p></div></div><div id="comments-container-6365" class="comments-container"></div><div id="comment-tools-6365" class="comment-tools"></div><div class="clear"></div><div id="comment-6365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6353"></span>

<div id="answer-container-6353" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6353-score" class="post-score" title="current number of votes">0</div><span id="post-6353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is normally built using nmake and a Makefile, not a Visual Studio project. There is an alternative CMake build system for Wireshark but I've not had much success with it on Windows and using Visual Studio Express compilers. I think CMake can be persuaded to output Visual Studio project files but I've never done that.</p><p>To debug on Windows your options are:</p><p>Use WinDbg. Downloadable from MS, works well but has a bit of a learning curve, but for simple debugging is sufficient. Use a more full featured version of Visual Studio, i.e. Pro or above and use the debugger command to "Attach To Process". Using CMake or by hand create a project file for Wireshark to use in Visual Studio Express.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '11, 04:19</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-6353" class="comments-container"><span id="6357"></span><div id="comment-6357" class="comment"><div id="post-6357-score" class="comment-score"></div><div class="comment-text"><p>Visual Studio 2008 EE will do Attach to Process. There is no need to upgrade to pro for this functionality.</p></div><div id="comment-6357-info" class="comment-info"><span class="comment-age">(14 Sep '11, 05:22)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="6370"></span><div id="comment-6370" class="comment"><div id="post-6370-score" class="comment-score"></div><div class="comment-text"><p>Ah, VS 2010 EE doesn't have that in the debug menu so I assumed it was the same for VS 2008.</p></div><div id="comment-6370-info" class="comment-info"><span class="comment-age">(14 Sep '11, 13:32)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-6353" class="comment-tools"></div><div class="clear"></div><div id="comment-6353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

