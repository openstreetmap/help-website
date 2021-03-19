+++
type = "question"
title = "Can TShark extract voice data from an RTP stream?"
description = '''In Wireshark, I can go to Telephony/RTP/Stream Analysis and then click &quot;Save Payload As...&quot; to dump the voice data into a file. Can I do this using TShark, too?'''
date = "2012-04-27T18:58:00Z"
lastmod = "2012-04-30T20:15:00Z"
weight = 10493
keywords = [ "voice", "rtp", "tshark" ]
aliases = [ "/questions/10493" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can TShark extract voice data from an RTP stream?](/questions/10493/can-tshark-extract-voice-data-from-an-rtp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10493-score" class="post-score" title="current number of votes">0</div><span id="post-10493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In Wireshark, I can go to Telephony/RTP/Stream Analysis and then click "Save Payload As..." to dump the voice data into a file. Can I do this using TShark, too?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-voice" rel="tag" title="see questions tagged &#39;voice&#39;">voice</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '12, 18:58</strong></p><img src="https://secure.gravatar.com/avatar/b31a2e10de8361fd3bc97873b576fb56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Homayoon&#39;s gravatar image" /><p><span>Homayoon</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Homayoon has no accepted answers">0%</span></p></div></div><div id="comments-container-10493" class="comments-container"></div><div id="comment-tools-10493" class="comment-tools"></div><div class="clear"></div><div id="comment-10493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10538"></span>

<div id="answer-container-10538" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10538-score" class="post-score" title="current number of votes">1</div><span id="post-10538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Homayoon has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>afaik that's not possible with tshark (please correct, if I'm wrong). However, there are open source tools, that can do it.</p><p><a href="http://sourceforge.net/projects/pcapsipdump/">http://sourceforge.net/projects/pcapsipdump/</a><br />
<a href="http://frox25.no-ip.org/~mtve/wiki/RtpExtract.html">http://frox25.no-ip.org/~mtve/wiki/RtpExtract.html</a><br />
</p><p>and for "big data":</p><p><a href="http://www.sipcapture.org/">http://www.sipcapture.org/</a><br />
<a href="http://sourceforge.net/projects/our/">http://sourceforge.net/projects/our/</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '12, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-10538" class="comments-container"><span id="10543"></span><div id="comment-10543" class="comment"><div id="post-10543-score" class="comment-score"></div><div class="comment-text"><p>My guess is you're right. Your links seem to provide a good alternative. Thanks.</p></div><div id="comment-10543-info" class="comment-info"><span class="comment-age">(30 Apr '12, 20:15)</span> <span class="comment-user userinfo">Homayoon</span></div></div></div><div id="comment-tools-10538" class="comment-tools"></div><div class="clear"></div><div id="comment-10538-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

