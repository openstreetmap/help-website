+++
type = "question"
title = "Cisco Video Conferencing"
description = '''We are having issues with our VC conferencing system where we will freeze up during a meeting. We are using Cisco Telepresence SX20 at our locations. When a conference is taking place we can see latency and packets loss. We have gone in and setup SPAN on two ports to mirror the traffic that is passi...'''
date = "2015-10-19T15:37:00Z"
lastmod = "2015-10-26T06:51:00Z"
weight = 46724
keywords = [ "videoconference", "video", "cisco", "h323" ]
aliases = [ "/questions/46724" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Cisco Video Conferencing](/questions/46724/cisco-video-conferencing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46724-score" class="post-score" title="current number of votes">0</div><span id="post-46724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are having issues with our VC conferencing system where we will freeze up during a meeting. We are using Cisco Telepresence SX20 at our locations. When a conference is taking place we can see latency and packets loss. We have gone in and setup SPAN on two ports to mirror the traffic that is passing through the endpoints and have attached laptops running wireshark to collect the data. The VC data is encrypted when it goes over the link so the data will just show UDP traffic in the PCAP files. I need to prove this from a packet level if possible.<br />
</p><p>There is QOS enabled on the switches and this has been verified to be configured properly between endpoints by Cisco TAC. We also had a third party come in and verify that our VC system was optimally setup. What is the best way to disseminate the information in the pcap files to determine if we are having WAN issues?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-videoconference" rel="tag" title="see questions tagged &#39;videoconference&#39;">videoconference</span> <span class="post-tag tag-link-video" rel="tag" title="see questions tagged &#39;video&#39;">video</span> <span class="post-tag tag-link-cisco" rel="tag" title="see questions tagged &#39;cisco&#39;">cisco</span> <span class="post-tag tag-link-h323" rel="tag" title="see questions tagged &#39;h323&#39;">h323</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '15, 15:37</strong></p><img src="https://secure.gravatar.com/avatar/e94a3b8fe5eb3a8d3a90143a501e5c3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fairview&#39;s gravatar image" /><p><span>fairview</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fairview has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-46724" class="comments-container"></div><div id="comment-tools-46724" class="comment-tools"></div><div class="clear"></div><div id="comment-46724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46725"></span>

<div id="answer-container-46725" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46725-score" class="post-score" title="current number of votes">2</div><span id="post-46725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I need to prove this from a packet level if possible.</p></blockquote><p>to prove what?</p><blockquote><p>What is the best way to disseminate the information in the pcap files to determine if we are having WAN issues?</p></blockquote><p>What I have done in similar cases:</p><ul><li>print the frames with tshark (ip, ports, ip.id, etc.)</li><li>run a script to figure out if/which frames are missing</li></ul><p>Caveats are:</p><p>If the frames are being modified (NAT, etc.) it might be hard to identify identical frames, as important parameters, required to identify the frames, might change, like IP, ports, IP.ID. If that is the case, all you can do is to create a hash value of the UDP payload and try to match identical frames within a sliding window. Sounds easy, but it is not, if you're not pretty familiar with some scripting language.</p><p>Maybe the easiest way for you to start with is this: Compare the number of frames on both sides. If there is a delta, you are loosing frames somewhere. Could be your switches, routers, firewalls, the ISP, the Internet, etc.</p><p>Then, try to work your way from the VC client up to the ISP, by sniffing at the VC clients, then in front and after the router (in parallel), in front an after the firewall (in parallel). If you compare the number of frames in those capture files and there is a delta, you know where you are loosing frames. If it's not in your network, it's within the network of the ISP or 'the Internet'. In that case, there is little you can do to figure out <strong>where</strong> you are loosing frames. All you can do is to measure the connection with iperf of similar tools and 'confront' the ISP with the measured packet loss.</p><p>BTW: In a few of the similar cases I was working on, the IPS and/or rate control (QoS) of the corporate firewall kicked in and dropped enough frames to cause video stream freezes etc. Did you check that?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '15, 16:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-46725" class="comments-container"><span id="46759"></span><div id="comment-46759" class="comment"><div id="post-46759-score" class="comment-score"></div><div class="comment-text"><p><span>@fairview</span>: You just awarded an extra point to me. I'm not sure if you really wanted to do that.</p><p>Here is what you probably wanted to do...</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-46759-info" class="comment-info"><span class="comment-age">(20 Oct '15, 07:27)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-46725" class="comment-tools"></div><div class="clear"></div><div id="comment-46725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46933"></span>

<div id="answer-container-46933" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46933-score" class="post-score" title="current number of votes">0</div><span id="post-46933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>here some question</p><ol><li>Do you trust DSCP where the WAN router connect it ?</li><li>Trust DSCP at correct switch ports ?</li><li>bandwidth allocation correctly set ?</li><li>Do you subscribe any QoS service from ISP?</li></ol><p>VC with 1% packet drop is disasters;</p><p>Provide PCAP should able to tell do ur ISP taging any DSCP</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '15, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/ee15000690effb5f7ee000775e3bfe76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="limvuihan&#39;s gravatar image" /><p><span>limvuihan</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="limvuihan has no accepted answers">0%</span></p></div></div><div id="comments-container-46933" class="comments-container"></div><div id="comment-tools-46933" class="comment-tools"></div><div class="clear"></div><div id="comment-46933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

