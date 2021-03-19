+++
type = "question"
title = "&quot;Unrecognized libpcap format&quot; error when piping to &quot;wireshark -k -i -&quot;"
description = '''Hi,  I have wireshark 1.8.6 on x86 platform. When I try to open a large .pcap file (&amp;gt;3 mb), it gives &quot;Unrecognized libpcap format&quot; error. I am sending input to wireshark via pipe. below is the cli command: tail -f pcap_ file_name | /usr/local/bin/wireshark -k -i -  Reason for using pipe input is ...'''
date = "2013-08-21T04:49:00Z"
lastmod = "2013-08-22T08:22:00Z"
weight = 23904
keywords = [ "pipe", "unrecognized" ]
aliases = [ "/questions/23904" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# ["Unrecognized libpcap format" error when piping to "wireshark -k -i -"](/questions/23904/unrecognized-libpcap-format-error-when-piping-to-wireshark-k-i-)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23904-score" class="post-score" title="current number of votes">0</div><span id="post-23904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have wireshark 1.8.6 on x86 platform. When I try to open a large .pcap file (&gt;3 mb), it gives "Unrecognized libpcap format" error.</p><p>I am sending input to wireshark via pipe. below is the cli command:</p><pre><code>tail -f pcap_ file_name | /usr/local/bin/wireshark -k -i -</code></pre><p>Reason for using pipe input is that, pcap file is generating at run time with real traffic on node.</p><p>Wireshark 1.8.6 does not support the large pcap files? Any help on this is appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pipe" rel="tag" title="see questions tagged &#39;pipe&#39;">pipe</span> <span class="post-tag tag-link-unrecognized" rel="tag" title="see questions tagged &#39;unrecognized&#39;">unrecognized</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '13, 04:49</strong></p><img src="https://secure.gravatar.com/avatar/c83ca22a760e356093e591f491b6744f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KumarM&#39;s gravatar image" /><p><span>KumarM</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KumarM has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Aug '13, 08:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-23904" class="comments-container"></div><div id="comment-tools-23904" class="comment-tools"></div><div class="clear"></div><div id="comment-23904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="23920"></span>

<div id="answer-container-23920" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23920-score" class="post-score" title="current number of votes">1</div><span id="post-23920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"tail -f" will start to read the whole file and will display the last 10 lines of the file and then list any new line to the file. So if your file does not contain 10 newlines yet in the binary data, the tail -f will indeed send the file header to wireshark. If it does already contain 10 newlines, the first lines will be skipped and so will the file header.</p><p>Workaround, use <code>"tail -1000000f pcap_ file_name | /usr/local/bin/wireshark -k -i -"</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '13, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-23920" class="comments-container"><span id="23921"></span><div id="comment-23921" class="comment"><div id="post-23921-score" class="comment-score"></div><div class="comment-text"><p>Thanks for pointing that out, but I don't think that's the biggest problem. I believe that you still need to ensure that the file is written in pcap format and not in pcapng format. For example, on Windows I do this:</p><p>Cmd: <code>dumpcap.exe -P -i 4 -w pcap-pipe-file</code></p><p>cygwin: <code>tail -c +0 -f pcap-pipe-file | Wireshark.exe -k -i -</code></p><p>As I indicated in my answer, if I don't use <code>-P</code>, then this always fails.</p></div><div id="comment-23921-info" class="comment-info"><span class="comment-age">(21 Aug '13, 13:06)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="23935"></span><div id="comment-23935" class="comment"><div id="post-23935-score" class="comment-score"></div><div class="comment-text"><p>True, but since the OP was having good results when the file was still small, I assumed that the file was already in pcap format :-)</p><p>(and thanks for the "-c +0", something learned for today :-))</p></div><div id="comment-23935-info" class="comment-info"><span class="comment-age">(21 Aug '13, 16:23)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="23966"></span><div id="comment-23966" class="comment"><div id="post-23966-score" class="comment-score"></div><div class="comment-text"><p><em>but since the OP was having good results when the file was still small</em></p><p>Well, this too is an assumption since there was no <strong>explicit</strong> mention of it working with small files. Maybe only big files were tried?</p><p><em>thanks for the "-c +0"</em></p><p>You're welcome. Every once in a while the padawan teaches the master something. :)</p></div><div id="comment-23966-info" class="comment-info"><span class="comment-age">(22 Aug '13, 08:22)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-23920" class="comment-tools"></div><div class="clear"></div><div id="comment-23920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23922"></span>

