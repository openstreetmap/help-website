+++
type = "question"
title = "TCP Window Update Scenarios"
description = '''In our application, we are using apache tomcat webserver running in 8081. It receives POST message from Client at 16:42:06.87 IST timeframe. It acknowledges by ACK packet with window size of 62356 bytes after 200ms. After some seconds (3-5 seconds), it also sends similar ACK packet but as a &quot;TCP Win...'''
date = "2015-06-16T02:22:00Z"
lastmod = "2015-06-17T14:49:00Z"
weight = 43202
keywords = [ "networking" ]
aliases = [ "/questions/43202" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Window Update Scenarios](/questions/43202/tcp-window-update-scenarios)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43202-score" class="post-score" title="current number of votes">0</div><span id="post-43202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In our application, we are using apache tomcat webserver running in 8081.</p><p>It receives POST message from Client at 16:42:06.87 IST timeframe. It acknowledges by ACK packet with window size of 62356 bytes after 200ms.</p><p>After some seconds (3-5 seconds), it also sends similar ACK packet but as a "TCP Window Update" packet of 65535 bytes (Buffer empty) to client. And then it sends 200 OK which means Successful Processing...</p><p>My question:</p><p>What are the scenarios which "TCP Window Update" packet would be sent from Server to Client.</p><p>Does this means webserver or Application-Layer took around 3-5 seconds to read 65535-62356(~ 3100) bytes which was in its TCP Receiver window and after reading, it has sent "TCP Window Update" packet since it is yet to send response</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-networking" rel="tag" title="see questions tagged &#39;networking&#39;">networking</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '15, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/e87988d1187d3f72281fa805fb050edb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sashi&#39;s gravatar image" /><p><span>Sashi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sashi has no accepted answers">0%</span></p></div></div><div id="comments-container-43202" class="comments-container"><span id="43286"></span><div id="comment-43286" class="comment"><div id="post-43286-score" class="comment-score"></div><div class="comment-text"><p>Could you provide us a trace?</p></div><div id="comment-43286-info" class="comment-info"><span class="comment-age">(17 Jun '15, 14:49)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-43202" class="comment-tools"></div><div class="clear"></div><div id="comment-43202-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

