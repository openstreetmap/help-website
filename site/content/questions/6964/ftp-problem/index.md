+++
type = "question"
title = "FTP Problem"
description = '''Hi ,  I have a problem witch my FTP server. The problem are packet lost. I captured traffic and I saw strange problem with ftp-data length value. Server and client have set MTU = 1460 but client sent data to server witch MTU 1590 bytes.  192.168.2.14 192.168.2.2 FTP-DATA 1078 FTP Data: 1024 bytes 19...'''
date = "2011-10-18T12:08:00Z"
lastmod = "2011-10-18T12:32:00Z"
weight = 6964
keywords = [ "ftp" ]
aliases = [ "/questions/6964" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [FTP Problem](/questions/6964/ftp-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6964-score" class="post-score" title="current number of votes">0</div><span id="post-6964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ,</p><p>I have a problem witch my FTP server. The problem are packet lost. I captured traffic and I saw strange problem with ftp-data length value.</p><p>Server and client have set MTU = 1460 but client sent data to server witch MTU 1590 bytes.<br />
</p><p>192.168.2.14 192.168.2.2 FTP-DATA 1078 FTP Data: 1024 bytes</p><p>192.168.2.14 192.168.2.2 FTP-DATA 1590 FTP Data: 1536 bytes</p><p>192.168.2.2 192.168.2.14 TCP 60 62305 &gt; 62057 [ACK] Seq=1 Ack=105909 Win=28288 Len=0</p><p>Why client sent data to server with mtu 1590 instead 1460 bytes ? Where is a problem ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ftp" rel="tag" title="see questions tagged &#39;ftp&#39;">ftp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '11, 12:08</strong></p><img src="https://secure.gravatar.com/avatar/4fa3dd94306addcfcb7f6d96411f90f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Robert&#39;s gravatar image" /><p><span>Robert</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Robert has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-6964" class="comments-container"></div><div id="comment-tools-6964" class="comment-tools"></div><div class="clear"></div><div id="comment-6964-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6966"></span>

<div id="answer-container-6966" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6966-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6966-score" class="post-score" title="current number of votes">2</div><span id="post-6966-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As far as I read your quote it doesn't say "MTU" anywhere, just that FTP sent 1536 bytes (which would be the TCP payload size, not the MTU).</p><p>There are a couple of reasons why you're seeing packets with that kind of "large" payload, for example if you're capturing your own, outgoing traffic. Your network card is probably doing something called "large send offloading", meaning that it slices the data into valid chunks before sending it out, but by then Wireshark has already captured it, fooling you :-)</p><p>Try to capture the same data on the other end, and you'll see that the packets arrive with valid sizes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '11, 12:17</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-6966" class="comments-container"><span id="6967"></span><div id="comment-6967" class="comment"><div id="post-6967-score" class="comment-score"></div><div class="comment-text"><p>yes , you have right :) I checked it and tcp payload size is 1460 bytes. I must remember about "large send offloading"</p><p>thank you Robert<br />
</p></div><div id="comment-6967-info" class="comment-info"><span class="comment-age">(18 Oct '11, 12:32)</span> <span class="comment-user userinfo">Robert</span></div></div></div><div id="comment-tools-6966" class="comment-tools"></div><div class="clear"></div><div id="comment-6966-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

