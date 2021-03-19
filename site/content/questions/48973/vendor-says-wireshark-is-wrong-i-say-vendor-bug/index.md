+++
type = "question"
title = "Vendor says wireshark is wrong - I say vendor bug"
description = '''Hello, Thanks for all the prior help this board has provided. I am working on a follow up from post https://ask.wireshark.org/questions/48464/snmp-string-with-displayed-as-23. TL;DR - I think this vendors software has issues handling characters typed into their web form with special characters (!#$%...'''
date = "2016-01-08T08:03:00Z"
lastmod = "2016-01-08T15:30:00Z"
weight = 48973
keywords = [ "snmp", "network", "websites", "software" ]
aliases = [ "/questions/48973" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Vendor says wireshark is wrong - I say vendor bug](/questions/48973/vendor-says-wireshark-is-wrong-i-say-vendor-bug)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48973-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, Thanks for all the prior help this board has provided. I am working on a follow up from post <a href="https://ask.wireshark.org/questions/48464/snmp-string-with-displayed-as-23.">https://ask.wireshark.org/questions/48464/snmp-string-with-displayed-as-23.</a> TL;DR - I think this vendors software has issues handling characters typed into their web form with special characters (!#$%^&amp;). From what I can tell, these special characters are manipulated to hex values. Though I am still dealing with this vendor who is insistent that we are typing characters into their web form incorrectly. To prove them incorrect, I made the 2 videos which I think is sufficient to prove my claim (6 mins total). Can anyone help point out why this would not be sufficient evidence to support my claim if you can think of any other possibilities?</p><p>Entering data in the webform on the local host of webserver and wireshark showing manipulation: <a href="https://www.youtube.com/watch?v=WdlBWTZl0zA&amp;feature=youtu.be">https://www.youtube.com/watch?v=WdlBWTZl0zA&amp;feature=youtu.be</a></p><p>I even made a 2nd video that I hope further proves this with switch debugging: <a href="https://www.youtube.com/watch?v=lZnvoXzwWQM">https://www.youtube.com/watch?v=lZnvoXzwWQM</a></p></div><div id="question-tags" class="tags-container tags">snmp network websites software</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '16, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/238d0902a59854cdc5e2bf4c42377512?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="crknipe123&#39;s gravatar image" /><p>crknipe123<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="crknipe123 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jan '16, 08:04</p></div></div><div id="comments-container-48973" class="comments-container"></div><div id="comment-tools-48973" class="comment-tools"></div><div class="clear"></div><div id="comment-48973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48978"></span>

<div id="answer-container-48978" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48978-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yeah, sure, "Wireshark is wrong" - nice try, lazy $vendor.</p><p>While your capture method isn't 100% optimal (only using a dedicated professional capture device with a Full Duplex TAP would be 99.999999% accurate), it is good enough for a simple reason: you're looking at application content, not timings, broken packets, out-of-orders, etc. So I rule it's valid as evidence in your case.</p><p>Now, Wireshark may or may not decode things correctly, but if you decode the hex view (by hand, if necessary) and get the same result, Wireshark can't be wrong. And, in your case, it isn't wrong.</p><p>Their web front end is manipulating your input before sending it, probably because they apply URI encoding routines by mistake. You should be able to find this in the client side Javascript if you look at the form action.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '16, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-48978" class="comments-container"><span id="48984"></span><div id="comment-48984" class="comment"><div id="post-48984-score" class="comment-score"></div><div class="comment-text"><p>Thanks again. I am pulling my hair out with their responses and this helps my confidence level.<br />
</p></div><div id="comment-48984-info" class="comment-info"><span class="comment-age">(08 Jan '16, 09:42)</span> crknipe123</div></div><span id="48985"></span><div id="comment-48985" class="comment"><div id="post-48985-score" class="comment-score">1</div><div class="comment-text"><p>Also if the function is failing on the snmp devices, then you either have the web front-end being incorrect or Wireshark and the snmp devices being incorrect. Occam's razor indicates it's likely to be the web front-end.</p></div><div id="comment-48985-info" class="comment-info"><span class="comment-age">(08 Jan '16, 09:49)</span> grahamb ♦</div></div><span id="48988"></span><div id="comment-48988" class="comment"><div id="post-48988-score" class="comment-score"></div><div class="comment-text"><p>@crknipe if you can, send me an email with the name of the vendor and the product to jasper[ät]packet-foo.com</p></div><div id="comment-48988-info" class="comment-info"><span class="comment-age">(08 Jan '16, 10:48)</span> Jasper ♦♦</div></div><span id="48995"></span><div id="comment-48995" class="comment"><div id="post-48995-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Yeah, sure, "Wireshark is wrong" - nice try, lazy $vendor.</p></blockquote><p>often it's just the first line support, who has no idea at all what Wireshark is and how to interpret the technical details. I suggest to escalate the ticket to the next level, where you usually find people with better technical skills ;-) This is (sadly) true for most vendors...</p></div><div id="comment-48995-info" class="comment-info"><span class="comment-age">(08 Jan '16, 15:32)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-48978" class="comment-tools"></div><div class="clear"></div><div id="comment-48978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48994"></span>

<div id="answer-container-48994" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48994-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I think this vendors software has issues handling characters typed into their web form with special characters (!#$%^&amp;). From what I can tell, these special characters are manipulated to hex values.</p></blockquote><p>Your videos are showing clearly that the HEX values of the community string are being modified. This is probably a result of web application security gone wrong. They might have tried to apply OWASP10 recommendations and failed to "normalize" input strings in a proper way.</p><blockquote><p>Though I am still dealing with this vendor who is insistent that we are typing characters into their web form incorrectly.</p></blockquote><p>Well, run a browser plugin (like Firedebug) to show them your input. Combined with the pcap file, they should accept that something is actually wrong in their tool.</p><p>Just to be sure: There is no security device (firewall, proxy, etc.) between your browser and the device where you are entering the SNMP community in the web GUI, right?</p><blockquote><p>Can anyone help point out why this would not be sufficient evidence to support my claim if you can think of any other possibilities?</p></blockquote><p>As your video shows 5 (or 6) input characters in the browser, but a few more characters in the HEX dump of the community string, it's pretty obvious that the software is doing something wrong. As you are running the software in a VM, you could try to get access to the web GUI code (maybe python or PHP) and show them where they fail ;-)</p><p>BTW: What kind of software is this?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '16, 15:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-48994" class="comments-container"></div><div id="comment-tools-48994" class="comment-tools"></div><div class="clear"></div><div id="comment-48994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

