+++
type = "question"
title = "Analyzing both directions of WebDAV transactions"
description = '''Hi, The Sample Captures page does not include capture filters for analyzing WebDAV traffic (unless WebDAV traffic is known under some other name?). I&#x27;m specifically trying to investigate the difference in how two programs request a folder listing from the server. One program completes in less than 2...'''
date = "2014-09-02T06:25:00Z"
lastmod = "2014-09-02T11:27:00Z"
weight = 35928
keywords = [ "capture-filter", "webdav" ]
aliases = [ "/questions/35928" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Analyzing both directions of WebDAV transactions](/questions/35928/analyzing-both-directions-of-webdav-transactions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35928-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, The <a href="http://wiki.wireshark.org/SampleCaptures">Sample Captures</a> page does not include capture filters for analyzing WebDAV traffic (unless WebDAV traffic is known under some other name?).</p><p>I'm specifically trying to investigate the difference in how two programs request a folder listing from the server. One program completes in less than 2 seconds, the other program takes 40+ seconds and almost 4 times the data is sent back from the server, so it looks like the second program requests a lot more than the folder contents. I'm running the webDAV server on a physically different computer in a test environment so it is setup as an HTTP server with only Basic Authentication so my expectations would be to see packets with username and password and also the "commands" or requests un-encrypted and in plain format.</p><p>My problem is that when I do a capture, I only see traffic FROM the WebDAV Server TO the client. I don't see any traffic at all from the client to the server. I would expect to see: a) client log-on and session opening traffic b) client request/command packets.</p><p>What I tried (all of the below were done with promiscuous mode on): 1) no capture filter, start capture before running test programs, end capture after programs complete, then using display filters to attempt to show any and all traffic TO the server using server MAC such as eth.addr == xx:xx:xx:xx:xx:xx I also used "destination" and "source" IP filters to see server to client and client to server traffic.. No luck. 2) using capture filters in various combinations such as: host 192.168.1.175 and host 192.168.1.9 or ether host XX:XX:XX:XX:XX:XX or ether dst XX:XX:XX:XX:XX:XX again, I get nothing going too the server?!</p><p>I have so far attempted the captures on the same PC as the webDAV client is running, which seems like it should be fine to do so since traffic to the server would originate on this machine. However, I also have SharkTap and could drum up other clients so I could do a man in the middle capture, though I'm not sure why I would need to go to that step?</p></div><div id="question-tags" class="tags-container tags">capture-filter webdav</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '14, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/50310a8f0dc870c06bea29fac8b86486?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WhiteFang&#39;s gravatar image" /><p>WhiteFang<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WhiteFang has no accepted answers">0%</span></p></div></div><div id="comments-container-35928" class="comments-container"><span id="35929"></span><div id="comment-35929" class="comment"><div id="post-35929-score" class="comment-score"></div><div class="comment-text"><p>I just completed a "man in the middle" (or so I think) capture using this capture filter: ether host XX:XX:XX:XX:XX:XX or ether host XX:XX:XX:XX:XX:XX By my assumption/understanding, this capture filter should capture EVERYTHING from those two MAC addresses.</p><p>The PC running the wireshark was connected to the center port on the SharkTap "hub". The other two ports were used to put the sharktap "in-line" between the client device and the network with the webdav server. The trace came back with 3 ARP's (not related) and 6 packets From the Server and nothing again from the client. What am I doing wrong? -Why is there no outbound from the client in my captures?</p></div><div id="comment-35929-info" class="comment-info"><span class="comment-age">(02 Sep '14, 06:59)</span> WhiteFang</div></div></div><div id="comment-tools-35928" class="comment-tools"></div><div class="clear"></div><div id="comment-35928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35935"></span>

<div id="answer-container-35935" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35935-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>WebDAV is a variant/an extension of HTTP communication (as you already know apparently :-)), so it is really a HTTP capture you're looking for, e.g. "tcp port http", or "tcp port 80".</p><p>Can you provide some sort of diagram of your capture setup? It's a bit difficult to understand how and what you're capturing otherwise.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '14, 11:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35935" class="comments-container"></div><div id="comment-tools-35935" class="comment-tools"></div><div class="clear"></div><div id="comment-35935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35936"></span>

<div id="answer-container-35936" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35936-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For completeness sake, my answer is below, though in the process of writing my answer, I found my "stupid user" problem.. I was NOT running code from the client device the way I thought I was, my debugger mode was still on and the "client" code executed from my laptop IDE, not from my client device. So a long story short, WebDAV (and similar) must be sniffed using "man-in-the-middle" to get complete picture of transactions. For broadest capture between two devices, uses "ether host" filters to capture anything and everything between two physical MAC addresses.</p><p>I used both of these capture filters and both worked now that I'm properly executing on the device: (ether host XX:XX:XX:XX:XX:XX or ether host XX:XX:XX:XX:XX:XX) and tcp port http ether host XX:XX:XX:XX:XX:XX or ether host XX:XX:XX:XX:XX:XX</p><p>My setup as shown ASCII art.. hope that helps:</p><p>Client device --&gt; SharkTap in / SharkTap out --&gt; WebDAV Server TAP port | PC with Wireshark SW</p><p>Basically, the PC running wireshark is connected to a SharkTap network sniffer that repeats all traffic on the two in/out ports onto a 3rd port, the tap, essentially acting as a good old fashioned "stupid" hub.. but you probably know that. :)</p><p>Hope this clarifies and helps someone else in the future!<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '14, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/50310a8f0dc870c06bea29fac8b86486?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WhiteFang&#39;s gravatar image" /><p>WhiteFang<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WhiteFang has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-35936" class="comments-container"></div><div id="comment-tools-35936" class="comment-tools"></div><div class="clear"></div><div id="comment-35936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

