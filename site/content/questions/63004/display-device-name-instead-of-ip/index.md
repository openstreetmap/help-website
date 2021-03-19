+++
type = "question"
title = "Display device name instead of IP"
description = '''I would like to somehow configure wireshark to display the device name (such as Bobs.iPhone or Bob.iMac) rather than the local IP (such as 192.168.1.172) — I&#x27;ve already configured Wireshark to resolve external IPs, but can&#x27;t figure out how to do the same for local IPs. I don&#x27;t have access to the rou...'''
date = "2017-07-22T19:22:00Z"
lastmod = "2017-07-22T20:56:00Z"
weight = 63004
keywords = [ "ip", "lan", "vlan", "configuration", "name-resolving" ]
aliases = [ "/questions/63004" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Display device name instead of IP](/questions/63004/display-device-name-instead-of-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63004-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to somehow configure wireshark to display the device name (such as Bobs.iPhone or Bob.iMac) rather than the local IP (such as 192.168.1.172) — I've already configured Wireshark to resolve external IPs, but can't figure out how to do the same for local IPs. I don't have access to the router control panel, and am using a mac.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">ip lan vlan configuration name-resolving</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '17, 19:22</strong></p><img src="https://secure.gravatar.com/avatar/fea2009f82772ec053325ee1a66efbf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johntheone88&#39;s gravatar image" /><p>johntheone88<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johntheone88 has no accepted answers">0%</span></p></div></div><div id="comments-container-63004" class="comments-container"></div><div id="comment-tools-63004" class="comment-tools"></div><div class="clear"></div><div id="comment-63004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63005"></span>

<div id="answer-container-63005" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63005-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Once you have enabled "Resolve Network Address" under Name Resolution in the View menu, you can right-click on the private IP address and click on "Edit Resolved name". There you will get an edit bar at the top to display whatever you wish.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '17, 20:56</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p>Rooster_50<br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-63005" class="comments-container"><span id="63006"></span><div id="comment-63006" class="comment"><div id="post-63006-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your message — unfortunately, I'm looking for the name to be automatically displayed, as I have no idea what the names of the internal IPs are (I'm sure there's some way to check using a 3rd party tool, but I'd like it to be automatic, if possible)</p></div><div id="comment-63006-info" class="comment-info"><span class="comment-age">(22 Jul '17, 22:58)</span> johntheone88</div></div><span id="63015"></span><div id="comment-63015" class="comment"><div id="post-63015-score" class="comment-score"></div><div class="comment-text"><blockquote><p>unfortunately, I'm looking for the name to be automatically displayed, as I have no idea what the names of the internal IPs are</p></blockquote><p>In order for the name to be automatically displayed:</p><ul><li><em>somebody</em> has to have an idea what the names of the internal IPs are;</li><li>that somebody has to make that information available in some form that Wireshark can access.</li></ul><p>So the first step is to find that somebody and ask them where to get the mappings of IP addresses to names in a form that Wireshark can use (which would either be a hosts file or a DNS server).</p></div><div id="comment-63015-info" class="comment-info"><span class="comment-age">(23 Jul '17, 11:48)</span> Guy Harris ♦♦</div></div><span id="63029"></span><div id="comment-63029" class="comment"><div id="post-63029-score" class="comment-score"></div><div class="comment-text"><p>If the devices obtain IP address via DHCP, some DHCP servers can set a DNS Dynamic update (A and PTR record). This would allow Wireshark (if querying the local DNS server) to resolve the internal addresses.</p></div><div id="comment-63029-info" class="comment-info"><span class="comment-age">(23 Jul '17, 20:17)</span> Rooster_50</div></div></div><div id="comment-tools-63005" class="comment-tools"></div><div class="clear"></div><div id="comment-63005-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

