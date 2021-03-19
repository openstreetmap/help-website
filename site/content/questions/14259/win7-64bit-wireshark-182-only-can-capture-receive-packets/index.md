+++
type = "question"
title = "win7 64bit wireshark 1.8.2 only can capture receive packets"
description = '''I can get no http.request.method == GET packets at all~ I can&#x27;t see my sent packets'''
date = "2012-09-14T00:44:00Z"
lastmod = "2016-09-08T05:51:00Z"
weight = 14259
keywords = [ "64bit", "windows7", "1.8.2" ]
aliases = [ "/questions/14259" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [win7 64bit wireshark 1.8.2 only can capture receive packets](/questions/14259/win7-64bit-wireshark-182-only-can-capture-receive-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14259-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can get no http.request.method == GET packets at all~ I can't see my sent packets</p></div><div id="question-tags" class="tags-container tags">64bit windows7 1.8.2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '12, 00:44</strong></p><img src="https://secure.gravatar.com/avatar/a4a6a846f8a4cb9f0c90bd834e51651c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qsLampard&#39;s gravatar image" /><p>qsLampard<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qsLampard has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Sep '12, 08:36</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-14259" class="comments-container"><span id="14560"></span><div id="comment-14560" class="comment"><div id="post-14560-score" class="comment-score"></div><div class="comment-text"><p>Interesting enough, or not, I am experiencing the same issue as you. I am running an IDS via a tap between two routers and I only see outbound traffic, nothing inbound even though the host is able to connect with no issues. The packets are going through but I am not able to see them. I've tried multiple hosts as an IDS and they all are Win 7 x64.</p><p>Out of curiosity - do you only see echo requests and no replies when you ping something?</p><p>What happens when you use Microsoft Network Monitor?</p></div><div id="comment-14560-info" class="comment-info"><span class="comment-age">(26 Sep '12, 15:18)</span> DigitalSyn</div></div><span id="14567"></span><div id="comment-14567" class="comment"><div id="post-14567-score" class="comment-score"></div><div class="comment-text"><p>I can see the echo replies but no requests~ By the way, I don't know how to use Microsoft Network Monitor</p></div><div id="comment-14567-info" class="comment-info"><span class="comment-age">(26 Sep '12, 21:23)</span> qsLampard</div></div><span id="14571"></span><div id="comment-14571" class="comment"><div id="post-14571-score" class="comment-score"></div><div class="comment-text"><p>Interesting again, I am experiencing the same issue.<br />
</p><p>MS NETMON, took me a little bit to figure it out. Can't tell you what to do of course but I would download, install it and fire it up. I don't have it loaded on the host I am at (can't install - no amdin) but there is an option to start capture, and then another to begin. When I head home tonight I will do a quick tut.</p></div><div id="comment-14571-info" class="comment-info"><span class="comment-age">(27 Sep '12, 07:10)</span> DigitalSyn</div></div><span id="14631"></span><div id="comment-14631" class="comment"><div id="post-14631-score" class="comment-score"></div><div class="comment-text"><p>Sorry partner for the late response. Actually I was rebuilding my IDS from the ground up for the past 4 days and I may have have a possible solution for you. Drop Win 7 x64; it is most likely how Microsoft handles the driver for the NIC cards and that is affecting how we see, or not see, full PCAP sessions. I didn't try a 32-bit version of Win 7; I went ahead and loaded Ubuntu 12.04 and I have been sipping on wine and eating cheese watching all of my PCAP on the screen.</p><p>Good luck ~</p></div><div id="comment-14631-info" class="comment-info"><span class="comment-age">(01 Oct '12, 16:21)</span> DigitalSyn</div></div><span id="14633"></span><div id="comment-14633" class="comment"><div id="post-14633-score" class="comment-score"></div><div class="comment-text"><p>actually, i have tried 32-bit version of Win 7, and it worked~~</p></div><div id="comment-14633-info" class="comment-info"><span class="comment-age">(01 Oct '12, 21:14)</span> qsLampard</div></div><span id="14634"></span><div id="comment-14634" class="comment not_top_scorer"><div id="post-14634-score" class="comment-score"></div><div class="comment-text"><p>Were you using the x64 version of Wireshark on Win7 x64? I and many colleagues capture all the time on Win7 x64 using the 32 bit version of Wireshark without any issues at all.</p></div><div id="comment-14634-info" class="comment-info"><span class="comment-age">(01 Oct '12, 23:46)</span> grahamb ♦</div></div><span id="14643"></span><div id="comment-14643" class="comment not_top_scorer"><div id="post-14643-score" class="comment-score"></div><div class="comment-text"><p>From a previous post - it looks like Wireshark 32-bit should work as well. Give that a go, as well qsLampard, on your Win7 x64 rig.</p></div><div id="comment-14643-info" class="comment-info"><span class="comment-age">(02 Oct '12, 12:02)</span> DigitalSyn</div></div></div><div id="comment-tools-14259" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-14259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55391"></span>

<div id="answer-container-55391" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55391-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="https://ask.wireshark.org/questions/11714/only-inbound-traffic">only-inbound-traffic</a> and search for other questions related to missing outbound traffic. Keywords <em>inbound</em> and <em>outbound</em> may help help.</p><p>See <a href="https://wiki.wireshark.org/CaptureSetup/InterferingSoftware">InterferingSoftware</a></p><p>In my case, installed VPN software prevented seeing outbound traffic and had to be uninstalled.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '16, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/01aa855068a6805deac3f3371c5b00d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kbulgrien&#39;s gravatar image" /><p>kbulgrien<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kbulgrien has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Sep '16, 05:53</p></div></div><div id="comments-container-55391" class="comments-container"></div><div id="comment-tools-55391" class="comment-tools"></div><div class="clear"></div><div id="comment-55391-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

