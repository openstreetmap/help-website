+++
type = "question"
title = "What is PCLI traffic and how to identify a traffic is PCLI traffic?"
description = '''Q: While capturing a multicast video feed on port 9000, I noticed Wireshark was identifying the content of the UDP packets as PCLI (Packet Cable Lawful Intercept) containing another IP datagram.Has anyone seen this issue before?Disabling the PCLI dissector fixes this. A: The PCLI dissector is regist...'''
date = "2014-06-14T03:16:00Z"
lastmod = "2014-06-15T07:49:00Z"
weight = 33798
keywords = [ "pcli", "multicast", "udp" ]
aliases = [ "/questions/33798" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What is PCLI traffic and how to identify a traffic is PCLI traffic?](/questions/33798/what-is-pcli-traffic-and-how-to-identify-a-traffic-is-pcli-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33798-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Q: While capturing a multicast video feed on port 9000, I noticed Wireshark was identifying the content of the UDP packets as PCLI (Packet Cable Lawful Intercept) containing another IP datagram.Has anyone seen this issue before?Disabling the PCLI dissector fixes this.</p><p>A: The PCLI dissector is registered to decode anything on UDP Port 9000. There are no heuristics in the dissector to check if the packet is indeed PCLI, nor does it seem to be an IANA allocated port.Disabling the dissector is the correct approach if your traffic isn't PCLI.</p><p>Q: What is PCLI traffic and how to identify a traffic is PCLI traffic?</p><p>Someone can help me? Thanks a lot.</p></div><div id="question-tags" class="tags-container tags">pcli multicast udp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '14, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/f6a9a9d896bffdeed18a01c1818ad3da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="a278497234&#39;s gravatar image" /><p>a278497234<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="a278497234 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jun '14, 03:17</p></div></div><div id="comments-container-33798" class="comments-container"></div><div id="comment-tools-33798" class="comment-tools"></div><div class="clear"></div><div id="comment-33798-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33824"></span>

<div id="answer-container-33824" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33824-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Has anyone seen this issue before?Disabling the PCLI dissector fixes this.</p></blockquote><p>Yes, and you have found the solution yourself. See also the following similar question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/9557/why-are-packets-incorrectly-identified-as-pcli">http://ask.wireshark.org/questions/9557/why-are-packets-incorrectly-identified-as-pcli</a></p></blockquote><p>Regarding your other question:</p><blockquote><p>Q: What is PCLI traffic and how to identify a traffic is PCLI traffic?</p></blockquote><p>That's a method to allow authorities (governments, police, 'agencies') to intercept (eavesdrop) internet traffic of users, sent over cable connections.</p><blockquote><p><a href="http://www.cablelabs.com/wp-content/uploads/specdocs/PKT-SP-ESP1.5-I02-070412.pdf">http://www.cablelabs.com/wp-content/uploads/specdocs/PKT-SP-ESP1.5-I02-070412.pdf</a><br />
<a href="http://en.wikipedia.org/wiki/PacketCable">http://en.wikipedia.org/wiki/PacketCable</a><br />
</p></blockquote><p>How can you identify PCLI traffic? Well, by reading and understanding the specs or by reading the Wireshark PCLI dissector code. By looking at the dissector code, it looks like PCLI encapsulates plain IP packets in the UDP payload, without any further protocol. So, the best way to 'identify' PCLI traffic would be to actually <strong>use the PCLI dissector</strong>. If it finds a valid IP structure in the PCLI payload, chances are pretty good <strong>that it is PCLI</strong>.</p><p>However, that's nothing you should be worried about. In your case it was just a coincidence with traffic on port UDP 9000 (the only sign for Wireshark to interpret that traffic as PCLI).</p><p>If you were the target of a surveillance, you would <strong>never see</strong> PCLI traffic, as that would reveal that surveillance ;-))</p><p>So, if you are afraid of 'lawful' surveillance, you can</p><ul><li>complain about the 'lawful' surveillance methods in front of your parliament.</li><li>try to hide your activities by using VPN services in foreign countries and/or Tor browser and/or encryption (don't trust anything that is using OpenSSL!!).</li><li>try to behave like the nice, noncritical guy your government wants you to be. So please no bad keywords in your mails and online searches! And no visiting of 'bad' websites! Please ask your government what is considered a bad keyword/website in your country. I'm sure they are absolutely willing to answer all your questions. After all <strong>you are the people</strong> (at least part of it) and <strong>you have the power</strong> to control the activities of the government ;-)) At least that's what they tell you 8 weeks before the next election.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '14, 07:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jun '14, 07:51</p></div></div><div id="comments-container-33824" class="comments-container"></div><div id="comment-tools-33824" class="comment-tools"></div><div class="clear"></div><div id="comment-33824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

