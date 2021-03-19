+++
type = "question"
title = "Translating TCP Stream to readable format"
description = '''I&#x27;m a total newbie. I&#x27;m trying to translate a TCP stream into a readable format. Ideally, I&#x27;d like to read the body of the emails I&#x27;m capturing. Is that possible with wireshark? If so, how?'''
date = "2011-02-23T07:20:00Z"
lastmod = "2011-02-23T07:30:00Z"
weight = 2518
keywords = [ "email" ]
aliases = [ "/questions/2518" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Translating TCP Stream to readable format](/questions/2518/translating-tcp-stream-to-readable-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2518-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm a total newbie. I'm trying to translate a TCP stream into a readable format. Ideally, I'd like to read the body of the emails I'm capturing. Is that possible with wireshark? If so, how?</p></div><div id="question-tags" class="tags-container tags">email</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '11, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/1e6e9c6fc2dfe2f547343bb1f329e416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shadow&#39;s gravatar image" /><p>Shadow<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shadow has no accepted answers">0%</span></p></div></div><div id="comments-container-2518" class="comments-container"></div><div id="comment-tools-2518" class="comment-tools"></div><div class="clear"></div><div id="comment-2518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2519"></span>

<div id="answer-container-2519" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2519-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you can do that. If you have already identified the TCP stream you can use the popup menu on one of the packets of the stream in the packet list and select the "Follow TCP Stream" option. That will open an additional window that contains the TCP playload in (more or less) readable format. It works especially well for all ASCII based TCP payloads.</p><p>If you don't have isolated the stream yet you can use the Statistics -&gt; Conversations to look for the correct communications and filter on that with the popup menu.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '11, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Feb '11, 07:31</p></div></div><div id="comments-container-2519" class="comments-container"><span id="2536"></span><div id="comment-2536" class="comment"><div id="post-2536-score" class="comment-score"></div><div class="comment-text"><p>Thanks! I'll try that and let you know how it goes.</p></div><div id="comment-2536-info" class="comment-info"><span class="comment-age">(23 Feb '11, 13:11)</span> Shadow</div></div><span id="2537"></span><div id="comment-2537" class="comment"><div id="post-2537-score" class="comment-score"></div><div class="comment-text"><p>("Answer" converted to a comment in keeping with the philosophy of ask.wireshark.org)</p></div><div id="comment-2537-info" class="comment-info"><span class="comment-age">(23 Feb '11, 13:21)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-2519" class="comment-tools"></div><div class="clear"></div><div id="comment-2519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

