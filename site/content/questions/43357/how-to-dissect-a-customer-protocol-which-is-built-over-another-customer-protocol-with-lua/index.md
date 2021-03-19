+++
type = "question"
title = "How to dissect a customer protocol which is built over another customer protocol with lua"
description = '''Hello all  Recently I was asked to dissect some customer protocols with lua.There are two customer protocols named A and B.Protocol A was built over TCP while B was built over A. The problem is that each of them could be fragmented and resembled, A could be fragmented by TCP,B could be fragmented by...'''
date = "2015-06-19T02:38:00Z"
lastmod = "2015-06-19T02:38:00Z"
weight = 43357
keywords = [ "lua" ]
aliases = [ "/questions/43357" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to dissect a customer protocol which is built over another customer protocol with lua](/questions/43357/how-to-dissect-a-customer-protocol-which-is-built-over-another-customer-protocol-with-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43357-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all Recently I was asked to dissect some customer protocols with lua.There are two customer protocols named A and B.Protocol A was built over TCP while B was built over A. The problem is that each of them could be fragmented and resembled, A could be fragmented by TCP,B could be fragmented by A,which makes me almost go crazy .So,can someone can help me? thanks a lot!!!</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '15, 02:38</strong></p><img src="https://secure.gravatar.com/avatar/bac8cbee0f3a1748b25438dff604892a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidNorth&#39;s gravatar image" /><p>DavidNorth<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidNorth has no accepted answers">0%</span></p></div></div><div id="comments-container-43357" class="comments-container"><span id="43611"></span><div id="comment-43611" class="comment"><div id="post-43611-score" class="comment-score"></div><div class="comment-text"><p>What is the format of the "A" protocol - in particular, does it have a length field at a fixed location, hopefully somewhere early on in its format? If so, getting it to be reassembled is fairly easy. If not, then it's harder. But the answer to that affects the answer to the whole thing, so we need to know that before getting into the rest of it.</p></div><div id="comment-43611-info" class="comment-info"><span class="comment-age">(27 Jun '15, 17:21)</span> Hadriel</div></div></div><div id="comment-tools-43357" class="comment-tools"></div><div class="clear"></div><div id="comment-43357-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

