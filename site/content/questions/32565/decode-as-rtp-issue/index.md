+++
type = "question"
title = "Decode as RTP issue"
description = '''Hello, I upgraded from version 1.4.x to version 1.10.7 and after the upgrade I could no longer decode my UDP packets logs to RTP instead it shows MPEG TS under the protocol column. Is there an option or configuration I need to do to see the RTP packets and it&#x27;s sequence number? Thanks, Rollin'''
date = "2014-05-06T14:43:00Z"
lastmod = "2014-05-07T04:40:00Z"
weight = 32565
keywords = [ "rtp" ]
aliases = [ "/questions/32565" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decode as RTP issue](/questions/32565/decode-as-rtp-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32565-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I upgraded from version 1.4.x to version 1.10.7 and after the upgrade I could no longer decode my UDP packets logs to RTP instead it shows MPEG TS under the protocol column. Is there an option or configuration I need to do to see the RTP packets and it's sequence number?</p><p>Thanks,</p><p>Rollin</p></div><div id="question-tags" class="tags-container tags">rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '14, 14:43</strong></p><img src="https://secure.gravatar.com/avatar/8d3c3e377b6300e24ffdfa0233bf52ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rollin&#39;s gravatar image" /><p>Rollin<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rollin has no accepted answers">0%</span></p></div></div><div id="comments-container-32565" class="comments-container"><span id="32578"></span><div id="comment-32578" class="comment"><div id="post-32578-score" class="comment-score"></div><div class="comment-text"><p>Are the PayloadType(PT) 33 for those packets?</p><h1 id="define-pt_mp2t-33-rfc-2250">define PT_MP2T 33 / <em>RFC 2250</em> /</h1></div><div id="comment-32578-info" class="comment-info"><span class="comment-age">(06 May '14, 22:45)</span> Anders ♦</div></div><span id="32584"></span><div id="comment-32584" class="comment"><div id="post-32584-score" class="comment-score"></div><div class="comment-text"><p>Anders,</p><p>Yes Payload type is 33.</p><p>Rollin</p></div><div id="comment-32584-info" class="comment-info"><span class="comment-age">(07 May '14, 04:26)</span> Rollin</div></div></div><div id="comment-tools-32565" class="comment-tools"></div><div class="clear"></div><div id="comment-32565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32585"></span>

<div id="answer-container-32585" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32585-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As this is the dedicated PT of MPEG TS your application shouldn't be using it for something else. You could try to disseable the dissector for MPEG TS to have it dissected as RTP only.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '14, 04:40</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-32585" class="comments-container"><span id="32587"></span><div id="comment-32587" class="comment"><div id="post-32587-score" class="comment-score"></div><div class="comment-text"><p>Thank you Anders.</p><p>Its fine now.</p></div><div id="comment-32587-info" class="comment-info"><span class="comment-age">(07 May '14, 04:52)</span> Rollin</div></div></div><div id="comment-tools-32585" class="comment-tools"></div><div class="clear"></div><div id="comment-32585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

