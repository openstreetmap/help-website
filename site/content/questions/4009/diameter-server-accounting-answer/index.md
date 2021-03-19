+++
type = "question"
title = "Diameter Server - Accounting Answer"
description = '''If HSS (Home Subscriber Server) acts as a Diameter Client and is sending Accounting Requests (I see in traffic), who acts as a Diameter Server?'''
date = "2011-05-08T13:59:00Z"
lastmod = "2014-04-04T15:16:00Z"
weight = 4009
keywords = [ "answer", "diameter", "client", "request", "accounting" ]
aliases = [ "/questions/4009" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Diameter Server - Accounting Answer](/questions/4009/diameter-server-accounting-answer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4009-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If HSS (Home Subscriber Server) acts as a Diameter Client and is sending Accounting Requests (I see in traffic), who acts as a Diameter Server?</p></div><div id="question-tags" class="tags-container tags">answer diameter client request accounting</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '11, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/13231e33ab17a93476f7b98c9d5b272a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wired&#39;s gravatar image" /><p>wired<br />
<span class="score" title="44 reputation points">44</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wired has one accepted answer">9%</span></p></div></div><div id="comments-container-4009" class="comments-container"><span id="4010"></span><div id="comment-4010" class="comment"><div id="post-4010-score" class="comment-score"></div><div class="comment-text"><p>As I know from studying and book IMS Signalling (by Ericsson), HSS acts as a Diameter Server? Why Client in my trace? :-s</p></div><div id="comment-4010-info" class="comment-info"><span class="comment-age">(08 May '11, 14:23)</span> wired</div></div><span id="31518"></span><div id="comment-31518" class="comment"><div id="post-31518-score" class="comment-score"></div><div class="comment-text"><p>you should know, HSS server can also invoke requests.</p><p>like HSS issue RTR to S-CSCF to deregister an identity, PPR to notify profile changes of any identity.</p></div><div id="comment-31518-info" class="comment-info"><span class="comment-age">(04 Apr '14, 09:20)</span> Sanny_D</div></div></div><div id="comment-tools-4009" class="comment-tools"></div><div class="clear"></div><div id="comment-4009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31534"></span>

<div id="answer-container-31534" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31534-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Many Diameter interfaces involve server-initiated exchanges. You see it even in the base protocol spec. A "server" from a Diameter perspective is not strictly defined by the originator of a message, and is usually defined within the context of a given Diameter application. In theory it's even possible for a single Diameter host to be a client for one application and a server for another unrelated application, over the same Diameter peering to an upstream agent.</p><p>To your question on who is "serving" the HSS's request, when you consider that Diameter itself is a blanket protocol with many applications running over it, with Diameter "Agents" potentially sitting between end systems, to call anything a "Server" you really need to base that terminology on the specific application you're concerned with, running over top of Diameter.</p><p>For example, for Diameter credit control (DCCA, RFC 4006), the state machine logic specifically calls for a Diameter Credit Control "Client" and a Diameter Credit Control "Server", where you are technically correct to say that a "Server" sends the Reauthentication Request (RAR) messages 'ONLY' because the credit control application spec specifically defines it as a "Server".</p><p>Or another way to look at it: If you have agents, your client is sending CER messages to an agent directly. Does that make the agent a server? You always have a given requester and answerer, but "Server" is ambiguous unless you give it the context of a specific application and scenario.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '14, 15:16</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Apr '14, 15:20</p></div></div><div id="comments-container-31534" class="comments-container"></div><div id="comment-tools-31534" class="comment-tools"></div><div class="clear"></div><div id="comment-31534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

