+++
type = "question"
title = "help with deciphering log....router crash issue"
description = '''i&#x27;m about out of hair to pull out. We are having a issue with our router (internally crashing - which drops our internet - its been replaced 3x&#x27;s and the last time a totally diff style router. They say its on our end which at this point i agree. sometimes its 10-15x a day sometimes its never. not su...'''
date = "2013-03-08T10:27:00Z"
lastmod = "2013-03-11T23:47:00Z"
weight = 19305
keywords = [ "router", "crash" ]
aliases = [ "/questions/19305" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [help with deciphering log....router crash issue](/questions/19305/help-with-deciphering-logrouter-crash-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19305-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i'm about out of hair to pull out. We are having a issue with our router (internally crashing - which drops our internet - its been replaced 3x's and the last time a totally diff style router. They say its on our end which at this point i agree. sometimes its 10-15x a day sometimes its never. not sure where to even start, figured packets was a good start.. router is 192.168.1.254 i even moved switch ports to see if that was it.</p><p>i was able to run a capture when it dropped, but honestly couldn't tell you what all this means in the logs. willing to toss some money if the problem can be found in the log.</p><p>here is the log (hopefully i logged correctly lol)</p><p>its about 40mb linked removed by me</p></div><div id="question-tags" class="tags-container tags">router crash</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '13, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/0b88b74db642ecee69896f823fddd8ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="slothy&#39;s gravatar image" /><p>slothy<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="slothy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Mar '13, 11:41</p></div></div><div id="comments-container-19305" class="comments-container"></div><div id="comment-tools-19305" class="comment-tools"></div><div class="clear"></div><div id="comment-19305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19370"></span>

<div id="answer-container-19370" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19370-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>its about 40mb linked removed by me</p></blockquote><p>can you please add the link again? Maybe it's a malformed IP packet that leads to the router crash !?!</p><p>Another possibility would be some 'instability' in the power supply (not enough voltage). Did you check that?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '13, 23:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-19370" class="comments-container"><span id="19449"></span><div id="comment-19449" class="comment"><div id="post-19449-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.dropbox.com/s/squeulsr9hadoc3/test_00007_20130308124320">https://www.dropbox.com/s/squeulsr9hadoc3/test_00007_20130308124320</a></p><p>i moved the router to a new power outlet to check yesterday - the weird thing is comcast says they don't see it drop on their end but it shows up in remote web log in ui..</p></div><div id="comment-19449-info" class="comment-info"><span class="comment-age">(13 Mar '13, 07:33)</span> slothy</div></div><span id="19481"></span><div id="comment-19481" class="comment"><div id="post-19481-score" class="comment-score">2</div><div class="comment-text"><p>I don't see any "general" problem. Without information about the time stamp where you observed the problem, it's hard to analyze it. Can you please add the time stamp?</p><p><strong>HOWEVER</strong>: What I found is a problem with DNS queries, beginning at frame 39993 (Display filter: dns.flags.rcode == 2). Your DNS server (192.168.1.4) responds with <strong>'server error'</strong>.</p><p>So maybe your problem is not related to the internet router but rather to DNS resolving. Is there any Forwarder configured on your DNS server 192.168.1.4? If so, please try to use a different DNS server, e.g. google dns: 8.8.8.8.</p></div><div id="comment-19481-info" class="comment-info"><span class="comment-age">(13 Mar '13, 16:34)</span> Kurt Knochner ♦</div></div><span id="19504"></span><div id="comment-19504" class="comment"><div id="post-19504-score" class="comment-score"></div><div class="comment-text"><p>funny you say that - i fixed that after i logged - was having some dns/slow issues.</p><p>i had a issue with ssl certs and had to rerun the sbs config, and i guess it deletes that from dns for some reason. Good eye!</p></div><div id="comment-19504-info" class="comment-info"><span class="comment-age">(14 Mar '13, 06:51)</span> slothy</div></div><span id="19505"></span><div id="comment-19505" class="comment"><div id="post-19505-score" class="comment-score"></div><div class="comment-text"><p>and for time stamp not sure how to do that, and my little peice of paper i had the drop time written down, look like the cleaning people well cleaned it off my desk... :(</p></div><div id="comment-19505-info" class="comment-info"><span class="comment-age">(14 Mar '13, 07:06)</span> slothy</div></div><span id="19541"></span><div id="comment-19541" class="comment not_top_scorer"><div id="post-19541-score" class="comment-score"></div><div class="comment-text"><p>so i think i found my needle in the haystack yesterday, walking past the server room, from the corner of my eye i seen the switches flicker a sec. investigated it, they and the router are plugged into a power strip which is plugged into our older ups. when i switched out let, i plugged into the other strip which well is plugged into our old ups also........ logged into router and sure enough its rebooted about the same time. So i moved the strip to our newer ups and haven't had a drop yet - wondering if the power loss for a millisec is enough to reboot the router internally and not the link.</p></div><div id="comment-19541-info" class="comment-info"><span class="comment-age">(15 Mar '13, 09:04)</span> slothy</div></div><span id="19642"></span><div id="comment-19642" class="comment"><div id="post-19642-score" class="comment-score">1</div><div class="comment-text"><p>as I suggested, an unstable power supply... ;-)</p></div><div id="comment-19642-info" class="comment-info"><span class="comment-age">(19 Mar '13, 06:35)</span> Kurt Knochner ♦</div></div><span id="19677"></span><div id="comment-19677" class="comment not_top_scorer"><div id="post-19677-score" class="comment-score"></div><div class="comment-text"><p>the weird thing is, comcast doesn't show a drop on their end is why i figured when i switch power outlets that was the issue. but thanks again 10000x kurt for your help!</p></div><div id="comment-19677-info" class="comment-info"><span class="comment-age">(20 Mar '13, 06:33)</span> slothy</div></div><span id="19686"></span><div id="comment-19686" class="comment not_top_scorer"><div id="post-19686-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but thanks again 10000x kurt for your help!</p></blockquote><p>You're welcome.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-19686-info" class="comment-info"><span class="comment-age">(20 Mar '13, 09:20)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-19370" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-19370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19326"></span>

<div id="answer-container-19326" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19326-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is a great tool, but I don't think it's the place to start in this case. I'd start with the router. I'd bring in someone who is expert with your model of router; someone who can look at the router logs, who can read the various performance counters, and who can use the router's built-in debugging features. If this is a high-end commercial router, then it will have a lot of troubleshooting and debugging features. If it's a SOHO class router, well, then it probably won't have much.</p><p>As far as the traffic you captured, I don't think we're seeing the whole picture. It looks like you ran Wireshark on 192.168.1.51. Almost all of the traffic through the router is to/from 192.168.1.51. Only 279 of the 41,583 frames are IP packets through the router from an internal host other than 192.168.1.51, and then only the outbound traffic was captured, so we only see half of the conversation.</p><p>See the <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Capture Setup</a> page on the Wireshark wiki for information on capturing on a switched Ethernet network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '13, 19:34</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-19326" class="comments-container"><span id="19359"></span><div id="comment-19359" class="comment"><div id="post-19359-score" class="comment-score"></div><div class="comment-text"><p>ya its a soho (comcast) - ill read up on the capture setup, and even give comcast a call and see if there is a way for them to turn on debugging.</p><p>thank you for your help!!</p></div><div id="comment-19359-info" class="comment-info"><span class="comment-age">(11 Mar '13, 11:39)</span> slothy</div></div></div><div id="comment-tools-19326" class="comment-tools"></div><div class="clear"></div><div id="comment-19326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

