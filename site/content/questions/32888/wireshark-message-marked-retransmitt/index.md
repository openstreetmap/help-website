+++
type = "question"
title = "Wireshark message marked [Retransmitt]"
description = '''Hi, I have received a wireshark log. Some of the queries are marked [Retransmission....]. When logging in the lab, and delaying the response to above timeout-limit. I get a new query with the same trans-ID, but it is not marked [Retransmission.....]. Could this action be triggered by something diffe...'''
date = "2014-05-19T06:01:00Z"
lastmod = "2014-05-19T08:00:00Z"
weight = 32888
keywords = [ "retransmission", "wireshark" ]
aliases = [ "/questions/32888" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark message marked \[Retransmitt\]](/questions/32888/wireshark-message-marked-retransmitt)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32888-score" class="post-score" title="current number of votes">0</div><span id="post-32888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have received a wireshark log. Some of the queries are marked [Retransmission....]. When logging in the lab, and delaying the response to above timeout-limit. I get a new query with the same trans-ID, but it is not marked [Retransmission.....]. Could this action be triggered by something different?</p><p>BR Frenzie</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '14, 06:01</strong></p><img src="https://secure.gravatar.com/avatar/5767c303c596376507fa1ed5884f10da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frenzie&#39;s gravatar image" /><p><span>Frenzie</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frenzie has no accepted answers">0%</span></p></div></div><div id="comments-container-32888" class="comments-container"></div><div id="comment-tools-32888" class="comment-tools"></div><div class="clear"></div><div id="comment-32888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32891"></span>

<div id="answer-container-32891" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32891-score" class="post-score" title="current number of votes">0</div><span id="post-32891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your forced new query probably does not have the same sequence number as the original one. You should compare the TCP layers of both packets to see if the sequence numbers are identical or not - if they're different you're not seeing a TCP retransmission, just an "application retransmission".</p><p>Retransmissions usually occur due to packet loss, which is not easy to recreate in a lab environment - at least not in a very exact kind of way.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '14, 06:10</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-32891" class="comments-container"><span id="32894"></span><div id="comment-32894" class="comment"><div id="post-32894-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer. But this leads to another one: Where/how can I set the parameters for these retransmissions?</p></div><div id="comment-32894-info" class="comment-info"><span class="comment-age">(19 May '14, 06:51)</span> <span class="comment-user userinfo">Frenzie</span></div></div><span id="32903"></span><div id="comment-32903" class="comment"><div id="post-32903-score" class="comment-score"></div><div class="comment-text"><p>What kind of parameters do you mean? If a segment is lost it is retransmitted, so if the receiver tells the sender that there is a gap in the packets it will trigger a retransmit at the sender. These mechanisms are more or less hard coded into the TCP stacks of each OS.</p></div><div id="comment-32903-info" class="comment-info"><span class="comment-age">(19 May '14, 08:00)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-32891" class="comment-tools"></div><div class="clear"></div><div id="comment-32891-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

