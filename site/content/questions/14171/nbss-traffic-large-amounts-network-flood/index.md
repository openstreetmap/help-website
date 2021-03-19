+++
type = "question"
title = "NBSS traffic... Large amounts = Network flood"
description = '''I have a Database server sitting in one vlan and a backup server sitting in another at our co-lo. Occasionally, we will lose connectivity to the co-lo. When I run wireshark on a span port, I see massive amounts of: 137 0.012353000 10.10.1.253 17.16.1.151 NBSS 1434 [TCP ACKed unseen segment] [TCP Out...'''
date = "2012-09-10T10:50:00Z"
lastmod = "2012-09-10T17:50:00Z"
weight = 14171
keywords = [ "nbss", "error" ]
aliases = [ "/questions/14171" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [NBSS traffic... Large amounts = Network flood](/questions/14171/nbss-traffic-large-amounts-network-flood)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14171-score" class="post-score" title="current number of votes">0</div><span id="post-14171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a Database server sitting in one vlan and a backup server sitting in another at our co-lo. Occasionally, we will lose connectivity to the co-lo. When I run wireshark on a span port, I see massive amounts of:</p><p>137 0.012353000 10.10.1.253 17.16.1.151 NBSS 1434 [TCP ACKed unseen segment] [TCP Out-Of-Order] NBSS Continuation Message</p><p>or similar. If I can connect to the ilo on my backup server, I hit reboot and the problem goes away and users go back to normal. I don't get what this is, can someone help me understand what this message is?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nbss" rel="tag" title="see questions tagged &#39;nbss&#39;">nbss</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '12, 10:50</strong></p><img src="https://secure.gravatar.com/avatar/87fb5011c914d4a5dbdac1ed24f38cfc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shetldar&#39;s gravatar image" /><p><span>shetldar</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shetldar has no accepted answers">0%</span></p></div></div><div id="comments-container-14171" class="comments-container"></div><div id="comment-tools-14171" class="comment-tools"></div><div class="clear"></div><div id="comment-14171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14176"></span>

<div id="answer-container-14176" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14176-score" class="post-score" title="current number of votes">0</div><span id="post-14176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's telling you a couple of things 1) Your span itself is dropping packets. We know this because Wireshark is telling you that it saw an acknowledgement packet for a packet it did not see. In other words, it didn't see the original packet from the sender to the receiver. However, it saw the ACK coming from the receiver to the sender. So clearly, this is not a "real" packet loss. It wouldn't acknowledge something it didn't see.</p><p>2) Assuming your server's IP are 10.x and 17.x, it's kicking off some replication/synchronization, bulkcopy or some other file copy job. And the file copy (using windows file copy aka NBSS) is saturating your pipes.</p><p>3) It's also telling you that you need to implement QoS if at all possible. The backup (?) traffic in question should have a lower QoS priority then your user traffic. In most cases, backup jobs or normal file copies are not time sensitive. It's not a transactional, time sensitive thing. So use QoS to give preferential treatment to your users traffic and lower the priority on the backup traffic.</p><p>Good luck!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '12, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-14176" class="comments-container"><span id="14180"></span><div id="comment-14180" class="comment"><div id="post-14180-score" class="comment-score"></div><div class="comment-text"><blockquote><p>(using windows file copy aka NBSS)</p></blockquote><p>I.e., the NetBIOS Session Service (NBSS) is used to transport SMB packets over TCP (Wireshark might also identify "SMB-over-TCP", i.e. port 443 traffic, as NBSS); SMB is the standard Windows remote file access protocol, so the backup is presumably doing a lot of copies to and/or from a "network drive" and thus causing a lot of network traffic saturating your pipes.</p><p>(Slightly more detailed explanation, in case the original poster wasn't familiar with NetBIOS-over-TCP and SMB.)</p></div><div id="comment-14180-info" class="comment-info"><span class="comment-age">(10 Sep '12, 17:50)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-14176" class="comment-tools"></div><div class="clear"></div><div id="comment-14176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

