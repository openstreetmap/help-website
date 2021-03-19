+++
type = "question"
title = "problem with loading external dll from a dissector"
description = '''Hi, I am trying to load an external dll using HINSTANCE hInstLib = LoadLibrary(LIBRARYLOCATION); where LIBRARYLOCATION is the path to my dll. However, the LoadLibrary returns NULL and checked the error message using GetLastErrorMessage(). The error number is 193 (ERROR_BAD_EXE_FORMAT). I have compil...'''
date = "2014-07-09T13:45:00Z"
lastmod = "2014-07-09T14:23:00Z"
weight = 34526
keywords = [ "loading", "from", "external", "dissector", "dll" ]
aliases = [ "/questions/34526" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [problem with loading external dll from a dissector](/questions/34526/problem-with-loading-external-dll-from-a-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34526-score" class="post-score" title="current number of votes">0</div><span id="post-34526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to load an external dll using HINSTANCE hInstLib = LoadLibrary(LIBRARYLOCATION); where LIBRARYLOCATION is the path to my dll. However, the LoadLibrary returns NULL and checked the error message using GetLastErrorMessage(). The error number is 193 (ERROR_BAD_EXE_FORMAT). I have compiled my wireshark code using MSVC_VARIANT=MSVC2010 and my sample dll is also built with Visual studio 2010. I have experimented a lot and end up with NO solution. Can anybody please help me what's wrong I am doing and what could be the solution? Thanks in Advance!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-loading" rel="tag" title="see questions tagged &#39;loading&#39;">loading</span> <span class="post-tag tag-link-from" rel="tag" title="see questions tagged &#39;from&#39;">from</span> <span class="post-tag tag-link-external" rel="tag" title="see questions tagged &#39;external&#39;">external</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-dll" rel="tag" title="see questions tagged &#39;dll&#39;">dll</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '14, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/58149b21432e45e3b3388d6097402d80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="julia&#39;s gravatar image" /><p><span>julia</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="julia has no accepted answers">0%</span></p></div></div><div id="comments-container-34526" class="comments-container"></div><div id="comment-tools-34526" class="comment-tools"></div><div class="clear"></div><div id="comment-34526-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34529"></span>

<div id="answer-container-34529" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34529-score" class="post-score" title="current number of votes">1</div><span id="post-34529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This error probably means that you are trying to load a 32bit DLL from a 64 bit version of Wireshark, or the opposite (64bit DLL and 32bit Wireshark). You must ensure that the DLL has the same format as Wireshark binary.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '14, 14:23</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-34529" class="comments-container"></div><div id="comment-tools-34529" class="comment-tools"></div><div class="clear"></div><div id="comment-34529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

