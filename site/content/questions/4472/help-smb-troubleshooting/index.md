+++
type = "question"
title = "Help SMB Troubleshooting ?"
description = '''Hello, I have current situation a client (win2k3) 1Gigbit net that using to edit video with flowing format HD 100mbit + 4 wave Chanel audio , the media is located on storage (exanet ,redhat based). The issue is that while the client reading the video and when he needs to slide/scroll back the video ...'''
date = "2011-06-09T06:05:00Z"
lastmod = "2011-06-14T10:22:00Z"
weight = 4472
keywords = [ "smb", "troubleshooting" ]
aliases = [ "/questions/4472" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Help SMB Troubleshooting ?](/questions/4472/help-smb-troubleshooting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4472-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have current situation a client (win2k3) 1Gigbit net that using to edit video with flowing format HD 100mbit + 4 wave Chanel audio , the media is located on storage (exanet ,redhat based). The issue is that while the client reading the video and when he needs to slide/scroll back the video the video is playing but the sound is getting behind the video lip-sync. I did a trace of 60 sec in around 22 sec to 27 slide/scroll back occur few sec after it we saw the sound getting behind the video lip-sync , in our video definition usually after 40ms DELAY we start to see lost frame or lip-sync issues . i did some analyze on the trace i can see that the storage having some delay read request issues few seconds after scrolling back the video more than half a minute and even more further. whats bothers me in the trace that when analyzing <strong>tcp.analysis.ack_rtt</strong> as well i can see that there is some periods of trace more than 50ms delays from both client and server , can i get into conclusion that the client suffer from some network congestion or also the storage?. any idea and tips would be appreciated since its one of my first <strong>smb</strong> analyzing. Please advice Thanks <img src="http://f8nlpa.sn2.livefilestore.com/y1p1REo95eNel8VEOALV5BMcJOrMFWTvy5t_7mP65buFKyoCtoFThyJsPhAkYVDaCAVAOgCR_VrH3EArER63o4S9izg89DSjh73/s4strace.png?psid=1" alt="alt text" /> <img src="http://f8nlpa.sn2.livefilestore.com/y1pAskbrGLmL_2PpdUSAQ6ZDXRduOdk5QCZCQEJu5_OOmAi9niZ8tQNr1-_ImKEMQ0Z6KMA7-nqoTi64Gk11p6bnz4EM5oQUH92/smbstat.png?psid=1" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">smb troubleshooting</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '11, 06:05</strong></p><img src="https://secure.gravatar.com/avatar/491b248bc5431fa4cfed4498e4633f51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tbaror&#39;s gravatar image" /><p>tbaror<br />
<span class="score" title="10 reputation points">10</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tbaror has no accepted answers">0%</span></p></img></div></div><div id="comments-container-4472" class="comments-container"></div><div id="comment-tools-4472" class="comment-tools"></div><div class="clear"></div><div id="comment-4472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="4554"></span>

<div id="answer-container-4554" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4554-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>                     Hi,</code></pre><p>You can go and start troubleshooting SMB in several way's but there's a lot of dark corners in that protocol! Here's what i do first: 1.check if SMB version 1 is used (in SMB 2.1, loads of things have changed): You can find these values in the SMB negotiation part of an SMB conversation, right after the TCP 3-way handshake, use “smb.cmd == 0x72” which means filter on all “SMB Command: Negotiate Protocol (0x72)” to see what dialects the client is capable of. The last dialect listed, NT LM 0.12, is SMB 1.0.</p><p>And after see what client and server have agreed upon, find the response to this request (eg “Negotiate Protocol Response (0x72)”) In short you can tell by only looking if the agreed upon value is SMB 1.0 by filtering on “smb.dialect.index == 5”</p><ol><li><p>if SMB 1, then look at the general flow of the conversation, by filtering on: a. filter on "smb" b. rightclick on a packet in the right stream and go "follow tcp stream"</p></li><li><p>with this filter you can then go and have a look at all the SMB service response Time statistics that matter for your conversation, by going: "statistics&gt;service response time&gt; SMB"</p></li></ol><p>Here you can find wich command gives the largest delay's , sort the rows, then right click and "prepare a filter" , use the filter (and save it for a rainy day) , f.i. "smb.cmd==50" Before you are all smb commands wich took the longest to complete, now mark 'm all by ctrl+shift+M, then clear..</p><ol><li>Now you can hop from marked packet to marked packet by using "ctrl+shift+N" to see what leads up to this command, or go and look inside of the packets and find out why a command is used.</li></ol><p>Maybe you've already used the time sort column to find the same answer?</p><p>View&gt;TimeDisplayFormat&gt;SecondsSincePreviousDisplayedPacket, then doubleclick on Time Column and go back up and see the packets that took the longest (be aware that this depends on your filter (eg filter on smb and this TimeFormat means that large time difference you see is the time that passed since the last packet that matched your smb filter was seen!).</p><p>If i find something interesting i always go back to the tcp stream concerning to see what follows what exactly. This is just a start, after you find what packets cause the delays you might need to sort out the application, sort out reg files, and so on...</p><p>PS loads of this i've actually picked up from Joke Snelders, go and read her blogs on wireshark http://www.lovemytool.com/blog/joke-snelders/ great stuff!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '11, 00:17</strong></p><img src="https://secure.gravatar.com/avatar/69710b84acce4cdf0a0cbdcb5930fda1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc&#39;s gravatar image" /><p>Marc<br />
<span class="score" title="147 reputation points">147</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc has 3 accepted answers">27%</span></p></img></div></div><div id="comments-container-4554" class="comments-container"></div><div id="comment-tools-4554" class="comment-tools"></div><div class="clear"></div><div id="comment-4554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4556"></span>

<div id="answer-container-4556" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4556-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks Cheers</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '11, 01:23</strong></p><img src="https://secure.gravatar.com/avatar/491b248bc5431fa4cfed4498e4633f51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tbaror&#39;s gravatar image" /><p>tbaror<br />
<span class="score" title="10 reputation points">10</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tbaror has no accepted answers">0%</span></p></div></div><div id="comments-container-4556" class="comments-container"></div><div id="comment-tools-4556" class="comment-tools"></div><div class="clear"></div><div id="comment-4556-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4564"></span>

<div id="answer-container-4564" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4564-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Now seeing your graphs, go and see why it takes so long between the read request from client to the acknowledgement from the server eg mark the read request, follow tcp stream, clear filtering, then start from marked packet untill you see the ack from storage.</p><p>Can't be that many packets? If the ack after the req is fast (eg low latency, fast response, which would mean no hardware issues) if the data after the ack is slow to come, probably means that the application proces is slow.</p><p>If this is the case go and "process explore" the storage.</p><p>regards , Marc</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '11, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/69710b84acce4cdf0a0cbdcb5930fda1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc&#39;s gravatar image" /><p>Marc<br />
<span class="score" title="147 reputation points">147</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc has 3 accepted answers">27%</span></p></div></div><div id="comments-container-4564" class="comments-container"></div><div id="comment-tools-4564" class="comment-tools"></div><div class="clear"></div><div id="comment-4564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

