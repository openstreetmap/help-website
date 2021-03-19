+++
type = "question"
title = "TCP window sizes"
description = '''1) if tcp syn request wants a 1576 byte &quot;put/write&quot; transfer, will it be sent along with syn   request or must send data transfer wait until the syn recieves an ack? 2) does the answer change if the syn request needs a 1576 byte &quot;get/read&quot; transfer? 3) can tcp syn be rejected due to a syn window par...'''
date = "2013-10-16T01:46:00Z"
lastmod = "2013-10-16T13:37:00Z"
weight = 26044
keywords = [ "window", "tcp", "size" ]
aliases = [ "/questions/26044" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP window sizes](/questions/26044/tcp-window-sizes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26044-score" class="post-score" title="current number of votes">0</div><span id="post-26044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>1) if tcp syn request wants a 1576 byte "put/write" transfer, will it be sent along with syn request or must send data transfer wait until the syn recieves an ack?</p><p>2) does the answer change if the syn request needs a 1576 byte "get/read" transfer?</p><p>3) can tcp syn be rejected due to a syn window parameter that isnt supported by the other side?</p><p>4) can the response accept the syn but throttle the syn window value proposal?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-window" rel="tag" title="see questions tagged &#39;window&#39;">window</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '13, 01:46</strong></p><img src="https://secure.gravatar.com/avatar/3018495ae51d20c8fb8a0339512d83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rtrauben&#39;s gravatar image" /><p><span>rtrauben</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rtrauben has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>16 Oct '13, 02:01</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-26044" class="comments-container"></div><div id="comment-tools-26044" class="comment-tools"></div><div class="clear"></div><div id="comment-26044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26045"></span>

<div id="answer-container-26045" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26045-score" class="post-score" title="current number of votes">1</div><span id="post-26045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>1 &amp; 2) SYN is not a request containing data, it is a session setup signal. So in classic TCP you have to do the Three Way Handshake first before transmitting data requests. There are some TCP protocol modifications that aim at sending data with the SYN, but they're not widely used at the moment. Some also have risks regarding the security of the connection, like T/TCP.</p><p>3) No. Well, theoretically a node can always refuse a session by sending an RST, yes, but it doesn't happen in the real world - at least not because of the Window size.</p><p>4) No. Window size is per node, so each node decides what Window to advertise. The other node has no saying in how large it should be.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '13, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-26045" class="comments-container"><span id="26047"></span><div id="comment-26047" class="comment"><div id="post-26047-score" class="comment-score"></div><div class="comment-text"><blockquote><p>There are some TCP protocol modifications that aim at sending data with the SYN, but they're not widely used at the moment.</p></blockquote><p>is that part of an RFC?</p></div><div id="comment-26047-info" class="comment-info"><span class="comment-age">(16 Oct '13, 03:05)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="26049"></span><div id="comment-26049" class="comment"><div id="post-26049-score" class="comment-score"></div><div class="comment-text"><p>Sort of: <a href="http://tools.ietf.org/html/draft-cheng-tcpm-fastopen-00">http://tools.ietf.org/html/draft-cheng-tcpm-fastopen-00</a></p></div><div id="comment-26049-info" class="comment-info"><span class="comment-age">(16 Oct '13, 03:18)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="26083"></span><div id="comment-26083" class="comment"><div id="post-26083-score" class="comment-score"></div><div class="comment-text"><p>Nice. Thanks!</p></div><div id="comment-26083-info" class="comment-info"><span class="comment-age">(16 Oct '13, 13:37)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26045" class="comment-tools"></div><div class="clear"></div><div id="comment-26045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

