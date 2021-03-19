+++
type = "question"
title = "Is there a way to capture/display filter the Root Link Query messages??"
description = '''Hi. As you know, the RLQ (Root Link Query) is such a BPDU message that is used by BackboneFast feature on Cisco switches in order to help fast STP recovery. now, is there a way to capture/display filter this kind of message?? '''
date = "2015-10-30T12:26:00Z"
lastmod = "2015-10-30T12:56:00Z"
weight = 47095
keywords = [ "stp", "rlq", "backbonefast" ]
aliases = [ "/questions/47095" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a way to capture/display filter the Root Link Query messages??](/questions/47095/is-there-a-way-to-capturedisplay-filter-the-root-link-query-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47095-score" class="post-score" title="current number of votes">0</div><span id="post-47095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. As you know, the <strong>RLQ</strong> (Root Link Query) is such a BPDU message that is used by <strong>BackboneFast</strong> feature on Cisco switches in order to help fast STP recovery. now, is there a way to capture/display filter this kind of message??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-stp" rel="tag" title="see questions tagged &#39;stp&#39;">stp</span> <span class="post-tag tag-link-rlq" rel="tag" title="see questions tagged &#39;rlq&#39;">rlq</span> <span class="post-tag tag-link-backbonefast" rel="tag" title="see questions tagged &#39;backbonefast&#39;">backbonefast</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '15, 12:26</strong></p><img src="https://secure.gravatar.com/avatar/8752544ec453a6d8e08fdde4d465eca7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MehranBazgir&#39;s gravatar image" /><p><span>MehranBazgir</span><br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MehranBazgir has no accepted answers">0%</span></p></div></div><div id="comments-container-47095" class="comments-container"></div><div id="comment-tools-47095" class="comment-tools"></div><div class="clear"></div><div id="comment-47095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47097"></span>

<div id="answer-container-47097" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47097-score" class="post-score" title="current number of votes">1</div><span id="post-47097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MehranBazgir has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>there is no RLQ BPDU dissector in Wireshark, so there is no way to set a display filter.</p><p>I don't know if it's possible to set a capture filter, as I don't have a sample pcap file, besides the hex code printed in a book I found.</p><blockquote><p><a href="https://books.google.de/books?id=bsiMVwVBGl8C&amp;lpg=PA72&amp;ots=TPMPehpqU1&amp;dq=rlq%20bpdu%20pcap&amp;hl=de&amp;pg=PA72#v=onepage&amp;q=rlq%20bpdu%20pcap&amp;f=false">https://books.google.de/books?id=bsiMVwVBGl8C&amp;lpg=PA72&amp;ots=TPMPehpqU1&amp;dq=rlq%20bpdu%20pcap&amp;hl=de&amp;pg=PA72#v=onepage&amp;q=rlq%20bpdu%20pcap&amp;f=false</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '15, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-47097" class="comments-container"></div><div id="comment-tools-47097" class="comment-tools"></div><div class="clear"></div><div id="comment-47097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

