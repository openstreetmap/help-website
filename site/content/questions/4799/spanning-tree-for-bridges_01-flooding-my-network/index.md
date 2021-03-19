+++
type = "question"
title = "Spanning-tree-(for-bridges)_01 flooding my network"
description = '''I am wondering what this is  31 0.088694 00:00:00_00:00:00 Spanning-tree-(for-bridges)_01 MAC CTRL 60 MAC PAUSE: pause_time: 8192 quanta The network slows down and pings are 2ms to about 6ms if the switch (new unmanaged gigabit) is rebooted things will go back to normal for a while 4-6 hours or even...'''
date = "2011-06-28T19:32:00Z"
lastmod = "2011-06-29T16:42:00Z"
weight = 4799
keywords = [ "mac-pause" ]
aliases = [ "/questions/4799" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Spanning-tree-(for-bridges)\_01 flooding my network](/questions/4799/spanning-tree-for-bridges_01-flooding-my-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4799-score" class="post-score" title="current number of votes">0</div><span id="post-4799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am wondering what this is</p><p>31 0.088694 00:00:00_00:00:00 Spanning-tree-(for-bridges)_01 MAC CTRL 60 MAC PAUSE: pause_time: 8192 quanta</p><p>The network slows down and pings are 2ms to about 6ms if the switch (new unmanaged gigabit) is rebooted things will go back to normal for a while 4-6 hours or even several days. There is a mix of workstation nics</p><p>Thanks folks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac-pause" rel="tag" title="see questions tagged &#39;mac-pause&#39;">mac-pause</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '11, 19:32</strong></p><img src="https://secure.gravatar.com/avatar/61aef5277be420315e1f9549400629a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Buckshot&#39;s gravatar image" /><p><span>Buckshot</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Buckshot has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jun '11, 03:31</strong> </span></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span></p></div></div><div id="comments-container-4799" class="comments-container"><span id="4809"></span><div id="comment-4809" class="comment"><div id="post-4809-score" class="comment-score">1</div><div class="comment-text"><p>PAUSE frames are link local. Meaning it only lives from RJ45 to RJ45 and doesn't get propagated beyond that. So if you are seeing this everywhere, it must be "everywhere connected to switch X" correct? PAUSE frame can be stupid at times. One thing the standard lacked was the ability to <em>stop</em> the pause condition when things got better. Some will send a puase-time set to zero, but I don't know that it's universal. You only need the PAUSE in rare conditions, so if the new switch is suspect, try turning off PAUSE fucntion completely. And ask the vendor if an FW update is avail. Good Luck!</p></div><div id="comment-4809-info" class="comment-info"><span class="comment-age">(29 Jun '11, 06:00)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-4799" class="comment-tools"></div><div class="clear"></div><div id="comment-4799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4807"></span>

<div id="answer-container-4807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4807-score" class="post-score" title="current number of votes">2</div><span id="post-4807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You have caught the rather elusive MAC PAUSE frame. The pause frame instructs the receiver to stop sending data for a certain time. The time is specified in the unit "quanta", where one quanta is time needed to send 512 bits. For a Gigabit network 1 Quanta equals 512 nanoseconds.</p><p>The 8192 quanta from your trace effectively shut down the receiver for roughly 4 milliseconds, which aligns nicely with the increase in the RTT from 2 to 6 msec.</p><p>MAC pause is a special frame that can be send by a switch or an end system to tell it's neighbor to slow down.</p><p>Typical scenarios for this frame are:</p><ul><li>A server is sending data faster than the switch can forward the frames. The pause frame would instruct the server to stop sending data</li><li>An end system can not process data as quickly as it floods in. The pause frame instructs the switch to stop sending data and buffer the frames.</li></ul><p>Some managed switches and NIC drivers can send and process the pause frames. This is a feature of the switch or the driver, and by far not supported by all devices.</p><p>If I can configure pause frames I usually allow the switch to slow down a workstation or server, but not vice versa. If any workstation can tell the switch to shut up you will quickly run out of buffers.</p><p>The sender of the MAC pause frame should transmit another frame with 0 quanta to inform the remote end that the device is back in business.</p><p>What makes me curious is your source MAC address of 00:00:00:00:00:00, which does not look like it is hand crafted. Try to track down the MAC address. Disable the pause frame on workstations and servers if you have unmanaged switches.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '11, 03:29</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-4807" class="comments-container"></div><div id="comment-tools-4807" class="comment-tools"></div><div class="clear"></div><div id="comment-4807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4826"></span>

<div id="answer-container-4826" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4826-score" class="post-score" title="current number of votes">0</div><span id="post-4826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you very much. The MAC address of 00:00:00:00:00:00 does throw me off but I know the switch that is the problem... now I just have to try and track down the offenders</p><p>Thanks again</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '11, 16:42</strong></p><img src="https://secure.gravatar.com/avatar/61aef5277be420315e1f9549400629a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Buckshot&#39;s gravatar image" /><p><span>Buckshot</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Buckshot has no accepted answers">0%</span></p></div></div><div id="comments-container-4826" class="comments-container"></div><div id="comment-tools-4826" class="comment-tools"></div><div class="clear"></div><div id="comment-4826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

