+++
type = "question"
title = "Can&#x27;t UNC to SAN (49173  &gt; [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_perm=1)"
description = '''I have a whole subnet on a 3650 that can&#x27;t UNC in to one of all of my SAN&#x27;s. When I attempt to UNC in to it using a laptop with wire shark installed I get back the returned black packets:  (49173 &amp;gt;Microsoft-ds [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_perm=1) (49175 &amp;gt;NetBIOS-ssn [SYN] Seq=...'''
date = "2014-05-07T14:55:00Z"
lastmod = "2014-05-07T15:31:00Z"
weight = 32623
keywords = [ "unc", "packets" ]
aliases = [ "/questions/32623" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't UNC to SAN (49173 &gt; \[SYN\] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK\_perm=1)](/questions/32623/cant-unc-to-san-49173-syn-seq0-win8192-len0-mss1460-ws8-sack_perm1)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32623-score" class="post-score" title="current number of votes">0</div><span id="post-32623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a whole subnet on a 3650 that can't UNC in to one of all of my SAN's. When I attempt to UNC in to it using a laptop with wire shark installed I get back the returned black packets:</p><pre><code>(49173  &gt;Microsoft-ds [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_perm=1)
(49175  &gt;NetBIOS-ssn [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_perm=1)
(49174  &gt;http [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_perm=1)</code></pre><p>What do these mean?<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-unc" rel="tag" title="see questions tagged &#39;unc&#39;">unc</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '14, 14:55</strong></p><img src="https://secure.gravatar.com/avatar/de64d1089e4cc4476ae8708fd90e5391?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="parakiteiz&#39;s gravatar image" /><p><span>parakiteiz</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="parakiteiz has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 May '14, 15:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-32623" class="comments-container"></div><div id="comment-tools-32623" class="comment-tools"></div><div class="clear"></div><div id="comment-32623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32624"></span>

<div id="answer-container-32624" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32624-score" class="post-score" title="current number of votes">1</div><span id="post-32624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>SYN means that the computer sending it tries to setup a connection, and when it's not answered with a SYN/ACK it is retried a couple of times, sometimes on alternate ports depending on the protocol.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '14, 15:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-32624" class="comments-container"></div><div id="comment-tools-32624" class="comment-tools"></div><div class="clear"></div><div id="comment-32624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

