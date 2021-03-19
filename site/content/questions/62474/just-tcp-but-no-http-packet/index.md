+++
type = "question"
title = "Just TCP but no HTTP packet"
description = '''Hi,  Before I grad and start my career as a APM/NPM consultant, those are the good times when I play wireshark tutorial. And TCP is always accompanied by HTTP. Today, I do a tcpdump and realized that there is always TCP two-way communication between a specific source-destination pair, but they are n...'''
date = "2017-07-03T09:39:00Z"
lastmod = "2017-07-03T09:51:00Z"
weight = 62474
keywords = [ "http", "tcp" ]
aliases = [ "/questions/62474" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Just TCP but no HTTP packet](/questions/62474/just-tcp-but-no-http-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62474-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Before I grad and start my career as a APM/NPM consultant, those are the good times when I play wireshark tutorial. And TCP is always accompanied by HTTP.</p><p>Today, I do a tcpdump and realized that there is always TCP two-way communication between a specific source-destination pair, but they are not HTTP packets between them. (i.e I type 'tcp' in display filter, returned the filter result; I type in 'http', returned nothing).</p><p>SO, WHAT COULD THIS POSSIBLY MEANS?</p><p>FYI, in case you wonder: No, no HTTPS/SSL/TLS here. We are talking about unencrypted traffic here.</p><p>Appreciate if any of the experts can share your thought on what could be the possbile scenario happening, the application shouldn't has any probelm as its already been deployed to production environment for a long time with large number of users.</p><p>Best Regards, Wai KEat</p></div><div id="question-tags" class="tags-container tags">http tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '17, 09:39</strong></p><img src="https://secure.gravatar.com/avatar/c1e2e51b48939f05f0d29e40b64909ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="waikeatahlok&#39;s gravatar image" /><p>waikeatahlok<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="waikeatahlok has no accepted answers">0%</span></p></div></div><div id="comments-container-62474" class="comments-container"></div><div id="comment-tools-62474" class="comment-tools"></div><div class="clear"></div><div id="comment-62474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62475"></span>

<div id="answer-container-62475" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62475-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sorry, but TCP is <strong>not</strong> always accompanied by HTTP. While HTTP is very often seen on the internet, that picture can be very different in business networks. There are lots of other protocols running on top of TCP, e.g. FTP, SMTP, POP3, IMAP, database connections, application protocols, etc.</p><p>I think that you should spend some more time on learning the basics of modern computer networks, because otherwise you may run into trouble (you said you want to consult on APM/NPM, which I guess means application/network performance monitoring). It seems to me that there are still big gaps in the foundation of your knowledge about how networks and applications work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '17, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-62475" class="comments-container"><span id="62476"></span><div id="comment-62476" class="comment"><div id="post-62476-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>Thanks for the quick response, I did manage to find this post (<a href="https://stackoverflow.com/questions/19852858/why-wireshark-display-filter-does-not-show-http-packets)">https://stackoverflow.com/questions/19852858/why-wireshark-display-filter-does-not-show-http-packets)</a> shortly after I posted the question.</p><p>Also, my client told me that application is using HTTP, and hence I do a tcpdump and have a look. I do understand that there can be many application layer protocol running on top of TCP. (Sorry for my bad English when typing the question)</p><p>Lastly, after reading that post on stackoverflow, I still don't understand my pcap file. That is because all the packets I see after applied 'tcp' filter, I can only 4 layer of data, which are frame, ethernet, IP and TCP. The last layer of data (i.e the app layer data in 5-layer-TCP/IP stack) is missing. I can only see 4 layers of data in packet content.</p></div><div id="comment-62476-info" class="comment-info"><span class="comment-age">(03 Jul '17, 10:02)</span> waikeatahlok</div></div><span id="62477"></span><div id="comment-62477" class="comment"><div id="post-62477-score" class="comment-score"></div><div class="comment-text"><p>Okay, so let's assume your pcap file contains HTTP, but Wireshark doesn't decoded it. Check that the TCP port you're seeing is in fact the one you should see HTTP on. Maybe it's a non-standard port, in which case you can either add that port to the list of ports in the preferences for the HTTP dissector, or use "Decode As" from the popup menu in the packet list to force Wireshark to decode that port as HTTP.</p></div><div id="comment-62477-info" class="comment-info"><span class="comment-age">(03 Jul '17, 10:11)</span> Jasper ♦♦</div></div><span id="62480"></span><div id="comment-62480" class="comment"><div id="post-62480-score" class="comment-score">1</div><div class="comment-text"><p>If you are serious about doing the capture using tcpdump, I'm almost sure you haven't asked it to capture complete packets, which explains why you cannot see anything above the TCP layer. The magic parameter to add to tcpdump's command line is <code>-s 0</code>. Without it, tcpdump only saves first 60 bytes of each captured frame. Which, BTW, could be also an answer to your <a href="https://ask.wireshark.org/questions/62228/application-data-packet-still-doesnt-decrypted-even-if-correct-ssl-keys-are-applied">other question</a>.</p></div><div id="comment-62480-info" class="comment-info"><span class="comment-age">(03 Jul '17, 12:32)</span> sindy</div></div></div><div id="comment-tools-62475" class="comment-tools"></div><div class="clear"></div><div id="comment-62475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

