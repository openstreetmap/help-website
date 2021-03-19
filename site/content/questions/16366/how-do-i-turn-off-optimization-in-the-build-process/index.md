+++
type = "question"
title = "how do i turn off optimization in the build process"
description = '''to enable better single step debugging.'''
date = "2012-11-27T21:35:00Z"
lastmod = "2012-11-28T05:36:00Z"
weight = 16366
keywords = [ "debug", "make", "makefile", "gcc" ]
aliases = [ "/questions/16366" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how do i turn off optimization in the build process](/questions/16366/how-do-i-turn-off-optimization-in-the-build-process)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16366-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>to enable better single step debugging.</p></div><div id="question-tags" class="tags-container tags">debug make makefile gcc</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '12, 21:35</strong></p><img src="https://secure.gravatar.com/avatar/56993b38fa37140b783e7913ec139f45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="protocolmagic&#39;s gravatar image" /><p>protocolmagic<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="protocolmagic has no accepted answers">0%</span></p></div></div><div id="comments-container-16366" class="comments-container"></div><div id="comment-tools-16366" class="comment-tools"></div><div class="clear"></div><div id="comment-16366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16382"></span>

<div id="answer-container-16382" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16382-score" class="post-score" title="current number of votes">6</div></div></td><td><div class="item-right"><div class="answer-body"><p>Given that the question is tagged with 'gcc' ...</p><p>You can disable optimization the same way(s) as for any autofoo make process.... :)</p><p>One way:</p><pre><code>CFLAGS=&#39;-g -O0&#39; ./configure      ## season to taste with configure options as needed</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Nov '12, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Nov '12, 05:42</p></div></div><div id="comments-container-16382" class="comments-container"><span id="16408"></span><div id="comment-16408" class="comment"><div id="post-16408-score" class="comment-score"></div><div class="comment-text"><p>it seems that you can also place the CFLAGS= after the .configure for wireshark.</p></div><div id="comment-16408-info" class="comment-info"><span class="comment-age">(28 Nov '12, 16:35)</span> protocolmagic</div></div></div><div id="comment-tools-16382" class="comment-tools"></div><div class="clear"></div><div id="comment-16382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

