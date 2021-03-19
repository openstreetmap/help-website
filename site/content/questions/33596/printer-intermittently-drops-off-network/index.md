+++
type = "question"
title = "Printer intermittently &quot;drops&quot; off network"
description = '''Hi all. Been having a problem with a copier that has scanning/printing capabilities for a month or so now. The machine will randomly drop from the network, you can still ping it but print jobs will fail and you are unable to access it&#x27;s web interface. The copier service people have replaced the NIC ...'''
date = "2014-06-09T15:00:00Z"
lastmod = "2014-06-15T03:01:00Z"
weight = 33596
keywords = [ "dropping", "drop", "printer", "copier", "dropped" ]
aliases = [ "/questions/33596" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Printer intermittently "drops" off network](/questions/33596/printer-intermittently-drops-off-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33596-score" class="post-score" title="current number of votes">0</div><span id="post-33596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all. Been having a problem with a copier that has scanning/printing capabilities for a month or so now. The machine will randomly drop from the network, you can still ping it but print jobs will fail and you are unable to access it's web interface. The copier service people have replaced the NIC and main control board and the problem is still present. We've gone through the motions of disabling any unused protocols on the machine in case it was creating too much traffic for the device, switched the IP address and completely uninstalled and reinstalled the drivers on our print server. I captured a log of my workstation trying to send a print job and this is what wireshark gave me when the job failed. I created a filter for my workstation(192.168.1.10) and the printer(192.168.1.11) on port 9100 since I would assume all the print data is going through that port. I'm still new to wireshark so if anyone could help me out and explain why all these lines are in Black/Red/Dark Grey compared to the light blue lines when the machine works normally I would greatly appreciate it, thanks.</p><pre><code>10683   700.434934000   192.168.1.11    192.168.1.10    TCP 62  [TCP ACKed unseen segment] hp-pdl-datastr &gt; 56487 [SYN, ACK] Seq=0 Ack=1020557286 Win=16384 Len=0 MSS=1460 WS=1
10684   700.434986000   192.168.1.10    192.168.1.11    TCP 54  56487 &gt; hp-pdl-datastr [RST] Seq=1020557286 Win=0 Len=0
10705   703.428448000   192.168.1.11    192.168.1.10    TCP 62  [TCP ACKed unseen segment] hp-pdl-datastr &gt; 56487 [SYN, ACK] Seq=0 Ack=1020557286 Win=16384 Len=0 MSS=1460 WS=1
10706   703.428554000   192.168.1.10    192.168.1.11    TCP 54  56487 &gt; hp-pdl-datastr [RST] Seq=1020557286 Win=0 Len=0
10707   703.437296000   192.168.1.10    192.168.1.11    TCP 66  56487 &gt; hp-pdl-datastr [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
10708   703.437747000   192.168.1.11    192.168.1.10    TCP 62  hp-pdl-datastr &gt; 56487 [SYN, ACK] Seq=0 Ack=1020557286 Win=16384 Len=0 MSS=1460 WS=1
10709   703.437816000   192.168.1.10    192.168.1.11    TCP 54  56487 &gt; hp-pdl-datastr [RST] Seq=1020557286 Win=0 Len=0</code></pre><p>This keeps going on over and over until I do a hard reboot on the machine, it prints the stuff out on the print queue and sure enough a few minutes later no more printing. I know this isnt a forum for other people to fix my problems but time is of the essence on this one so any help is nice!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dropping" rel="tag" title="see questions tagged &#39;dropping&#39;">dropping</span> <span class="post-tag tag-link-drop" rel="tag" title="see questions tagged &#39;drop&#39;">drop</span> <span class="post-tag tag-link-printer" rel="tag" title="see questions tagged &#39;printer&#39;">printer</span> <span class="post-tag tag-link-copier" rel="tag" title="see questions tagged &#39;copier&#39;">copier</span> <span class="post-tag tag-link-dropped" rel="tag" title="see questions tagged &#39;dropped&#39;">dropped</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '14, 15:00</strong></p><img src="https://secure.gravatar.com/avatar/5023932293fc51aba957fa3ab5eb4f6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="osty&#39;s gravatar image" /><p><span>osty</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="osty has no accepted answers">0%</span></p></div></div><div id="comments-container-33596" class="comments-container"><span id="33598"></span><div id="comment-33598" class="comment"><div id="post-33598-score" class="comment-score"></div><div class="comment-text"><p>Would you be able to upload the packet capture and post the URL here (<a href="https://appliance.cloudshark.org/upload/">https://appliance.cloudshark.org/upload/</a> )?</p><p>One comment is that those "RST" flags are being sent from your workstation to terminate the TCP session after it tries to initiate a session (at the end there, you see SYN from your workstation to establish a session, SYN ACK in response from the printer, and RST to terminate sent by the workstation).</p><p>WIthout seeing the full trace it's hard to say what reds/blacks you're talking about, but there are a few common/normal causes that aren't actual problems, though those RST flags do look like they could be related to your problem since those are session disconnects when you're just trying to establish a TCP connection.</p><p>Also, you say you assume that 9100 is the correct port. To be safe, can you please do that trace without any port-level filtering between your workstation and the printer?</p></div><div id="comment-33598-info" class="comment-info"><span class="comment-age">(09 Jun '14, 17:54)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-33596" class="comment-tools"></div><div class="clear"></div><div id="comment-33596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33705"></span>

<div id="answer-container-33705" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33705-score" class="post-score" title="current number of votes">0</div><span id="post-33705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's time consuming and annoying to do packet analysis based on text exports and screen shots (not in your case), so please post the capture file somewhere, like: google drive, dropbox, cloudshark.org. Thank you!</p><p>Now, for the problem: By looking at the text output, we can see, that the SYN-ACK arrives with the wrong sequence number, and thus the client sends a RESET.</p><p>Explanation:</p><p>SYN frame uses SEQ=0, which is an indication, that relative sequences numbers is activated for the TCP protocol (default setting), so Wireshark will remember the real sequence number (whatever it might be) and count from there. Thus the SYN is shown with SEQ=0.</p><p>SYN-ACK frame shows <strong>Ack=1020557286</strong>. This is <strong>wrong</strong> it should be ACK=1 (remember the relative sequence numbers), so the TCP stack of the server ACKs 1020557286 bytes, while it should have ACKed only one byte (the SYN flag).</p><p>RESET: The client send a RESET, because the SYN-ACK is totally wrong.</p><p>So, everything O.K. on the client side. There seems to be a bug in the firmware of the printer. As you say, that the problem occurs for a month or so, I guess it was caused by a firmware upgrade (or downgrade), that took place ~ one month ago.</p><pre><code>10707   703.437296000   192.168.1.10    192.168.1.11    TCP 66  56487 &gt; hp-pdl-datastr [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
10708   703.437747000   192.168.1.11    192.168.1.10    TCP 62  hp-pdl-datastr &gt; 56487 [SYN, ACK] Seq=0 Ack=1020557286 Win=16384 Len=0 MSS=1460 WS=1
10709   703.437816000   192.168.1.10    192.168.1.11    TCP 54  56487 &gt; hp-pdl-datastr [RST] Seq=1020557286 Win=0 Len=0</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '14, 05:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jun '14, 06:14</strong> </span></p></div></div><div id="comments-container-33705" class="comments-container"><span id="33799"></span><div id="comment-33799" class="comment"><div id="post-33799-score" class="comment-score"></div><div class="comment-text"><p>Yes totally agree with Kurt but one more interesting thing to notice is that within span of 3 second client has opened atleast 3 session with same source port and printer is acking with same ack no everytime.</p></div><div id="comment-33799-info" class="comment-info"><span class="comment-age">(14 Jun '14, 04:07)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="33815"></span><div id="comment-33815" class="comment"><div id="post-33815-score" class="comment-score"></div><div class="comment-text"><p>Yes, interesting that the client does not increase the source port after the reset.</p><p>BTW: It's not necessarily the <strong>same</strong> ACK number, it's probably just the same ACK <strong>delta</strong> (remember the relative SEQ number display in Wireshark). So, until <span>@osty</span> posts the capture file, we cannot know which SEQ number the client was using for the new connection attempts.</p></div><div id="comment-33815-info" class="comment-info"><span class="comment-age">(15 Jun '14, 03:01)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-33705" class="comment-tools"></div><div class="clear"></div><div id="comment-33705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

