+++
type = "question"
title = "Rogue PC on the Network"
description = '''Can WireShark help me locate a rogue system, down to the physical location/port? '''
date = "2011-05-13T17:06:00Z"
lastmod = "2011-06-05T12:38:00Z"
weight = 4085
keywords = [ "rogue", "physical", "system", "location" ]
aliases = [ "/questions/4085" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Rogue PC on the Network](/questions/4085/rogue-pc-on-the-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4085-score" class="post-score" title="current number of votes">0</div><span id="post-4085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can WireShark help me locate a rogue system, down to the physical location/port?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rogue" rel="tag" title="see questions tagged &#39;rogue&#39;">rogue</span> <span class="post-tag tag-link-physical" rel="tag" title="see questions tagged &#39;physical&#39;">physical</span> <span class="post-tag tag-link-system" rel="tag" title="see questions tagged &#39;system&#39;">system</span> <span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '11, 17:06</strong></p><img src="https://secure.gravatar.com/avatar/e42c2f45ca414fd8350bc6b6553215c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HFlores&#39;s gravatar image" /><p><span>HFlores</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HFlores has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Feb '12, 19:29</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4085" class="comments-container"></div><div id="comment-tools-4085" class="comment-tools"></div><div class="clear"></div><div id="comment-4085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="4089"></span>

<div id="answer-container-4089" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4089-score" class="post-score" title="current number of votes">1</div><span id="post-4089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can help you detect traffic from Rogue PC's, but it can't tell you which port the PC is connected too. You need to use the ARP tables on your routers and the Forwarding Databases on your switches to track down the port. The steps you need to take are:</p><ol><li><p>Detect traffic from the Rogue PC with Wireshark. This is the most difficult step, as it might nog be very visible. Once you have the IP address of the Rogue PC, you can continue</p></li><li><p>Log in to the router that is connected to the subnet of which the found IP is part of. Get the ARP entry for that IP and copy the MAC address</p></li><li><p>From the router downwards log into the switches and lookup the MAC address in the forwarding database.</p></li><li><p>If the MAC is found on a switchlink, follow the link to the next switch until you find the access-port on which the MAC is listed. That's where you will find your ROgue PC</p></li></ol><p>Good luck!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '11, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4089" class="comments-container"><span id="4111"></span><div id="comment-4111" class="comment"><div id="post-4111-score" class="comment-score"></div><div class="comment-text"><p>Very nice and THANK you I'll try this out. Herbert</p></div><div id="comment-4111-info" class="comment-info"><span class="comment-age">(17 May '11, 16:46)</span> <span class="comment-user userinfo">HFlores</span></div></div></div><div id="comment-tools-4089" class="comment-tools"></div><div class="clear"></div><div id="comment-4089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4140"></span>

<div id="answer-container-4140" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4140-score" class="post-score" title="current number of votes">0</div><span id="post-4140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If your computer is connected to a Cisco switch which is running CDP, (Cisco Discovery Protocol), then the switch and port number you are connected to is identified in your capture file. You can use the Display Filter, CDP, to narrow down your results and see only that traffic, and you will see "Device ID: SwitchName Port ID: PortID under the Info section of the captured packet. Also, you can use wiresharkportable and tshark to identify ports on other computers in your network by installing wiresharkportable on a jumpdrive, then on the remote computer, runn winpcap installer, and then the following command:</p><pre><code>@echo off 
winpcap_4_1_2.exe
tshark -i interface# -R cdp       [where interface# is the number of the interface your are capturing]</code></pre><p>save the above from notepad as a .cmd file, like "whoami.cmd". Then run the command from the users computer. There may be a delay while you wait for CDP to broadcast, you can speed this up by opening up the browser and surfing around a little in the background.</p><p>There may be a discovery protocol available for nortel switches or others, but I haven't researched those.</p><p>Hope this helps, John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '11, 05:49</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 May '11, 06:01</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-4140" class="comments-container"><span id="4142"></span><div id="comment-4142" class="comment"><div id="post-4142-score" class="comment-score"></div><div class="comment-text"><p>This is useful indeed when you want to know on which switchport a "known" system is connected, but I believe the OP was trying to locate an unknown system on his/her network.</p><p>(BTW I edited your answer and deleted the second one that was only a correction to the answer, you can always edit your answers after posting them)</p></div><div id="comment-4142-info" class="comment-info"><span class="comment-age">(19 May '11, 06:04)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="4144"></span><div id="comment-4144" class="comment"><div id="post-4144-score" class="comment-score"></div><div class="comment-text"><p>Thank you. Also, I thought your solution was effective.<br />
</p><p>John</p></div><div id="comment-4144-info" class="comment-info"><span class="comment-age">(19 May '11, 08:28)</span> <span class="comment-user userinfo">John_Modlin</span></div></div><span id="4145"></span><div id="comment-4145" class="comment"><div id="post-4145-score" class="comment-score"></div><div class="comment-text"><p>Thank you John, I do appreciate the info. We do have CISCO switches and I know the IP address from DHCP and the listed NetBIOS name. I'll have to see if CDP is loaded/activated. thanks again, herbert</p></div><div id="comment-4145-info" class="comment-info"><span class="comment-age">(19 May '11, 08:56)</span> <span class="comment-user userinfo">HFlores</span></div></div></div><div id="comment-tools-4140" class="comment-tools"></div><div class="clear"></div><div id="comment-4140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4387"></span>

<div id="answer-container-4387" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4387-score" class="post-score" title="current number of votes">0</div><span id="post-4387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Also, while not wireshark, netscantools pro has a feature known has 'switch port mapper'. It will collect all the arp info from your switches and combining that with a ping sweep will show you all the devices connected to your switches including mac and ip and the associated port number.<br />
Very cool :)</p><p>John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '11, 12:38</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-4387" class="comments-container"></div><div id="comment-tools-4387" class="comment-tools"></div><div class="clear"></div><div id="comment-4387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

