+++
type = "question"
title = "Piping remote tcpdump to local Wireshark no longer working"
description = '''A couple days ago, this command was working: ssh root@10.123.123.123 &#x27;ssh host2 &quot;tcpdump -i bond1.800 -s0 -U -w - port 9990 or port 5060 or port 3868&quot;&#x27; | wireshark -k -i -  I was able to open wireshark on my local machine with that command, and I was able to see the packets arriving in wireshark as ...'''
date = "2017-02-10T08:00:00Z"
lastmod = "2017-02-10T08:00:00Z"
weight = 59332
keywords = [ "pipe", "tcpdump", "cygwin", "wireshark" ]
aliases = [ "/questions/59332" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Piping remote tcpdump to local Wireshark no longer working](/questions/59332/piping-remote-tcpdump-to-local-wireshark-no-longer-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59332-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A couple days ago, this command was working:</p><pre><code>ssh [email protected] &#39;ssh host2 &quot;tcpdump -i bond1.800 -s0 -U -w - port 9990 or port 5060 or port 3868&quot;&#39; | wireshark -k -i -</code></pre><p>I was able to open wireshark on my local machine with that command, and I was able to see the packets arriving in wireshark as the remote host was capturing them. Then I closed wireshark, which ended the command. I tried running the command again a second time (the exact same command) and it no longer worked. I've also tried rebooting my machine, but to no avail.<br />
</p><p>If I run it with "cat -" instead of wireshark, I see a constant stream of packets.</p><pre><code>ssh [email protected] &#39;ssh host2 &quot;tcpdump -i bond1.800 -s0 -U -w - port 9990 or port 5060 or port 3868&quot;&#39; | cat -</code></pre><p>It will keep outputting the packets to my terminal until I end it with Ctrl C. But if I do it with wireshark, I get the following output:</p><pre><code>ssh [email protected] &#39;ssh host2 &quot;tcpdump -i bond1.800 -s0 -U -w - port 9990 or port 5060 or port 3868&quot;&#39; | wireshark -k -i -
Password:
tcpdump: listening on bond1.800, link-type EN10MB (Ethernet), capture size 65535 bytes
19 packets captured
19 packets received by filter
0 packets dropped by kernel</code></pre><p>As you can see, only 19 packets came through before the trace mysteriously ended. Those packets were not displayed in wireshark.<br />
</p><p>My setup is a local Windows 7 laptop with Wireshark Version 2.2.4 (v2.2.4-0-gcc3dc1b), and I am running those commands in Cygwin. At the time that the command was working, I was also able to open wireshark to watch packets from another remote host, with this command:</p><pre><code>ssh -C [email protected] &#39;tcpdump -i bond0 -i eth2 -i eth3 -i eth4 -i eth5 -i eth6 -i eth7 -s0 -U -w - port 5060 or port 3868&#39; | wireshark -k -i -</code></pre><p>I don't think all of the interfaces were working (it might have just been capturing on <code>eth7</code>), but it was capturing packets and displaying them in wireshark on my local machine. That one also stopped working at the same time. I didn't change any parameters in wireshark, or install any different packages. Everything stayed the same from the working iteration to the failing iteration.</p><p>Any help in diagnosing this issue is greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">pipe tcpdump cygwin wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '17, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/e96b0196e8e968b1a2d8f6ddfda87ab1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lemurshark&#39;s gravatar image" /><p>Lemurshark<br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lemurshark has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-59332" class="comments-container"><span id="59337"></span><div id="comment-59337" class="comment"><div id="post-59337-score" class="comment-score"></div><div class="comment-text"><p>I don't have an answer for you, as this always worked for me in my testing, but something to check - is <code>tcpdump</code> still running on the remote host? Only when I logged into the remote host and manually killed <code>tcpdump</code>, then I saw the capture summary information; otherwise I'd never see. Also, as far as I know, <code>tcpdump</code> only accepts a single interface for its <code>-i</code> option, so if you specify more than one, only the last one will be the active interface upon which it captures.</p></div><div id="comment-59337-info" class="comment-info"><span class="comment-age">(10 Feb '17, 13:15)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-59332" class="comment-tools"></div><div class="clear"></div><div id="comment-59332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

