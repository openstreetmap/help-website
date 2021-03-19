+++
type = "question"
title = "Tshark - average time"
description = '''I have a large pcap file with a lot of Solicit, advertise, request and reply packets. I would like to calculate average time of address assignment. In this file is for example 100000 solicit packets but only 50000 reply packets - so only 50000 address is assigned. Is it possible to count average tim...'''
date = "2015-12-30T15:40:00Z"
lastmod = "2015-12-30T15:40:00Z"
weight = 48764
keywords = [ "tshark" ]
aliases = [ "/questions/48764" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark - average time](/questions/48764/tshark-average-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48764-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a large pcap file with a lot of Solicit, advertise, request and reply packets. I would like to calculate average time of address assignment. In this file is for example 100000 solicit packets but only 50000 reply packets - so only 50000 address is assigned. Is it possible to count average time of real address assignments? I have tried with: tshark -n -q -z 'io,stat,0,AVG(frame.time_relative)frame.time_relative' but with no effect.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Dec '15, 15:40</strong></p><img src="https://secure.gravatar.com/avatar/5a74bb5e2a46cd343fd29fc5fa2b182b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="razz9&#39;s gravatar image" /><p>razz9<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="razz9 has no accepted answers">0%</span></p></div></div><div id="comments-container-48764" class="comments-container"><span id="49026"></span><div id="comment-49026" class="comment"><div id="post-49026-score" class="comment-score"></div><div class="comment-text"><p>can you please define what you mean by "address assignments" and "real address assignments" ?</p></div><div id="comment-49026-info" class="comment-info"><span class="comment-age">(09 Jan '16, 12:18)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-48764" class="comment-tools"></div><div class="clear"></div><div id="comment-48764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

