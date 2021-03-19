+++
type = "question"
title = "Hosts machine names used in Display filter macros?"
description = '''I have a hosts file with several IP addresses mapped to strings like VCG, VS, and VSTG (which are my server names). I have many display filter macros with these same IP addresses hard-coded into the macros. Is there a way to use the same strings from my hosts file in my display filter macros? Thus e...'''
date = "2016-03-24T19:49:00Z"
lastmod = "2016-03-24T22:12:00Z"
weight = 51168
keywords = [ "filter", "macro", "hosts", "display", "file" ]
aliases = [ "/questions/51168" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Hosts machine names used in Display filter macros?](/questions/51168/hosts-machine-names-used-in-display-filter-macros)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51168-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a hosts file with several IP addresses mapped to strings like VCG, VS, and VSTG (which are my server names). I have many display filter macros with these same IP addresses hard-coded into the macros.</p><p>Is there a way to use the same strings from my hosts file in my display filter macros? Thus eliminating the need for the hard-coding of the IP addresses?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">filter macro hosts display file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '16, 19:49</strong></p><img src="https://secure.gravatar.com/avatar/b3270ea804306e71984b713be60df166?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rbw006&#39;s gravatar image" /><p>rbw006<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rbw006 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Mar '16, 03:53</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-51168" class="comments-container"></div><div id="comment-tools-51168" class="comment-tools"></div><div class="clear"></div><div id="comment-51168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51169"></span>

<div id="answer-container-51169" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51169-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try</p><pre><code>ip.host contains &quot;VCG&quot; or ip.host contains &quot;VS&quot;</code></pre><p>and see if this satisfies your needs</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '16, 22:12</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-51169" class="comments-container"></div><div id="comment-tools-51169" class="comment-tools"></div><div class="clear"></div><div id="comment-51169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

