+++
type = "question"
title = "Finding router model, release number and firmware using wireshark"
description = '''Hi, Is there away to find the router model, firmware and the release number using wireshark? Have a packet I am playing around with and a few questions I a friend sent me and am trying to learn the correct ways to use wireshark to figure them out. '''
date = "2017-07-18T10:05:00Z"
lastmod = "2017-07-18T15:01:00Z"
weight = 62844
keywords = [ "router" ]
aliases = [ "/questions/62844" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Finding router model, release number and firmware using wireshark](/questions/62844/finding-router-model-release-number-and-firmware-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62844-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Is there away to find the router model, firmware and the release number using wireshark? Have a packet I am playing around with and a few questions I a friend sent me and am trying to learn the correct ways to use wireshark to figure them out.</p></div><div id="question-tags" class="tags-container tags">router</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '17, 10:05</strong></p><img src="https://secure.gravatar.com/avatar/aee8489136c023abf69ed04b97ec6c26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pyrotaz&#39;s gravatar image" /><p>pyrotaz<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pyrotaz has no accepted answers">0%</span></p></div></div><div id="comments-container-62844" class="comments-container"><span id="62854"></span><div id="comment-62854" class="comment"><div id="post-62854-score" class="comment-score"></div><div class="comment-text"><p>Here is the pcap file I need help with attempting to figure out the following: The IP address of the router? The model of the router if possible? The firmware of the router? The release number of the router is using? And last the ip address of the user who logged into the router admin panel?</p><p><a href="https://www.dropbox.com/s/4thsx9xa52gmalq/NCL-2015-PCAP3.cap?dl=0">pcap file</a></p></div><div id="comment-62854-info" class="comment-info"><span class="comment-age">(18 Jul '17, 14:38)</span> pyrotaz</div></div><span id="62855"></span><div id="comment-62855" class="comment"><div id="post-62855-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-62855-info" class="comment-info"><span class="comment-age">(18 Jul '17, 14:45)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-62844" class="comment-tools"></div><div class="clear"></div><div id="comment-62844-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62846"></span>

<div id="answer-container-62846" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62846-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>With just a few exceptions, a single packet is of a little use here. Some tools do detect equipment properties by stimulating it with connection attempts using various protocols and comparing the reaction to a database of known ones, but a single packet sent by a given device tells you almost nothing expect if the model etc. would be intentionally written there.</p><p>An LLDP frame is an example of such one, it tells you a lot about its sender because it is its very purpose, but it can be only captured on a neighboring equipment. Similar vendor-specific protocols (e.g. CDP) exist. Any packet from a given device captured in the LAN has that device's MAC address as a source but a MAC address can only tell you the vendor (also not always), rarely the exact model and never the firmware release (because MAC address normally doesn't change depending on the firmware release).</p><p>Some application protocols (like e.g. SIP) also may include model and firmware information, but it is not a rule.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '17, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jul '17, 10:44</p></div></div><div id="comments-container-62846" class="comments-container"><span id="62851"></span><div id="comment-62851" class="comment"><div id="post-62851-score" class="comment-score"></div><div class="comment-text"><p>If the router is SNMP-enabled, it ought to be possible to explicitly query the router for this type of information.</p></div><div id="comment-62851-info" class="comment-info"><span class="comment-age">(18 Jul '17, 11:51)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-62846" class="comment-tools"></div><div class="clear"></div><div id="comment-62846-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62856"></span>

<div id="answer-container-62856" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62856-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, you have changed the scope of the question seriously - this is not a single packet, this is a capture of a good deal of wireless traffic.</p><p>The file contains the WPA negotiation of two Apple devices so if you know the passphrase to the WiFi network, you should be able to make Wireshark decrypt the WPA communication for you, there is a Wireshark manual page covering that topic and a number of Questions on this site, dealing with some issues people ran into. Once you succeed here, there should be a plaintext http communication which should contain the information about router firmware version etc., and the IP addresses will become visible.</p><p>There is another nice function of Wireshark which allows you to save the html pages transmitted by packets captured, so you may even see the graphical rendering of them if you open the saved files in a browser.</p><p>I suppose you do have the passphrase, otherwise the quest would have no solution. Rumour has it that TKIP is a weak encryption but Wireshark doesn't contain tools for decrypting TKIP without knowing the passphrase.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '17, 15:01</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-62856" class="comments-container"><span id="62859"></span><div id="comment-62859" class="comment"><div id="post-62859-score" class="comment-score"></div><div class="comment-text"><p>Note that if the router is a home Wi-Fi router, it might not support the LLDP or CDP protocols; I think those are mainly used for "enterprise" equipment, to keep track of the equipment in a complex network. Therefore, there might not be any packets carrying detailed information about the router.</p><p>To determine that, you'd have to decrypt the traffic, using the password, as sindy indicated. If there isn't LLDP or CDP traffic, perhaps there will be other traffic giving that information.</p></div><div id="comment-62859-info" class="comment-info"><span class="comment-age">(18 Jul '17, 18:49)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-62856" class="comment-tools"></div><div class="clear"></div><div id="comment-62856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

