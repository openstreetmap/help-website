+++
type = "question"
title = "ICMP data field corruption"
description = '''Hello, my (old) laptop is unable to establish a wireless link over a cardbus WLAN card. After disabling WLAN encryption, I am able to send an echo request and there is an echo response from the server. Using WireShark, I can see that the ICMP checksum is wrong because the ICMP data is corrupted. Typ...'''
date = "2012-07-15T14:52:00Z"
lastmod = "2012-07-16T14:10:00Z"
weight = 12729
keywords = [ "icmp", "data", "corruption" ]
aliases = [ "/questions/12729" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [ICMP data field corruption](/questions/12729/icmp-data-field-corruption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12729-score" class="post-score" title="current number of votes">0</div><span id="post-12729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>my (old) laptop is unable to establish a wireless link over a cardbus WLAN card. After disabling WLAN encryption, I am able to send an echo request and there is an echo response from the server. Using WireShark, I can see that the ICMP checksum is wrong because the ICMP data is corrupted. Typically, 4 bytes "62 63 64 65" are blanked to "00 00 00 00" in the ICMP data field. Always the same locations are blanked:</p><p>Echo request ICMP data: 61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 61 62 63 64 65 66 67 68 69</p><p>Echo response ICMP data: 61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 61 00 00 00 00 66 67 68 69</p><p>The laptop has WinXP SP3 installed. The cardbus card works fine in another laptop.<br />
What can I check next? What kind of tools (freeware) can I use to analyze? Is it possible to view the ICMP data when it is transferred from the network card to the memory?</p><p>Thanks for help. manuel</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-corruption" rel="tag" title="see questions tagged &#39;corruption&#39;">corruption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '12, 14:52</strong></p><img src="https://secure.gravatar.com/avatar/2b670607c621fc5c6af7bb8f27cb2428?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manuel&#39;s gravatar image" /><p><span>manuel</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manuel has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-12729" class="comments-container"></div><div id="comment-tools-12729" class="comment-tools"></div><div class="clear"></div><div id="comment-12729-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12731"></span>

<div id="answer-container-12731" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12731-score" class="post-score" title="current number of votes">0</div><span id="post-12731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The ICMP checksum is probably not really wrong, and neither is the ICMP data corrupt. What you're doing is capturing on a system that is sending out packets through a network card that helps the system by taking over certain tasks from the CPU. If that happens, the calculation of checksums for IP, TCP, ICMP etc. is done just in that last moment before the packet goes out on to the actual physical medium, which is way after Wireshark has already picked it up. Google for "checksum offloading" or take a look here: <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChAdvChecksums.html">http://www.wireshark.org/docs/wsug_html_chunked/ChAdvChecksums.html</a></p><p>If you don't believe me you can easily check this: only packets going OUT are affected. Capture them at the other node (as incoming packets) and you'll see they'll have perfect checksums.</p><p>I guess the cardbus card has some issues when trying to establish an encryption when running on Windows XP (or does the other laptop also run Windows XP? In that case you need to find out what the difference between the two systems is).</p><p>If you can't find any other reason you should probably try to talk to the vendor about it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '12, 21:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jul '12, 21:09</strong> </span></p></div></div><div id="comments-container-12731" class="comments-container"><span id="12781"></span><div id="comment-12781" class="comment"><div id="post-12781-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>Thanks for the reply. I went through the attached link but I'm still not convinced:<br />
</p><p>Sending OUT an echo request from my laptop is not a problem: I can manually validate the checksum and also Wireshark reports a valid checksum. And: the other node replies with an echo response. So, I can assume that the echo request packet has been correctly sent out by my laptop and also correctly received at the other node (which is a FritzBox).</p><p>When receiving the echo response my laptop has a problem: the ICMP data field contains four bytes blanked to zero as described above. I can manually calculate and confirm that Wireshark is correct in reporting 'invalid checksum'. If I replace the four zeros by the four bytes "62 63 64 65" that I actually would expect, the manually calculated checksum matches the received checksum.</p><p>So, I think I really can conclude that something goes wrong while receiving the echo response on my laptop. And either there is no checksum offloading to the card because otherwise Wireshark would not even see this broken packet (as described in the link). Or the packet is still correct when it is received by the card and gets corrupted before Wireshark gets access on it.</p><p>Now, my question is: is there a way of logging the data transfer from the card to the memory? Or a tool that tells me which process/program is accessing which address in memory? I tried Sysinternals Process Explorer but I did not get this detailed information. What else could I try?</p><p>Regards<br />
manuel</p></div><div id="comment-12781-info" class="comment-info"><span class="comment-age">(16 Jul '12, 12:41)</span> <span class="comment-user userinfo">manuel</span></div></div><span id="12787"></span><div id="comment-12787" class="comment"><div id="post-12787-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure if there is a tool that could log data going from card to memory. My approach would be to actually stop capturing on a node taking part in the conversation (which is not a good capture setup anyway). Instead, capture with a 3rd, passive device to see what actually is transmitted on the wire (using a SPAN port, or even better: a TAP). That way you can make sure the packet is correct when it comes in.</p></div><div id="comment-12787-info" class="comment-info"><span class="comment-age">(16 Jul '12, 14:10)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-12731" class="comment-tools"></div><div class="clear"></div><div id="comment-12731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12783"></span>

<div id="answer-container-12783" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12783-score" class="post-score" title="current number of votes">0</div><span id="post-12783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Typically, <strong>4 bytes</strong> "62 63 64 65" <strong>are blanked</strong> to "00 00 00 00" <strong>in the ICMP data field</strong>. Always the same locations are blanked:</p></blockquote><p>There should be no data modification in the payload. Sounds like your PCCARD is broken. If the card works in another laptop, your PCCARD slot might be broken (or something else on that laptop). Could be a strange driver problem as well.</p><p>Try to boot the laptop with a linux distribution (maybe Ubuntu) and check if the PCCARD works there. The old ones will be detected quite well, if they are not too old ;-)</p><p>If it works on linux, it's a driver problem. Try to reinstall the driver. If it's the same on linux, I assume it's a hardware problem (see above).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '12, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jul '12, 13:00</strong> </span></p></div></div><div id="comments-container-12783" class="comments-container"></div><div id="comment-tools-12783" class="comment-tools"></div><div class="clear"></div><div id="comment-12783-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

