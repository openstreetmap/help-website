+++
type = "question"
title = "Pause frame flood"
description = '''Every couple of weeks our network gets hit by a pause frame flood that effectively brings down our entire network. This has happened at least five times now since I started my new job as sole IT-technician at a manufacturing plant. Our network is entirely made up of dumb L2 switches so locating the ...'''
date = "2013-03-16T09:52:00Z"
lastmod = "2013-03-16T10:50:00Z"
weight = 19559
keywords = [ "flood", "stp", "mac-pause" ]
aliases = [ "/questions/19559" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Pause frame flood](/questions/19559/pause-frame-flood)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19559-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Every couple of weeks our network gets hit by a pause frame flood that effectively brings down our entire network. This has happened at least five times now since I started my new job as sole IT-technician at a manufacturing plant. Our network is entirely made up of dumb L2 switches so locating the offending device has proven to be tricky.</p><p>So far I have only managed to find which port on our central patch panel the packet are coming from, . Pulling the TP-cable instantly brings the rest of the network back up. The flood lasts for about 30 to 45 minutes, after that I can plug the cable back in and everything looks normal again, like nothing ever happened.</p><p>So, I was hoping that somebody here maybe has some knowledge of what might be going on.</p><p>Every frame looks like this, and as you can see the source MAC isn't even a real MAC address, but instead spells out REALTK in ASCII.</p><pre><code>0000  01 80 c2 00 00 01 52 45  41 4c 54 4b 88 08 00 01   ......RE ALTK....  
0010  ff ff 00 00 00 00 00 00  00 00 00 00 00 00 00 00   ........ ........  
0020  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00   ........ ........  
0030  00 00 00 00 00 00 00 00  00 00 00 00               ........ ....</code></pre><p>I would really appreciate if somebody could shed some light on this.</p></div><div id="question-tags" class="tags-container tags">flood stp mac-pause</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '13, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/147797d01a44f1125706dd7e2fb496b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JonC&#39;s gravatar image" /><p>JonC<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JonC has no accepted answers">0%</span></p></div></div><div id="comments-container-19559" class="comments-container"><span id="19561"></span><div id="comment-19561" class="comment"><div id="post-19561-score" class="comment-score"></div><div class="comment-text"><p>If you haven't already done so, a web search for the terms "spanning tree for bridges", "pause frame" will find hits about pause frame floods &amp; etc. which may be of help.</p><p>Also search "ethernet pause frame" "flood"</p></div><div id="comment-19561-info" class="comment-info"><span class="comment-age">(16 Mar '13, 10:35)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-19559" class="comment-tools"></div><div class="clear"></div><div id="comment-19559-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19563"></span>

<div id="answer-container-19563" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19563-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is a <em>real</em> MAC address, just not what we're used to. It has the Locally Administered bit set, so it's up to the network administrator to make sure it's unique within the realm of the network.</p><p>That's the theory at least, in reality I think it's just a reference to a Realtek network interface.</p><p>The fact that it affects your whole network tells me that the switches used are not 802.1D compliant, otherwise they would have trapped these pause frames.</p><p>The fact that it lasts a good half an hour means that some network device got it panties in a bunch. With this 'made up' source mac address it's not easy to find out which. At least you know from which uplink it comes, so it's just a matter of tracking it down from there. To give you time to do that get yourself a 802.1D compliant switch and patch it in between the central patch panel and the offending uplink. That at least would isolate the problem so only part of the network would be affected. Make sure to test out this switch with ethtool or alike before patching it in.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '13, 10:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19563" class="comments-container"></div><div id="comment-tools-19563" class="comment-tools"></div><div class="clear"></div><div id="comment-19563-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

