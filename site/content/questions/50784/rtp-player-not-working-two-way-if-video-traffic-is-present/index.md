+++
type = "question"
title = "RTP player not working two way if Video traffic is present"
description = '''When attempting to use RTP player for two-way video traffic, we get only one RTP direction for the Decode to play back the RTP both audio(g711) and video (H264) . When we do it with out the video on, the two way RTP audio traffic is fine for RTP player. It seems specific to the video transmission? W...'''
date = "2016-03-09T08:51:00Z"
lastmod = "2016-03-09T08:51:00Z"
weight = 50784
keywords = [ "9300" ]
aliases = [ "/questions/50784" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RTP player not working two way if Video traffic is present](/questions/50784/rtp-player-not-working-two-way-if-video-traffic-is-present)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50784-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When attempting to use RTP player for two-way video traffic, we get only one RTP direction for the Decode to play back the RTP both audio(g711) and video (H264) . When we do it with out the video on, the two way RTP audio traffic is fine for RTP player. It seems specific to the video transmission? We are using WireShark version (Wireshark-win64-1.12.9) with SPAN ports setup on a cisco switch.</p><p>What can we do to WS to make this work for the video/camera phone traffic?</p></div><div id="question-tags" class="tags-container tags">9300</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '16, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/b1aa23239c454a4feb88388fe9ec03f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wrhuff49&#39;s gravatar image" /><p>wrhuff49<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wrhuff49 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '16, 09:39</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-50784" class="comments-container"><span id="50785"></span><div id="comment-50785" class="comment"><div id="post-50785-score" class="comment-score"></div><div class="comment-text"><p>Hard to say without seeing the capture. I could speculate that the analysis is confused by 4 RTP streams per SIP session and takes only the first two it comes across, but it is just a fast shot.</p></div><div id="comment-50785-info" class="comment-info"><span class="comment-age">(09 Mar '16, 09:28)</span> sindy</div></div></div><div id="comment-tools-50784" class="comment-tools"></div><div class="clear"></div><div id="comment-50784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

