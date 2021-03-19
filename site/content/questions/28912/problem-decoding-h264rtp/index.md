+++
type = "question"
title = "problem decoding h264/RTP"
description = '''I am trying to analyse a problem with H264 data over RTP when using FU-A fragmentation. Sometimes wireshark can decode the first 3 fields in the packets and sometimes it can&#x27;t. I think that the problem is likely in my data, not wireshark because all of the h264 packets in a given file with either de...'''
date = "2014-01-15T07:02:00Z"
lastmod = "2014-01-15T07:02:00Z"
weight = 28912
keywords = [ "h264_decode" ]
aliases = [ "/questions/28912" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [problem decoding h264/RTP](/questions/28912/problem-decoding-h264rtp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28912-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to analyse a problem with H264 data over RTP when using FU-A fragmentation. Sometimes wireshark can decode the first 3 fields in the packets and sometimes it can't. I think that the problem is likely in my data, not wireshark because all of the h264 packets in a given file with either decode or not. I have manually decoded several of the fields in packets that fail to decode and they seem correct. How can I track down the origin of this problem?</p><p>Thank you, Chuck Crisler</p></div><div id="question-tags" class="tags-container tags">h264_decode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '14, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/92841c0f34c63e535d2d6eb7a212c9e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChuckCrisler&#39;s gravatar image" /><p>ChuckCrisler<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChuckCrisler has no accepted answers">0%</span></p></div></div><div id="comments-container-28912" class="comments-container"><span id="28918"></span><div id="comment-28918" class="comment"><div id="post-28918-score" class="comment-score"></div><div class="comment-text"><p>Hi, Wireshark does not do H.264 reasembly so it's not unlikly that it's a Wireshark bug. As far as I remember wireshark should not try to dissect h.264 unless it starts with a NAL unit identifier or somthing like that. You could open a bug report and attach a sall sample trace.</p></div><div id="comment-28918-info" class="comment-info"><span class="comment-age">(15 Jan '14, 07:15)</span> Anders ♦</div></div></div><div id="comment-tools-28912" class="comment-tools"></div><div class="clear"></div><div id="comment-28912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

