+++
type = "question"
title = "802.11 Block ACK and the Radiotap Header"
description = '''While monitoring Block ACK operation, when I capture a block of QoS data packets, the Radiotap Header for the first data packet of the block includes a normal MAC timestamp and RSSI value of 0. The second data packet of the block indicates a MAC timestamp of 0 and an RSSI value of 0. The third and f...'''
date = "2011-12-22T16:30:00Z"
lastmod = "2011-12-22T16:30:00Z"
weight = 8091
keywords = [ "blockack" ]
aliases = [ "/questions/8091" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [802.11 Block ACK and the Radiotap Header](/questions/8091/80211-block-ack-and-the-radiotap-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8091-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>While monitoring Block ACK operation, when I capture a block of QoS data packets, the Radiotap Header for the first data packet of the block includes a normal MAC timestamp and RSSI value of 0. The second data packet of the block indicates a MAC timestamp of 0 and an RSSI value of 0. The third and final data packet of the block indicates a MAC timestamp of 0 and a normal RSSI value. I have two theories. My first theory, regarding the MAC timestamp, is that the MAC receives the entire block of packets together (in response to some triggering event) and thus the sole MAC timestamp denotes the time at which all of the packets have been presented to the MAC. Such MAC timestamp is then only included in the Radiotap Header of the first packet. My second theory, regarding the RSSI, is that only one RSSI value is captured for the entire block of data packets, and such RSSI value is only included in the Radiotap Header of the last packet. Can anyone out there critique my theories?</p></div><div id="question-tags" class="tags-container tags">blockack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '11, 16:30</strong></p><img src="https://secure.gravatar.com/avatar/02cf4ed95be4ca7470e1bd5ed538c62d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="S_P&#39;s gravatar image" /><p>S_P<br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="S_P has no accepted answers">0%</span></p></div></div><div id="comments-container-8091" class="comments-container"><span id="8104"></span><div id="comment-8104" class="comment"><div id="post-8104-score" class="comment-score"></div><div class="comment-text"><p>Are you seeing the block ACK after aggregated data frames or after regular ones ?</p></div><div id="comment-8104-info" class="comment-info"><span class="comment-age">(23 Dec '11, 01:08)</span> Landi</div></div><span id="8143"></span><div id="comment-8143" class="comment"><div id="post-8143-score" class="comment-score"></div><div class="comment-text"><p>Not sure. Is there a flag in the data frames that indicate this? Are you referring to A-MPDU operation?</p></div><div id="comment-8143-info" class="comment-info"><span class="comment-age">(27 Dec '11, 11:46)</span> S_P</div></div><span id="8152"></span><div id="comment-8152" class="comment"><div id="post-8152-score" class="comment-score"></div><div class="comment-text"><p>Kind of because I'm not sure if radiotap headers get confused with aggregated data, but to say that very clear - that's just a <em>guess</em> I have !</p></div><div id="comment-8152-info" class="comment-info"><span class="comment-age">(28 Dec '11, 07:40)</span> Landi</div></div></div><div id="comment-tools-8091" class="comment-tools"></div><div class="clear"></div><div id="comment-8091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

