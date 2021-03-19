+++
type = "question"
title = "Need to get RTP sequence number from payload dissector"
description = '''I have written a Lua payload dissector for a dynamic RTP payload (https://github.com/FOXNEOAdvancedTechnology/RFC4175-dissector) However now I would like to get access to the RTP sequence number (rtp.seq) of the RTP packet where my payload lives, but do so inside my payload dissector (the RTP sequen...'''
date = "2015-11-24T15:09:00Z"
lastmod = "2015-11-24T15:09:00Z"
weight = 47943
keywords = [ "lua", "dissector", "rtp" ]
aliases = [ "/questions/47943" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need to get RTP sequence number from payload dissector](/questions/47943/need-to-get-rtp-sequence-number-from-payload-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47943-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have written a Lua payload dissector for a dynamic RTP payload (<a href="https://github.com/FOXNEOAdvancedTechnology/RFC4175-dissector)">https://github.com/FOXNEOAdvancedTechnology/RFC4175-dissector)</a></p><p>However now I would like to get access to the RTP sequence number (rtp.seq) of the RTP packet where my payload lives, but do so inside my payload dissector (the RTP sequence number needs to be added to an "extended sequence number" in the payload for display in the dissector).</p><p>How can you do this? Thanks!</p></div><div id="question-tags" class="tags-container tags">lua dissector rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '15, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/37eb6eae4d4dc6defa77e80c8a86959e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mpeg2tom&#39;s gravatar image" /><p>mpeg2tom<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mpeg2tom has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Nov '15, 15:10</p></div></div><div id="comments-container-47943" class="comments-container"></div><div id="comment-tools-47943" class="comment-tools"></div><div class="clear"></div><div id="comment-47943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

