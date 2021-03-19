+++
type = "question"
title = "filtering out X2AP transmissions for a single UE"
description = '''I would like to filter X2AP related transmissions for a single UE only but I dont know how to do this yet as I am a newbie in Wireshark. What filter can I use? Thanks'''
date = "2016-04-20T23:29:00Z"
lastmod = "2016-04-22T18:45:00Z"
weight = 51829
keywords = [ "x2ap", "capture-filter", "lte", "display-filter" ]
aliases = [ "/questions/51829" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [filtering out X2AP transmissions for a single UE](/questions/51829/filtering-out-x2ap-transmissions-for-a-single-ue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51829-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to filter X2AP related transmissions for a single UE only but I dont know how to do this yet as I am a newbie in Wireshark. What filter can I use? Thanks</p></div><div id="question-tags" class="tags-container tags">x2ap capture-filter lte display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '16, 23:29</strong></p><img src="https://secure.gravatar.com/avatar/ca02d0b4dedd058552f233c010585a1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fearfox&#39;s gravatar image" /><p>fearfox<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fearfox has no accepted answers">0%</span></p></div></div><div id="comments-container-51829" class="comments-container"></div><div id="comment-tools-51829" class="comment-tools"></div><div class="clear"></div><div id="comment-51829-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51886"></span>

<div id="answer-container-51886" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51886-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To start off with, a few useful filters:</p><ul><li>x2ap.UE_X2AP_ID (gives the X2AP procedure for a given UE context across an X2 handover)</li><li>x2ap.gTP_TEID (gives the GTP tunnel identifiers, used both for X2 GTP as well as S1 GTP)</li><li>gtp.teid (search for GTP payload of a given GTP tunnel ID)</li><li>x2ap.mME_UE_S1AP_ID (value maps to the UE Context ID used by the MME for the S1AP signaling for the UE being moved over)</li></ul><p>What filters to use depend on what you are trying to do though. For example, if you have a phone number and are trying to "search for it's X2 traffic", that's not a one-step process. Usually if you're doing it long-hand it goes something like this:</p><ul><li>Start by knowing something that will identify the UE in mobility management procedures (eg: IMSI or GUTI/M-TMSI as the case may be)</li><li>Search for the above identifier's in S1-MME to find the UE at that level. Note that while identifiers in initiation of UE Contexts are sent prior to any standard encryption mechanisms, the use of temporary identifiers may mean some recursive searching or knowledge of the mobile operator (particularly HSS's knowledge of the serving MME, and the MME's knowledge of the assigned temp identifier to that UE) to get a usable search criteria for the UE in raw mobility signaling flows.</li><li>Catch that identifier in use within a transaction over S1AP signaling (S1-MME interface) such that you can grab the MME and eNodeB's "UE Context ID" value in use for that ECM connection</li><li>Follow the MME UE Context ID through the ECM connection until you see a path switch request come in for it, always from a new "target" eNodeB.</li><li>From there, you know you have X2AP signaling between the source and target eNodeB's for the X2 HO. So, search over X2AP signaling between them based on the MME UE Context ID. That will lead you to the X2AP context identifier, for which you can follow the handover preparation exchange.</li><li>From the handover preparation exchange, the GTP identifiers will lead you to follow the S1 and X2 GTP bearers as needed, depending on what you're looking for.</li></ul><p>Now, that is assuming you are starting from nothing but an IMSI or GUTI. If you already know some of that information or you have a different starting point, your process will be quite different.</p><p>Always with Wireshark protocol analysis, knowing the protocol is paramount. Knowing the "right display filters" is intuitive if you know what identifiers exist logically between the systems that can be mapped to things. Right click and "copy as filter" on any field you want in Wireshark and it will produce the filter format for it, but this is less than 1% of the battle.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '16, 18:45</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Apr '16, 18:55</p></div></div><div id="comments-container-51886" class="comments-container"></div><div id="comment-tools-51886" class="comment-tools"></div><div class="clear"></div><div id="comment-51886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

