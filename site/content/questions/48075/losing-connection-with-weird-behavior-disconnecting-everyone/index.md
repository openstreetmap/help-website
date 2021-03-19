+++
type = "question"
title = "Losing connection with weird behavior (disconnecting everyone)"
description = ''' Hi all, I need some expertise advise. I suspect this guy is doing something bad in our server. our connected client loses connection. is this a modern kind of attack? he keep send ACK, so strange that why server 192.168.1.10 with CHECKSUM error.  port 4 4 4 0 5 is connect server port 5 5 5 2 3 is g...'''
date = "2015-11-30T04:19:00Z"
lastmod = "2015-11-30T15:12:00Z"
weight = 48075
keywords = [ "ack", "disconnect" ]
aliases = [ "/questions/48075" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Losing connection with weird behavior (disconnecting everyone)](/questions/48075/losing-connection-with-weird-behavior-disconnecting-everyone)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48075-score" class="post-score" title="current number of votes">0</div><span id="post-48075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="http://oi66.tinypic.com/2s7gi9w.jpg" alt="alt text" /> Hi all,</p><p>I need some expertise advise. I suspect this guy is doing something bad in our server. our connected client loses connection. is this a modern kind of attack? he keep send ACK, so strange that why server 192.168.1.10 with CHECKSUM error.</p><p>port 4 4 4 0 5 is connect server port 5 5 5 2 3 is game server port</p><p>hope somebody can enlighten on this. whether there's something i have to fix.</p><p>regards</p><p>MM</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-disconnect" rel="tag" title="see questions tagged &#39;disconnect&#39;">disconnect</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '15, 04:19</strong></p><img src="https://secure.gravatar.com/avatar/b28e4bba49352b3b1e2f015d72556540?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmguy&#39;s gravatar image" /><p><span>mmguy</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmguy has no accepted answers">0%</span></p></img></div></div><div id="comments-container-48075" class="comments-container"></div><div id="comment-tools-48075" class="comment-tools"></div><div class="clear"></div><div id="comment-48075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48103"></span>

<div id="answer-container-48103" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48103-score" class="post-score" title="current number of votes">0</div><span id="post-48103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Easy one first, the TCP checksum errors can be ignored as the trace was taken at the server and checksum is offloaded to the ethernet card.... Edit-Preferences-TCP - uncheck validate checksum to 'fix' those ... ;-)</p><p>Secondly - providing serious advice on a screenshot alone is close to impossible . The client closes the connections pretty early with a RST, nothing that should do much harm to your server...</p><p>If this is about a game server, it might be viable to share the capture file on cloudshark or other places to look at the payload...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '15, 11:16</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-48103" class="comments-container"><span id="48109"></span><div id="comment-48109" class="comment"><div id="post-48109-score" class="comment-score"></div><div class="comment-text"><p>Hi MrEEde,</p><p>thank you for your reply. here is the capture file: <a href="https://www.cloudshark.org/captures/6b6ff5ac3d8a">https://www.cloudshark.org/captures/6b6ff5ac3d8a</a> I really appreciate your time for considering in helping me.</p><p>Game Server Port is 5 5 5 2 3 and 5 5 5 0 9 Connect server Port is 4 4 4 0 5</p><p>rgds</p><p>MM</p></div><div id="comment-48109-info" class="comment-info"><span class="comment-age">(30 Nov '15, 15:12)</span> <span class="comment-user userinfo">mmguy</span></div></div></div><div id="comment-tools-48103" class="comment-tools"></div><div class="clear"></div><div id="comment-48103-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

