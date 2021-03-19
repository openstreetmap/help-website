+++
type = "question"
title = "Can not see any traffic from a server created by rackspace cloud"
description = '''Hi, I am trying to monitor the traffic between my machine and a server (windows server 2008)that was created by rackspace in the cloud.  I have the IP address of the server. But there is no data being captured by wireshare for it. Do I need to setup or enable something on the server or on my machine...'''
date = "2014-06-03T03:26:00Z"
lastmod = "2014-06-04T22:28:00Z"
weight = 33340
keywords = [ "server" ]
aliases = [ "/questions/33340" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can not see any traffic from a server created by rackspace cloud](/questions/33340/can-not-see-any-traffic-from-a-server-created-by-rackspace-cloud)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33340-score" class="post-score" title="current number of votes">0</div><span id="post-33340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to monitor the traffic between my machine and a server (windows server 2008)that was created by rackspace in the cloud.</p><p>I have the IP address of the server. But there is no data being captured by wireshare for it.</p><p>Do I need to setup or enable something on the server or on my machine?</p><p>I even installed winpcap on the server and enabled remote packet capturing in services.</p><p>But in wireshark it can not find the ip address when I try to add the ip address to remote capture interfaces. It says the server is not responding in a timely manner.</p><p>I can ping the server...</p><p>I not sure what else to try out here...</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '14, 03:26</strong></p><img src="https://secure.gravatar.com/avatar/3005d6c714e07d6101e92456f96484dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fiona&#39;s gravatar image" /><p><span>Fiona</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fiona has no accepted answers">0%</span></p></div></div><div id="comments-container-33340" class="comments-container"><span id="33341"></span><div id="comment-33341" class="comment"><div id="post-33341-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I not sure what else to try out here...</p></blockquote><p>Let's start with the basics ;-)</p><ul><li><strong>where</strong> do you want to capture the traffic? On the client or on the server?</li><li><strong>what</strong> traffic are you interested in. Traffic going to the server or traffic coming from the server?</li><li><strong>How</strong> did you try to capture? On the server itself (by installing Wireshark on it) or on the client?</li></ul></div><div id="comment-33341-info" class="comment-info"><span class="comment-age">(03 Jun '14, 05:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="33342"></span><div id="comment-33342" class="comment"><div id="post-33342-score" class="comment-score"></div><div class="comment-text"><p>Thanks :)</p><p>where do you want to capture the traffic? On the client or on the server? I want to capture the traffic on the client.</p><p>what traffic are you interested in. Traffic going to the server or traffic coming from the server? I am interested in both traffic.</p><p>How did you try to capture? On the server itself (by installing Wireshark on it) or on the client? I installed wireshark on the client and I tried to capture the traffic.</p></div><div id="comment-33342-info" class="comment-info"><span class="comment-age">(03 Jun '14, 06:37)</span> <span class="comment-user userinfo">Fiona</span></div></div><span id="33350"></span><div id="comment-33350" class="comment"><div id="post-33350-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I installed wireshark on the client and I tried to capture the traffic.</p></blockquote><p>Did you try to capture the traffic of <strong>that client</strong> or the whole traffic to/from the server, meaning also traffic from other clients.</p></div><div id="comment-33350-info" class="comment-info"><span class="comment-age">(03 Jun '14, 08:32)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="33353"></span><div id="comment-33353" class="comment"><div id="post-33353-score" class="comment-score"></div><div class="comment-text"><p>I am not up to speed with setting up servers and clients as you can tell :) I was capturing all of the traffic on the network.</p><p>I am using a browser on my laptop as a"client" - this is being used to connect to the rackspace account where I can create and remotely connect to a server.</p><p>And I am running jar of beans emulator as another client on the same laptop - here I can run a rackspace app to also log into my account and create servers.</p><p>But none of the captured traffic has the IP address of the created server...</p></div><div id="comment-33353-info" class="comment-info"><span class="comment-age">(03 Jun '14, 11:40)</span> <span class="comment-user userinfo">Fiona</span></div></div></div><div id="comment-tools-33340" class="comment-tools"></div><div class="clear"></div><div id="comment-33340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33355"></span>

<div id="answer-container-33355" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33355-score" class="post-score" title="current number of votes">0</div><span id="post-33355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>this is being <strong>used to connect to the rackspace account</strong> where I can create and remotely connect to a server.</p><p>jar of beans emulator as another client on the same laptop - here I can <strong>run a rackspace app</strong> to also log into my account and create servers.</p><p>But <strong>none of the captured traffic has the IP address of the created server</strong>...</p></blockquote><p>Well, if you connect to the <strong>Rackspace (management) server</strong> to create the virtual server, why to you expect to see the IP address of the created server instead of the Rackspace IPs you are connected to !?!</p><p>Only if you are connecting directly to the IP Address of the new server, <strong>without</strong> any VPN, Wireshark will show the IP address of that server!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '14, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-33355" class="comments-container"><span id="33373"></span><div id="comment-33373" class="comment"><div id="post-33373-score" class="comment-score"></div><div class="comment-text"><p>Thanks for putting clarity on it for me.</p><p>That makes sense now :)</p><p>Thanks Fiona</p></div><div id="comment-33373-info" class="comment-info"><span class="comment-age">(04 Jun '14, 03:20)</span> <span class="comment-user userinfo">Fiona</span></div></div><span id="33416"></span><div id="comment-33416" class="comment"><div id="post-33416-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-33416-info" class="comment-info"><span class="comment-age">(04 Jun '14, 22:28)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-33355" class="comment-tools"></div><div class="clear"></div><div id="comment-33355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

