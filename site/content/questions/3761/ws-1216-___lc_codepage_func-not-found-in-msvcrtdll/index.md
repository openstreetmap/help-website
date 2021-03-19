+++
type = "question"
title = "WS 1.2.16 - ___lc_codepage_func not found in msvcrt.dll"
description = '''if W2k is no longer supported, can someone please update the User Guide section 1.2.2 to indicate that version 1.2.15 is the last available and supported version? additionally, it would be a GoodThing&amp;lt;tm&amp;gt; if the installer would note this and refuse to continue... this check should be made befo...'''
date = "2011-04-27T13:58:00Z"
lastmod = "2011-04-27T22:13:00Z"
weight = 3761
keywords = [ "msvcrt", "w2k", "1.2.16", "error" ]
aliases = [ "/questions/3761" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WS 1.2.16 - \_\_\_lc\_codepage\_func not found in msvcrt.dll](/questions/3761/ws-1216-___lc_codepage_func-not-found-in-msvcrtdll)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3761-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>if W2k is no longer supported, can someone please update the User Guide section 1.2.2 to indicate that version 1.2.15 is the last available and supported version?</p><p>additionally, it would be a GoodThing&lt;tm&gt; if the installer would note this and refuse to continue... this check should be made before one is asked about uninstalling 1.2.15...</p><p>1.2.16 does actually install but dies on execution with the following error... The procedure entry point ___k_codepage_func could not be located in the dynamic link library msvcrt.dll.</p><p>( i'm not sure on the number of underscore characters before the k in that error. i have written it with three because i am unable to copy'n'paste the error message :( )</p></div><div id="question-tags" class="tags-container tags">msvcrt w2k 1.2.16 error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '11, 13:58</strong></p><img src="https://secure.gravatar.com/avatar/4c9e8d356fa39d5c1d825681520073b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wkitty42&#39;s gravatar image" /><p>wkitty42<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wkitty42 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 May '11, 15:04</p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span></p></div></div><div id="comments-container-3761" class="comments-container"><span id="4296"></span><div id="comment-4296" class="comment"><div id="post-4296-score" class="comment-score"></div><div class="comment-text"><p>Have the same problem in Windows 2000, I Saw the dll dependences and don't have any dependences... is a bug? Do you know how to resolve this issue? Do yo have a workaround?</p><p>Thanks Andres (from Argentina) NeO83666</p></div><div id="comment-4296-info" class="comment-info"><span class="comment-age">(31 May '11, 09:21)</span> NeO83666</div></div></div><div id="comment-tools-3761" class="comment-tools"></div><div class="clear"></div><div id="comment-3761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3778"></span>

<div id="answer-container-3778" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3778-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's a bug that should be filed in <a href="https://bugs.wireshark.org/bugzilla/">Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '11, 22:13</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3778" class="comments-container"><span id="3825"></span><div id="comment-3825" class="comment"><div id="post-3825-score" class="comment-score"></div><div class="comment-text"><p>ok... which bug?</p><ol><li><p>the one about the codepage function missing?</p></li><li><p>or the installer failing to refuse to install on an unsupported system?</p></li><li><p>or the one about not being able to copy'n'paste the error? ;)</p></li></ol><p>i'll assume the codepage function bug and see if i can wade into bugzilla and get a report filed...</p></div><div id="comment-3825-info" class="comment-info"><span class="comment-age">(29 Apr '11, 15:04)</span> wkitty42</div></div><span id="3826"></span><div id="comment-3826" class="comment"><div id="post-3826-score" class="comment-score"></div><div class="comment-text"><p>ok... if i've done this properly, it is the following...</p><p>Bug 5874 - ___k_codepage_func could not be located in the dynamic link library msvcrt.dll</p></div><div id="comment-3826-info" class="comment-info"><span class="comment-age">(29 Apr '11, 15:21)</span> wkitty42</div></div></div><div id="comment-tools-3778" class="comment-tools"></div><div class="clear"></div><div id="comment-3778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

