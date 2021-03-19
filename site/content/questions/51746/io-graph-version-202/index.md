+++
type = "question"
title = "IO graph version 2.0.2"
description = '''Hello, I&#x27;m trying to perform a graph regarding some filters. But the graph is always showed with the same X axis(0 - 400000secons). So the packets are almost non-visible(the traces is only 400 seconds). Could everyone help me out to fix this? Thanks in advance, BR.'''
date = "2016-04-18T02:18:00Z"
lastmod = "2016-04-18T02:35:00Z"
weight = 51746
keywords = [ "graph", "io" ]
aliases = [ "/questions/51746" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IO graph version 2.0.2](/questions/51746/io-graph-version-202)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51746-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm trying to perform a graph regarding some filters. But the graph is always showed with the same X axis(0 - 400000secons). So the packets are almost non-visible(the traces is only 400 seconds).</p><p>Could everyone help me out to fix this?</p><p>Thanks in advance,</p><p>BR.</p></div><div id="question-tags" class="tags-container tags">graph io</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '16, 02:18</strong></p><img src="https://secure.gravatar.com/avatar/c36fd60b6172be76f222ef3f5309acd3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="germanv&#39;s gravatar image" /><p>germanv<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="germanv has no accepted answers">0%</span></p></div></div><div id="comments-container-51746" class="comments-container"></div><div id="comment-tools-51746" class="comment-tools"></div><div class="clear"></div><div id="comment-51746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51747"></span>

<div id="answer-container-51747" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51747-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried to right-click on the graph and zoom in X-axis? I know it is not a solution but should help if you only need it occasionally.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '16, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-51747" class="comments-container"><span id="51748"></span><div id="comment-51748" class="comment"><div id="post-51748-score" class="comment-score"></div><div class="comment-text"><p>Thank you. It looks this workaround can be useful for now.</p></div><div id="comment-51748-info" class="comment-info"><span class="comment-age">(18 Apr '16, 02:48)</span> germanv</div></div><span id="51750"></span><div id="comment-51750" class="comment"><div id="post-51750-score" class="comment-score"></div><div class="comment-text"><p>OK, so now think about <a href="https://bugs.wireshark.org/bugzilla/enter_bug.cgi">filing a bug</a> (of "nice to have" severity) asking to automatically adjust the X zoom to span from the timestamp of the earliest filtered frame of all curves to the timestamp of the latest filtered frame of all curves.</p></div><div id="comment-51750-info" class="comment-info"><span class="comment-age">(18 Apr '16, 03:10)</span> sindy</div></div><span id="51789"></span><div id="comment-51789" class="comment"><div id="post-51789-score" class="comment-score"></div><div class="comment-text"><p>(@sindy, I converted your comment to an answer. And then converted the followup comments to comments on the answer--which isn't exactly trivial.)</p></div><div id="comment-51789-info" class="comment-info"><span class="comment-age">(19 Apr '16, 08:49)</span> JeffMorriss ♦</div></div><span id="53580"></span><div id="comment-53580" class="comment"><div id="post-53580-score" class="comment-score"></div><div class="comment-text"><p>Personally I couldn't live with this new capability as it's almost impossible to use and has all that zooming nonsense. The IOgraph is really one of the most powerful aspects of wireshark as it helps to characterize network behaviour and faults. This new tool just doesn't work in my view and I have downgraded to release 1.</p></div><div id="comment-53580-info" class="comment-info"><span class="comment-age">(21 Jun '16, 01:17)</span> Graham Heath</div></div></div><div id="comment-tools-51747" class="comment-tools"></div><div class="clear"></div><div id="comment-51747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

