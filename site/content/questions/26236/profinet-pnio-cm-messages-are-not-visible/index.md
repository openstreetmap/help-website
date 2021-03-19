+++
type = "question"
title = "Profinet: PNIO-CM messages are not visible"
description = '''Dear Sir/Madam, I found the following problem, though i cannot find a possible solution to fix it. When trying to measure the startup of a Profinet Device, the IO controller will set a connection to the IO Device using application and communication relations. With the newest build of Wireshark (Vers...'''
date = "2013-10-21T04:41:00Z"
lastmod = "2013-10-21T04:58:00Z"
weight = 26236
keywords = [ "pnio-cm", "pnio", "profinet" ]
aliases = [ "/questions/26236" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Profinet: PNIO-CM messages are not visible](/questions/26236/profinet-pnio-cm-messages-are-not-visible)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26236-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Sir/Madam,</p><p>I found the following problem, though i cannot find a possible solution to fix it. When trying to measure the startup of a Profinet Device, the IO controller will set a connection to the IO Device using application and communication relations. With the newest build of Wireshark (Version 1.10.2 (SVN Rev 51934 from /trunk-1.10)) and WinPcap 4.1.3 i cannot seem to measure these messages. Using another computer this works fine though... Is there a way to visualize these messages, or aren't these hidden at all? The used protocol is PNIO, and the corresponding frames are PNIO-CM frames, which is an underlying protocol using the Profinet IO Context Manager. I can see every PNIO frame on the network, just not the PNIO-CM frames.</p><p>What i already tried is the following:</p><p>*Reinstall wireshark with newest release and reinstall WinPcap aswell</p><p>*Clear all user preferences</p><p>*Measure with another computer (gave no problems)</p><p>Please note i did have to go into the registry and change some values to be able to visualize the VLAN tag in the Profinet (Industrial Ethernet) frames. This was completed without error.</p></div><div id="question-tags" class="tags-container tags">pnio-cm pnio profinet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '13, 04:41</strong></p><img src="https://secure.gravatar.com/avatar/3211fe7876229f82af1d95e64500c2cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lique&#39;s gravatar image" /><p>Lique<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lique has no accepted answers">0%</span></p></div></div><div id="comments-container-26236" class="comments-container"></div><div id="comment-tools-26236" class="comment-tools"></div><div class="clear"></div><div id="comment-26236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26239"></span>

<div id="answer-container-26239" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26239-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>*Measure with another computer (gave no problems)</p></blockquote><p>O.K. so it must be related to that one system. And <strong>usually</strong> if you don't see some frames while capturing there is some security and/or network related software installed, that blocks those frames.</p><p>Please check, if any <a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">interfering software</a> is installed on that system (like AV, IPS, IDS, Endpoint Security, <strong>VPN clients</strong>, Firewalls, etc.). If so, first try to disable it. If that does not help (sometimes disabling isn't enough), please uninstall the suspicious piece of software.</p><p>A few days ago, a user reported, that DNE Update caused problems with outgoing frames.</p><blockquote><p><a href="http://ask.wireshark.org/questions/26150/i-see-only-http11-200-ok-response-packets">http://ask.wireshark.org/questions/26150/i-see-only-http11-200-ok-response-packets</a></p></blockquote><p>So, please check any network related software as well.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '13, 04:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Oct '13, 04:59</p></div></div><div id="comments-container-26239" class="comments-container"><span id="26241"></span><div id="comment-26241" class="comment"><div id="post-26241-score" class="comment-score"></div><div class="comment-text"><p>Dear Kurt,</p><p><strong>Disabling the Symantec Endpoint Protection did work indeed</strong>. I will try and find settings to let all Profinet messages pass through and post them here to help future problems</p><p>Kind Regards,</p><p>Thomas</p></div><div id="comment-26241-info" class="comment-info"><span class="comment-age">(21 Oct '13, 05:11)</span> Lique</div></div><span id="26242"></span><div id="comment-26242" class="comment"><div id="post-26242-score" class="comment-score"></div><div class="comment-text"><p>Good and thanks for the updates on Symantec Endpoint!</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-26242-info" class="comment-info"><span class="comment-age">(21 Oct '13, 05:14)</span> Kurt Knochner ♦</div></div><span id="26244"></span><div id="comment-26244" class="comment"><div id="post-26244-score" class="comment-score"></div><div class="comment-text"><p>To allow the PNIO-CM messages through your symantec endpoint protection firewall, edit the following firewall rules:</p><p>Allow all traffic on UDP using remote &amp; local ports 1212 (lupa), 34964 (profinet-cm), 49154 and 49155</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Instellingen_UDP_Ports_SEP.png" alt="alt text" /></p><p>Kind regards,</p><p>Thomas</p></div><div id="comment-26244-info" class="comment-info"><span class="comment-age">(21 Oct '13, 06:11)</span> Lique</div></div></div><div id="comment-tools-26239" class="comment-tools"></div><div class="clear"></div><div id="comment-26239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

