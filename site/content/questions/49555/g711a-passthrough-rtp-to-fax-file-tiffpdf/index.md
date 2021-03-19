+++
type = "question"
title = "G711A passthrough RTP to FAX File (TIFF/PDF ?)"
description = '''Dear all, I looked all over the web to an option to convert RTP stream of a passthrough FAX to a readable file, but i could not find it. I have an RTP Stream captured that i would like to convert to a TIFF Image of the faxed file. Can you help me with a way to do it ? Thank you. PS : I have Wireshar...'''
date = "2016-01-27T08:16:00Z"
lastmod = "2016-01-27T09:50:00Z"
weight = 49555
keywords = [ "g711a", "pdf", "fax", "rtp", "tiff" ]
aliases = [ "/questions/49555" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [G711A passthrough RTP to FAX File (TIFF/PDF ?)](/questions/49555/g711a-passthrough-rtp-to-fax-file-tiffpdf)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49555-score" class="post-score" title="current number of votes">0</div><span id="post-49555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear all,</p><p>I looked all over the web to an option to convert RTP stream of a passthrough FAX to a readable file, but i could not find it.</p><p>I have an RTP Stream captured that i would like to convert to a TIFF Image of the faxed file.</p><p>Can you help me with a way to do it ?</p><p>Thank you.</p><p>PS : I have Wireshark2 and a pcapng dump from which i extracted the G711a rtpdump.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-g711a" rel="tag" title="see questions tagged &#39;g711a&#39;">g711a</span> <span class="post-tag tag-link-pdf" rel="tag" title="see questions tagged &#39;pdf&#39;">pdf</span> <span class="post-tag tag-link-fax" rel="tag" title="see questions tagged &#39;fax&#39;">fax</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-tiff" rel="tag" title="see questions tagged &#39;tiff&#39;">tiff</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '16, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/6cffb17442267e2423a40cb5fddbf847?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elmehdierroussafi&#39;s gravatar image" /><p><span>elmehdierrou...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elmehdierroussafi has no accepted answers">0%</span></p></div></div><div id="comments-container-49555" class="comments-container"></div><div id="comment-tools-49555" class="comment-tools"></div><div class="clear"></div><div id="comment-49555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49560"></span>

<div id="answer-container-49560" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49560-score" class="post-score" title="current number of votes">0</div><span id="post-49560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What you need is:</p><ul><li><p>in Wireshark: <code>Telephony -&gt; RTP -&gt; Stream Analysis -&gt; Save -&gt; Forward stream audio</code></p></li><li><p>using Audacity or another audio editor/converter: change the internal format of the audio file from .au to .wav</p></li><li><p>using <a href="https://github.com/jart/spandsp/blob/master/tests/fax_decode.c">this project</a>: convert the .wav contents into the .tiff picture.</p></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '16, 09:50</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-49560" class="comments-container"></div><div id="comment-tools-49560" class="comment-tools"></div><div class="clear"></div><div id="comment-49560-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