<div id="answer-container-23922" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23922-score" class="post-score" title="current number of votes">1</div><span id="post-23922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><code>tail -f pcap_ file_name | /usr/local/bin/wireshark -k -i -</code></p></blockquote><p>Pcap files have, at the beginning, a file header that indicates that the file is a pcap file and specifies, among other things, the link-layer header type for the packets in the file. (And pcap-ng files have, at the beginning, several data blocks that provide equally-necessary information.)</p><p>Using the <code>tail</code> command means that the file header might not be sent to Wireshark, even if you run it with <code>-f</code>; if the header isn't sent to Wireshark, it is impossible for Wireshark to read the data.</p><p>So it is <em>impossible</em> to use the <code>tail</code> command on a capture file and pipe the results to Wireshark and be certain that this will work.</p><p>Therefore, <em>you must not use <code>tail</code></em>.</p><p>Instead, you would need to do something such as find or write a program that reads a file <em>in its entirety</em> and writes it to the standard output and, when it reaches the end of the file, waits for the file to get longer and, when it does, reads the new data and writes it out. I don't know whether any such programs exist; if not, you will have to write it.</p><p>Alternatively, if whatever program is writing that pcap file can be made to write to a named pipe, you could create a named pipe, have it write to that pipe, and run Wireshark with the <code>-i</code> flag and with that named pipe, rather than <code>-</code>, as the argument to <code>-i</code>.</p><p>Or, if the program can write the pcap file to its standard output, you could run it, have it write to its standard output and pipe <em>its</em> output to <code>/usr/local/bin/wireshark -k -i -</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '13, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23922" class="comments-container"></div><div id="comment-tools-23922" class="comment-tools"></div><div class="clear"></div><div id="comment-23922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23909"></span>

<div id="answer-container-23909" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23909-score" class="post-score" title="current number of votes">0</div><span id="post-23909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is that you need to send the whole file to Wireshark not just a section I think. Hence wireshark think the file is broken as the header(s) are missing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '13, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-23909" class="comments-container"></div><div id="comment-tools-23909" class="comment-tools"></div><div class="clear"></div><div id="comment-23909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23913"></span>

<div id="answer-container-23913" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23913-score" class="post-score" title="current number of votes">0</div><span id="post-23913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How is <code>pcap_file_name</code> being created, i.e., by which process - <a href="http://www.tcpdump.org/tcpdump_man.html">tcpdump</a>, <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a>, <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark</a>, <a href="http://www.wireshark.org/docs/man-pages/wireshark.html">wireshark</a>?<br />
</p><p>The default capture file format with 1.8 is pcapng, but Wireshark has problems reading that type of file from a pipe it seems, so assuming it's dumpcap doing the capturing, you could use the <code>-P</code> option to force dumpcap to write a pcap file instead of pcapng file. If it's tshark or wireshark doing the capturing, then you could either use the <code>-o capture.pcap_ng:FALSE</code> command-line option or change the preference in Wireshark via:</p><pre><code>Edit -&gt; Preferences -&gt; Capture -&gt; Capture packets in pcap-ng format: -&gt; [deselect] -&gt; OK</code></pre><p>If it's tcpdump, (or something else) doing the capturing, then you'll likely need to provide additional information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '13, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Aug '13, 08:11</strong> </span></p></div></div><div id="comments-container-23913" class="comments-container"></div><div id="comment-tools-23913" class="comment-tools"></div><div class="clear"></div><div id="comment-23913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

