+++
type = "question"
title = "rtp audio stream - no min / max values in statistics"
description = '''Hello, I looking to stream RTP Video / Audio through some WLAN access point to measure the network stability. VLC acts as streaming server and client on each respective side and the audio content is fine on the client side.  But for any reason I dont see the min / max values in the RTP Stream Analys...'''
date = "2015-12-10T03:12:00Z"
lastmod = "2015-12-14T03:12:00Z"
weight = 48416
keywords = [ "rtp_statistics" ]
aliases = [ "/questions/48416" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [rtp audio stream - no min / max values in statistics](/questions/48416/rtp-audio-stream-no-min-max-values-in-statistics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48416-score" class="post-score" title="current number of votes">0</div><span id="post-48416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I looking to stream RTP Video / Audio through some WLAN access point to measure the network stability. VLC acts as streaming server and client on each respective side and the audio content is fine on the client side. But for any reason I dont see the min / max values in the RTP Stream Analysis of Wireshark. Even if have for each packet values for delta, jitter and skew.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/rtp-stream-analysis_1MgRGgH.PNG" alt="alt text" /></p><p>The results are the same using wireshark 1.x or 2.0</p><p>The capture contains the whole RTSP and RTP exchanges.</p><p>any idea about what is going on or what I'm not aware of ?</p><p>Regards David</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp_statistics" rel="tag" title="see questions tagged &#39;rtp_statistics&#39;">rtp_statistics</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '15, 03:12</strong></p><img src="https://secure.gravatar.com/avatar/c696827e1368b7e6661001c2f0fc4d21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stroumpf&#39;s gravatar image" /><p><span>stroumpf</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stroumpf has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Dec '15, 00:24</strong> </span></p></div></div><div id="comments-container-48416" class="comments-container"><span id="48478"></span><div id="comment-48478" class="comment"><div id="post-48478-score" class="comment-score"></div><div class="comment-text"><p>Min/max values of what? Jitter? Can you post the capture so that we know what you are talking about?</p></div><div id="comment-48478-info" class="comment-info"><span class="comment-age">(12 Dec '15, 11:55)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-48416" class="comment-tools"></div><div class="clear"></div><div id="comment-48416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48501"></span>

<div id="answer-container-48501" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48501-score" class="post-score" title="current number of votes">0</div><span id="post-48501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Put this way it looks like a bug to me.</p><p>Please file a bug at <a href="https://bugs.wireshark.org/bugzilla/enter_bug.cgi">bugzilla</a> if you can attach your capture file to it. If privacy reasons prevent you from doing so, there is little point in opening the bug, as it will not be reproducible without the capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '15, 00:55</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48501" class="comments-container"><span id="48505"></span><div id="comment-48505" class="comment"><div id="post-48505-score" class="comment-score"></div><div class="comment-text"><p>Note that if a bug (or attachment) is marked as "Private" it will only be accessible to the submitter and the Wireshark Core Developers.</p></div><div id="comment-48505-info" class="comment-info"><span class="comment-age">(14 Dec '15, 03:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-48501" class="comment-tools"></div><div class="clear"></div><div id="comment-48501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

