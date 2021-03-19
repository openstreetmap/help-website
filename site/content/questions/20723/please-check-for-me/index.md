+++
type = "question"
title = "please check for me."
description = '''link text No. 1 is the wireshark file. link text No.2 is the error file. Could you check for me between 203.126.29.157 and 192.168.0.2 any packet lost? Because I see with red color line. Thanks, Ko Htwe'''
date = "2013-04-22T19:39:00Z"
lastmod = "2013-04-22T21:03:00Z"
weight = 20723
keywords = [ "loss", "sip", "tcp", "packet", "packetloss" ]
aliases = [ "/questions/20723" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [please check for me.](/questions/20723/please-check-for-me)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20723-score" class="post-score" title="current number of votes">0</div><span id="post-20723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><a href="http://www.sendspace.com/file/yx35vh">link text</a> No. 1 is the wireshark file.</p><p><a href="http://www.sendspace.com/file/ppli7d">link text</a></p><p>No.2 is the error file. Could you check for me between 203.126.29.157 and 192.168.0.2 any packet lost?</p><p>Because I see with red color line.</p><p>Thanks, Ko Htwe</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-loss" rel="tag" title="see questions tagged &#39;loss&#39;">loss</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-packetloss" rel="tag" title="see questions tagged &#39;packetloss&#39;">packetloss</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '13, 19:39</strong></p><img src="https://secure.gravatar.com/avatar/993a5013c0195ec1f207d5983af47efc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aungkohtwe&#39;s gravatar image" /><p><span>aungkohtwe</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aungkohtwe has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Mar '14, 10:57</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-20723" class="comments-container"></div><div id="comment-tools-20723" class="comment-tools"></div><div class="clear"></div><div id="comment-20723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20725"></span>

<div id="answer-container-20725" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20725-score" class="post-score" title="current number of votes">0</div><span id="post-20725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aungkohtwe has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ko Htwe,</p><p>What is the "problem" that you are seeing?</p><p>As far as I can see the RST packed in red is simply the end of a successful TLS conversation between the client to the SIP server. The client initiated the close with a FIN, the server ACKed that, but also followed up with the RST.</p><p>There is an immediate followup conversation (initiated at 4284) that seems to use the same certificate, and is still going on at the end of the capture.</p><p>Martin</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '13, 21:03</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-20725" class="comments-container"></div><div id="comment-tools-20725" class="comment-tools"></div><div class="clear"></div><div id="comment-20725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

