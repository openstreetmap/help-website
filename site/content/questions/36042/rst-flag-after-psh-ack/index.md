+++
type = "question"
title = "RST flag after PSH, ACK"
description = '''Hi, i got two applications - client and server talking to each other. After they both are executed, client sends message to server - in wireshark i see PSH, ACK packet coming.  Server gets data, but server replies on it with RST packet, and client got 0 bytes received - my question is way this happe...'''
date = "2014-09-06T08:26:00Z"
lastmod = "2014-09-07T06:02:00Z"
weight = 36042
keywords = [ "tcp" ]
aliases = [ "/questions/36042" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RST flag after PSH, ACK](/questions/36042/rst-flag-after-psh-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36042-score" class="post-score" title="current number of votes">0</div><span id="post-36042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i got two applications - client and server talking to each other. After they both are executed, client sends message to server - in wireshark i see PSH, ACK packet coming. Server gets data, but server replies on it with RST packet, and client got 0 bytes received - my question is way this happening ? Server is not doing any close syscall...</p><p>Thx in advance fot any help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '14, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/e0ba5cee6aada692ac9305b959fdd247?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wojciech%20Jedruch&#39;s gravatar image" /><p><span>Wojciech Jed...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wojciech Jedruch has no accepted answers">0%</span></p></div></div><div id="comments-container-36042" class="comments-container"><span id="36048"></span><div id="comment-36048" class="comment"><div id="post-36048-score" class="comment-score"></div><div class="comment-text"><p>If the server doesn't issue the close it's probably some security software running on the platform. What are the operating systems of client and server? Where did you trace? Can you upload a sample trace to <a href="https://appliance.cloudshark.org/upload/">https://appliance.cloudshark.org/upload/</a> Rgds Matthias</p></div><div id="comment-36048-info" class="comment-info"><span class="comment-age">(06 Sep '14, 22:52)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="36056"></span><div id="comment-36056" class="comment"><div id="post-36056-score" class="comment-score"></div><div class="comment-text"><p>It appeared that if server was killed, client didnt do anything with connection; therefore for new instance of server executed client was sending thoroght connection that has been alerady finished by one side, and i suppose therefore server send RST flag. This is my observation - do you think it can be possible ?</p></div><div id="comment-36056-info" class="comment-info"><span class="comment-age">(07 Sep '14, 06:02)</span> <span class="comment-user userinfo">Wojciech Jed...</span></div></div></div><div id="comment-tools-36042" class="comment-tools"></div><div class="clear"></div><div id="comment-36042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

