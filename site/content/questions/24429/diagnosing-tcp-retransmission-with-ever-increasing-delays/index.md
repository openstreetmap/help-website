+++
type = "question"
title = "Diagnosing TCP Retransmission with ever increasing delays"
description = '''I&#x27;m trying to diagnose some connectivity issues between a remote proxy (EZProxy) which is having trouble connecting to a load balanced webserver. Looking at a tshark dump from the load balancer, I can see the initial SYN packet to establish a port 80 connection. This is swiftly followed by an Out-Of...'''
date = "2013-09-06T08:25:00Z"
lastmod = "2013-09-06T09:50:00Z"
weight = 24429
keywords = [ "delay", "retransmission", "syn" ]
aliases = [ "/questions/24429" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Diagnosing TCP Retransmission with ever increasing delays](/questions/24429/diagnosing-tcp-retransmission-with-ever-increasing-delays)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24429-score" class="post-score" title="current number of votes">0</div><span id="post-24429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to diagnose some connectivity issues between a remote proxy (EZProxy) which is having trouble connecting to a load balanced webserver.</p><p>Looking at a tshark dump from the load balancer, I can see the initial SYN packet to establish a port 80 connection. This is swiftly followed by an Out-Of-Order SYN packet.</p><p>Then there's a sequence of 2 SYN retransmissions after 3 seconds, then again after a further 6 seconds, then 12, 24, 48 and then 96 seconds when finally I see an ACK and an HTTP request packet.</p><ul><li>What would cause that kind of behaviour?</li><li>load balancer is using <a href="http://www.linuxvirtualserver.org/software/ipvs.html">ipvs</a>, sending packets to realservers via the LVS-DR direct routing method</li><li><a href="https://www.dropbox.com/s/7xjdryh58naxkpr/24429.pcap">https://www.dropbox.com/s/7xjdryh58naxkpr/24429.pcap</a> contains traces where ip.src==ip of proxy</li><li>I've also noticed that reducing the cluster size to a single webserver makes the problem go away. Perhaps I'm seeing some issue with ipvs here?</li></ul><p>Pointers on where to look next much appreciated.</p><p>(note, I would reply to comments but all my responses have tripped the spam filter!)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-delay" rel="tag" title="see questions tagged &#39;delay&#39;">delay</span> <span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '13, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/e8056bedcd8650385431cbfd26ee84bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Dixon&#39;s gravatar image" /><p><span>Paul Dixon</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Dixon has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Sep '13, 09:24</strong> </span></p></div></div><div id="comments-container-24429" class="comments-container"><span id="24431"></span><div id="comment-24431" class="comment"><div id="post-24431-score" class="comment-score"></div><div class="comment-text"><p>Did you capture the client-side and server-side traffic on the load balancer?</p><p>Is it possible to provide (parts) of the capture file on google docs, dropbox, cloudshark, etc.?</p></div><div id="comment-24431-info" class="comment-info"><span class="comment-age">(06 Sep '13, 08:55)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-24429" class="comment-tools"></div><div class="clear"></div><div id="comment-24429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24435"></span>

<div id="answer-container-24435" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24435-score" class="post-score" title="current number of votes">0</div><span id="post-24435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Paul Dixon has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Solved - the problem was the assumption that it was a specific client causing the problem.</p><p>It was actually rather simple - one of the realservers in the cluster was not configured with the IP address of the cluster, so was rejecting any connection attempts directed to it.</p><p>Ultimately, I would have found this by analysing the traffic on each realserver in turn, but as I was setting up tshark on the problem server, I noticed it was missing some IP address assignments.</p><p>Doh!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '13, 09:50</strong></p><img src="https://secure.gravatar.com/avatar/e8056bedcd8650385431cbfd26ee84bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Dixon&#39;s gravatar image" /><p><span>Paul Dixon</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Dixon has one accepted answer">100%</span></p></div></div><div id="comments-container-24435" class="comments-container"></div><div id="comment-tools-24435" class="comment-tools"></div><div class="clear"></div><div id="comment-24435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

