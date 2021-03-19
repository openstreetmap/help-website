+++
type = "question"
title = "Download from mac on wireless decreases until it stops."
description = '''Hi all, just trying to get up to speed on Wireshark, I want to see what&#x27;s going on and why it ultimately fails. The issue briefly mentioned is, I have a PC system with broadband being supplied by Virgin and a Home 120 modem attached to a Netgear WGT624 router, the PC functions fine and networking/in...'''
date = "2010-10-26T07:42:00Z"
lastmod = "2010-10-26T10:08:00Z"
weight = 654
keywords = [ "wireless", "downloads", "macbook" ]
aliases = [ "/questions/654" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Download from mac on wireless decreases until it stops.](/questions/654/download-from-mac-on-wireless-decreases-until-it-stops)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-654-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, just trying to get up to speed on Wireshark, I want to see what's going on and why it ultimately fails.</p><p>The issue briefly mentioned is, I have a PC system with broadband being supplied by Virgin and a Home 120 modem attached to a Netgear WGT624 router, the PC functions fine and networking/internet is pretty much as it should be. When the Macbook connects wirelessly again internet and network are all good and signal strength is strong with a good channel selection, it does however have the odd connection drop. When the macbook tries to connect the kb's start to fall ultimately resulting in a download fail, but it also knocks out the internet for itself and the PC and only a router reboot gets it back. The file that is being downloaded is the Microsoft Office trial 2008 from Mactopia, but others also fail.</p><p>I think I'm going to need some help, I'm not sure which filters I need to apply to the macs airport to understand what's happening and how to read the information being given.</p><p>I think this is an interesting case, and would love to at the very least understand why its happening but would be great to solve the puzzle.</p><p>Kind regards Lee</p></div><div id="question-tags" class="tags-container tags">wireless downloads macbook</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '10, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/cdc773cf4e492c724d829b8f376fba29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="darkan9el&#39;s gravatar image" /><p>darkan9el<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="darkan9el has no accepted answers">0%</span></p></div></div><div id="comments-container-654" class="comments-container"><span id="657"></span><div id="comment-657" class="comment"><div id="post-657-score" class="comment-score"></div><div class="comment-text"><p>First step is to capture the WLAN traffic. You want to capture the management, control and data frames - as I work on a Windows host, I use AirPcap adapters to let me do this.</p><p>Don't apply any filters to start -just capture on the channel that your systems are using. Afterwards you can apply a display filter for traffic to/from a specific WLAN hardware address - type wlan. into the display area and it will show you all the field names associated with WLAN traffic for filtering.</p><p>Start with the traffic capture first though.</p></div><div id="comment-657-info" class="comment-info"><span class="comment-age">(26 Oct '10, 08:52)</span> lchappell ♦</div></div></div><div id="comment-tools-654" class="comment-tools"></div><div class="clear"></div><div id="comment-654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="670"></span>

<div id="answer-container-670" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-670-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you for the info will run a capture to see what I get back.</p><p>thanks again for the advice.</p><p>much appreciated</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '10, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/cdc773cf4e492c724d829b8f376fba29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="darkan9el&#39;s gravatar image" /><p>darkan9el<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="darkan9el has no accepted answers">0%</span></p></div></div><div id="comments-container-670" class="comments-container"></div><div id="comment-tools-670" class="comment-tools"></div><div class="clear"></div><div id="comment-670-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

