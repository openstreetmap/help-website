+++
type = "question"
title = "what is the mean of suspected retransmission ??"
description = '''here i have number of FDR produce data and transmitted to local server through internet when i capture traffic strange retransmission packets appear repeatedly why ?? please find attached  http://www.mediafire.com/download/bnw155591jf5fj5/tcp_stram_0.pcapng how come the data source send retransmit r...'''
date = "2014-05-24T09:53:00Z"
lastmod = "2014-05-25T03:40:00Z"
weight = 33038
keywords = [ "tcp-retransmit" ]
aliases = [ "/questions/33038" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [what is the mean of suspected retransmission ??](/questions/33038/what-is-the-mean-of-suspected-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33038-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33038-score" class="post-score" title="current number of votes">0</div><span id="post-33038-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>here i have number of FDR produce data and transmitted to local server through internet when i capture traffic strange retransmission packets appear repeatedly why ??</p><p>please find attached <a href="http://www.mediafire.com/download/bnw155591jf5fj5/tcp_stram_0.pcapng">http://www.mediafire.com/download/bnw155591jf5fj5/tcp_stram_0.pcapng</a></p><p>how come the data source send retransmit request</p><p>thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp-retransmit" rel="tag" title="see questions tagged &#39;tcp-retransmit&#39;">tcp-retransmit</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '14, 09:53</strong></p><img src="https://secure.gravatar.com/avatar/583f60448e616e6c6f8408eb6620006a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shady&#39;s gravatar image" /><p><span>shady</span><br />
<span class="score" title="11 reputation points">11</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shady has no accepted answers">0%</span></p></div></div><div id="comments-container-33038" class="comments-container"></div><div id="comment-tools-33038" class="comment-tools"></div><div class="clear"></div><div id="comment-33038-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33040"></span>

<div id="answer-container-33040" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33040-score" class="post-score" title="current number of votes">1</div><span id="post-33040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A retransmit is not a request - keep in mind that everything in square brackets are things that Wireshark adds, not something that is part of a packet.</p><p>Looks like you have retransmissions because the ACK did not get back to the sender, e.g. frame 30 is retransmitted in frame 34 even though it was ACKed in 32.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '14, 11:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-33040" class="comments-container"><span id="33048"></span><div id="comment-33048" class="comment"><div id="post-33048-score" class="comment-score"></div><div class="comment-text"><p>thank you for your reply</p><p>in the file you downloaded i separated only one TCP stream</p><p>in the complete capture file you will find the same problem for all TCP conversation</p><p>another point all retransmissions are always sent from the sender (FDR)this indicate a problem in server configuration</p><p>or what is the cause of this problem ?</p></div><div id="comment-33048-info" class="comment-info"><span class="comment-age">(25 May '14, 03:27)</span> <span class="comment-user userinfo">shady</span></div></div><span id="33050"></span><div id="comment-33050" class="comment"><div id="post-33050-score" class="comment-score">1</div><div class="comment-text"><p>packet loss is rarely a server configuration problem. Usually packets get lost on the network due to congestion or other problems.</p><p>Congestion means that when a link is overbooked packets will be buffered at first, but if more and more are coming in they will be discarded. Which results in retransmits.</p></div><div id="comment-33050-info" class="comment-info"><span class="comment-age">(25 May '14, 03:40)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-33040" class="comment-tools"></div><div class="clear"></div><div id="comment-33040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

