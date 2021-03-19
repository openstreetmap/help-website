+++
type = "question"
title = "How do I create a statistic which side closes the most connections?"
description = '''I&#x27;m analyzing a packet dump where a client is talking to a server via TCP/IP. Sometimes the connection gets closed by one of the two machines with the usual handshake (FIN/ACK, FIN/ACK, ACK). After that, the client immediately opens a new connection and the process repeats after a few packets were s...'''
date = "2011-05-16T06:50:00Z"
lastmod = "2011-05-20T23:20:00Z"
weight = 4095
keywords = [ "analyze", "statistics", "flags", "tcp", "ip" ]
aliases = [ "/questions/4095" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I create a statistic which side closes the most connections?](/questions/4095/how-do-i-create-a-statistic-which-side-closes-the-most-connections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4095-score" class="post-score" title="current number of votes">1</div><span id="post-4095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm analyzing a packet dump where a client is talking to a server via TCP/IP. Sometimes the connection gets closed by one of the two machines with the usual handshake (FIN/ACK, FIN/ACK, ACK). After that, the client immediately opens a new connection and the process repeats after a few packets were sent.</p><p>How do I create a statistic which side (client or server) initiated the most connection shutdowns?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-analyze" rel="tag" title="see questions tagged &#39;analyze&#39;">analyze</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-flags" rel="tag" title="see questions tagged &#39;flags&#39;">flags</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '11, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/544d7761aabdfe3f146e74a418859262?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grimmig&#39;s gravatar image" /><p><span>grimmig</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grimmig has no accepted answers">0%</span></p></div></div><div id="comments-container-4095" class="comments-container"><span id="4099"></span><div id="comment-4099" class="comment"><div id="post-4099-score" class="comment-score"></div><div class="comment-text"><p>Does the menu "Statistics &gt; Conversations List &gt; TCP" help you?</p></div><div id="comment-4099-info" class="comment-info"><span class="comment-age">(16 May '11, 22:14)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="4159"></span><div id="comment-4159" class="comment"><div id="post-4159-score" class="comment-score"></div><div class="comment-text"><p>No. It only shows that conversations happened and who started them, but not who closed them.</p><p>I think what I need is a filter that shows only first FIN packet in a conversation. Then I can simply run awk over the output and count the lines for each IP.</p></div><div id="comment-4159-info" class="comment-info"><span class="comment-age">(19 May '11, 23:43)</span> <span class="comment-user userinfo">grimmig</span></div></div></div><div id="comment-tools-4095" class="comment-tools"></div><div class="clear"></div><div id="comment-4095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4170"></span>

<div id="answer-container-4170" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4170-score" class="post-score" title="current number of votes">1</div><span id="post-4170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="grimmig has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would pass all SYN/FIN/RST packets to a little perl (or awk) script that will keep a list of sessions that are created (SYN, no ACK), then when the first FIN or RST for that session comes, you can set a flag "closed-by-client" or "closed-by-server" for that session and once the while file is processed, you can create the statistics.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '11, 23:20</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4170" class="comments-container"></div><div id="comment-tools-4170" class="comment-tools"></div><div class="clear"></div><div id="comment-4170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

