+++
type = "question"
title = "Source/client packets don&#x27;t display in wireshark but inbound response packet are seen"
description = '''Weird issue. I used to see all outbound and inbound packets in wireshark on my Lenovo Thinkpad T520 but now I can&#x27;t see or capture any outbound packets but I certainly see the inbound/response packets. I am using Win7, fully patched, with 1.8.1 currently but upgrading didn&#x27;t help. My colleagues who ...'''
date = "2013-07-09T16:28:00Z"
lastmod = "2013-07-10T01:10:00Z"
weight = 22771
keywords = [ "inbound" ]
aliases = [ "/questions/22771" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Source/client packets don't display in wireshark but inbound response packet are seen](/questions/22771/sourceclient-packets-dont-display-in-wireshark-but-inbound-response-packet-are-seen)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22771-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Weird issue. I used to see all outbound and inbound packets in wireshark on my Lenovo Thinkpad T520 but now I can't see or capture any outbound packets but I certainly see the inbound/response packets. I am using Win7, fully patched, with 1.8.1 currently but upgrading didn't help. My colleagues who have T520 models works without issue. I have removed the network drivers and re-installed them. Anyone have any ideas why this might be happening?</p></div><div id="question-tags" class="tags-container tags">inbound</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '13, 16:28</strong></p><img src="https://secure.gravatar.com/avatar/c439411f6f3c7ebcb7ff638c5866dc61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="markvi&#39;s gravatar image" /><p>markvi<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="markvi has no accepted answers">0%</span></p></div></div><div id="comments-container-22771" class="comments-container"><span id="22772"></span><div id="comment-22772" class="comment"><div id="post-22772-score" class="comment-score"></div><div class="comment-text"><p>Is this a wired or wireless connection? If wired, are there VLAN tags present?</p></div><div id="comment-22772-info" class="comment-info"><span class="comment-age">(09 Jul '13, 16:38)</span> Jasper ♦♦</div></div><span id="22778"></span><div id="comment-22778" class="comment"><div id="post-22778-score" class="comment-score"></div><div class="comment-text"><p>Is it possible that you have more than 1 interface and outbound packets are leaving on one interface while inbound packets are arriving on another interface? Wireshark 1.8 supports capturing on multiple interfaces simultaneously, so you could try doing that.</p><p>Do you have any capture filter applied which might be excluding outbound packets?</p></div><div id="comment-22778-info" class="comment-info"><span class="comment-age">(09 Jul '13, 17:58)</span> cmaynard ♦♦</div></div><span id="22799"></span><div id="comment-22799" class="comment"><div id="post-22799-score" class="comment-score"></div><div class="comment-text"><p>The laptop has both a wired and wireless interface. I have tried the various combinations including enabling both, selected only the wired, selecting only the wireless, etc and no combo seems to make a difference. I have verified there is no filter attached and the settings look correct.</p></div><div id="comment-22799-info" class="comment-info"><span class="comment-age">(10 Jul '13, 06:16)</span> markvi</div></div></div><div id="comment-tools-22771" class="comment-tools"></div><div class="clear"></div><div id="comment-22771-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22787"></span>

<div id="answer-container-22787" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22787-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess it's some <a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">interfering software</a> (AV, Firewall, Endpoint Security, VPN Client, etc.). Disable all of them OR boot the system with a bootable Linux CD (BackTrack, Ubuntu, Knoppix) and then try again, just to rule out any hardware problems. If it works with Linux, it's most certainly some software on your system or a system setting (TCP offloading in the driver, etc. - see links below).</p><p>Please see also (my) answers to the following questions (especially regarding chimney).</p><blockquote><p><a href="http://ask.wireshark.org/questions/11714/only-inbound-traffic">http://ask.wireshark.org/questions/11714/only-inbound-traffic</a><br />
<a href="http://ask.wireshark.org/questions/13131/wireshark-does-not-capture-packets-w-payloads">http://ask.wireshark.org/questions/13131/wireshark-does-not-capture-packets-w-payloads</a><br />
<a href="http://ask.wireshark.org/questions/17865/tcp-retransmits-on-windows-server-for-slow-connections">http://ask.wireshark.org/questions/17865/tcp-retransmits-on-windows-server-for-slow-connections</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '13, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jul '13, 01:10</p></div></div><div id="comments-container-22787" class="comments-container"><span id="22800"></span><div id="comment-22800" class="comment"><div id="post-22800-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the info. I can try using the Linux boot approach to rule out hardware.</p></div><div id="comment-22800-info" class="comment-info"><span class="comment-age">(10 Jul '13, 06:18)</span> markvi</div></div><span id="22808"></span><div id="comment-22808" class="comment"><div id="post-22808-score" class="comment-score"></div><div class="comment-text"><p>O.K. If that works, please disable chimney first (see one of the links) and then check for any interfering software (see above).</p></div><div id="comment-22808-info" class="comment-info"><span class="comment-age">(10 Jul '13, 07:09)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-22787" class="comment-tools"></div><div class="clear"></div><div id="comment-22787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

