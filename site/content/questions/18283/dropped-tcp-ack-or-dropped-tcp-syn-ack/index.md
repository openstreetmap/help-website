+++
type = "question"
title = "Dropped TCP ACK or dropped TCP SYN, ACK"
description = '''I have a web server with 10 IP Addresses and about 10,000 clients. Every couple of months I will get one client that can&#x27;t connect to one IP Address. All other clients can connect and the one client having trouble with the one IP Address can connect to call the other IP Addresses on the server. The ...'''
date = "2013-02-04T07:18:00Z"
lastmod = "2013-02-04T15:28:00Z"
weight = 18283
keywords = [ "ack", "dropped", "tcp" ]
aliases = [ "/questions/18283" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dropped TCP ACK or dropped TCP SYN, ACK](/questions/18283/dropped-tcp-ack-or-dropped-tcp-syn-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18283-score" class="post-score" title="current number of votes">0</div><span id="post-18283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a web server with 10 IP Addresses and about 10,000 clients. Every couple of months I will get one client that can't connect to one IP Address. All other clients can connect and the one client having trouble with the one IP Address can connect to call the other IP Addresses on the server. The problem last for a couple of months and clears on it's own.</p><p>The packet capture shows one client to server SYN, a couple of server to client SYN, ACK's, then a server to client RST, and finally a "A segment before this frame wasn't captured." It seems like the client's ACK is not getting to the server for the one IP Address.</p><p>There are no firewalls that are blocking by IP Address. Is there anything other than a firewall that would cause this?</p><p>Maybe the source is not receiving the SYN, ACK from the destination. The packet capture shows the source sending the same SYN sequence number about 10 times. I guess we would have to run the packet capture on both ends to see.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-dropped" rel="tag" title="see questions tagged &#39;dropped&#39;">dropped</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '13, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/30ca11c69f8a037c7d1d0ffa0dd93034?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steve1&#39;s gravatar image" /><p><span>Steve1</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steve1 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Feb '13, 09:01</strong> </span></p></div></div><div id="comments-container-18283" class="comments-container"></div><div id="comment-tools-18283" class="comment-tools"></div><div class="clear"></div><div id="comment-18283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18298"></span>

<div id="answer-container-18298" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18298-score" class="post-score" title="current number of votes">0</div><span id="post-18298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As always, having a packet capture to look at will make it much easier to help you solve this issue. If you can upload a capture file to www.cloudshark.org and post the link here, that would be great.</p><p>You describe a capture, I assume it has been made on the client itself? You also state that the source (client) sends SYNs with the same sequence number. Does every SYN result in a SYN/ACK from the server? What is the mac-address in the SYN/ACK? Are the IP and TCP checksums correct (you can enable checksum verification in the IP and TCP protocol preferences).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '13, 15:28</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18298" class="comments-container"></div><div id="comment-tools-18298" class="comment-tools"></div><div class="clear"></div><div id="comment-18298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

