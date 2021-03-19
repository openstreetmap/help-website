+++
type = "question"
title = "What is Flow ID in Wireshark and how is it useful?"
description = '''What is Flow ID in Wireshark and how is it useful? Actually I attended a quick troubleshooting webinar yesterday, where the presenter shown some tricks using flow ID, to track the conversation of Client to Reverse Proxy, and Reverse Proxy to Backend Server. However I couldn&#x27;t find the same using my ...'''
date = "2014-11-24T22:49:00Z"
lastmod = "2014-11-25T07:55:00Z"
weight = 38117
keywords = [ "flow", "id" ]
aliases = [ "/questions/38117" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What is Flow ID in Wireshark and how is it useful?](/questions/38117/what-is-flow-id-in-wireshark-and-how-is-it-useful)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38117-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is Flow ID in Wireshark and how is it useful?</p><p>Actually I attended a quick troubleshooting webinar yesterday, where the presenter shown some tricks using flow ID, to track the conversation of Client to Reverse Proxy, and Reverse Proxy to Backend Server.</p><p>However I couldn't find the same using my Wireshark standard capture (I am using Wireshark 1.12). Any help?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">flow id</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '14, 22:49</strong></p><img src="https://secure.gravatar.com/avatar/c6a44d4a18f4da1685f04f40df43110d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swo0sh_gt&#39;s gravatar image" /><p>swo0sh_gt<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swo0sh_gt has no accepted answers">0%</span></p></div></div><div id="comments-container-38117" class="comments-container"></div><div id="comment-tools-38117" class="comment-tools"></div><div class="clear"></div><div id="comment-38117-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38123"></span>

<div id="answer-container-38123" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38123-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It was probably the "tcp.stream" filter, not flow, e.g. "tcp.stream==1".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '14, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-38123" class="comments-container"></div><div id="comment-tools-38123" class="comment-tools"></div><div class="clear"></div><div id="comment-38123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

