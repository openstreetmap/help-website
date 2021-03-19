+++
type = "question"
title = "Track specific diameter requests without response"
description = '''Hi Experts, Is there any functionality specific to diameter wherein I can track requests which don&#x27;t have response or wherein response is other than success I believe we can use following filter for processing radius traffic.  (radius.req &amp;amp;&amp;amp; !radius.rspframe) Please advise.'''
date = "2016-11-24T12:06:00Z"
lastmod = "2016-11-25T08:29:00Z"
weight = 57617
keywords = [ "diameter" ]
aliases = [ "/questions/57617" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Track specific diameter requests without response](/questions/57617/track-specific-diameter-requests-without-response)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57617-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts,</p><p>Is there any functionality specific to diameter wherein I can track requests which don't have response or wherein response is other than success</p><p>I believe we can use following filter for processing radius traffic.</p><p><em>(radius.req &amp;&amp; !radius.rspframe)</em></p><p>Please advise.</p></div><div id="question-tags" class="tags-container tags">diameter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '16, 12:06</strong></p><img src="https://secure.gravatar.com/avatar/d1e5efe891c907bf6be8231eca9db31a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vijay%20Gharge&#39;s gravatar image" /><p>Vijay Gharge<br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vijay Gharge has no accepted answers">0%</span></p></div></div><div id="comments-container-57617" class="comments-container"></div><div id="comment-tools-57617" class="comment-tools"></div><div class="clear"></div><div id="comment-57617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57637"></span>

<div id="answer-container-57637" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57637-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The filter you've found for RADIUS, <code>radius.req and !radius.rspframe</code>, does identify requests without a matching response in the capture, as the embedded dissector creates the cross-reference pseudofields <code>radius.reqframe</code> and <code>radius.rspframe</code>.</p><p>The diameter dissector does the same, except that the pseudo-fields are called <code>diameter.answer_to</code> and <code>diameter.answer_in</code>. So the equivalent of your filter, showing only requests without a matching response, would be <code>diameter.flags.request == 1 and !diameter.answer_in</code>.</p><p>However, that's the maximum you can get from the embedded dissector.</p><p>To display-filter requests which have received responses with other than successful result, you need two things:</p><ul><li><p>to define what an "other than successful result" means in your context, because not all diameter applications contain the <code>Result-Code</code> AVP. Is <code>diameter.flags.error == 1</code> a sufficient criterion?</p></li><li><p>to use a <a href="https://wiki.wireshark.org/Lua/Dissectors#postdissectors">Lua post-dissector</a> or <a href="https://wiki.wireshark.org/Mate">MATE</a> to use fields from dissection trees of response packets for creation of your own pseudo-field(s) in the dissection tree of the request packets, allowing to display-filter the requests on these pseudo-fields. MATE does a lot of things automatically but in its own way, while Lua gives you more flexibility but you have to type much more to achieve the goal.</p></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '16, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Nov '16, 13:40</p></div></div><div id="comments-container-57637" class="comments-container"><span id="57640"></span><div id="comment-57640" class="comment"><div id="post-57640-score" class="comment-score"></div><div class="comment-text"><p>Thanks @Sindy for answer. While I will definitely try first solution, working on 2nd solution (LUA / MATE) is beyond my capacity. Will attempt, though :-)</p></div><div id="comment-57640-info" class="comment-info"><span class="comment-age">(25 Nov '16, 11:56)</span> Vijay Gharge</div></div></div><div id="comment-tools-57637" class="comment-tools"></div><div class="clear"></div><div id="comment-57637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

