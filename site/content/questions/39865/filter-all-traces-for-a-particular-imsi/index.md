+++
type = "question"
title = "Filter all traces for a particular IMSI"
description = '''Hi  I would like to know , how can we filtered out all related traces of a particular request on a production system.  For example , in a telecom network , how can we filtered out all related data for a particular IMSI ? Regards Luke.'''
date = "2015-02-14T20:31:00Z"
lastmod = "2015-02-15T12:35:00Z"
weight = 39865
keywords = [ "imsi" ]
aliases = [ "/questions/39865" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filter all traces for a particular IMSI](/questions/39865/filter-all-traces-for-a-particular-imsi)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39865-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I would like to know , how can we filtered out all related traces of a particular request on a production system.</p><p>For example , in a telecom network , how can we filtered out all related data for a particular IMSI ?</p><p>Regards Luke.</p></div><div id="question-tags" class="tags-container tags">imsi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '15, 20:31</strong></p><img src="https://secure.gravatar.com/avatar/c47703d618d332e48938f591da8a272c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="luke_devon&#39;s gravatar image" /><p>luke_devon<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="luke_devon has no accepted answers">0%</span></p></div></div><div id="comments-container-39865" class="comments-container"><span id="42185"></span><div id="comment-42185" class="comment"><div id="post-42185-score" class="comment-score"></div><div class="comment-text"><p>If it is GSM_MAP, you'd use as a display filter "gsm_map.imsi_digits contains 123456789012345" or some partial IMSI thereof. In newer versions of Wireshark, it's "gsm_map.imsi"</p><p>What Quadratic said is right about SS7 applications. In an ANSI network, there will be an E212/IMSI in the SCCP called party address for messaging that is being routed to a mobile global title (UpdateLocation, SendAuthenticationInfo, etc). In an ITU network, instead of E212/IMSI it will be a hybrid E214 for those same messages types. Note that for supplementary services type messages (i.e. hen a user sends *129# for balance inquiry) the IMSI is actually in the TCAP layer as a "destination reference".</p><p>If you give more specifics we can probably help you more.</p></div><div id="comment-42185-info" class="comment-info"><span class="comment-age">(07 May '15, 07:24)</span> tiger762</div></div></div><div id="comment-tools-39865" class="comment-tools"></div><div class="clear"></div><div id="comment-39865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39873"></span>

<div id="answer-container-39873" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39873-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There isn't anything as simple as that, but on a per-protocol basis it can certainly be done. For example:</p><ul><li>In Diameter S6a/S6d, 'diameter.User-Name==imsi' will get you the request. Then filter on that request's "diameter.Session-Id" value and you have the request/response for that IMSI.</li><li>In RANAP messaging, first you'd need to find an IMSI-based procedure (typically within the Common-Id IE) and search for the SCCP association id to grab. Search for that association id, and you get the full dialogue.</li><li>In policy control applications, typically it's the same as S6a except that diameter.Subscription-Id-Data would be used insead of diameter.User-Name.</li><li>In Sigtran/SS7 applications, at the SCCP layer often you have E.212/E.214 translation in use. In those cases, the called/calling party address can be searched for, mapped to a TCAP transaction, then that TCAP transaction can be searched for to get the full dialogue. For E.164-translated exchanges, you might not have an IMSI number at all so it would again depend on the application you're tracing.</li><li>In SGsAP, that protocol contains the IMSI in every single message in either direction (gsm_a.imsi==imsi), so it's dirt simple to trace.</li><li>In S1AP, IMSIs appear in some types of procedures but not all. You'd typically need to map out temporary identifiers for these (M-TMSIs), map them to IMSI from previous exchanges, then sort out the UE Contexts based on the MME UE Context ID and the eNodeB UE Context ID fields, realizing that both can change throughout the context due to mobility events.</li><li>For SIP, potentially you can get the IMSI out of a URI or would have to map it to a URI. From that, get related SIP exchanges on URI and take the Call ID from it to trace such a session.</li><li>For GTP, the procedure is similar between GTPv1 and v2 but either way you'd need to search for IMSI first, from it grab the sequence number, map it to the Create Session Response, then from that response you have all the GTP TEID values to include in a subsequent display filter for all the requests/responses mapping to tunnels set up for a given subscriber IMSI.</li></ul><p>And I could keep going. :)</p><p>My point here is that your tracing methodology will depend greatly on the protocol, especially if you want all signaling that relates to a subscriber rather than just messages that contain the IMSI verbatim.</p><p>Now, in a telecom context typically you have trace tools (eg: Tektronix) to do this, though depending on what you're trying to do it isn't impossible to just built these trace tools from scratch. It's definitely not built into wireshark proper, though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '15, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Feb '15, 12:37</p></div></div><div id="comments-container-39873" class="comments-container"><span id="39874"></span><div id="comment-39874" class="comment"><div id="post-39874-score" class="comment-score"></div><div class="comment-text"><p>Well, the development version of Wireshark (1.99.x) should make this easier: a lot of the places where Wireshark finds an IMSI (e.g., diameter.User-Name for S6a/S6d) now has a non-protocol-specific filter: e212.imsi . SCCP is the same (if the NP is appropriate). I forget what other protocols have been converted but I'm pretty sure Anders did a bunch.</p></div><div id="comment-39874-info" class="comment-info"><span class="comment-age">(15 Feb '15, 15:25)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-39873" class="comment-tools"></div><div class="clear"></div><div id="comment-39873-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

