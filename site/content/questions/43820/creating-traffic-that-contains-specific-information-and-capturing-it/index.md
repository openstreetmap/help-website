+++
type = "question"
title = "Creating traffic that contains specific information and capturing it."
description = '''Hi there,  I&#x27;ve got a little homework for a college course here.  We got a number assigned and have to create traffic that includes said number. We then have to capture that traffic with Wireshark and make a screenshot of the capture where our assigned numbers are visable. I&#x27;m pretty new to Wireshar...'''
date = "2015-07-02T08:16:00Z"
lastmod = "2015-07-02T08:51:00Z"
weight = 43820
keywords = [ "capture", "traffic", "homework" ]
aliases = [ "/questions/43820" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Creating traffic that contains specific information and capturing it.](/questions/43820/creating-traffic-that-contains-specific-information-and-capturing-it)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43820-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I've got a little homework for a college course here.</p><p>We got a number assigned and have to create traffic that includes said number. We then have to capture that traffic with Wireshark and make a screenshot of the capture where our assigned numbers are visable.</p><p>I'm pretty new to Wireshark, I've only played around with it so far and am now looking for a bit of help on how to create that traffic and how to navigate through Wireshark to get the information I need.</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">capture traffic homework</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '15, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/7ca1dd3e34c65897d6b44fcc800dcb6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Seby&#39;s gravatar image" /><p>Seby<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Seby has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jul '15, 08:52</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-43820" class="comments-container"></div><div id="comment-tools-43820" class="comment-tools"></div><div class="clear"></div><div id="comment-43820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43822"></span>

<div id="answer-container-43822" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43822-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The hardest part is definitely creating the traffic. Presumably the course covers network programming (or it is a prerequisite), and given that I would suggest you use UDP to send your "assigned" number somewhere (off the local machine, e.g. to your gateway modem\router. Use UDP as it doesn't require a "listening" connection at the other end as TCP does.</p><p>Then start Wireshark, select the interface to capture on, start the capture, run your application to send the UDP data, stop the capture, use a display filter for "udp.port=xxx", where xxx is the destination port used in your application, see your data, job done.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '15, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-43822" class="comments-container"><span id="43823"></span><div id="comment-43823" class="comment"><div id="post-43823-score" class="comment-score"></div><div class="comment-text"><p>I see. Thank you very much. I'm gonna see how far I get and report back later.</p></div><div id="comment-43823-info" class="comment-info"><span class="comment-age">(02 Jul '15, 09:14)</span> Seby</div></div><span id="43825"></span><div id="comment-43825" class="comment"><div id="post-43825-score" class="comment-score"></div><div class="comment-text"><p>Well, it worked like a charm! I sent a package (I put the number in as the package name) to my router and found it in Wireshark. I just don't know under what section I have to look in Wireshark to find the number again.</p><p>EDIT: Nevermind! I found the number. I'm surprised it was actually that easy. Again thank you very much for your help.</p></div><div id="comment-43825-info" class="comment-info"><span class="comment-age">(02 Jul '15, 09:26)</span> Seby</div></div></div><div id="comment-tools-43822" class="comment-tools"></div><div class="clear"></div><div id="comment-43822-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

