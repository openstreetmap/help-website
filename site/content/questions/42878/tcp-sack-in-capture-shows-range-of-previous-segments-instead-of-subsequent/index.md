+++
type = "question"
title = "TCP SACK in capture shows range of previous segments instead of subsequent"
description = '''I am a bit confused with following capture  As I red SACK must acknowledge last/highest in-order segment and hints about subsequent received segments after missing one. But in this capture I see that in SACK option field numbers are not greater than ACK number but smaller instead. Here is the partia...'''
date = "2015-06-04T04:37:00Z"
lastmod = "2015-06-08T06:29:00Z"
weight = 42878
keywords = [ "tcp", "sack" ]
aliases = [ "/questions/42878" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TCP SACK in capture shows range of previous segments instead of subsequent](/questions/42878/tcp-sack-in-capture-shows-range-of-previous-segments-instead-of-subsequent)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42878-score" class="post-score" title="current number of votes">0</div><span id="post-42878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am a bit confused with following capture <img src="https://osqa-ask.wireshark.org/upfiles/SACK_2vPB49u.jpg" alt="alt text" /></p><p>As I red SACK must acknowledge last/highest in-order segment and hints about subsequent received segments after missing one. But in this capture I see that in SACK option field numbers are not greater than ACK number but smaller instead.</p><p>Here is the partial damp <a href="https://www.cloudshark.org/captures/9b04d7772096">https://www.cloudshark.org/captures/9b04d7772096</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-sack" rel="tag" title="see questions tagged &#39;sack&#39;">sack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '15, 04:37</strong></p><img src="https://secure.gravatar.com/avatar/4f86795c7a782fccae8a0b7bd270d1d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mongolio&#39;s gravatar image" /><p><span>mongolio</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mongolio has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jun '15, 03:01</strong> </span></p></div></div><div id="comments-container-42878" class="comments-container"></div><div id="comment-tools-42878" class="comment-tools"></div><div class="clear"></div><div id="comment-42878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42883"></span>

<div id="answer-container-42883" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42883-score" class="post-score" title="current number of votes">1</div><span id="post-42883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mongolio has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's a D-SACK, not a SACK. D-SACK is an extension to SACK, and is used to tell the sender that one or more segments were retransmitted even though they were already acknowledged. See <a href="https://tools.ietf.org/html/rfc2883">RFC 2883</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '15, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42883" class="comments-container"><span id="42906"></span><div id="comment-42906" class="comment"><div id="post-42906-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot. I red RFC 2883 and now can’t understand why in my example receiver sends 3 ACK with D-SACK option instead of sending one - block of duplicated packets forms contiguous sequence of data:</p><p>5381090-5382450</p><p>5382450-5383810</p><p>5383810-5385170</p></div><div id="comment-42906-info" class="comment-info"><span class="comment-age">(04 Jun '15, 21:46)</span> <span class="comment-user userinfo">mongolio</span></div></div><span id="42908"></span><div id="comment-42908" class="comment"><div id="post-42908-score" class="comment-score"></div><div class="comment-text"><p>hard to say, because you keep posting screenshots that have been cut off. Screenshots are always a lot harder to read than a real capture file, but if you also leave out IPs and Frame indexes it is basically useless for tracking TCP behavior and identifying why a diagnosis was made.</p><p>My guess is that the stack decided to tell the sender each time a spurious retransmission arrives directly that it was not required. Other than acknowledging packets there is not delay mechanism to do that for multiple segments, because a stack has absolutely no reason to expect multiple spurious retransmission in a row.</p></div><div id="comment-42908-info" class="comment-info"><span class="comment-age">(05 Jun '15, 01:52)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="42909"></span><div id="comment-42909" class="comment"><div id="post-42909-score" class="comment-score"></div><div class="comment-text"><p>Added partial capture file to initial post</p></div><div id="comment-42909-info" class="comment-info"><span class="comment-age">(05 Jun '15, 03:02)</span> <span class="comment-user userinfo">mongolio</span></div></div><span id="42915"></span><div id="comment-42915" class="comment"><div id="post-42915-score" class="comment-score">1</div><div class="comment-text"><p>As I guessed, the D-SACKs are for the three retransmissions.</p></div><div id="comment-42915-info" class="comment-info"><span class="comment-age">(05 Jun '15, 04:02)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="42967"></span><div id="comment-42967" class="comment not_top_scorer"><div id="post-42967-score" class="comment-score"></div><div class="comment-text"><p>As I understood RFC2883 this can be done with one ACK containing full range of segments from 5381090 to 5385170, instead of sent ACK for each retransmitted packet. Is it depends on individual TCP algorithm realization or I misunderstand RFC?</p><p>And to be honest I can’t understand why we need such an explicit notification of duplicate frames - previously I have thought that if sender would miss some ACKs but would receive some subsequent ACKs it will result in all segments successfully ACKed. For e.g. if ACK for segment 10 and 11 were lost but ACK for segment 12 arrived timely than sender will implicitly ACKs segment 10 and 11 cos TCP use cumulative ACKs.</p></div><div id="comment-42967-info" class="comment-info"><span class="comment-age">(08 Jun '15, 03:34)</span> <span class="comment-user userinfo">mongolio</span></div></div><span id="42968"></span><div id="comment-42968" class="comment"><div id="post-42968-score" class="comment-score">1</div><div class="comment-text"><p>It depends on the individual TCP stack. And D-SACK is trying to help the sender adjusting it's sending behavior by giving feedback.</p></div><div id="comment-42968-info" class="comment-info"><span class="comment-age">(08 Jun '15, 03:36)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="42970"></span><div id="comment-42970" class="comment not_top_scorer"><div id="post-42970-score" class="comment-score"></div><div class="comment-text"><p>Jasper, normally if sender sent retransmit by timeout (not by fast retransmit) then it will decrease CWND not by the MD rule but till the initial CWND value and start with the slow-start algorithm?</p></div><div id="comment-42970-info" class="comment-info"><span class="comment-age">(08 Jun '15, 05:59)</span> <span class="comment-user userinfo">mongolio</span></div></div><span id="42972"></span><div id="comment-42972" class="comment not_top_scorer"><div id="post-42972-score" class="comment-score"></div><div class="comment-text"><p>Most stacks I've seen do that, yes, so on RTO based retransmissions you see a slow start (that's actually the only time you'll still see a slow start at all these days). Again, this behavior is stack dependent, so it may or may not happen.</p></div><div id="comment-42972-info" class="comment-info"><span class="comment-age">(08 Jun '15, 06:29)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-42883" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-42883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

