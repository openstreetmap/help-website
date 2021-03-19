+++
type = "question"
title = "Request: INVITE &quot;address of SIP client&quot;, with session description"
description = ''' SIP client sends request to SBC. &quot;unknown&quot; IP (I&#x27;m waiting for the answer from my collaborator what&#x27;s that IP) sends request to P-CSCF.  Question: When sending request INVITE to SBC, SIP client tells him its SIP address, right? When sending request INVITE to P-CSCF, does this &quot;unknown&quot; IP know SIP ...'''
date = "2011-04-30T15:58:00Z"
lastmod = "2011-04-30T17:01:00Z"
weight = 3855
keywords = [ "sip", "request", "invite", "address", "know" ]
aliases = [ "/questions/3855" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Request: INVITE "address of SIP client", with session description](/questions/3855/request-invite-address-of-sip-client-with-session-description)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3855-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><ol><li>SIP client sends request to SBC.</li><li>"unknown" IP (I'm waiting for the answer from my collaborator what's that IP) sends request to P-CSCF.</li></ol><p>Question:</p><p>When sending request INVITE to SBC, SIP client tells him its SIP address, right? When sending request INVITE to P-CSCF, does this "unknown" IP know SIP address or wants it?</p><p>(I suspect this "unknown" IP belongs to device from Ericsson TSP applications "box" (regarding to my IMS reference paper), where HSS, I-CSCF, S-CSCF, P-CSCF etc. are.)</p><p>Maybe a little confused question (and thinking)...but I'm dilemma.</p></div><div id="question-tags" class="tags-container tags">sip request invite address know</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '11, 15:58</strong></p><img src="https://secure.gravatar.com/avatar/13231e33ab17a93476f7b98c9d5b272a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wired&#39;s gravatar image" /><p>wired<br />
<span class="score" title="44 reputation points">44</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wired has one accepted answer">9%</span></p></div></div><div id="comments-container-3855" class="comments-container"><span id="3856"></span><div id="comment-3856" class="comment"><div id="post-3856-score" class="comment-score"></div><div class="comment-text"><p>9 2.304519s SIP client Session Border Controller (SBC) SIP/SDP 917 Request: INVITE sip:[email protected]_domain.net, with session description</p><p>13 2.311316s 10.253.70.197 P-CSCF SIP/SDP 1105 Request: INVITE sip:[email protected]_domain.net, with session description</p><p>These packets are parts of prepaid call from SIP client do circuit switched domain.</p></div><div id="comment-3856-info" class="comment-info"><span class="comment-age">(30 Apr '11, 16:01)</span> wired</div></div><span id="3857"></span><div id="comment-3857" class="comment"><div id="post-3857-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure I understand the question, on IP level the client's (UE) INVITE will go to the IP of the SBG:s access side, on the core side the sourc IP will be that of the SBG:s core interface. e.g The INVITE going to P-CSCF will have the IP address of SBG core. /Anders</p></div><div id="comment-3857-info" class="comment-info"><span class="comment-age">(30 Apr '11, 16:58)</span> Anders ♦</div></div><span id="3861"></span><div id="comment-3861" class="comment"><div id="post-3861-score" class="comment-score"></div><div class="comment-text"><p>That's ok, fine explanation.</p><p>But in Wireshark info (about packet) there's a sip:[email protected]_domain.net (in real it's actual SIP address of client), so if I understand clearly, INVITE going from 10.253.70.197 to P-CSCF, includes this SIP address?</p></div><div id="comment-3861-info" class="comment-info"><span class="comment-age">(30 Apr '11, 23:44)</span> wired</div></div></div><div id="comment-tools-3855" class="comment-tools"></div><div class="clear"></div><div id="comment-3855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3858"></span>

<div id="answer-container-3858" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3858-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If it helps, here you can see where this IP lies.</p><p><img src="http://file.si/pfiles/171341/Zajeta%20slika.PNG" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '11, 17:01</strong></p><img src="https://secure.gravatar.com/avatar/13231e33ab17a93476f7b98c9d5b272a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wired&#39;s gravatar image" /><p>wired<br />
<span class="score" title="44 reputation points">44</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wired has one accepted answer">9%</span></p></img></div></div><div id="comments-container-3858" class="comments-container"></div><div id="comment-tools-3858" class="comment-tools"></div><div class="clear"></div><div id="comment-3858-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

