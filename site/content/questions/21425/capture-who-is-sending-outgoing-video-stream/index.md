+++
type = "question"
title = "capture who is sending outgoing video stream"
description = '''Hi, I&#x27;m new to wireshark, but I get the concept of what it does, I hope.... I am an IT consultant and have been hired by a company to see who is streaming a TV program from their network. they have been contacted by the TV station that an IP on their network has been doing this to a bit torrent. I h...'''
date = "2013-05-23T15:28:00Z"
lastmod = "2013-05-24T00:55:00Z"
weight = 21425
keywords = [ "videostream" ]
aliases = [ "/questions/21425" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [capture who is sending outgoing video stream](/questions/21425/capture-who-is-sending-outgoing-video-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21425-score" class="post-score" title="current number of votes">0</div><span id="post-21425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm new to wireshark, but I get the concept of what it does, I hope.... I am an IT consultant and have been hired by a company to see who is streaming a TV program from their network. they have been contacted by the TV station that an IP on their network has been doing this to a bit torrent. I have placed my switch with the port mirroring on the lan between the last switch and the router/firewall. I started capturing packets but quickly ran out of memory. I was hoping to only capture packets that are outbound and only video. I assume video packets can have many forms so that may not be a good filter but will leave it to you to educate me. Once I have the packets, I know wireshark well enough to find which IP they are coming from but it will be a very time consuming task, so if someone has a better way to do this, I am all ears. thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-videostream" rel="tag" title="see questions tagged &#39;videostream&#39;">videostream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '13, 15:28</strong></p><img src="https://secure.gravatar.com/avatar/f5cea79845d707e7d3e2152e84643bc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikestefani&#39;s gravatar image" /><p><span>mikestefani</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikestefani has no accepted answers">0%</span></p></div></div><div id="comments-container-21425" class="comments-container"></div><div id="comment-tools-21425" class="comment-tools"></div><div class="clear"></div><div id="comment-21425-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21426"></span>

<div id="answer-container-21426" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21426-score" class="post-score" title="current number of votes">0</div><span id="post-21426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As it is related to streaming media why can't you try to capture on port 554(rtsp control) to get the details of who is initiating the stream.Set the capture filter to port 554 and you will get the control flow if that is the protocol(RTSP) in picture.</p><p>Example Syntax for capture filter:</p><p>host a.b.c.d and port 554</p><p>Where a.b.c.d is your streaming server IP.Above capture filter tells to capture only traffic to or from your host with to or from port 554.</p><p>or simply do a capture of port 554 on your capture filter as specified below:</p><p>port 554</p><p>Regarding running out of memory</p><p>There is a work around feature called ring buffer .you can avoid running out of memory with ring buffer technique and check this post</p><p><a href="http://ask.wireshark.org/questions/21323/monitor-247-but-retain-only-15-minutes">http://ask.wireshark.org/questions/21323/monitor-247-but-retain-only-15-minutes</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '13, 15:52</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 May '13, 16:59</strong> </span></p></div></div><div id="comments-container-21426" class="comments-container"></div><div id="comment-tools-21426" class="comment-tools"></div><div class="clear"></div><div id="comment-21426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21434"></span>

<div id="answer-container-21434" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21434-score" class="post-score" title="current number of votes">0</div><span id="post-21434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would first look in the router/firewall for session table entries that point to BitTorrent. Also have a look at the NAT table. Of course this all depends on what kind of router/firewall it is and whether you can look at those tables. It also depends on how large the network is and how big those tables are.</p><p>You could also just capture the SYN packets by using the capture filter "tcp[13]=2", this way you can capture much longer and you have a good overview of communications over your router/firewall.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '13, 00:55</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21434" class="comments-container"></div><div id="comment-tools-21434" class="comment-tools"></div><div class="clear"></div><div id="comment-21434-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

