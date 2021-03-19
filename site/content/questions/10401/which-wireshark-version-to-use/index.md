+++
type = "question"
title = "Which Wireshark Version to Use"
description = '''I have Windows 2008 Server, 64bit, running on my box. Which is the most stable version of Wireshark to run?'''
date = "2012-04-23T08:57:00Z"
lastmod = "2012-04-23T09:09:00Z"
weight = 10401
keywords = [ "version", "wireshark" ]
aliases = [ "/questions/10401" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Which Wireshark Version to Use](/questions/10401/which-wireshark-version-to-use)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10401-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have Windows 2008 Server, 64bit, running on my box. Which is the most stable version of Wireshark to run?</p></div><div id="question-tags" class="tags-container tags">version wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '12, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/3e61de7453e178446a376a76deeba2b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BaselineTech&#39;s gravatar image" /><p>BaselineTech<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BaselineTech has no accepted answers">0%</span></p></div></div><div id="comments-container-10401" class="comments-container"></div><div id="comment-tools-10401" class="comment-tools"></div><div class="clear"></div><div id="comment-10401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10403"></span>

<div id="answer-container-10403" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10403-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>32bit or 64bit stable versions are pretty much the same when it comes to stability - at least that's my observation. The 64bit version seems to be able to handle larger traces, but still has some functionality missing (usually found in the known bugs list in the release notes).</p><p>But just to add a warning: if you're trying to install Wireshark on your server because you want to capture what it does wrong you should be aware that that kind of approach is problematic in many ways. You should use an additional PC on a SPAN port instead if you can - the captured data is more consistent than doing a local capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '12, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-10403" class="comments-container"></div><div id="comment-tools-10403" class="comment-tools"></div><div class="clear"></div><div id="comment-10403-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10404"></span>

<div id="answer-container-10404" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10404-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do you mean 1.4 or 1.6 or possibly 1.7?</p><p>Both 1.4 and 1.6 are in maintenance mode now where they only get bugfixes, so by definition, the latest in each version has most bugs fixed. 1.7 or the nightly build is on the bleeding edge of development and shouldn't be considered stable.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '12, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-10404" class="comments-container"></div><div id="comment-tools-10404" class="comment-tools"></div><div class="clear"></div><div id="comment-10404-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

