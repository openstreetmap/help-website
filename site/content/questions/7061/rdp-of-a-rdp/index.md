+++
type = "question"
title = "RDP of a RDP"
description = '''Hi Folks..... and thanks for reading my question. First some background: I have a situation where I have a user in India using RDP to connect to a virtual desktop (VDI on VMWare View) in a data center in the U.S. This works OK. The user then starts a remote control session from the VDI to remote con...'''
date = "2011-10-25T08:34:00Z"
lastmod = "2011-10-26T03:16:00Z"
weight = 7061
keywords = [ "rdp", "windowing" ]
aliases = [ "/questions/7061" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [RDP of a RDP](/questions/7061/rdp-of-a-rdp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7061-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7061-score" class="post-score" title="current number of votes">0</div><span id="post-7061-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Folks.....</p><p>and thanks for reading my question. First some background:</p><p>I have a situation where I have a user in India using RDP to connect to a virtual desktop (VDI on VMWare View) in a data center in the U.S. This works OK. The user then starts a remote control session from the VDI to remote control (via RDP) a Sharepoint server in that same data center. I hope that is clear.</p><p>On occasion this runs quite slow. I have captured packets on the VDI so I can see both the connection from the user machine to the VDI as well as the VDI to the Sharepoint server. When looking at the packets with Wireshark I can see that on the TCP connection from the VDI to the Sharepoint server the TCP Calculated Window Size often drops to zero or 100 or 200 bytes (that is what the VDI is advertising to the Sharepoint server). Note this is the LAN connection within the data center. On the other RDP/TCP connection, from the client machine to the VDI, the TCP Calculated Window Size stays at about 64k throughout with only minor fluctuations. This is the WAN connection back to India.</p><ol><li>It seems (to me anyway) as if this situation is saying that there is some type of resource shortage on the VDI because it is not processing the received packets quickly enough and therefore sending back the low TCP Calculated Window Size value in the ACKs. Does this sound reasonable? Any ideas on where to look for a potential resource shortage?</li><li>Am I reading the situation incorrectly? Any other ideas?</li><li>Generally speaking can one TCP connection influence another? Like can what is going on on the TCP/RDP session from the client to the VDI influence the behavior of the TCP/RDP session between the VDI and the Sharepoint server? Up at the application layer are they even aware of each other?</li></ol><p>Any feedback would be much appreciated. Thanks, F</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rdp" rel="tag" title="see questions tagged &#39;rdp&#39;">rdp</span> <span class="post-tag tag-link-windowing" rel="tag" title="see questions tagged &#39;windowing&#39;">windowing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '11, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/d6de2db9e8d2dea8e691e94a8859008a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fredonians&#39;s gravatar image" /><p><span>Fredonians</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fredonians has no accepted answers">0%</span></p></div></div><div id="comments-container-7061" class="comments-container"></div><div id="comment-tools-7061" class="comment-tools"></div><div class="clear"></div><div id="comment-7061-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7076"></span>

<div id="answer-container-7076" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7076-score" class="post-score" title="current number of votes">1</div><span id="post-7076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A small window size usually indicates a resource shortage on the system advertising the small window. This is one of the best indicators for a network engineer to pin a problem to a certain server.</p><p>Alas, it's not that easy.</p><p>Window Scaling often causes a TCP connection to show window sizes of a few hundred byte. If Wireshark sees the 3-way handshake it observes the window scale factor and calculates the correct window size. The next line in the decode shows the scaling factor.</p><p>If Wireshark does not know about the 3-way handshake you still see the term "calculated window size", but the scaling factor is reported as -1 to show an unknown scale factor.</p><p>Make sure, that you have recorded the 3-way handshake before interpreting the window size.</p><p>If you have the 3-way handshake and are still are at 200 byte window size something is wrong. Here are a few reasons that we found when analyzing network traffic:</p><ul><li>The server is really out of resources and completely overloaded. In these cases I try to visualize the workload using the Load-Graph in IO-Graphs and collect service response time statistics. This only works for a few protocols.</li><li>A workstation receives large graphical images (like bitmaps) but the system can not visualize the data as quick as it comes in (caused by a slow bus or low end graphics card). Increasing the systems TCP receive window solved this problem without spending money.</li><li>Some transparent device modifies the TCP window size while the packet flows through. We have observed this behaviour in several products that manage bandwidths. The devices sometimes use algorithms that go back to the 80-ies or 90-ies. We usually categorize them as snake oil.</li><li>Installing a virus scanner on a workstation can cause a smaller receive window. Though I have never seen the window size go so small that it creates performance problems.</li></ul><p>When analyzing small TCP windows I look at the next few frames in the connection. The system with the small window should send a window update within a few milliseconds, advertising a much bigger receive window. If these window updates are not coming in the sender usually waits several seconds before sending a small packet.</p><p>Oh, and one more thing: If you are in India and your server is in the US calculate the optimum window size for this link:</p><p>Calculate your bandwidth in Byte per second and multiply by your round trip time in seconds. If this value is significantly higher than 64k you can get better throughput by activating window scaling.</p><p>Hope that helps. Keep on hunting!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '11, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Oct '11, 03:22</strong> </span></p></div></div><div id="comments-container-7076" class="comments-container"></div><div id="comment-tools-7076" class="comment-tools"></div><div class="clear"></div><div id="comment-7076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

