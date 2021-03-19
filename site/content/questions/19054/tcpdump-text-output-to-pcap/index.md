+++
type = "question"
title = "tcpdump text output to pcap"
description = '''I have a raw tcpdump text file like  tcpdump: verbose output suppressed, use -v or -vv for full protocol decode listening on eth0, link-type EN10MB (Ethernet), capture size 96 bytes 17:22:24.464282 IP 1.4.0.2.50425 &amp;gt; 1.4.1.75.8009: P 3284624349:3284624961(612) ack 4160875603 win 602 &amp;lt;nop,nop,t...'''
date = "2013-03-01T11:06:00Z"
lastmod = "2014-06-24T17:32:00Z"
weight = 19054
keywords = [ "text", "conversion", "tcpdump", "pcap" ]
aliases = [ "/questions/19054" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [tcpdump text output to pcap](/questions/19054/tcpdump-text-output-to-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19054-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a raw tcpdump text file like</p><pre><code>tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 96 bytes
17:22:24.464282 IP 1.4.0.2.50425 &gt; 1.4.1.75.8009: P 3284624349:3284624961(612) ack 4160875603 win 602 &lt;nop,nop,timestamp 1267965975 3686849135&gt;
17:22:24.464353 IP 1.4.0.2.50425 &gt; 1.4.1.75.8009: P 612:1401(789) ack 1 win 602 &lt;nop,nop,timestamp 1267965975 3686849135&gt;</code></pre><p>Where Wireshark responds to opening the file "The file "xxxxx" isn't a capture file in a format wireshark understands.</p><p>Do you have a converter? or something that will assist me?</p></div><div id="question-tags" class="tags-container tags">text conversion tcpdump pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '13, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/fd24a5329ffcc3ee192600d196a70d8a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BeastyISNT&#39;s gravatar image" /><p>BeastyISNT<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BeastyISNT has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jun '14, 17:23</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-19054" class="comments-container"><span id="19056"></span><div id="comment-19056" class="comment"><div id="post-19056-score" class="comment-score"></div><div class="comment-text"><p>I also tried</p><p>editcap -F libpcap ws_gsk_web001_v3 output.pcap editcap: Can't open ws_gsk_web001_v3: The file isn't a capture file in a known format</p><p>I also tried -T unknown, -T unknown-nettl, -T ether, -T eht0</p><p>Your thoughts. and Thank you for your time and effort.</p></div><div id="comment-19056-info" class="comment-info"><span class="comment-age">(01 Mar '13, 11:10)</span> BeastyISNT</div></div></div><div id="comment-tools-19054" class="comment-tools"></div><div class="clear"></div><div id="comment-19054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="19059"></span>

<div id="answer-container-19059" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19059-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Where Wireshark responds to opening the file "The file "xxxxx" isn't a capture file in a format wireshark understands.</p></blockquote><p>Sure, as your tcpdump output is just text based. Wireshark needs a binary format called pcap or pcap-ng.</p><blockquote><p>Do you have a converter? or something that will assist me?</p></blockquote><p>No, but you can write the tcpdump output in pcap format.</p><blockquote><p><code>tcpdump -ni eth0 -s0 -w /var/tmp/capture.pcap</code><br />
</p></blockquote><p>Then open that file with Wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '13, 11:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-19059" class="comments-container"><span id="19061"></span><div id="comment-19061" class="comment"><div id="post-19061-score" class="comment-score"></div><div class="comment-text"><p>Would love to re-run the tcpdump; however the data is provided by a hosted tier. I do not have access to run the process. Will check into <a href="http://code.google.com/p/pcapr/wiki/Xtractr">http://code.google.com/p/pcapr/wiki/Xtractr</a> as stated in the first comment.</p></div><div id="comment-19061-info" class="comment-info"><span class="comment-age">(01 Mar '13, 11:34)</span> BeastyISNT</div></div><span id="19063"></span><div id="comment-19063" class="comment"><div id="post-19063-score" class="comment-score"></div><div class="comment-text"><p>xtractr won't help, as it needs a pcap file, which you don't get from the hosted tier.</p></div><div id="comment-19063-info" class="comment-info"><span class="comment-age">(01 Mar '13, 12:12)</span> Kurt Knochner ♦</div></div><span id="19064"></span><div id="comment-19064" class="comment"><div id="post-19064-score" class="comment-score"></div><div class="comment-text"><blockquote><p>or something that will assist me?</p></blockquote><p>BTW: assist in what? Troubleshooting or converting?</p></div><div id="comment-19064-info" class="comment-info"><span class="comment-age">(01 Mar '13, 12:30)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-19059" class="comment-tools"></div><div class="clear"></div><div id="comment-19059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19058"></span>

