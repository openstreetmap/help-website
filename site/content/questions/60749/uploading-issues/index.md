+++
type = "question"
title = "Uploading Issues"
description = '''To whom it may concern, While I am not new to Help Desk work I am relatively new to advanced networking operations such as deciphering Wireshark messages as related to tracking down why errors pop up in applications when uploading files over the internet. If I&#x27;m able to, I&#x27;m going to attached 3 Wire...'''
date = "2017-04-11T11:22:00Z"
lastmod = "2017-04-12T00:05:00Z"
weight = 60749
keywords = [ "files", "upload" ]
aliases = [ "/questions/60749" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Uploading Issues](/questions/60749/uploading-issues)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60749-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>To whom it may concern, While I am not new to Help Desk work I am relatively new to advanced networking operations such as deciphering Wireshark messages as related to tracking down why errors pop up in applications when uploading files over the internet. If I'm able to, I'm going to attached 3 Wireshark captures to this message. One is from the device that was doing the uploading and the other 2 were from the Cisco ASA firewall's ingress_egress capturing TCP only. These captures were all performed simultaneously, of course, but the added twist is my ASA captures are about 8 minutes fast (sorry about that). The time on the 'Nancy' capture is correct and the specific times the PC was throwing out each error message during the upload were at 2:08 p.m., 2:09 p.m. and 2:14 p.m. Wireshark captures are located at: <a href="https://drive.google.com/open?id=0B6yAAiHYJtJSU3phWUl3eFdseDQ">https://drive.google.com/open?id=0B6yAAiHYJtJSU3phWUl3eFdseDQ</a></p></div><div id="question-tags" class="tags-container tags">files upload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '17, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/03a8fb8c182668999f380e3dc4193ac9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mahrsmusic&#39;s gravatar image" /><p>mahrsmusic<br />
<span class="score" title="4 reputation points">4</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mahrsmusic has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Apr '17, 11:27</p></div></div><div id="comments-container-60749" class="comments-container"></div><div id="comment-tools-60749" class="comment-tools"></div><div class="clear"></div><div id="comment-60749-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60756"></span>

<div id="answer-container-60756" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60756-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've taken the time to answer this one because I think that it might make a nice case study one day.</p><p>I can't tell you why but I can tell you what is happening.</p><p>There are many HTTPS connections to 52.5.5.205 in this capture. The 7 connections have client port numbers 57519, 57565, 57568, 57580, 57587, 57589 &amp; 57638 and they all have a similar form in the way they terminate. Since they sessions are encrypted, we can't see what the transactions contained or if there were any HTTP error messages within them.</p><p>Using the last one, port 57638, as an example, here's what happens:</p><ol><li>There is short burst of normal looking activity.</li><li>Then there is 21 seconds of inactivity.</li><li>The server presumably times out and issues a Final (packet #138287).</li><li>The client ACKs (#18288) that Final but doesn't send one of its own.</li><li>After a further 9 seconds, the client sends a burst of 64 KB of data, spread across 4 round trips (#139262 - #139359).</li><li>The server acknowledges all the data.</li><li>The server, however, does not send any response to that data (because it has already closed the connection).</li><li>The client then sends its own Final (#139360).</li></ol><p>These connections/terminations seem to match the times you mention. Further, they look the same in your other ASA captures.</p><p>My suspicion would be that these requests with no response are triggering your error messages.</p><p>The questions you might like to find answers to are:</p><ul><li>Does your server have a timeout setting of around 20-21 seconds?</li><li>Can that be made longer (as a test)?</li><li>Why doesn't your client send any data in that 21 seconds?</li><li>Or, why does the client wait 30 seconds to send its last request.</li></ul><p>I note that there was lots and lots of other traffic in your PC trace. Just for fun (other readers might like to test their skills in finding these) here are some other items that I found interesting.</p><ol><li>The GoDaddy SSL certificate for "*lifelogics.org" expired on 31-05-03 (May 31 2003?) but the application still accepts it.</li><li>In the SMB2 file server connection to 10.10.105.114 there are many accesses to a "thumbs.db" file that is at least 64 MB in size. All the accesses are for 4 KB at a time (as SMB does).</li><li>SMB2 traffic to a different file server contains dozens of accesses to "Paris\UPDATES\PixMoveNancy.exe" that fail with "ACCESS_DENIED".</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '17, 00:05</strong></p><img src="https://secure.gravatar.com/avatar/35a0c1d0cf15b9d54d73bf54ae28abcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Philst&#39;s gravatar image" /><p>Philst<br />
<span class="score" title="431 reputation points">431</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Philst has 6 accepted answers">27%</span></p></div></div><div id="comments-container-60756" class="comments-container"><span id="61082"></span><div id="comment-61082" class="comment"><div id="post-61082-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much! I tried to cast my vote but it's says I'm not able to at this time. AWESOME ANSWER! Thank you again, so much! I've been trying to learn Wireshark for the past 2 weeks (and study for my CCNA, raise 3 kids, etc. etc.). Your help is SO MUCH APPRECIATED!!!!</p></div><div id="comment-61082-info" class="comment-info"><span class="comment-age">(27 Apr '17, 16:23)</span> mahrsmusic</div></div></div><div id="comment-tools-60756" class="comment-tools"></div><div class="clear"></div><div id="comment-60756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

