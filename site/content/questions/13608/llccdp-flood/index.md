+++
type = "question"
title = "LLC/CDP flood"
description = '''Hi,  I am seeing on my network a flood of LLC packets all seeming to come from the same MAC address (which is a mitel phone about 4 switches away from the capturing PC).  Even stranger it is now unpluged and I am still seeing the traffic!!  So I need some help in picking apart the wireshark log and ...'''
date = "2012-08-14T04:23:00Z"
lastmod = "2012-08-14T10:02:00Z"
weight = 13608
keywords = [ "llc", "flood", "cdp" ]
aliases = [ "/questions/13608" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [LLC/CDP flood](/questions/13608/llccdp-flood)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13608-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am seeing on my network a flood of LLC packets all seeming to come from the same MAC address (which is a mitel phone about 4 switches away from the capturing PC).</p><p>Even stranger it is now unpluged and I am still seeing the traffic!!</p><p>So I need some help in picking apart the wireshark log and tracking down where this data is coming from.</p><pre><code>23535   58.942635000    172.16.225.136  CDP/VTP/DTP/PAgP/UDLD   CDP 121 Device ID: SEP08000F4D55BB  Port ID: Port 1</code></pre></div><div id="question-tags" class="tags-container tags">llc flood cdp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '12, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/d93ef297f89c59c1df8878f80ce4c37b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DevilWAH&#39;s gravatar image" /><p>DevilWAH<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DevilWAH has no accepted answers">0%</span></p></div></div><div id="comments-container-13608" class="comments-container"></div><div id="comment-tools-13608" class="comment-tools"></div><div class="clear"></div><div id="comment-13608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13613"></span>

<div id="answer-container-13613" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13613-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>CDP is a Cisco proprietary protocol. They use it to learn about other switches in the network.</p><blockquote><p><code>http://de.wikipedia.org/wiki/Cisco_Discovery_Protocol</code><br />
</p></blockquote><p>So, these packets are from one of your switches, that has CDP enabled. It's nothing to worry about, as long as it is not <strong>really flooding</strong> the network with these packets.</p><p>You can disable CDP with this command:</p><blockquote><p><code>no cdp enable</code><br />
</p></blockquote><p>For further information, please check the Cisco site:</p><blockquote><p><code>http://www.cisco.com/en/US/tech/tk962/technologies_tech_note09186a00801aa000.shtml</code><br />
</p></blockquote><p>BTW:</p><blockquote><p>I am seeing on my network a flood of LLC packets</p></blockquote><p>What is a flood in that case? How many packtes per second/minute do you see?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '12, 07:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Aug '12, 07:09</p></div></div><div id="comments-container-13613" class="comments-container"></div><div id="comment-tools-13613" class="comment-tools"></div><div class="clear"></div><div id="comment-13613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13617"></span>

<div id="answer-container-13617" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13617-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As CDP packets are multicast packets, they can be forwarded by switches if they do not absorb them. Cisco switches will receive the CDP packets and not forward them. Maybe your L2 network has a loop that is not blocked anywhere with spanning-tree, maybe only for a specific vlan?</p><p>The fact that you have a storm of these messages even after you disconnect the source does suggest a loop too.</p><p>What kind of switches are you using and what does the topology look like?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '12, 10:02</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-13617" class="comments-container"></div><div id="comment-tools-13617" class="comment-tools"></div><div class="clear"></div><div id="comment-13617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

