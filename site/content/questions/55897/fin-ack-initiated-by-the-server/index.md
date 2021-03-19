+++
type = "question"
title = "FIN, ACK initiated by the server"
description = '''Please help me in the following query. I have a client opening and closing socket with server. Generally client send FIN packet to sever to close the session. But sometimes server initiates the FIN but its difficult to trace it in wireshark as I have to analyze long list of logs. So is there any fil...'''
date = "2016-09-27T04:45:00Z"
lastmod = "2016-09-27T09:56:00Z"
weight = 55897
keywords = [ "ack.", "fin" ]
aliases = [ "/questions/55897" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [FIN, ACK initiated by the server](/questions/55897/fin-ack-initiated-by-the-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55897-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55897-score" class="post-score" title="current number of votes">1</div><span id="post-55897-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Please help me in the following query.</p><p>I have a client opening and closing socket with server. Generally client send FIN packet to sever to close the session. But sometimes server initiates the FIN but its difficult to trace it in wireshark as I have to analyze long list of logs. So is there any filter I can use to narrow down my search.</p><p>I am looking for a FILTER when server initiates FIN, ACK.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack." rel="tag" title="see questions tagged &#39;ack.&#39;">ack.</span> <span class="post-tag tag-link-fin" rel="tag" title="see questions tagged &#39;fin&#39;">fin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '16, 04:45</strong></p><img src="https://secure.gravatar.com/avatar/d5530659c84d8407b8637fbe924bfe25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="singhmanpreet294&#39;s gravatar image" /><p><span>singhmanpree...</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="singhmanpreet294 has no accepted answers">0%</span></p></div></div><div id="comments-container-55897" class="comments-container"></div><div id="comment-tools-55897" class="comment-tools"></div><div class="clear"></div><div id="comment-55897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55898"></span>

<div id="answer-container-55898" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55898-score" class="post-score" title="current number of votes">1</div><span id="post-55898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>(tcp.flags.fin == 1) and (tcp.flags.ack == 1) and (ip.src == a.b.c.d)</code>, replacing a.b.c.d with the server's ip address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '16, 04:59</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-55898" class="comments-container"><span id="55920"></span><div id="comment-55920" class="comment"><div id="post-55920-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer. But it will still not filter out if server initiates FIN, ACK in the first place. It will show all the FIN, ACK packet irrespective of who initiated it.</p><p>So this filter wont be able to help me much.</p></div><div id="comment-55920-info" class="comment-info"><span class="comment-age">(27 Sep '16, 09:12)</span> <span class="comment-user userinfo">singhmanpree...</span></div></div><span id="55925"></span><div id="comment-55925" class="comment"><div id="post-55925-score" class="comment-score"></div><div class="comment-text"><p>So you only want packets with FIN, ACK and the client hasn't sent a FIN yet.<br />
</p><p>Unfortunately, filters only work on each individual packet to include or exclude it based on the values in that packet, they can't look backwards or forwards in the packet list for values in other related packets.</p><p>Wireshark does have a tool, <a href="https://wiki.wireshark.org/Mate">MATE</a>, that can be used to build associations between packets that might be able to help you.</p></div><div id="comment-55925-info" class="comment-info"><span class="comment-age">(27 Sep '16, 09:55)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="55926"></span><div id="comment-55926" class="comment"><div id="post-55926-score" class="comment-score"></div><div class="comment-text"><p>So this is true but you could try the following:</p><ol><li><p>Use the filter from above to colorize the packets</p></li><li><p>Use the following display filter TCP.flags.syn==1 and TCP.flags.fin==1</p></li><li><p>Apply the stream Id as a column</p></li><li><p>Sort the trace by stream id column</p></li></ol><p>Now it should be easier to find the relevant fin packets</p></div><div id="comment-55926-info" class="comment-info"><span class="comment-age">(27 Sep '16, 09:56)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-55898" class="comment-tools"></div><div class="clear"></div><div id="comment-55898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

