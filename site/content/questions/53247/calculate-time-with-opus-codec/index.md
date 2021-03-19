+++
type = "question"
title = "Calculate time with Opus codec"
description = '''Hello i have captured some RTP traffic and I can see using Wireshark that the codec used is Opus. And from the SDP it should use a sample rate of 48000 Hz. Now the problem. If I have an RTP timestamp value, is 1/48000 its timestamp unit? I have problems while calculating the jitter. According to the...'''
date = "2016-06-06T10:40:00Z"
lastmod = "2016-06-08T08:05:00Z"
weight = 53247
keywords = [ "sample", "opus", "clock", "rtp", "wireshark" ]
aliases = [ "/questions/53247" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Calculate time with Opus codec](/questions/53247/calculate-time-with-opus-codec)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53247-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53247-score" class="post-score" title="current number of votes">0</div><span id="post-53247-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>i have captured some RTP traffic and I can see using Wireshark that the codec used is Opus. And from the SDP it should use a sample rate of 48000 Hz. Now the problem. If I have an RTP timestamp value, is 1/48000 its timestamp unit? I have problems while calculating the jitter. According to the RTP statistics tab, the value should be around 3 ms. With a max of 9.</p><p>I use the formula D = (Ri - Rj) - (Si - Sj) and multiplie the timestamp value with 1/48000 sec for Si and Sj. Is that wrong?</p><p>Hope you could help me</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sample" rel="tag" title="see questions tagged &#39;sample&#39;">sample</span> <span class="post-tag tag-link-opus" rel="tag" title="see questions tagged &#39;opus&#39;">opus</span> <span class="post-tag tag-link-clock" rel="tag" title="see questions tagged &#39;clock&#39;">clock</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '16, 10:40</strong></p><img src="https://secure.gravatar.com/avatar/9057d9972c7dbd2019d1785547a0e146?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Haumea&#39;s gravatar image" /><p><span>Haumea</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Haumea has no accepted answers">0%</span></p></div></div><div id="comments-container-53247" class="comments-container"></div><div id="comment-tools-53247" class="comment-tools"></div><div class="clear"></div><div id="comment-53247-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53250"></span>

<div id="answer-container-53250" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53250-score" class="post-score" title="current number of votes">1</div><span id="post-53250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Haumea has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The timestamp unit should normally be <code>1/(sample rate from SDP)</code> (in seconds) as you expect. You can check that the implementation you capture is correct by taking frames i and j far enough from each other (like 50 packets or more), calculating the difference of RTP timestamps between them, and dividing the value by 48000. If the implementation is correct, the result you get should almost match the difference of frame (capture) timestamps which are expressed in seconds and their decimal fractions. If these two values differ by order of magnitude, something is wrong.</p><p>But I don't understand what is the actual problem, do you disagree with the jitter values as calculated by Wireshark?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '16, 12:31</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-53250" class="comments-container"><span id="53263"></span><div id="comment-53263" class="comment"><div id="post-53263-score" class="comment-score"></div><div class="comment-text"><p>I did some errors during calculation! I got two values that differed by order of magnitude! Thanks!</p></div><div id="comment-53263-info" class="comment-info"><span class="comment-age">(07 Jun '16, 01:50)</span> <span class="comment-user userinfo">Haumea</span></div></div><span id="53277"></span><div id="comment-53277" class="comment"><div id="post-53277-score" class="comment-score"></div><div class="comment-text"><p>Has the rate rtp packets come at to do with the bandwidth the implementation has? I got a rate of 0.08 ms, which corresponds to a 12KHz band (1/12000*1000). Is it correct?</p></div><div id="comment-53277-info" class="comment-info"><span class="comment-age">(07 Jun '16, 06:17)</span> <span class="comment-user userinfo">Haumea</span></div></div><span id="53282"></span><div id="comment-53282" class="comment"><div id="post-53282-score" class="comment-score"></div><div class="comment-text"><p>As it my originally comment came out to actually be an Answer, I've converted it as such. If it has answered your Question, please accept it by clicking the checkmark icon next to the Answer.</p><p>To your additional question, what bandwidth do you talk about, the audio one or the network one?</p><p>Just a remark first, the value you have stated (0,08 ms) seems to be a rounded value of 1/48000 kHz, i.e. not time between packets but duration represented by a single sample.</p><p>Opus is a compressing codec which may use constant packet rate but uses a variable bit rate - e.g. you may see that the packets' RTP timestamps are always 20 ms = 960 "samples" apart but their size varies. BTW, you need a specific post-process to extract the audio from the RTP capture, as you need to convey to the Opus decoder the information about packet borders which is not part of its bit stream itself.</p><p>As for the audio bandwidth, Shannon-Kotelnik's theorem says that the maximum frequency which can be sampled safely is 1/2 of the sampling rate, which means 0-24 kHz (not 12) theoretical audio bandwidth in case of 48 kHz sampling rate. But the trouble with Opus is that it dynamically changes even the sampling rate, so the 48000 is stated in the SDP solely for the purpose of scaling the RTP timestamps and does not express the actual sampling rate used.</p><p>You can determine the audio bandwidth from packet rate only for codecs whose compression ratio is constant and known and which compress the input signal regardless what it actually is. E. g. PCMA compresses each original (11-bit) sample into one byte, so if you have 160 bytes of payload every 20 milliseconds, you know that there are 8000 samples/second so the audio bandwidth is 0-4 kHz. But already with G.729, which also has a constant bit rate, you cannot really talk about audio bandwidth because it is a speech-optimized codec and it doesn't transmit an image of the full frequency spectrum.</p></div><div id="comment-53282-info" class="comment-info"><span class="comment-age">(07 Jun '16, 07:12)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="53318"></span><div id="comment-53318" class="comment"><div id="post-53318-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot!</p></div><div id="comment-53318-info" class="comment-info"><span class="comment-age">(08 Jun '16, 08:05)</span> <span class="comment-user userinfo">Haumea</span></div></div></div><div id="comment-tools-53250" class="comment-tools"></div><div class="clear"></div><div id="comment-53250-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

