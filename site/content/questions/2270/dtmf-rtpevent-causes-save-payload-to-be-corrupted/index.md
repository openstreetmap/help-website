+++
type = "question"
title = "DTMF RTPEVENT causes Save Payload to be corrupted"
description = '''Analysing G729 RTP Stream where there are RTPEVENT frames for DTMF signalling. After extracting RTP using Analyse &amp;gt; Save Payload and converting to .au with normal method, found that with the start of the first DTMF digit, the converted audio is &quot;wonkey&quot;. Sounds like cross-talk from many, many con...'''
date = "2011-02-10T06:57:00Z"
lastmod = "2011-02-10T09:02:00Z"
weight = 2270
keywords = [ "g729", "rtp", "dtmf" ]
aliases = [ "/questions/2270" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [DTMF RTPEVENT causes Save Payload to be corrupted](/questions/2270/dtmf-rtpevent-causes-save-payload-to-be-corrupted)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2270-score" class="post-score" title="current number of votes">0</div><span id="post-2270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Analysing G729 RTP Stream where there are RTPEVENT frames for DTMF signalling. After extracting RTP using Analyse &gt; Save Payload and converting to .au with normal method, found that with the start of the first DTMF digit, the converted audio is "wonkey". Sounds like cross-talk from many, many conversations. Can hear pulses corresponding to DTFM entry.</p><p>If I manually strip the RTPEVENT frames from the pcap before processing as above - all is well.</p><p>Using another tool (Voipmonitor) to convert original pcap to .raw there is no problem with te extracted audio.</p><p>Seems that presense of the RTPEVENT packet is confusing the stream analysis process. Am I doing something wrong?</p><p>Thanks, John</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-g729" rel="tag" title="see questions tagged &#39;g729&#39;">g729</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-dtmf" rel="tag" title="see questions tagged &#39;dtmf&#39;">dtmf</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '11, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/40c4c54f4be3979e96c0da457da61ec4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnrcampbell&#39;s gravatar image" /><p><span>johnrcampbell</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnrcampbell has no accepted answers">0%</span></p></div></div><div id="comments-container-2270" class="comments-container"></div><div id="comment-tools-2270" class="comment-tools"></div><div class="clear"></div><div id="comment-2270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2272"></span>

<div id="answer-container-2272" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2272-score" class="post-score" title="current number of votes">0</div><span id="post-2272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's little you're doing wrong. Wireshark is really tailored to continues PCM A/u-law stream. All the 'fancy' Video, RTP Event, VAD/CN packets disrupt this process.</p><p>Is this feature open for improvement? Yes. There's just no one willing/able to invest the time to improve this difficult peace of code.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '11, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2272" class="comments-container"></div><div id="comment-tools-2272" class="comment-tools"></div><div class="clear"></div><div id="comment-2272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

