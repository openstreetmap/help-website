+++
type = "question"
title = "Is there an import facility for Linux logfiles"
description = '''I have some firewall logs (UFW/kern/syslog entries). Is there a way to import this data to Wireshark for some analysis/pictorial representation?'''
date = "2014-08-09T17:27:00Z"
lastmod = "2014-08-10T09:28:00Z"
weight = 35349
keywords = [ "syslog", "ufw", "linux" ]
aliases = [ "/questions/35349" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is there an import facility for Linux logfiles](/questions/35349/is-there-an-import-facility-for-linux-logfiles)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35349-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have some firewall logs (UFW/kern/syslog entries). Is there a way to import this data to Wireshark for some analysis/pictorial representation?</p></div><div id="question-tags" class="tags-container tags">syslog ufw linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '14, 17:27</strong></p><img src="https://secure.gravatar.com/avatar/1fcb17940df6c45665dd1ddef78611a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ColinJDenman&#39;s gravatar image" /><p>ColinJDenman<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ColinJDenman has no accepted answers">0%</span></p></div></div><div id="comments-container-35349" class="comments-container"></div><div id="comment-tools-35349" class="comment-tools"></div><div class="clear"></div><div id="comment-35349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35354"></span>

<div id="answer-container-35354" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35354-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Short answer is that Wireshark analyses packets, not logs. However, if you set up your Linux system as a syslog client and capture the UDP stream containing the syslog entries as packets, in concept that would contain them in a packet capture file that could be loaded into Wireshark.</p><p>What exactly are you looking to graph or get pictorial representations for? It's unlikely Wirrshark can do much more with the log files than awk/sed/grep or vi can for most practical purposes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '14, 03:54</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Aug '14, 03:55</p></div></div><div id="comments-container-35354" class="comments-container"><span id="35359"></span><div id="comment-35359" class="comment"><div id="post-35359-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I'd figured wireshark was the best tool for the job, and the data in the logs is sufficiently related to get useful info from.</p><p>I've recently switched ISP and want to see the traffic flow over time. The log is 1.8GB, a capture file would be even bigger.</p><p>I thought it might be possible to generate connection graphs of various kinds to understand the traffic coming in (like intrusion stuff).</p><p>I though it might be possible since one of the import formats is BSD pf logfiles (presumably not raw packet dumps), so I figured there would be something available for linux standard firewall logging.</p><p>Wireshark seems an obvious choice for this kind of analysis.</p></div><div id="comment-35359-info" class="comment-info"><span class="comment-age">(10 Aug '14, 05:42)</span> ColinJDenman</div></div><span id="35363"></span><div id="comment-35363" class="comment"><div id="post-35363-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Wireshark seems an obvious choice for this kind of analysis.</p></blockquote><p>Why do you think that? Wireshark is a <strong>network analysis/troubleshooting</strong> tool , <strong>not</strong> a log analysis tool !??!</p></div><div id="comment-35363-info" class="comment-info"><span class="comment-age">(10 Aug '14, 06:14)</span> Kurt Knochner ♦</div></div><span id="35366"></span><div id="comment-35366" class="comment"><div id="post-35366-score" class="comment-score"></div><div class="comment-text"><p>No need for hysteria. The source format is unusual but not radically different from capture, just much less detailed. Why wouldn't one want wireshark to do more than it does. Is the supported BSD pf input radically different from a normal logfile? In the end its all network traffic data. A capture file is just a compact logfile presumably, is it so much different to parse.</p></div><div id="comment-35366-info" class="comment-info"><span class="comment-age">(10 Aug '14, 06:30)</span> ColinJDenman</div></div><span id="35368"></span><div id="comment-35368" class="comment"><div id="post-35368-score" class="comment-score"></div><div class="comment-text"><p>No hysteria at all, at least not on my side.</p><blockquote><p>The source format is unusual but not radically different from capture, just much less detailed.</p></blockquote><p>I don't think so.</p><p>Can you please describe why you believe that a capture file is similar to a BSD pf log file?</p><blockquote><p>A capture file is just a compact logfile presumably,</p></blockquote><p>erm, let me think about that..... Nope!</p><blockquote><p>Why wouldn't one want wireshark to do more than it does</p></blockquote><p>That's actually a very good idea. Please implement that feature and submit the patches for the benefit of all Wireshark users.</p><p>You can use TFShark as a starting point:</p><blockquote><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9607">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9607</a></p></blockquote></div><div id="comment-35368-info" class="comment-info"><span class="comment-age">(10 Aug '14, 06:40)</span> Kurt Knochner ♦</div></div><span id="35385"></span><div id="comment-35385" class="comment"><div id="post-35385-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I've recently switched ISP and want to see the traffic flow over time. The log is 1.8GB, a capture file would be even bigger.</p></blockquote><p>What exactly do these log files contain? Counts of bytes and a directional context? If so, a one-liner AWK script would probably be enough to do what you want. Another option is to use tools designed to graph network usage, like NetFlow analyzers.</p><p>Wireshark <em>can</em> meet the basic requirement of monitoring and graphing network usage over time, though as you're talking about potentially huge amounts of data that becomes less and less practical. A simpler tshark-based statistics script might serve your purpose.</p><p>One example I did for a network was to set up dumpcap to do hourly packet captures, then run tshark -Z against those hourly captures to generate packet/byte counts of all sorts of different traffic types (limited only by Wireshark's supported display filter matching), which I piped to an excel file before deleting the packet capture file I'd gathered the stats from. In that case they wanted all kinds of different metrics out of the packet capture file but a lump sum of bytes is easily done by this method also. By this method you never have more than one time interval worth of packet data (to save on disk space) you're using dumpcap except for the statistics query (to save significantly on memory), and the only piece that hits the CPU to any real degree is the one stats grab on the hour (or you could offset it if the CPU is busy on the hour for other hourly things).</p></div><div id="comment-35385-info" class="comment-info"><span class="comment-age">(10 Aug '14, 12:26)</span> Quadratic</div></div></div><div id="comment-tools-35354" class="comment-tools"></div><div class="clear"></div><div id="comment-35354-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35384"></span>

<div id="answer-container-35384" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35384-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think I know where the confusion, regarding the import of <strong>log files</strong> into Wireshark, might have come from...</p><p>You said:</p><blockquote><p>I though it might be possible since <strong>one of the import formats is BSD pf logfiles</strong> (presumably not raw packet dumps)</p></blockquote><p>You might have thought that <strong>BSD pf logs</strong> are real text log files, but they are in fact <strong>pcap</strong> files, created by the <strong><a href="http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-5.5/man4/pflog.4?query=pflog&amp;sec=4&amp;manpath=OpenBSD-5%2e5">pflog</a></strong> feature of OpenBSD</p><blockquote><p><a href="http://www.openbsd.org/faq/pf/logging.html">http://www.openbsd.org/faq/pf/logging.html</a></p></blockquote><p>The BSD pf log <strong>capture files</strong> can be opened with Wireshark, as they are actually pcap files.</p><p>Wireshark is not able to do what you are requesting, as it's a network analysis/troubleshooting tool, not a log analysis tool. If you desperately need that feature, here are your options:</p><ul><li>implement it yourself (see TFShark for an example)</li><li>create an enhancement request at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and hope that somebody implements it for you</li></ul><p><strong>However</strong>, importing text based (firewall)logs, won't get you very far, as they contain by far not enough information to make Wireshark useful in any way.</p><p>On <strong>Windows</strong>, the following tool could be a possible solution for you: <a href="http://www.wallwatcher1.com/">Wallwatcher</a></p><p>See here: <a href="http://ask.wireshark.org/questions/35360/wireshark-sending-syslog-data-to-my-pc-from-dd-wrt-not-working">http://ask.wireshark.org/questions/35360/wireshark-sending-syslog-data-to-my-pc-from-dd-wrt-not-working</a></p><p>On <strong>Linux</strong>, one of the following iptables analysis tools, might be useful.</p><blockquote><p><a href="http://www.gege.org/iptables/">http://www.gege.org/iptables/</a><br />
<a href="http://fwlogwatch.inside-security.de/">http://fwlogwatch.inside-security.de/</a><br />
<a href="http://sourceforge.net/projects/lila/">http://sourceforge.net/projects/lila/</a><br />
<a href="http://tud.at/programm/fwanalog/">http://tud.at/programm/fwanalog/</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '14, 09:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-35384" class="comments-container"></div><div id="comment-tools-35384" class="comment-tools"></div><div class="clear"></div><div id="comment-35384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

