+++
type = "question"
title = "Listening to EVRC-B UDP/RTP stream"
description = '''Hi,  I captured a UDP stream that was created using an EVRC-B codec and I would like to play it back so I am able to here the audio. Is there a way on how to accomplish this either using wireshark or a another program along with wireshark? Thank you,  Mike W. '''
date = "2015-01-09T12:54:00Z"
lastmod = "2015-01-10T04:43:00Z"
weight = 39010
keywords = [ "udp", "codec", "evrc", "rtp", "stream" ]
aliases = [ "/questions/39010" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Listening to EVRC-B UDP/RTP stream](/questions/39010/listening-to-evrc-b-udprtp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39010-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I captured a UDP stream that was created using an EVRC-B codec and I would like to play it back so I am able to here the audio. Is there a way on how to accomplish this either using wireshark or a another program along with wireshark?</p><p>Thank you,</p><p>Mike W.</p></div><div id="question-tags" class="tags-container tags">udp codec evrc rtp stream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jan '15, 12:54</strong></p><img src="https://secure.gravatar.com/avatar/0d68cf7461c4472391aee7e45f486d80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mike7seven&#39;s gravatar image" /><p>mike7seven<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mike7seven has no accepted answers">0%</span></p></div></div><div id="comments-container-39010" class="comments-container"></div><div id="comment-tools-39010" class="comment-tools"></div><div class="clear"></div><div id="comment-39010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39019"></span>

<div id="answer-container-39019" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39019-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please read my answer to a similar question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/26222/how-to-play-rtp-payload-which-is-in-amr-codec">https://ask.wireshark.org/questions/26222/how-to-play-rtp-payload-which-is-in-amr-codec</a><br />
</p></blockquote><p>Instead of AMR player, you can use <a href="https://ffmpeg.org/ffplay.html">ffplay</a>, which <a href="https://lists.mplayerhq.hu/pipermail/mplayer-users/2013-January/085890.html">"should" support EVRC</a>. If <strong>ffplay</strong> does not work in your environment or is not what you are looking for, please google a working EVRC player yourself ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '15, 04:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jan '15, 04:43</p></div></div><div id="comments-container-39019" class="comments-container"><span id="39085"></span><div id="comment-39085" class="comment"><div id="post-39085-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><p>I wish I could tell you that this solved what I am attempting to complete, but it didn't. I have ffmpeg installed but I don't quite understand how I get the file to export or convert to Wireshark.</p><p>Thank you,</p><p>Mike</p></div><div id="comment-39085-info" class="comment-info"><span class="comment-age">(12 Jan '15, 13:00)</span> mike7seven</div></div></div><div id="comment-tools-39019" class="comment-tools"></div><div class="clear"></div><div id="comment-39019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

