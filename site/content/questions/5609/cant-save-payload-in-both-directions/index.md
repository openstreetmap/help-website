+++
type = "question"
title = "can&#x27;t save payload in both directions"
description = '''i have the latest stable version 1.6.1 installed. i&#x27;m trying to extract audio from a VoIP call. unfortunately, i&#x27;m able to save in either forward or reversed direction but not both. when attempting to save in .au format i get the following error: &quot;can&#x27;t save in a file: saving in au format supported ...'''
date = "2011-08-09T20:36:00Z"
lastmod = "2011-08-10T01:34:00Z"
weight = 5609
keywords = [ ".raw", "payload", ".au" ]
aliases = [ "/questions/5609" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [can't save payload in both directions](/questions/5609/cant-save-payload-in-both-directions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5609-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i have the latest stable version 1.6.1 installed. i'm trying to extract audio from a VoIP call. unfortunately, i'm able to save in either forward or reversed direction but not both. when attempting to save in .au format i get the following error: "can't save in a file: saving in au format supported for alaw/ulaw streams"</p><p>when attempted to save in .raw format i get the following error: "can't save in a file: unable to save raw data in both directions"</p><p>i was previously able to save in these formats in both directions. i've seen previous posts of this error without any solutions. most of these were posts that mentioned the bug was fixed in older versions.</p><p>any suggestions?</p><p>ps - this is on windows 7</p></div><div id="question-tags" class="tags-container tags">.raw payload .au</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '11, 20:36</strong></p><img src="https://secure.gravatar.com/avatar/b828afb64c04f4697a913a269613f3f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cesto&#39;s gravatar image" /><p>cesto<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cesto has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Aug '11, 20:38</p></div></div><div id="comments-container-5609" class="comments-container"></div><div id="comment-tools-5609" class="comment-tools"></div><div class="clear"></div><div id="comment-5609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5617"></span>

<div id="answer-container-5617" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5617-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The error "can't save in a file: saving in au format supported for alaw/ulaw streams" only comes up when saving in one direction, not both.</p><p>The raw format never can save both directions.</p><p>Anyway, most likely cause is 'unclean' RTP streams, that is packet with payload type other that PCM A-law (8) or µ-law (0).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '11, 01:34</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5617" class="comments-container"><span id="5632"></span><div id="comment-5632" class="comment"><div id="post-5632-score" class="comment-score"></div><div class="comment-text"><p>Hi Jaap,</p><p>I can assure you the error comes up with I select "both" directions under .au format. Also, I have the RTP packet selected which shows G.711 pcmu (u-law).</p><p>When you say it's most likely due to an unclean RTP stream, is this from the VoIP device? Is there any adjustments I can make to avoid this error? Also, can I extract the audio from this stream that has been already capture since it plays correctly through the wireshark player?</p><p>thanks again!</p></div><div id="comment-5632-info" class="comment-info"><span class="comment-age">(10 Aug '11, 14:25)</span> cesto</div></div><span id="5636"></span><div id="comment-5636" class="comment"><div id="post-5636-score" class="comment-score"></div><div class="comment-text"><p>i misread your reply about the u-law being 0 which it is as well. here's a cut and paste of the RTP packet:</p><p>Payload type: ITU-T G.711 PCMU (0)</p><p>i'm at a loss here, i can't seem to narrow this down to a device issue or wireshark issue.</p></div><div id="comment-5636-info" class="comment-info"><span class="comment-age">(10 Aug '11, 18:04)</span> cesto</div></div></div><div id="comment-tools-5617" class="comment-tools"></div><div class="clear"></div><div id="comment-5617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

