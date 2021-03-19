+++
type = "question"
title = "Converting RTP to .au or playing - Not Taking into Account Timestamp field"
description = '''I have a capture and it appears if the Timestamp within the RTP packet is too large that correct delay between frames is not kept intact when converting to .au or when using Wireshark&#x27;s playback feature.   Normal voice does not seem to have this problem, but pre-recorded speech playback in an automa...'''
date = "2010-11-16T13:16:00Z"
lastmod = "2010-11-16T13:16:00Z"
weight = 977
keywords = [ "player", "convert", "audio", "rtp", ".au" ]
aliases = [ "/questions/977" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Converting RTP to .au or playing - Not Taking into Account Timestamp field](/questions/977/converting-rtp-to-au-or-playing-not-taking-into-account-timestamp-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-977-score" class="post-score" title="current number of votes">0</div><span id="post-977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a capture and it appears if the Timestamp within the RTP packet is too large that correct delay between frames is not kept intact when converting to .au or when using Wireshark's playback feature.<br />
</p><p>Normal voice does not seem to have this problem, but pre-recorded speech playback in an automated system seems to have this issue.<br />
</p><p>I have a small file I can share to illustrate what I'm talking about, but I have an 8second capture. Between the 2nd second and the 7th second, there is a time-gap of 4,856 ms (4.8 seconds) that the RTP stream analysis properly detects. However, when the file is converted to an .au file or the playback feature is used, the resulting audio and RTP-Player window shows the entire length as only 4 seconds long (rather than just over 8 seconds).<br />
However, the RTP graph depicts the entire 8 seconds.<br />
</p><p>Is there anyway to have Wireshark properly account for the gap in between frames using either the timestamp w/i the packets or the timestamp of the received frame?<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-player" rel="tag" title="see questions tagged &#39;player&#39;">player</span> <span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span> <span class="post-tag tag-link-audio" rel="tag" title="see questions tagged &#39;audio&#39;">audio</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-.au" rel="tag" title="see questions tagged &#39;.au&#39;">.au</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '10, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/22ab32ca924e80d6360ce02020b85f7f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TaddyOH&#39;s gravatar image" /><p><span>TaddyOH</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TaddyOH has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-977" class="comments-container"></div><div id="comment-tools-977" class="comment-tools"></div><div class="clear"></div><div id="comment-977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

