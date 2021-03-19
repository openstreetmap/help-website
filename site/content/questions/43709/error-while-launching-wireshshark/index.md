+++
type = "question"
title = "Error while launching wireshshark"
description = '''I have developed one plugin in lua in wireshark 1.12.6(32 bit).Now i am trying to start wireshark.While the time of launching wireshark i am getting this error!  How to solve this?'''
date = "2015-06-30T02:07:00Z"
lastmod = "2015-06-30T03:02:00Z"
weight = 43709
keywords = [ "lua", "wireshark", "error" ]
aliases = [ "/questions/43709" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Error while launching wireshshark](/questions/43709/error-while-launching-wireshshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43709-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have developed one plugin in lua in wireshark 1.12.6(32 bit).Now i am trying to start wireshark.While the time of launching wireshark i am getting this error!</p><p><img src="https://osqa-ask.wireshark.org/upfiles/error_wireshark_7v1GciG.png" /></p><p>How to solve this?</p></div><div id="question-tags" class="tags-container tags">lua wireshark error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '15, 02:07</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p>ankit<br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></img></div></div><div id="comments-container-43709" class="comments-container"></div><div id="comment-tools-43709" class="comment-tools"></div><div class="clear"></div><div id="comment-43709-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43712"></span>

<div id="answer-container-43712" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43712-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A guess is that the dll you're trying to load "xerceslua.dll" isn't the correct bitness for the version of Wireshark you're using, e.g. you have Wireshark x64 and the dll is x86.</p><p>When it does load, you might also have issues with different versions of the MSVCRT (C run-time library) as supplied by the compiler used to build them. Unfortunately Windows processes and dynamically loaded modules, i.e. DLL's, must use the same version of CRT. You can check the CRT used by Wireshark from the Help -&gt; About Wireshark dialog, but for Wireshark 1.12 it's VS2010 (or MSVCR100.dll to be precise).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '15, 03:02</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-43712" class="comments-container"><span id="43771"></span><div id="comment-43771" class="comment"><div id="post-43771-score" class="comment-score"></div><div class="comment-text"><p>Thanks @grahamb i found the solution as you suggested</p></div><div id="comment-43771-info" class="comment-info"><span class="comment-age">(01 Jul '15, 02:25)</span> ankit</div></div></div><div id="comment-tools-43712" class="comment-tools"></div><div class="clear"></div><div id="comment-43712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

