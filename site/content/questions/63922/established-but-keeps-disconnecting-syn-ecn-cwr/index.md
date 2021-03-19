+++
type = "question"
title = "Established But Keeps Disconnecting [SYN, ECN, CWR]"
description = '''Hi Guys, I&#x27;m having trouble to keep the connectivity between client and server steady. Can you help me analyze?  Thank you so much. Regards, CJ'''
date = "2017-10-16T02:49:00Z"
lastmod = "2017-10-18T03:10:00Z"
weight = 63922
keywords = [ "ecn", "cwr", "disconnect", "intermittent" ]
aliases = [ "/questions/63922" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Established But Keeps Disconnecting \[SYN, ECN, CWR\]](/questions/63922/established-but-keeps-disconnecting-syn-ecn-cwr)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63922-score" class="post-score" title="current number of votes">0</div><span id="post-63922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys,</p><p>I'm having trouble to keep the connectivity between client and server steady. Can you help me analyze?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/dt.JPG" alt="alt text" /></p><p>Thank you so much.</p><p>Regards, CJ</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ecn" rel="tag" title="see questions tagged &#39;ecn&#39;">ecn</span> <span class="post-tag tag-link-cwr" rel="tag" title="see questions tagged &#39;cwr&#39;">cwr</span> <span class="post-tag tag-link-disconnect" rel="tag" title="see questions tagged &#39;disconnect&#39;">disconnect</span> <span class="post-tag tag-link-intermittent" rel="tag" title="see questions tagged &#39;intermittent&#39;">intermittent</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '17, 02:49</strong></p><img src="https://secure.gravatar.com/avatar/eeb5a23e45969c7e82469e38fb3043c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian%20Joseph&#39;s gravatar image" /><p><span>Christian Jo...</span><br />
<span class="score" title="-11 reputation points">-11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian Joseph has no accepted answers">0%</span></p></img></div></div><div id="comments-container-63922" class="comments-container"></div><div id="comment-tools-63922" class="comment-tools"></div><div class="clear"></div><div id="comment-63922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63924"></span>

<div id="answer-container-63924" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63924-score" class="post-score" title="current number of votes">0</div><span id="post-63924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Christian Joseph has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks as though the client (10.252.239.151) doesn't like the 62 bytes of data sent from the server as it gracefully closes the connection within 40 ms or so of receiving the data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '17, 03:21</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Oct '17, 04:27</strong> </span></p></div></div><div id="comments-container-63924" class="comments-container"><span id="63928"></span><div id="comment-63928" class="comment"><div id="post-63928-score" class="comment-score"></div><div class="comment-text"><p>That's not a network problem. Packets are delivered fine, no loss, nothing. This is stack or (most likely) application.</p></div><div id="comment-63928-info" class="comment-info"><span class="comment-age">(16 Oct '17, 03:50)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="63929"></span><div id="comment-63929" class="comment"><div id="post-63929-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/2911/christian">@christian</a>-joseph,</p><p>My answer could have been better, I meant the client application as made clear by the comment from <a href="https://ask.wireshark.org/users/145/jasper">@Jasper</a>.</p></div><div id="comment-63929-info" class="comment-info"><span class="comment-age">(16 Oct '17, 04:09)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="63957"></span><div id="comment-63957" class="comment"><div id="post-63957-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/1225/grahamb">@grahamb</a> as per checking the config, 10.229.6.142 is configured as the server, I'm quite confused on that part.</p></div><div id="comment-63957-info" class="comment-info"><span class="comment-age">(17 Oct '17, 00:56)</span> <span class="comment-user userinfo">Christian Jo...</span></div></div><span id="63959"></span><div id="comment-63959" class="comment"><div id="post-63959-score" class="comment-score"></div><div class="comment-text"><p>Oops, typo, sorry about that. Fixed in answer.</p></div><div id="comment-63959-info" class="comment-info"><span class="comment-age">(17 Oct '17, 04:26)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="63991"></span><div id="comment-63991" class="comment"><div id="post-63991-score" class="comment-score"></div><div class="comment-text"><p>Thanks. As I try to troubleshoot further, when I telnet internally to 10.229.6.142:11138, it immediately closes the connection, the response is "connection closed by foreign host". Do you think this has something to do to the problem?</p></div><div id="comment-63991-info" class="comment-info"><span class="comment-age">(17 Oct '17, 23:34)</span> <span class="comment-user userinfo">Christian Jo...</span></div></div><span id="63995"></span><div id="comment-63995" class="comment not_top_scorer"><div id="post-63995-score" class="comment-score"></div><div class="comment-text"><p>That seems to be different behaviour than that shown in your question. Is the telnet client sending anything to the server to trigger the connection close?</p></div><div id="comment-63995-info" class="comment-info"><span class="comment-age">(18 Oct '17, 03:10)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-63924" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-63924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

