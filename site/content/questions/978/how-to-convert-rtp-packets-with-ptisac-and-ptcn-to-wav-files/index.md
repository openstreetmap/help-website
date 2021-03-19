+++
type = "question"
title = "How to convert RTP packets with PT=ISAC and PT=CN to .wav files?"
description = '''Hi,all, I&#x27;m capturing telephony call packets between two endpoints. In my captured packets, there are RTP packets with payload type PT=PCMA, ISAC and CN(What is CN? what kind of codec?) I know how to save packets with PT=PCMA to .au files. However, when it comes to ISAC and CN, I have no idea how to...'''
date = "2010-11-16T16:26:00Z"
lastmod = "2010-11-16T17:29:00Z"
weight = 978
keywords = [ "format", "audio", "isac", "rtp", ".au" ]
aliases = [ "/questions/978" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to convert RTP packets with PT=ISAC and PT=CN to .wav files?](/questions/978/how-to-convert-rtp-packets-with-ptisac-and-ptcn-to-wav-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-978-score" class="post-score" title="current number of votes">0</div><span id="post-978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,all, I'm capturing telephony call packets between two endpoints. In my captured packets, there are RTP packets with payload type PT=PCMA, ISAC and CN(What is CN? what kind of codec?) I know how to save packets with PT=PCMA to .au files. However, when it comes to ISAC and CN, I have no idea how to convert them to .au or .wav files? Do you have any idea on this?　Thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-format" rel="tag" title="see questions tagged &#39;format&#39;">format</span> <span class="post-tag tag-link-audio" rel="tag" title="see questions tagged &#39;audio&#39;">audio</span> <span class="post-tag tag-link-isac" rel="tag" title="see questions tagged &#39;isac&#39;">isac</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-.au" rel="tag" title="see questions tagged &#39;.au&#39;">.au</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '10, 16:26</strong></p><img src="https://secure.gravatar.com/avatar/2edef74a36aba8b70b94d9885864e7b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="esolve&#39;s gravatar image" /><p><span>esolve</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="esolve has no accepted answers">0%</span></p></div></div><div id="comments-container-978" class="comments-container"></div><div id="comment-tools-978" class="comment-tools"></div><div class="clear"></div><div id="comment-978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="979"></span>

<div id="answer-container-979" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-979-score" class="post-score" title="current number of votes">1</div><span id="post-979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>ISAC is a GIPS codec; see <a href="http://www.gipscorp.com/">http://www.gipscorp.com/</a> for details. CN is the "comfort noise" payload described in RFC 3389; as I understand it, it's used by several protocols.</p><p>I don't know of a save-to-au facility for the ISAC codec. Wireshark's save-to-au facility only works for the G.711 codec.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '10, 17:29</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-979" class="comments-container"></div><div id="comment-tools-979" class="comment-tools"></div><div class="clear"></div><div id="comment-979-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

