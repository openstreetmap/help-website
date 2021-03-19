+++
type = "question"
title = "information per LTE user"
description = '''Hi, Does Wireshark has a way to display information per LTE user (Data/ VoLTE protocols S1AP, GTPv2, Diameter)? (similar to ISUP VoiP Call analysis option) BR, Diana'''
date = "2014-06-24T01:59:00Z"
lastmod = "2014-06-24T21:33:00Z"
weight = 34109
keywords = [ "lte" ]
aliases = [ "/questions/34109" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [information per LTE user](/questions/34109/information-per-lte-user)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34109-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Does Wireshark has a way to display information per <strong>LTE</strong> user (Data/ VoLTE protocols S1AP, GTPv2, Diameter)? (similar to ISUP VoiP Call analysis option)</p><p>BR, Diana</p></div><div id="question-tags" class="tags-container tags">lte</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '14, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/900044aef60dc6223168781e5d576bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dianalab9&#39;s gravatar image" /><p>Dianalab9<br />
<span class="score" title="26 reputation points">26</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dianalab9 has no accepted answers">0%</span></p></div></div><div id="comments-container-34109" class="comments-container"></div><div id="comment-tools-34109" class="comment-tools"></div><div class="clear"></div><div id="comment-34109-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34146"></span>

<div id="answer-container-34146" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34146-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It doesn't have a great subscriber trace tool concept, though since you're including VoLTE in that mix it does support some SIP analytics and call breakdowns, mapping SIP to RTP streams, etc. (see the telephony section) For the rest, it supports the protocols but not a call trace.</p><p>It's not too difficult to write such a trace program though, since you can script it out with a few recursive lookups on packet captures using Wireshark's tshark command utility if it's not built in.</p><p>For example, trace something like S6a or Ro with:</p><pre><code>tshark -r {file} -R diameter.User-Name=={imsi} -T fields -e diameter.Session-Id
tshark -r {file} -R diameter.Session-Id=={list of all unique IDs returned in the above command}</code></pre><p>Each protocol is a little bit different, but most of the recursion logic is at least similar. Diameter is easy in general to trace, as is GTP and GTPv2 (for gtpv2.imsi, take unique sequence numbers, for matching sequence numbers take TEID(s), search for all with those TEIDs), though S1AP/NAS is challenging if you're talking about a need to map out GUTI/S-TMSI procedures to a UE out of a capture file, plus you're more likely to be setting up encryption on authentication with the UE at the NAS layer at least, so you're limited in what Wireshark can see for the Attach, for example.</p><p>With a fair amount of effort and my passable Perl background I've got a per-protocol tracer that supports just about anything out of the EPC, GPRS or IMS worlds. It's funny you mention ISUP, as that is probably the most challenging due to the nature of CICs and their reuse in multi-streaming Sigtran links.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '14, 21:33</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jun '14, 21:35</p></div></div><div id="comments-container-34146" class="comments-container"></div><div id="comment-tools-34146" class="comment-tools"></div><div class="clear"></div><div id="comment-34146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

