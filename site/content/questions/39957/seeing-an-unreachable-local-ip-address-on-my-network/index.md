+++
type = "question"
title = "Seeing an unreachable local IP address on my network"
description = '''So I was running wireshark, and I kept getting this ARP packets about who is at &quot;192.168.1.10&quot;   It appears to be a rogue IP address on my network because when I attempt to ping it, and check my arp cache, this is what happens: ![alt text][2] What measures can I take to make sure my network isn&#x27;t co...'''
date = "2015-02-19T10:41:00Z"
lastmod = "2015-02-19T18:42:00Z"
weight = 39957
keywords = [ "arpspoofing", "security" ]
aliases = [ "/questions/39957" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Seeing an unreachable local IP address on my network](/questions/39957/seeing-an-unreachable-local-ip-address-on-my-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39957-score" class="post-score" title="current number of votes">0</div><span id="post-39957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I was running wireshark, and I kept getting this ARP packets about who is at "192.168.1.10"</p><p><img src="https://osqa-ask.wireshark.org/upfiles/weirdipaddress_HGlFnZC.PNG" alt="alt text" /></p><p>It appears to be a rogue IP address on my network because when I attempt to ping it, and check my arp cache, this is what happens:</p><p>![alt text][2]</p><p>What measures can I take to make sure my network isn't compromised because recently, I did a wireshark trace on my brother's computer and I noticed an ARP poisoning attack to his cache:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/part1ARPattack.PNG" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/part2ARPattack.PNG" alt="alt text" /></p><p>These ARP requests which was obviously an attempt at ARP poisoining had some mysterious SNMP get requests made (which I have some trouble reading but working on how to read SNMP messages in wireshark)</p><p><img src="https://osqa-ask.wireshark.org/upfiles/SNMP_getrequests.PNG" alt="alt text" /></p><p>Can someone kindly share some light on this situation, especially with devices that don't exist on my network having IP addresses? There is a rogue right?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arpspoofing" rel="tag" title="see questions tagged &#39;arpspoofing&#39;">arpspoofing</span> <span class="post-tag tag-link-security" rel="tag" title="see questions tagged &#39;security&#39;">security</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '15, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/4784c5fb1a0142030d51a339706a456c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beldum&#39;s gravatar image" /><p><span>Beldum</span><br />
<span class="score" title="49 reputation points">49</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beldum has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Feb '15, 18:41</strong> </span></p></div></div><div id="comments-container-39957" class="comments-container"></div><div id="comment-tools-39957" class="comment-tools"></div><div class="clear"></div><div id="comment-39957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39962"></span>

<div id="answer-container-39962" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39962-score" class="post-score" title="current number of votes">1</div><span id="post-39962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your computer, 192.168.1.18, is attempting to communicate with 192.168.1.10, so apparently at one time there was a device with that address on your network. It could be lots of things. For example, did you ever replace a network printer, but leave it configured on the computer? If so, the computer could still be trying to communicate with that printer.</p><p>If this is a Windows PC, you might try searching the registry to see if that IP address is stored somewhere. That might give you a clue what process on your computer is trying to communicate with that IP address.</p><p>What you are calling an ARP poisoning attack is not; it is an ARP scan. By itself, this is not malicious. It could be a precursor to an attack, but the ARP scan itself is not an attack. The device with IP address 192.168.43.43 is scanning your brother's entire address space to see what devices respond. It could also be some sort of network discovery tool. Some home routers will do an ARP scan periodically. My Netopia home router, for example, does an ARP scan every five minutes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '15, 16:15</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></img></div></div><div id="comments-container-39962" class="comments-container"><span id="39963"></span><div id="comment-39963" class="comment"><div id="post-39963-score" class="comment-score"></div><div class="comment-text"><p>Jim, thanks for the explanation.</p></div><div id="comment-39963-info" class="comment-info"><span class="comment-age">(19 Feb '15, 18:42)</span> <span class="comment-user userinfo">Beldum</span></div></div></div><div id="comment-tools-39962" class="comment-tools"></div><div class="clear"></div><div id="comment-39962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

