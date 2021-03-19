+++
type = "question"
title = "Can we call a dissector plugin from another dissector plugin?"
description = '''Folks, As per my requirements i will have to dissect eth header for all packets of my relevant protocol. So i was wondering if we have such functionality , i may write another plugin for eth and call it from my protocol plugin.'''
date = "2012-08-06T05:09:00Z"
lastmod = "2012-08-06T06:02:00Z"
weight = 13387
keywords = [ "dissector", "wireshark" ]
aliases = [ "/questions/13387" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can we call a dissector plugin from another dissector plugin?](/questions/13387/can-we-call-a-dissector-plugin-from-another-dissector-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13387-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Folks,</p><p>As per my requirements i will have to dissect eth header for all packets of my relevant protocol. So i was wondering if we have such functionality , i may write another plugin for eth and call it from my protocol plugin.</p></div><div id="question-tags" class="tags-container tags">dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '12, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p>yogeshg<br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div></div><div id="comments-container-13387" class="comments-container"></div><div id="comment-tools-13387" class="comment-tools"></div><div class="clear"></div><div id="comment-13387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13392"></span>

<div id="answer-container-13392" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13392-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not entirely sure what it is you're trying to do, but, yes dissectors/plugins can call other dissectors/plugins either directly (call_dissector()) or indirectly (caller registers a dissector table and then eventually calls dissector_try_uint() or similar and the callee registers itself for a value in that dissector table with dissector_add_uint() or similar).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '12, 06:02</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-13392" class="comments-container"><span id="13398"></span><div id="comment-13398" class="comment"><div id="post-13398-score" class="comment-score"></div><div class="comment-text"><p>thanks for your answer ,could you point me any example for this ? some plugin where this is being used</p></div><div id="comment-13398-info" class="comment-info"><span class="comment-age">(06 Aug '12, 07:48)</span> yogeshg</div></div><span id="13399"></span><div id="comment-13399" class="comment"><div id="post-13399-score" class="comment-score"></div><div class="comment-text"><p>Almost all dissectors behave like this. For one example, see packet-sctp.c.</p></div><div id="comment-13399-info" class="comment-info"><span class="comment-age">(06 Aug '12, 08:19)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-13392" class="comment-tools"></div><div class="clear"></div><div id="comment-13392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

