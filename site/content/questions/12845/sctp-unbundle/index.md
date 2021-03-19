+++
type = "question"
title = "SCTP unbundle"
description = '''hello,  i`m looking for some method capable of separating bundled SCTP chunks into separate frames. i think this guy is modifying editcap for sctp-unbundle, but i do not know how to get it . . . https://gitorious.org/~vasilvelichkov thanks'''
date = "2012-07-19T02:03:00Z"
lastmod = "2012-07-19T02:10:00Z"
weight = 12845
keywords = [ "bundling", "sctp", "editcap", "unbundle" ]
aliases = [ "/questions/12845" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SCTP unbundle](/questions/12845/sctp-unbundle)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12845-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello,</p><p>i`m looking for some method capable of separating bundled SCTP chunks into separate frames. i think this guy is modifying editcap for sctp-unbundle, but i do not know how to get it . . .</p><p><a href="https://gitorious.org/~vasilvelichkov">https://gitorious.org/~vasilvelichkov</a></p><p>thanks</p></div><div id="question-tags" class="tags-container tags">bundling sctp editcap unbundle</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '12, 02:03</strong></p><img src="https://secure.gravatar.com/avatar/e54875615ec43ae037763b07a908ba1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="knuf&#39;s gravatar image" /><p>knuf<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="knuf has no accepted answers">0%</span></p></div></div><div id="comments-container-12845" class="comments-container"></div><div id="comment-tools-12845" class="comment-tools"></div><div class="clear"></div><div id="comment-12845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12847"></span>

<div id="answer-container-12847" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12847-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>besides the tool you mentioned, you can try this perl script:</p><blockquote><p><code>http://frox25.no-ip.org/~mtve/wiki/SctpDechunk.html</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '12, 02:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-12847" class="comments-container"><span id="12855"></span><div id="comment-12855" class="comment"><div id="post-12855-score" class="comment-score"></div><div class="comment-text"><p>thanks, that script works fine, however, are there any plans to include that feature in some of the ws` tools?</p><p>rgds</p></div><div id="comment-12855-info" class="comment-info"><span class="comment-age">(19 Jul '12, 05:07)</span> knuf</div></div><span id="12857"></span><div id="comment-12857" class="comment"><div id="post-12857-score" class="comment-score"></div><div class="comment-text"><p>volunteers are welcome to take that challenge ;-)</p></div><div id="comment-12857-info" class="comment-info"><span class="comment-age">(19 Jul '12, 06:05)</span> Kurt Knochner ♦</div></div><span id="20267"></span><div id="comment-20267" class="comment"><div id="post-20267-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Can you please provide an instruction on how I run this script in wireshark to try it out?</p><p>BR Harkap</p></div><div id="comment-20267-info" class="comment-info"><span class="comment-age">(10 Apr '13, 02:09)</span> harkap</div></div><span id="20268"></span><div id="comment-20268" class="comment"><div id="post-20268-score" class="comment-score"></div><div class="comment-text"><p>It's a Perl script that processes a capture file. From a shell (or command prompt) on a system that has perl available execute the file passing in the path to a capture file.</p></div><div id="comment-20268-info" class="comment-info"><span class="comment-age">(10 Apr '13, 02:50)</span> grahamb ♦</div></div><span id="20386"></span><div id="comment-20386" class="comment"><div id="post-20386-score" class="comment-score">1</div><div class="comment-text"><p>Since I just tried out this script, I thought I'd share some advice on how to get it to work.</p><p>As already mentioned by others, it's a Perl script. I'm using perl 5, version 14, subversion 2 (v5.14.2) built for i686-linux-gnu-thread-multi-64int. You need to pass two arguments to the script: the input and output filenames.</p><p>The input file is a packet capture file and should contain only SCTP packets within IP within Ethernet frames. You can achieve this by using a capture filter for SCTP (e.g., -f sctp in Tshark). If you don't use this capture filter, your packet capture will feature non-SCTP and non-IP packets that the script cannot currently process. In my case, the script failed some one second into the packet capture as it encountered an ARP packet.</p><p>The output file will also be a packet capture, although with the packets reorganized in a different way. My understanding is that the script scans the input packet capture file and processes each SCTP packet as follows.</p><p>If the SCTP packet contains only one chunk, then it is output as is to the output file.</p><p>Otherwise (i.e., the SCTP packet contains more than one chunk), the script generates n packets (as many as the chunks) each of which features a replica of the Frame, Ethernet, and IP parts of the multi-chunk packet, and one single SCTP chunk.</p><p>Don't worry about the output file size being smaller than the input file size. Since the Frame, Ethernet, and IP parts are replicated for multi-chunk packets, I was actually expecting an output file larger than the input file. Instead I've got the output file being approximately 10% smaller in size than the input file. However, this may happen because there are relatively many SACK chunks in SCTP packets that are filtered out (not output) by the script.</p><p>Finally, you can use the output packet capture file with Wireshark or Tshark.</p></div><div id="comment-20386-info" class="comment-info"><span class="comment-age">(12 Apr '13, 13:22)</span> tshark-user</div></div></div><div id="comment-tools-12847" class="comment-tools"></div><div class="clear"></div><div id="comment-12847-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

