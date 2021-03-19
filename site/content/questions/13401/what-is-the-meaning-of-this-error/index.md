+++
type = "question"
title = "What is the meaning of this error?"
description = '''&quot;&#92;Device&#92;NPF_{12D8C25E-1599-4276-A1DD-C37CE0539DE8}&quot; is the proper interface.  What does this mean?'''
date = "2012-08-06T13:19:00Z"
lastmod = "2012-08-06T14:37:00Z"
weight = 13401
keywords = [ "npf", "error" ]
aliases = [ "/questions/13401" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What is the meaning of this error?](/questions/13401/what-is-the-meaning-of-this-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13401-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>&quot;\Device\NPF_{12D8C25E-1599-4276-A1DD-C37CE0539DE8}&quot; is the proper interface.</code></pre><p>What does this mean?</p></div><div id="question-tags" class="tags-container tags">npf error</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '12, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/d53a45c3c5d14f44a1190205d768641a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RadioRebel&#39;s gravatar image" /><p>RadioRebel<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RadioRebel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Aug '12, 13:55</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-13401" class="comments-container"></div><div id="comment-tools-13401" class="comment-tools"></div><div class="clear"></div><div id="comment-13401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13404"></span>

<div id="answer-container-13404" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13404-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That information is displayed by dumpcap, if you specify the wrong interface for option -i. The full error message is this:</p><blockquote><p><code>Please check that "\Device\NPF_{12D8C25E-1599-4276-A1DD-C37CE0539DE8}" is the proper interface.</code><br />
</p></blockquote><p>Please double check, that the given interface is among those listed with</p><blockquote><p><code>dumpcap -D -M</code></p></blockquote><p>You can use the interface number (also listed by dumpcap -D -M), instead of the device specifier, like this:</p><blockquote><p><code>dumpcap -n -i 3</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '12, 14:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-13404" class="comments-container"><span id="13410"></span><div id="comment-13410" class="comment"><div id="post-13410-score" class="comment-score"></div><div class="comment-text"><p>And the <em>full</em> full error message would also include</p><pre><code>The capture session could not be initiated (XXX).</code></pre><p>with some XXX message giving the reason <em>why</em> WinPcap (as used by Wireshark) couldn't open <code>\Device\NPF_{12D8C25E-1599-4276-A1DD-C37CE0539DE8}</code>.</p><p>If you didn't see all of that, there's a bug.</p></div><div id="comment-13410-info" class="comment-info"><span class="comment-age">(06 Aug '12, 19:12)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-13404" class="comment-tools"></div><div class="clear"></div><div id="comment-13404-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

