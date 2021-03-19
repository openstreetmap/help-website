+++
type = "question"
title = "Within the scope of a Wireshark dissector, Is it possible to detect out order sequence ids (based on arrival time) in PTP V2?"
description = '''Is it possible to detect out order sequence ids (based on arrival time) in PTP V2?  This would be for both file open and streaming pcaps, and the ordering would also be based on packets that share a &quot;flow&quot; direction (based on the &quot;class&quot; of message_id they belong too as well. I am attempting to do t...'''
date = "2012-02-15T22:00:00Z"
lastmod = "2012-02-15T22:00:00Z"
weight = 9051
keywords = [ "ptp", "storing", "sequence_id", "dissector", "tvb" ]
aliases = [ "/questions/9051" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Within the scope of a Wireshark dissector, Is it possible to detect out order sequence ids (based on arrival time) in PTP V2?](/questions/9051/within-the-scope-of-a-wireshark-dissector-is-it-possible-to-detect-out-order-sequence-ids-based-on-arrival-time-in-ptp-v2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9051-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to detect out order sequence ids (based on arrival time) in PTP V2?</p><p>This would be for both file open and streaming pcaps, and the ordering would also be based on packets that share a "flow" direction (based on the "class" of message_id they belong too as well. I am attempting to do this at the PTP dissector level, but due to overall design philosophy of the role of a dissector, I am not sure detecting sequence id discontinuity at the dissector level is even possible. My current approach is two stored the needed info for each packet in message_id grouped sets of linked lists that can are sorted by arrival time and then waked through to check for discontinuity in the seq_ids.</p></div><div id="question-tags" class="tags-container tags">ptp storing sequence_id dissector tvb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '12, 22:00</strong></p><img src="https://secure.gravatar.com/avatar/9da2e9fc67b04d5827f0413c73612df3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wintermut3&#39;s gravatar image" /><p>wintermut3<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wintermut3 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Feb '12, 05:34</p></div></div><div id="comments-container-9051" class="comments-container"></div><div id="comment-tools-9051" class="comment-tools"></div><div class="clear"></div><div id="comment-9051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

