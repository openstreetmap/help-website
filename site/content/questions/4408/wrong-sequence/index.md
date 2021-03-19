+++
type = "question"
title = "wrong sequence"
description = '''Hi,  I am new in using Wireshark. I am capturing VoIP calls and I was wondering what happens to the Wrong sequnce packets. Are they dropped at the receiver&#x27;s end? Are they calculated as part of the lost packets percentage? thank you in advance'''
date = "2011-06-06T08:41:00Z"
lastmod = "2011-06-10T08:20:00Z"
weight = 4408
keywords = [ "wrong", "packets", "rtp", "lost", "sequence" ]
aliases = [ "/questions/4408" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wrong sequence](/questions/4408/wrong-sequence)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4408-score" class="post-score" title="current number of votes">0</div><span id="post-4408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am new in using Wireshark. I am capturing VoIP calls and I was wondering what happens to the Wrong sequnce packets. Are they dropped at the receiver's end? Are they calculated as part of the lost packets percentage? thank you in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wrong" rel="tag" title="see questions tagged &#39;wrong&#39;">wrong</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-lost" rel="tag" title="see questions tagged &#39;lost&#39;">lost</span> <span class="post-tag tag-link-sequence" rel="tag" title="see questions tagged &#39;sequence&#39;">sequence</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '11, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/510e2d19e5cf4596d2afb59467c68c6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lefkothea%20Vaitsi&#39;s gravatar image" /><p><span>Lefkothea Va...</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lefkothea Vaitsi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jun '11, 16:58</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4408" class="comments-container"></div><div id="comment-tools-4408" class="comment-tools"></div><div class="clear"></div><div id="comment-4408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4413"></span>

<div id="answer-container-4413" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4413-score" class="post-score" title="current number of votes">3</div><span id="post-4413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The nature of RTP transport over UDP is inherently unreliable. Unreliable for delivery and order. So, wrong sequence numbers are to be expected at the receiver side. For media playout the RTP packets have to be placed in order again in the jitter buffer and the payloads accessed in that order. Therefore Wronng Sequence != Lost Packet.</p><p>You should study <a href="http://www.cs.columbia.edu/~hgs/rtp/faq.html">Some Frequently Asked Questions about RTP</a>, a really informative page.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '11, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4413" class="comments-container"><span id="4421"></span><div id="comment-4421" class="comment"><div id="post-4421-score" class="comment-score"></div><div class="comment-text"><p>Hi again, thanks for the answer, the FAQs are really helpful. Let me see if I got it right now. The lost packets percentage are those that never reached the receiver while the wrong sequence packets are lost as well due to the jitter buffer handling. For example if in a call I have total packets=3115, lost=117, seq errors=140 that means only 2858 packets were played at the receiver, 117 were lost on their way there and 140 were lost after reached the receiver. Is that right? Thanks and sorry for being such a pain.</p></div><div id="comment-4421-info" class="comment-info"><span class="comment-age">(07 Jun '11, 03:05)</span> <span class="comment-user userinfo">Lefkothea Va...</span></div></div></div><div id="comment-tools-4413" class="comment-tools"></div><div class="clear"></div><div id="comment-4413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4423"></span>

<div id="answer-container-4423" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4423-score" class="post-score" title="current number of votes">1</div><span id="post-4423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Once they reach the receiver they are not lost, they're there! It's only that they are received in an unexpected order. Whether they are in time for playout is a whole different matter. That depends on how large the jitter buffer is.</p><p>Let say packet size is 20ms, jitter buffer is 20ms. The packets are received as such:</p><ol><li>Rx_time=0, seq=0, RTP_ts=0</li><li>Rx_time=20, seq=1, RTP_ts=20</li></ol><p>All is fine.</p><ol><li>Rx_time=40, seq=2, RTP_ts=40</li><li>Rx_time=57, seq=4, RTP_ts=80</li><li>Rx_time=60, seq=3, RTP_ts=60</li><li>Rx_time=100, seq=5, RTP_ts=100</li></ol><p>Here you see that RTP packet sequence number 4 overtook RTP packet sequence number 3 during transport, but is early enough at the receiver for playout. So this one is counted as sequence error, but cannot be considered lost or too late.</p><p>Lets continue.</p><ol><li>Rx_time=120, seq=6, RTP_ts=120</li><li>Rx_time=160, seq=8, RTP_ts=160</li><li>Rx_time=180, seq=9, RTP_ts=180</li><li>Rx_time=190, seq=7, RTP_ts=140</li></ol><p>Now RTP packet sequence number 7 is late. Assuming the Rx_time is the same timebase as used for the jitter buffer, you can see that RTP_ts + jitter buffer size &lt; Rx_time for RTP packet sequence number 7. Therefore it is too late for playout. So this one is counted as sequence error, but cannot be considered lost, only too late.</p><p>The notion of 'too late' depends on the intelligence of the (usually adaptive) jitter buffer in the receiver. Since Wireshark it just a Man-in-the-Middle it cannot make that determination.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '11, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4423" class="comments-container"><span id="4504"></span><div id="comment-4504" class="comment"><div id="post-4504-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer it is clear now. However, what confuses me is the Rx_time. I presume that the RTP_ts(time stamp)is the one I can see in the RTP stream analysis. thank you</p></div><div id="comment-4504-info" class="comment-info"><span class="comment-age">(10 Jun '11, 08:20)</span> <span class="comment-user userinfo">Lefkothea Va...</span></div></div></div><div id="comment-tools-4423" class="comment-tools"></div><div class="clear"></div><div id="comment-4423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

