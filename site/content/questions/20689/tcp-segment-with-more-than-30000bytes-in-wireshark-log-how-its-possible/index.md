+++
type = "question"
title = "TCP segment with more than 30000bytes in wireshark log, how it&#x27;s possible???"
description = '''when I tested the FTP and monitored the log through wireshark, I found something very strange. since it started, the TCP segment size has been more than 30000bytes even the MSS which shared before was 1400 bytes. how the TCP send a segment to destination with this kind of big bytes.'''
date = "2013-04-21T19:57:00Z"
lastmod = "2015-05-28T00:58:00Z"
weight = 20689
keywords = [ "tcp-segment" ]
aliases = [ "/questions/20689" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP segment with more than 30000bytes in wireshark log, how it's possible???](/questions/20689/tcp-segment-with-more-than-30000bytes-in-wireshark-log-how-its-possible)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20689-score" class="post-score" title="current number of votes">1</div><span id="post-20689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>when I tested the FTP and monitored the log through wireshark, I found something very strange. since it started, the TCP segment size has been more than 30000bytes even the MSS which shared before was 1400 bytes. how the TCP send a segment to destination with this kind of big bytes.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp-segment" rel="tag" title="see questions tagged &#39;tcp-segment&#39;">tcp-segment</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '13, 19:57</strong></p><img src="https://secure.gravatar.com/avatar/3d71676dff939d12e717118778a36dd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="burnall&#39;s gravatar image" /><p><span>burnall</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="burnall has no accepted answers">0%</span></p></div></div><div id="comments-container-20689" class="comments-container"></div><div id="comment-tools-20689" class="comment-tools"></div><div class="clear"></div><div id="comment-20689-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20692"></span>

<div id="answer-container-20692" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20692-score" class="post-score" title="current number of votes">6</div><span id="post-20692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>TCP doesn't send it to the destination. What you're seeing is the result of the TCP segmentation offloading functionality: <a href="http://wiki.wireshark.org/CaptureSetup/Offloading">http://wiki.wireshark.org/CaptureSetup/Offloading</a></p><p>It basically means that you did the capture <strong>on</strong> the PC that sent the data and you captured it in a way it was never sent. The network card will cut the large block into smaller segments, but only after you've already picked it up in Wireshark. Capture on the other PC to see that there are in fact small segments coming in. You can also tell by looking at the acknowledges - you'll get a lot more than just one for the big segment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '13, 01:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Apr '13, 12:04</strong> </span></p></div></div><div id="comments-container-20692" class="comments-container"><span id="20703"></span><div id="comment-20703" class="comment"><div id="post-20703-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much, dude!</p></div><div id="comment-20703-info" class="comment-info"><span class="comment-age">(22 Apr '13, 06:41)</span> <span class="comment-user userinfo">burnall</span></div></div><span id="20704"></span><div id="comment-20704" class="comment"><div id="post-20704-score" class="comment-score"></div><div class="comment-text"><p>If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-20704-info" class="comment-info"><span class="comment-age">(22 Apr '13, 06:43)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="42714"></span><div id="comment-42714" class="comment"><div id="post-42714-score" class="comment-score"></div><div class="comment-text"><p>Jasper, in link you provided there is one more offload method - TCP chimney. Did i understand correctly that TCP chimney is one of TOE realization where TCP offloaded from CPU only after connection is established - during transfer, and then passed back to CPU to finish connection?</p></div><div id="comment-42714-info" class="comment-info"><span class="comment-age">(27 May '15, 21:30)</span> <span class="comment-user userinfo">mongolio</span></div></div><span id="42718"></span><div id="comment-42718" class="comment"><div id="post-42718-score" class="comment-score">1</div><div class="comment-text"><p>yes, TCP chimney means that the network card takes over segmentation and CRC calculation from the CPU.</p></div><div id="comment-42718-info" class="comment-info"><span class="comment-age">(28 May '15, 00:58)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-20692" class="comment-tools"></div><div class="clear"></div><div id="comment-20692-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

