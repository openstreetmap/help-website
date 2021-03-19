+++
type = "question"
title = "Using dumpcap on several servers and sending the pcaps to a fileserver/LUN"
description = '''Hey all, We have come upon quite a large issue that seems to just not go away. We currently have dumpcap setup on over 2 dozen media servers as a scheduled task to run all the time. It captures on both NICS of our Media Servers, 1 NIC handles data, other NIC handles voice. As of right now, we are ha...'''
date = "2016-03-30T09:31:00Z"
lastmod = "2016-03-30T10:28:00Z"
weight = 51293
keywords = [ "dumpcap" ]
aliases = [ "/questions/51293" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using dumpcap on several servers and sending the pcaps to a fileserver/LUN](/questions/51293/using-dumpcap-on-several-servers-and-sending-the-pcaps-to-a-fileserverlun)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51293-score" class="post-score" title="current number of votes">0</div><span id="post-51293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey all,</p><p>We have come upon quite a large issue that seems to just not go away. We currently have dumpcap setup on over 2 dozen media servers as a scheduled task to run all the time. It captures on both NICS of our Media Servers, 1 NIC handles data, other NIC handles voice. As of right now, we are having the dumpcap dump the pcaps on our "E" drive. What I would like to do is to have all those servers log to a fileserver or LUN. I am aware that I could just put the path into the scheduled task. My question is has anyone done this before? Do you recommend it or what do you recommend? Also, what did it do to your network saturation?</p><p>Thank you in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '16, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/86aa00583e4d3f1713efcf851c3d1ea3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JonNolan81&#39;s gravatar image" /><p><span>JonNolan81</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JonNolan81 has no accepted answers">0%</span></p></div></div><div id="comments-container-51293" class="comments-container"></div><div id="comment-tools-51293" class="comment-tools"></div><div class="clear"></div><div id="comment-51293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51294"></span>

<div id="answer-container-51294" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51294-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51294-score" class="post-score" title="current number of votes">0</div><span id="post-51294-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My recent practical experience has shown that creation of each file on a remote fileserver (assuming you are using circular file buffers to facilitate a "continuous" capture) takes too long for tcpdump's buffering to handle even though my frame rate is just about 4000 frames per second, so I've ended up writing tcpdump's output to local ramdisk and then using a script to move the data to the final destination at the "file server" (where another script takes care about compressing them). I do admit that nfs is not the fastest available means so your environment may be more favourable. I don't expect dumpcap's buffering to be significantly different from tcpdump's, and I admit I might have overcome that "file creation lag" issue by instructing tcpdump to use several megabytes of buffers - it is just something you have to think about and test before starting to use the remote file storage routinely.</p><p>The other point is whether your media servers' NICs have enough spare bandwidth to more than triple the traffic in Tx direction during transfer of the captured data, as each captured byte causes another one to be sent over the network plus some overhead of the file transfer protocol used. Here I am lucky as I am capturing at USB so the Ethernet bandwidth used to copy the files does not compete with the source traffic, and don't need to throttle the file transfers; in your case, the traffic bursts caused by file transfers could cause packet loss unless you would use traffic policing, giving the signalling some priority over transfer of the capture files, which could mean a significant modification of the "natural" behaviour of the gateways. So think about the peak volume of the source traffic at both NICs and the spare bandwidth available at the signalling NIC (which is likely to carry much less source traffic than the media one).</p><p>The last point is the available bandwidth of those interfaces of the switches to which the file server is connected: 0.9 Gbit/s of capture data (assuming 0.3 Gbit/s per media direction plus 50 Mbit/s per signalling direction plus some overhead) from each of the 10 sources generate a 10 Gbit/s flow to the file server.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '16, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-51294" class="comments-container"><span id="51295"></span><div id="comment-51295" class="comment"><div id="post-51295-score" class="comment-score"></div><div class="comment-text"><p>Thank you Sindy. Those are very good points and ones that I will have to test out. I was thinking about starting with 1 server and monitoring its behavior so see if any issues arise. I will update this thread with the result.</p></div><div id="comment-51295-info" class="comment-info"><span class="comment-age">(30 Mar '16, 10:24)</span> <span class="comment-user userinfo">JonNolan81</span></div></div><span id="51296"></span><div id="comment-51296" class="comment"><div id="post-51296-score" class="comment-score"></div><div class="comment-text"><p>A technical remark: I've converted your post into a Comment to my Answer as the post itself was was not an Answer to your Question. The idea of the site is to build a Q&amp;A knowledge base, see the site FAQ.</p></div><div id="comment-51296-info" class="comment-info"><span class="comment-age">(30 Mar '16, 10:28)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-51294" class="comment-tools"></div><div class="clear"></div><div id="comment-51294-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

