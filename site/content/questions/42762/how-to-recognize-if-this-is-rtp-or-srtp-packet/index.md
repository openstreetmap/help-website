+++
type = "question"
title = "how to recognize if this is RTP or SRTP packet ?"
description = '''I have two captured files, taken in different scenario. One of them - when I perform : &quot;Decode as&quot; to the UDP packets it shows unknown packet type 3. I suppose this may be the SRTP packet stream. But in another capture, all SIP packets are encrypted and &quot;Try to dissect RTP packets from decode outsid...'''
date = "2015-05-30T08:12:00Z"
lastmod = "2015-06-11T04:46:00Z"
weight = 42762
keywords = [ "encryption", "srtp", "rtp" ]
aliases = [ "/questions/42762" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to recognize if this is RTP or SRTP packet ?](/questions/42762/how-to-recognize-if-this-is-rtp-or-srtp-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42762-score" class="post-score" title="current number of votes">0</div><span id="post-42762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two captured files, taken in different scenario. One of them - when I perform : "Decode as" to the UDP packets it shows unknown packet type 3. I suppose this may be the SRTP packet stream. But in another capture, all SIP packets are encrypted and "Try to dissect RTP packets from decode outside conversation" gives the RTP packets with dynamic payload type 108, SSRC and time. My understanding is if wireshark can dissect RTP packets and see its heading, it should be unencrypted RTP packets.Can anybody please suggest me if I am wrong ? Or is there any possibility that even if wireshark can show the RTP headings, this RTP packet still can be encrypted ??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encryption" rel="tag" title="see questions tagged &#39;encryption&#39;">encryption</span> <span class="post-tag tag-link-srtp" rel="tag" title="see questions tagged &#39;srtp&#39;">srtp</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '15, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/4ec917e3556fb6d9c03cc0e39ec7732a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shas&#39;s gravatar image" /><p><span>Shas</span><br />
<span class="score" title="1 reputation points">1</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shas has no accepted answers">0%</span></p></div></div><div id="comments-container-42762" class="comments-container"><span id="42763"></span><div id="comment-42763" class="comment"><div id="post-42763-score" class="comment-score"></div><div class="comment-text"><p>can you provide the capture file? It's hard to follow your description without it.</p></div><div id="comment-42763-info" class="comment-info"><span class="comment-age">(30 May '15, 08:42)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="42764"></span><div id="comment-42764" class="comment"><div id="post-42764-score" class="comment-score"></div><div class="comment-text"><p>this is the capture file, which i assume is not encrypted. <a href="https://www.cloudshark.org/captures/3d0876f70a45">https://www.cloudshark.org/captures/3d0876f70a45</a></p></div><div id="comment-42764-info" class="comment-info"><span class="comment-age">(30 May '15, 09:01)</span> <span class="comment-user userinfo">Shas</span></div></div><span id="43072"></span><div id="comment-43072" class="comment"><div id="post-43072-score" class="comment-score"></div><div class="comment-text"><p>Actually you cannot differentiate between srtp and rtp packets as they have the exact same headers.So even if the packet is encrypted the header is not. so you will still see them as rtp packets in wireshark!</p></div><div id="comment-43072-info" class="comment-info"><span class="comment-age">(11 Jun '15, 04:46)</span> <span class="comment-user userinfo">koundi</span></div></div></div><div id="comment-tools-42762" class="comment-tools"></div><div class="clear"></div><div id="comment-42762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

