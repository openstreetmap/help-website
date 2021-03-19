+++
type = "question"
title = "Does RTP player decode a 180 Ringing into audible ring back tone?"
description = '''Hi, The call I am tracing is supposed to use the 180 Ringing SIP message to indicate to the caller that the callee has recevied the invite, and the caller can play ring back tone to the caller&#x27;s speaker. This call should not be sending the ring back tone encoded as audio into RTP. When using the RTP...'''
date = "2013-09-12T09:12:00Z"
lastmod = "2013-09-12T21:54:00Z"
weight = 24610
keywords = [ "decode_rtp" ]
aliases = [ "/questions/24610" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Does RTP player decode a 180 Ringing into audible ring back tone?](/questions/24610/does-rtp-player-decode-a-180-ringing-into-audible-ring-back-tone)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24610-score" class="post-score" title="current number of votes">0</div><span id="post-24610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>The call I am tracing is supposed to use the 180 Ringing SIP message to indicate to the caller that the callee has recevied the invite, and the caller can play ring back tone to the caller's speaker. This call should not be sending the ring back tone encoded as audio into RTP. When using the RTP player utility to decode the call audio, the player plays out a ring back tone as part of the audio decocde.</p><p>My question is, is the RTP player seeing the 180 Ringing in the packet trace and using that to trigger ring back tone in the audio playout? Or is the RTP player just playing out what is decoded from the RTP, meaning the ring back tone was encoded as audio into RTP packets?</p><p>Thanks, Carl</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode_rtp" rel="tag" title="see questions tagged &#39;decode_rtp&#39;">decode_rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '13, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/ea854f1827686e0ba7523e9fe7d5db34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cklatsky&#39;s gravatar image" /><p><span>cklatsky</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cklatsky has no accepted answers">0%</span></p></div></div><div id="comments-container-24610" class="comments-container"></div><div id="comment-tools-24610" class="comment-tools"></div><div class="clear"></div><div id="comment-24610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24622"></span>

<div id="answer-container-24622" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24622-score" class="post-score" title="current number of votes">0</div><span id="post-24622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The audio player will not add any audio by it self. The ring back tone is normaly used as a trough connection test and is sent by the B subscriber or equipment as close to the B subscriber as possible.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '13, 21:54</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-24622" class="comments-container"></div><div id="comment-tools-24622" class="comment-tools"></div><div class="clear"></div><div id="comment-24622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

