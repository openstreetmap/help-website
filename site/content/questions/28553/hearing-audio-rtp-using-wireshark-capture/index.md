+++
type = "question"
title = "Hearing audio (RTP) using Wireshark capture."
description = '''I already have wireshark trace files that include SIP for messaging and also the RTP packets. What option / setting should I turn ON, to hear the audio stream?'''
date = "2014-01-03T09:06:00Z"
lastmod = "2014-01-03T10:27:00Z"
weight = 28553
keywords = [ "audio" ]
aliases = [ "/questions/28553" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Hearing audio (RTP) using Wireshark capture.](/questions/28553/hearing-audio-rtp-using-wireshark-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28553-score" class="post-score" title="current number of votes">0</div><span id="post-28553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I already have wireshark trace files that include SIP for messaging and also the RTP packets. What option / setting should I turn ON, to hear the audio stream?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-audio" rel="tag" title="see questions tagged &#39;audio&#39;">audio</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jan '14, 09:06</strong></p><img src="https://secure.gravatar.com/avatar/26e0c8fa62c201911914f120a35c55ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VeeGee&#39;s gravatar image" /><p><span>VeeGee</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VeeGee has no accepted answers">0%</span></p></div></div><div id="comments-container-28553" class="comments-container"></div><div id="comment-tools-28553" class="comment-tools"></div><div class="clear"></div><div id="comment-28553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28554"></span>

<div id="answer-container-28554" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28554-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28554-score" class="post-score" title="current number of votes">0</div><span id="post-28554-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With the trace file loaded, go to Telephony -&gt; RTP -&gt; Stream Analysis. Pick the stream you want to hear and hit Player.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '14, 09:49</strong></p><img src="https://secure.gravatar.com/avatar/30cc5fc9359f635b56982b7b85d2cc62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sblar1&#39;s gravatar image" /><p><span>sblar1</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sblar1 has no accepted answers">0%</span></p></div></div><div id="comments-container-28554" class="comments-container"></div><div id="comment-tools-28554" class="comment-tools"></div><div class="clear"></div><div id="comment-28554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28556"></span>

<div id="answer-container-28556" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28556-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28556-score" class="post-score" title="current number of votes">0</div><span id="post-28556-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark will not playback G729 out of the box. to decode G729 follow this link <a href="http://wiki.wireshark.org/HowToDecodeG729">How to Decode G729</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '14, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/94630d1ea1108afeafb344e884044d15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Boaz%20Galil&#39;s gravatar image" /><p><span>Boaz Galil</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Boaz Galil has no accepted answers">0%</span></p></div></div><div id="comments-container-28556" class="comments-container"></div><div id="comment-tools-28556" class="comment-tools"></div><div class="clear"></div><div id="comment-28556-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

