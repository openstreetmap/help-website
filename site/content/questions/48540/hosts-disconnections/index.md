+++
type = "question"
title = "hosts disconnections"
description = '''Hello, we have a network with some hosts with static ip adresses;  It&#x27;s happening that some of them are getting disconnected; we would like to monitor network traffic to and from this hosts, could you suggest me wich is the best procedure or filter to set to check this kind of disconnections with wi...'''
date = "2015-12-15T10:37:00Z"
lastmod = "2016-04-01T06:52:00Z"
weight = 48540
keywords = [ "disconnection" ]
aliases = [ "/questions/48540" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [hosts disconnections](/questions/48540/hosts-disconnections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48540-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48540-score" class="post-score" title="current number of votes">0</div><span id="post-48540-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>we have a network with some hosts with static ip adresses; It's happening that some of them are getting disconnected; we would like to monitor network traffic to and from this hosts, could you suggest me wich is the best procedure or filter to set to check this kind of disconnections with wireshark ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-disconnection" rel="tag" title="see questions tagged &#39;disconnection&#39;">disconnection</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '15, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/9a2fb41233096e289a4376ccb8740fc6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="prometeus&#39;s gravatar image" /><p><span>prometeus</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="prometeus has no accepted answers">0%</span></p></div></div><div id="comments-container-48540" class="comments-container"><span id="48541"></span><div id="comment-48541" class="comment"><div id="post-48541-score" class="comment-score">1</div><div class="comment-text"><p>Please precise what you mean by "getting disconnected", I guess their Ethernet cables do not jump out of the switch? I.e. what application reports the disconnection?</p></div><div id="comment-48541-info" class="comment-info"><span class="comment-age">(15 Dec '15, 10:41)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="48560"></span><div id="comment-48560" class="comment"><div id="post-48560-score" class="comment-score"></div><div class="comment-text"><p>Hallo Sindy,</p><p>thanks for your comment.</p><p>I mean we cannot control them or even ping them.</p><p>These hosts are robots being controlled by an application server through a netgear hub. These hosts don't get disconnected when we connect directly to them (i mean without any hub, switch or application server controlling them). On the application server there is a software controlling their status (this is the same software running on the pc we use for debug), we randomly detect these losses but on the contrary when we connect directly through a pc we can control them.</p><p>So we want to trace the reason of these disconnections</p></div><div id="comment-48560-info" class="comment-info"><span class="comment-age">(16 Dec '15, 02:09)</span> <span class="comment-user userinfo">prometeus</span></div></div></div><div id="comment-tools-48540" class="comment-tools"></div><div class="clear"></div><div id="comment-48540-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48567"></span>

<div id="answer-container-48567" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48567-score" class="post-score" title="current number of votes">1</div><span id="post-48567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK,</p><blockquote><p>we cannot control them or even ping them.</p></blockquote><p>in this case you would want to split the path between the application server and those hosts into parts, and Wireshark may not be enough for investigation.</p><p>You may run Wireshark on the application server and watch whether, while the issue exists and you cannot ping them, one of the following happens:</p><ul><li><p>the application server is sending the icmp echo requests and nothing at all comes back (which means it knows the MAC address of the hosts but they either don't receive the requests at all or don't attempt to answer them),</p></li><li><p>the application server is sending the icmp echo requests but arp requests come back (which means the host has received the icmp request but doesn't know the MAC to which it should send the response),</p></li><li><p>the application server is sending arp requests instead of icmp echo requests and nothing comes back (which means that the arp cache of the server has timed out and the hosts do not respond even to the arp requests).</p></li></ul><p>Is the NetGear box really a hub or is it actually a switch?<br />
If it is a manageable switch, does its monitoring report any events on the ports to which the hosts are connected?<br />
If not, can you replace it with another switch before diving into some deep studies?<br />
</p><p>Also, it may sound not scientific enough but when connecting to the host directly from a PC, do you remove the cable from the NetGear and insert it to the PC, or do you disconnect the cable towards the switch port at the host end and replace it with another cable connected to the PC? Rotten or ill-crimped cables as well as specific understanding of L1 speed and duplex negotiation by some equipment vendors can create mysterious behaviour, while Wireshark can only tell you what happens starting from L2 upwards.</p><p>If we talk about robots, there may be EMC issues, long cables, damaged cables... all that affects L1 so it is invisible for Wireshark (except consequences).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '15, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Dec '15, 06:21</strong> </span></p></div></div><div id="comments-container-48567" class="comments-container"><span id="48599"></span><div id="comment-48599" class="comment"><div id="post-48599-score" class="comment-score"></div><div class="comment-text"><p>Dear Sindi<br />
</p><p>OK I will split in parts and Start from the application server</p><p>For now:<br />
</p><ul><li><p>yes it's a hub</p></li><li><p>I disconnect the cable towards the switch port at the host end and replace it with another cable connected to the PC</p></li></ul><p>I will let you know later<br />
We exclude L1 problems for now</p><p>Thanks for your Support<br />
Regards</p></div><div id="comment-48599-info" class="comment-info"><span class="comment-age">(17 Dec '15, 01:35)</span> <span class="comment-user userinfo">prometeus</span></div></div><span id="51336"></span><div id="comment-51336" class="comment"><div id="post-51336-score" class="comment-score"></div><div class="comment-text"><p>Hallo Sindy, I have a feedback with regards of this problems.</p><p>Basically we solved these problems installing near each robot a netgear gigabit swithc GS105Ev2.</p><p>What's happened in your opinion.</p><p>Regards</p></div><div id="comment-51336-info" class="comment-info"><span class="comment-age">(01 Apr '16, 01:32)</span> <span class="comment-user userinfo">prometeus</span></div></div><span id="51347"></span><div id="comment-51347" class="comment"><div id="post-51347-score" class="comment-score">1</div><div class="comment-text"><p>I could suspect two types of explanation, but too much information is missing:</p><ul><li><p>mechanical/chemical (the RJ-45 receptacles on the hub do not like the RJ-45 plugs of your cables due to incompatible mechanical tolerances, or because the hub's contacts are dirty/oxidized, assuming any hub cannot be newer than 10 years). Are there any vibrations coming from the robot's operation which could be transferred to the hubs/cables?</p></li><li><p>L1 electrical issue coming from the fact that the robots' interfaces do not implement 10 Mbit/s mode properly but work fine at 100 or even 1000 Mbit/s. You may confirm (but not refutate (widerlegen)) this assumption if you can force the GS105Ev2's ports to 10 Mbit/s Half Duplex with auto-negotiation off, simulating a 10 Mbit/s <em>hub</em> (hence half-duplex mode) as closely as possible this way. (I mention fixed values and switching off auto-negotiation as two separate settings because some equipment is able to perform the negotiation procedure but accept/offer only a single value of speed and a single value of duplex).</p></li></ul><p>But I guess once you've already spent the $$$ and it has solved the issue, there is little practical value of this information.</p></div><div id="comment-51347-info" class="comment-info"><span class="comment-age">(01 Apr '16, 06:52)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-48567" class="comment-tools"></div><div class="clear"></div><div id="comment-48567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

