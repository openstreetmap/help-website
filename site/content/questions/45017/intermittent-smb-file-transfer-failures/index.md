+++
type = "question"
title = "Intermittent SMB File Transfer Failures"
description = '''Hi, I&#x27;m using packet captures to troubleshoot failed file transfers between 2 hosts and have a few questions about what I&#x27;m seeing. It looks to me like there is a loop some where and I need someone here to help with that theory to see if I should continue with my current method of troubleshooting or...'''
date = "2015-08-12T13:02:00Z"
lastmod = "2015-08-12T14:02:00Z"
weight = 45017
keywords = [ "padding", "ipid", "smb", "vm" ]
aliases = [ "/questions/45017" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Intermittent SMB File Transfer Failures](/questions/45017/intermittent-smb-file-transfer-failures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45017-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm using packet captures to troubleshoot failed file transfers between 2 hosts and have a few questions about what I'm seeing. It looks to me like there is a loop some where and I need someone here to help with that theory to see if I should continue with my current method of troubleshooting or go down a different rabbit hole.</p><p><strong>THE SCENARIO:</strong></p><p>A Solaris Zone on an LDOM (client) is using SMBv1 to copy log files from several Windows 2008 servers. These W2K8 servers are themselves VMs running on a VMware vSphere 5 host on a Cisco UCS. Most of the time the file transfers work but sometimes they fail. The frequency of the failures changes. Sometimes 100 transfers will work and then the 101st fails. Other times every 2nd transfer fails. The client experiences about a 20 second delay before an error is returned and it closes the connection. From the captures I believe that the client end is good. I am seeing some things I can't explain on the server side.</p><p><strong>MY OBSERVATIONS:</strong></p><p>1) I can see the 20 second delay on the client side - frame #654 to #655.</p><p>2) The server side capture is where I'm seeing things that I can't explain.</p><p>3) There are DUP ACKs from the client and retransmissions from the server, neither of which show up in the client capture. I've captured at various points in the path to rule out a bad capture at the client or a malfunctioning client.</p><p>4) The DUP ACKs (frames 642-646, 650, 667, 669, 671, 673, 675, 677, 679) all have an ethernet padding of ac:1f:80:36:ac:1f. When everything is working properly, normal ACKs have an ethernet padding of aa:aa:00:00:aa:aa. All other values in the DUP ACKs seem to be the same as in a normal ACK (i.e. src and dst MAC addresses).</p><p>5) The DUP ACKs also have an IP.ID value that doesn't fit into the normal range of ACKs from client to server. In fact, the IP.ID value of the DUP ACKs (client to server) are the exact same as the retransmissions (server to client) that immediately preceed the DUP ACK.</p><p>6) The DUP ACKs appear less than 1ms after each retransmission which is less than the iRTT</p><p><strong>THE CAPTURES:</strong></p><p><a href="https://drive.google.com/file/d/0B1VCXEQQl2dKU05LR3M2UFViLXc/view?usp=sharing">client side</a></p><p><a href="https://drive.google.com/file/d/0B1VCXEQQl2dKMExyUG5ZRWNNY0U/view?usp=sharing">server side</a></p><p><a href="https://drive.google.com/file/d/0B1VCXEQQl2dKRENpMFVaM1dKUVU/view?usp=sharing">normal padding</a></p><p><a href="https://drive.google.com/file/d/0B1VCXEQQl2dKVU1tMlZwVE5jWGs/view?usp=sharing">abnormal padding</a></p><p>The client and server captures have both been sanitized using TraceWrangler but unfortunately this changed the ethernet padding. The normal and abnormal padding captures each contain a few packets that were unsanitized so you can see what I see.</p><p><strong>THE QUESTIONS:</strong></p><p>1) Does the value used in ethernet padding hold any significance or is it randomly generated? It doesn't look random to me</p><p>2) Can I use the ethernet padding value to figure out where the frames are originating since I don't see them on the client side?</p><p>3) Can I assume a server side problem since The IP.ID value on the DUP ACKs is the same as for the retransmissions (and is out of range as compared to other client to server traffic) and the DUP ACKs happen right after each retransmission?</p><p>Thanks,</p><p>Bruno</p></div><div id="question-tags" class="tags-container tags">padding ipid smb vm</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '15, 13:02</strong></p><img src="https://secure.gravatar.com/avatar/03769b6187cefe87be2b755ce4b27e8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bruno%20Wollmann&#39;s gravatar image" /><p>Bruno Wollmann<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bruno Wollmann has no accepted answers">0%</span></p></div></div><div id="comments-container-45017" class="comments-container"></div><div id="comment-tools-45017" class="comment-tools"></div><div class="clear"></div><div id="comment-45017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45021"></span>

<div id="answer-container-45021" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45021-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>My guess is there is an "invisible" device between client and server. Take a look at the TTL values in the server trace coming from 172.31.20.97 - most of the time it's 58 (probably 6 hops away), but when the trouble starts we see a TTL of 254 (1 hop away). It looks like there is something right in front of the server, probably a load balancer or traffic shaper. You should identify that device and find out what it's doing, because it looks like it's the reason for your trouble.</p><p>Best way to see this is to select the TTL in any of the packets, and use the popup menu to select "Apply as column". Then filter on "ip.src == 172.31.20.97".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '15, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-45021" class="comments-container"><span id="45022"></span><div id="comment-45022" class="comment"><div id="post-45022-score" class="comment-score"></div><div class="comment-text"><p>It was my guess, too.</p></div><div id="comment-45022-info" class="comment-info"><span class="comment-age">(12 Aug '15, 14:26)</span> Christian_R</div></div><span id="45032"></span><div id="comment-45032" class="comment"><div id="post-45032-score" class="comment-score"></div><div class="comment-text"><p>I see it now that you pointed it out. I got so focused on the ip.id and padding I stopped looking for other clues. There is a transparent LB in the same VLAN as the server. I will check this out and let you know what I find.</p><p>Thanks</p></div><div id="comment-45032-info" class="comment-info"><span class="comment-age">(12 Aug '15, 21:13)</span> Bruno Wollmann</div></div><span id="45838"></span><div id="comment-45838" class="comment"><div id="post-45838-score" class="comment-score"></div><div class="comment-text"><p>I finally got to the bottom of this.</p><p>As pointed out by Jasper, the problem was 1 hop away and in this section of the customer's network there are 2 transparent devices. 1 is a firewall and the other is an IPS. The captures proved that the IPS was causing the problem but it took a few weeks to convince the vendor of this. After a couple more packet captures and many emails back and forth the vendor finally acknowledged a bug in their code. This was a great learning experience for me and I was able to get answers for question #1 and 2 in my original post. I learned that ethernet padding means nothing really as I couldn't use it to pinpoint the source of the trouble packets.</p></div><div id="comment-45838-info" class="comment-info"><span class="comment-age">(14 Sep '15, 20:01)</span> Bruno Wollmann</div></div></div><div id="comment-tools-45021" class="comment-tools"></div><div class="clear"></div><div id="comment-45021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

