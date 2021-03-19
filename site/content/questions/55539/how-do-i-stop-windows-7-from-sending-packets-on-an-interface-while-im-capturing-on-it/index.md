+++
type = "question"
title = "How do I stop Windows 7 from sending packets on an interface while I&#x27;m capturing on it?"
description = '''I have my PC connected to a CISCO switch port with the port in SPAN - However I see some traffic initiated by the PC. these appear to be broadcasts of Netbios name resolutions I tried changing the binding on the port and removed all protocols - that shuts the port down and I can not use it for captu...'''
date = "2016-09-13T15:37:00Z"
lastmod = "2016-10-08T22:54:00Z"
weight = 55539
keywords = [ "windows7" ]
aliases = [ "/questions/55539" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I stop Windows 7 from sending packets on an interface while I'm capturing on it?](/questions/55539/how-do-i-stop-windows-7-from-sending-packets-on-an-interface-while-im-capturing-on-it)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55539-score" class="post-score" title="current number of votes">0</div><span id="post-55539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have my PC connected to a CISCO switch port with the port in SPAN - However I see some traffic initiated by the PC. these appear to be broadcasts of Netbios name resolutions I tried changing the binding on the port and removed all protocols - that shuts the port down and I can not use it for capture. I happen to have Airmagnet software installed on this PC and binding it just to that does appear to work.<br />
Is there a way on windows to keep the port up but not have it used for anything so I can see only traffic initiated from elsewhere? For example a "Wireshark capture protocol" that can be selected for the port? TIA Ross</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '16, 15:37</strong></p><img src="https://secure.gravatar.com/avatar/3a058cc2ff4addb9763d000a44ad873d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rjwilson01&#39;s gravatar image" /><p><span>rjwilson01</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rjwilson01 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Sep '16, 18:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-55539" class="comments-container"><span id="55550"></span><div id="comment-55550" class="comment"><div id="post-55550-score" class="comment-score"></div><div class="comment-text"><p>I operate in this manner all the time with my WindowsXP, Windows7, and Windows8.1 OSs. I deselect all the bindings and then can only receive traffic, which it does. I recommend this to my colleagues when they have a dedicated wired sniffing adapter. This works with Linux as well if I zero out the IP address.</p><p>Except for the (hopefully) minor inconvenience of having to discard that traffic once capture is there any other problem? Cisco SPAN, by default, does not pass ingress traffic on a span port destination so I would think it would not be affecting the network proper due to it's presence.</p><p>Default Config: Ingress forwarding (destination port) Disabled</p><p>What OS are you on?</p></div><div id="comment-55550-info" class="comment-info"><span class="comment-age">(14 Sep '16, 02:37)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="55551"></span><div id="comment-55551" class="comment"><div id="post-55551-score" class="comment-score">1</div><div class="comment-text"><p>I see you are on Windows7 - didn't read the title. I know our corporate policy is that when a wired link is available WiFi turns off. This isn't the same thing as that is controlled by the BIOS in the Dell's we use but could there be some group policy or something blocking the traffic? Or maybe anti-virus/firewall?</p></div><div id="comment-55551-info" class="comment-info"><span class="comment-age">(14 Sep '16, 04:03)</span> <span class="comment-user userinfo">Bob Jones</span></div></div></div><div id="comment-tools-55539" class="comment-tools"></div><div class="clear"></div><div id="comment-55539-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="55563"></span>

<div id="answer-container-55563" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55563-score" class="post-score" title="current number of votes">0</div><span id="post-55563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In the adapter settings, uncheck IPv4 and IPv6. This will disable the stacks and prevent TX on the adapter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '16, 17:32</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p><span>Rooster_50</span><br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-55563" class="comments-container"></div><div id="comment-tools-55563" class="comment-tools"></div><div class="clear"></div><div id="comment-55563-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56245"></span>

<div id="answer-container-56245" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56245-score" class="post-score" title="current number of votes">0</div><span id="post-56245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thnaks - after a lot of fiddling - What I am seeing appears to be a feature of Cisco's Anyconnect VPN software With the Cisco software installed If I un-link all protocols - the adapter gets disabled and Wire-shark cannot use it On a very similar machine (same base build image ) but without the Cisco's any-connect added what you described works and I can unlink all protocols and the card does not get disabled.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '16, 22:54</strong></p><img src="https://secure.gravatar.com/avatar/3a058cc2ff4addb9763d000a44ad873d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rjwilson01&#39;s gravatar image" /><p><span>rjwilson01</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rjwilson01 has no accepted answers">0%</span></p></div></div><div id="comments-container-56245" class="comments-container"></div><div id="comment-tools-56245" class="comment-tools"></div><div class="clear"></div><div id="comment-56245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

