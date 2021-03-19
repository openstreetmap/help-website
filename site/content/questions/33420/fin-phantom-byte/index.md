+++
type = "question"
title = "FIN Phantom byte"
description = '''218, 82.5999, 10.24.233.34 - 10.24.238.2 ,102, smtp → 54361, [FIN, ACK] Seq=450 Ack=1169,Len=0  219, 82.6001, 10.24.238.2 - 10.24.233.34, 102,54361 → smtp ,[FIN, ACK] Seq=1169 Ack=450, Len=0  220, 82.6003, 10.24.238.2 - 10.24.233.34, 102, 54361 → smtp [ACK] Seq=1170 Ack=451, Len=0  221, 82.6003, 10....'''
date = "2014-06-05T00:50:00Z"
lastmod = "2014-06-05T05:51:00Z"
weight = 33420
keywords = [ "fin" ]
aliases = [ "/questions/33420" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [FIN Phantom byte](/questions/33420/fin-phantom-byte)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33420-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33420-score" class="post-score" title="current number of votes">0</div><span id="post-33420-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>218, 82.5999, 10.24.233.34 - 10.24.238.2 ,102, smtp → 54361, [FIN, ACK] Seq=450 Ack=1169,Len=0

219, 82.6001, 10.24.238.2 - 10.24.233.34, 102,54361 → smtp ,[FIN, ACK] Seq=1169 Ack=450, Len=0

220, 82.6003, 10.24.238.2 - 10.24.233.34, 102, 54361 → smtp [ACK] Seq=1170 Ack=451, Len=0

221, 82.6003, 10.24.233.34 -10.24.238.2,  102,  smtp → 54361 [ACK] Seq=451 Ack=1170, Len=0</code></pre><p>Hi,In above session termination process why in packet 220 sequence no increased by 1 and in second fin ack packet ack is not increased by 1.as per my understanding during session termination process only ack byte(phantom) increases by one.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fin" rel="tag" title="see questions tagged &#39;fin&#39;">fin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '14, 00:50</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p><span>kishan pandey</span><br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jun '14, 02:02</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-33420" class="comments-container"></div><div id="comment-tools-33420" class="comment-tools"></div><div class="clear"></div><div id="comment-33420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33427"></span>

<div id="answer-container-33427" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33427-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33427-score" class="post-score" title="current number of votes">1</div><span id="post-33427-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kishan pandey has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In packet 219, 10.24.238.2 sends a FIN flag with Sequence No. 1169, so the next packet needs to use Sequence No. 1170, which it does in packet 220.</p><p>The other node sends its FIN in packet 218 with Sequence No. 450, and thus has to use sequence no. 451 in its next packet. Which is packet 221, and it does.</p><p>Looks all good to me, but maybe I haven't understood the question :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '14, 02:29</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-33427" class="comments-container"><span id="33432"></span><div id="comment-33432" class="comment"><div id="post-33432-score" class="comment-score"></div><div class="comment-text"><p>Thanks jasper,why did it increase 1 byte(1170) in seq in packet 220 as the last ack received(218) was 1169.As per my understanding During FIN exchange only ack increases by 1 byte and not seq field.</p></div><div id="comment-33432-info" class="comment-info"><span class="comment-age">(05 Jun '14, 02:47)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="33433"></span><div id="comment-33433" class="comment"><div id="post-33433-score" class="comment-score"></div><div class="comment-text"><p>ACK and sequence both increase - the receiver has to notify that it got the FIN flag (so +1 on the ACK), and the sender has to continue at the sequence after the FIN, so +1 on the sequence.</p></div><div id="comment-33433-info" class="comment-info"><span class="comment-age">(05 Jun '14, 02:51)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="33436"></span><div id="comment-33436" class="comment"><div id="post-33436-score" class="comment-score"></div><div class="comment-text"><p>215, 82.5999, 10.24.233.34 - 10.24.238.2 ,102, smtp → 54365, [FIN, ACK] Seq=450 Ack=434,Len=0</p><p>216, 82.6001, 10.24.238.2 - 10.24.233.34, 102,54365 → smtp ,[FIN, ACK] Seq=434 Ack=451, Len=0</p><p>227, 82.6003, 10.24.238.2 - 10.24.233.34, 102, 54365 → smtp [ACK] Seq=451 Ack=435, Len=0</p><p>Thanks for explanation jasper,Curiosity is growing now,One more FIN termination in same capture and now the pattern is different.Now if we see only ack has increased(packet 216) and seq numbers are same as lask ack.</p></div><div id="comment-33436-info" class="comment-info"><span class="comment-age">(05 Jun '14, 04:31)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="33437"></span><div id="comment-33437" class="comment"><div id="post-33437-score" class="comment-score">1</div><div class="comment-text"><p>in 215 10.24.233.34 sends a FIN with seq 450, so in 216 that packet is ACKed by 450+1. Which is correct. The seq in 216 is 434, same as the last ack in 215, which means there was no outstanding data to be acknowledged. Everything okay there, too.</p><p>Are you sure you got packet 227 right? It looks like you turned the IPs and ports around for that quote... it should be the ACK for 216 but source and destination is in the wrong order. I guess you copied it incorrectly.</p></div><div id="comment-33437-info" class="comment-info"><span class="comment-age">(05 Jun '14, 04:43)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="33439"></span><div id="comment-33439" class="comment"><div id="post-33439-score" class="comment-score"></div><div class="comment-text"><p>yes not copied properly,an packet analyst knows everything.I Understand it now properly.</p></div><div id="comment-33439-info" class="comment-info"><span class="comment-age">(05 Jun '14, 05:36)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="33440"></span><div id="comment-33440" class="comment not_top_scorer"><div id="post-33440-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-33440-info" class="comment-info"><span class="comment-age">(05 Jun '14, 05:51)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-33427" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-33427-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

