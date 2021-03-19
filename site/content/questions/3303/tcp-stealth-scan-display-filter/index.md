+++
type = "question"
title = "TCP Stealth Scan Display Filter"
description = '''I am trying to come up with a display filter to help detect TCP Stealth Scans (or &quot;Half-Open&quot; scans). Since those are usually characterized by three packets: SYN - SYN/ACK - RST I&#x27;m trying the filter:  tcp.stream &amp;amp;&amp;amp; (tcp.flags.syn == 1 || tcp.flags.reset == 1) It seems to be working somewhat...'''
date = "2011-04-03T08:57:00Z"
lastmod = "2013-09-07T12:21:00Z"
weight = 3303
keywords = [ "filter" ]
aliases = [ "/questions/3303" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Stealth Scan Display Filter](/questions/3303/tcp-stealth-scan-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3303-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to come up with a display filter to help detect TCP Stealth Scans (or "Half-Open" scans).</p><p>Since those are usually characterized by three packets: SYN - SYN/ACK - RST</p><p>I'm trying the filter:</p><p>tcp.stream &amp;&amp; (tcp.flags.syn == 1 || tcp.flags.reset == 1)</p><p>It seems to be working somewhat - but I'm not sure if that is the correct use of the tcp.stream primitive. Is there a better way to identify patterns across multiple packets?</p><p>My Thanks...</p></div><div id="question-tags" class="tags-container tags">filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '11, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/eb859ad26d92eb0902b45ba20a167917?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kpalmgren&#39;s gravatar image" /><p>kpalmgren<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kpalmgren has no accepted answers">0%</span></p></div></div><div id="comments-container-3303" class="comments-container"></div><div id="comment-tools-3303" class="comment-tools"></div><div class="clear"></div><div id="comment-3303-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3304"></span>

<div id="answer-container-3304" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3304-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This will not work, Wireshark display filters work on a per packet basis. You might be able to achieve what you want with <a href="http://wiki.wireshark.org/Lua">LUA</a> or <a href="http://wiki.wireshark.org/Mate">MATE</a>, which both can be used to "keep state" and filter on the result.</p><p>The field tcp.stream is just an index to an individual TCP session (stream) and will always be true for tcp packets.</p><p>You might be able to get what you want by looking more closely at the RST packets and use the (relative) sequence and acknowledgment numbers to get what you want. Also the tcp.flags.ack field might be important in distinguishing the different causes for a TCP RST.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '11, 09:06</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Apr '11, 09:09</p></div></div><div id="comments-container-3304" class="comments-container"><span id="3305"></span><div id="comment-3305" class="comment"><div id="post-3305-score" class="comment-score"></div><div class="comment-text"><p>Hmmm... Ok. I was not aware exactly how tcp.stream worked.<br />
</p><p>On further testing using tcp.flags.reset == 1 || tcp.flags.ack == 1 without the tcp.stream seems to give me identical results.</p><p>Not exactly what I was looking for - but it certainly narrows the search.</p><p>My Thanx!</p></div><div id="comment-3305-info" class="comment-info"><span class="comment-age">(03 Apr '11, 10:28)</span> kpalmgren</div></div><span id="3308"></span><div id="comment-3308" class="comment"><div id="post-3308-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment", as this is how the Q&amp;A site works best, see the FAQ)</p><p>Actually, I did not mean you to use the filter "tcp.flags.reset==1 || tcp.flags.ack==1" as that will give you also all the proper tcp communications. What I meant was to look for a pattern in the ACK flag, the SEQ field and the ACK field of the TCP RST packets to find a pattern that matches all TCP RST packets due to the stealth scan.</p></div><div id="comment-3308-info" class="comment-info"><span class="comment-age">(03 Apr '11, 13:41)</span> SYN-bit ♦♦</div></div><span id="3309"></span><div id="comment-3309" class="comment"><div id="post-3309-score" class="comment-score"></div><div class="comment-text"><p>I just tested it and when I spoof a SYN, the SYN/ACK to the spoofed IP, causes this system to send a RST with the ACK flag not set and the SEQ = 1. A TCP SYN to a closed port causes the ACK flag to be set in the resulting TCP RST and a TCP RST in the middle of a session should have a valid SEQ field according to the TCP RFC (ie the relative sequence number should not be one). This means a filter like:</p><p>"tcp.flags.reset==1 &amp;&amp; tcp.flags.ack==0 &amp;&amp; tcp.seq==1"</p><p>(OK, this filter can have false positives, but I think you will get quite a good result with it to start with)</p></div><div id="comment-3309-info" class="comment-info"><span class="comment-age">(03 Apr '11, 13:46)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-3304" class="comment-tools"></div><div class="clear"></div><div id="comment-3304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24449"></span>

<div id="answer-container-24449" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24449-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks to a friend of mine, I can provide a follow-up to this post. If you create the mate script below - then go to Edit | Preferences -&gt; expand Protocols and type Mate to get to the Mate configuration screen. Enter the absolute path to your mate script file.</p><p>Then with that in place, you can use this filter to see TCP conversations consisting of exactly 3 packets (a signature of a TCP stealth scan):</p><p>mate.tcp_conversations.NumOfPdus == 3</p><p>To see TCP conversations of 4 packets (indicator of a full-open port scan) use</p><p>mate.tcp_conversations.NumOfPdus == 4</p><p>==== snip - Mate script below ===</p><pre><code>Pdu tcp_pdu Proto tcp Transport ip {
        Extract addr From ip.addr; 
        Extract port From tcp.port;
    Extract tcp_seq From tcp.seq;
    Extract tcp_start From tcp.flags.syn;
    Extract tcp_stop From tcp.flags.fin;
    Extract tcp_stop From tcp.flags.reset;
};

Gop tcp_conversations On tcp_pdu Match (addr, addr, port, port) {
    Start (tcp_start = 1);
    Stop (tcp_stop = 1);
};

Done;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '13, 12:21</strong></p><img src="https://secure.gravatar.com/avatar/eb859ad26d92eb0902b45ba20a167917?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kpalmgren&#39;s gravatar image" /><p>kpalmgren<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kpalmgren has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Sep '13, 07:26</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-24449" class="comments-container"><span id="24460"></span><div id="comment-24460" class="comment"><div id="post-24460-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the edit grahamb - I could not for the life of me figure out how to keep the formatting on that script. I'm sure that is a big help to all.</p></div><div id="comment-24460-info" class="comment-info"><span class="comment-age">(08 Sep '13, 15:56)</span> kpalmgren</div></div><span id="24468"></span><div id="comment-24468" class="comment"><div id="post-24468-score" class="comment-score"></div><div class="comment-text"><p>@kpalmgren - select the chunk of text to be formatted as code, then use the "code" button (the one with binary on it) on the edit box toolbar.</p></div><div id="comment-24468-info" class="comment-info"><span class="comment-age">(09 Sep '13, 02:29)</span> grahamb ♦</div></div></div><div id="comment-tools-24449" class="comment-tools"></div><div class="clear"></div><div id="comment-24449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