<div id="answer-container-19058" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19058-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please have a look at the answers to this similar <a href="http://ask.wireshark.org/questions/14376/generating-tshark-decoded-output-from-tcpdump-pcap-file-without-tshark">question</a>...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '13, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-19058" class="comments-container"></div><div id="comment-tools-19058" class="comment-tools"></div><div class="clear"></div><div id="comment-19058-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19079"></span>

<div id="answer-container-19079" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19079-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As the output of tcpdump was its text-mode output, the only information available in the file is the information tcpdump printed; even if it were possible to convert that file to a pcap file, the pcap file would not contain any more information than is available in the printout - the TCP payload of the two packets you showed, for example, is <em>permanently lost</em> and you will not <em>ever</em> be able to get it back.</p><p>If you need that information in order to solve a problem, you're out of luck. At best, you can try to get another trace, if whatever problem you're trying to diagnose can be made to happen again, and this time have them use tcpdump with the <code>-w</code> option, so that it writes out a pcap file. They should also use <code>-s 0</code> in the tcpdump command, so that they get the full packet data.</p><p>Apple have <a href="http://developer.apple.com/library/mac/#qa/qa1176/_index.html">a pretty good technical note</a> on how to take network traces; it discusses this from the point of view of an OS X user, and mentions some OS X-only tools, but it also mentions tcpdump in the "Getting Started With tcpdump" section, and that section applies to other UN*Xes, once you replace "If you're running on a system prior to OS X 10.6" with "If you're using tcpdump 0.x or 1.0.x" and "on OS X 10.6 and later" with "with tcpdump 1.1.0 and later", and replace the stuff talking about the <code>-i</code> option with whatever is appropriate for your OS and machine. That note mentions both <code>-w</code> and <code>-s 0</code>, as they are <em>very</em> important for getting traces to be sent to somebody else to analyze.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '13, 15:36</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19079" class="comments-container"><span id="34070"></span><div id="comment-34070" class="comment"><div id="post-34070-score" class="comment-score"></div><div class="comment-text"><p>Thanks Everyone who responded it was very helpful! Not sure how I mark this as answered.</p></div><div id="comment-34070-info" class="comment-info"><span class="comment-age">(23 Jun '14, 05:58)</span> bz6djs</div></div><span id="34073"></span><div id="comment-34073" class="comment"><div id="post-34073-score" class="comment-score"></div><div class="comment-text"><p>you can't in this question, as it's not your own question. If you think <a href="http://ask.wireshark.org/questions/33987/need-to-convert-a-tcpdump-text-file-to-pcap-file">your own question</a> has been answered, click on the check mark.</p></div><div id="comment-34073-info" class="comment-info"><span class="comment-age">(23 Jun '14, 06:16)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-19079" class="comment-tools"></div><div class="clear"></div><div id="comment-19079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="34143"></span>

<div id="answer-container-34143" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34143-score" class="post-score" title="current number of votes">-1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use -vvv to create a pcap file which Wireshark can open.</p><p>tcpdump -i eth0 -s 0 -vvv -w ./dump.pcap</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '14, 17:32</strong></p><img src="https://secure.gravatar.com/avatar/658cda1c649bfc4b390eeaf90b7a84e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TiME2014&#39;s gravatar image" /><p>TiME2014<br />
<span class="score" title="0 reputation points">0</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TiME2014 has no accepted answers">0%</span></p></div></div><div id="comments-container-34143" class="comments-container"><span id="34144"></span><div id="comment-34144" class="comment"><div id="post-34144-score" class="comment-score"></div><div class="comment-text"><p><code>-v</code> isn't used when you're using <code>-w</code>; <code>-w</code> is the flag to tell tcpdump to write a pcap file, which tcpdump and Wireshark (and some other tools) can read.</p><p>I.e.</p><pre><code>tcpdump -i eth0 -s 0 -w ./dump.pcap</code></pre><p>is sufficient.</p></div><div id="comment-34144-info" class="comment-info"><span class="comment-age">(24 Jun '14, 18:13)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-34143" class="comment-tools"></div><div class="clear"></div><div id="comment-34143-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

