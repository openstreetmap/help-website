+++
type = "question"
title = "How to decode UDP as RTP tshark only"
description = '''In the GUI I can use Analyze &amp;gt; Decode as... &amp;gt; RTP Searching on google I find two &quot;ways&quot; of doing this: tshark -n -r file.pcap -o rtp.heuristic_rtp:TRUE -w p_out.pcap and tshark -n -r file.pcap -d udp.port==#,rtp -w p_out.pcap (where # is the port number) neither of these work. When I open the ...'''
date = "2016-02-15T23:42:00Z"
lastmod = "2016-02-16T12:44:00Z"
weight = 50226
keywords = [ "h264", "udp", "rtp", "h264_decode", "tshark" ]
aliases = [ "/questions/50226" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to decode UDP as RTP tshark only](/questions/50226/how-to-decode-udp-as-rtp-tshark-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50226-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In the GUI I can use Analyze &gt; Decode as... &gt; RTP</p><p>Searching on google I find two "ways" of doing this:</p><p><code>tshark -n -r file.pcap -o rtp.heuristic_rtp:TRUE -w p_out.pcap</code></p><p>and</p><p><code>tshark -n -r file.pcap -d udp.port==#,rtp -w p_out.pcap</code> (where # is the port number)</p><p>neither of these work. When I open the p_out.pcap in wireshark it's still in UDP</p><p>What is the proper method for achieving this?</p></div><div id="question-tags" class="tags-container tags">h264 udp rtp h264_decode tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '16, 23:42</strong></p><img src="https://secure.gravatar.com/avatar/2a64be647ac8ec21b76a6c042bebb6e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="testname0110&#39;s gravatar image" /><p>testname0110<br />
<span class="score" title="15 reputation points">15</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="testname0110 has 3 accepted answers">75%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Feb '16, 00:35</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-50226" class="comments-container"></div><div id="comment-tools-50226" class="comment-tools"></div><div class="clear"></div><div id="comment-50226-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50228"></span>

<div id="answer-container-50228" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50228-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>When I open the p_out.pcap in wireshark it's still in UDP</p></blockquote><p>The pcap (or pcapng, or any other capture file format) does <em>not</em> store the <code>Decode as...</code> or any other preferences. So whatever you tell tshark only affects that particular run. So what you did was actually an equivalent of <code>cp file.pcap p_out.pcap</code>.</p><p>So you could use "display filter" <code>-Y rtp</code> in combination with e.g. the <code>-d udp.port==#,rtp</code> to allow only RTP packets from the input file <code>file.pcap</code> to be written to the output file <code>p_out.pcap</code>, but to display them as RTP when you handle the <code>p_out.pcap</code> by tshark or Wireshark, the <code>decode as</code> still needs to be stored in your preferences folder (in case of Wireshark 2.0.1, the file name is decode_as_entries). Or you may use <code>-o</code> to tell tshark how to override/extend the stored preferences.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '16, 01:06</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50228" class="comments-container"><span id="50243"></span><div id="comment-50243" class="comment"><div id="post-50243-score" class="comment-score"></div><div class="comment-text"><p>Are you saying that the changes are being made but only within that command line? So if I need the file in that format I need to pipe it immediately in the same command to use it in that format?</p></div><div id="comment-50243-info" class="comment-info"><span class="comment-age">(16 Feb '16, 11:28)</span> testname0110</div></div><span id="50246"></span><div id="comment-50246" class="comment"><div id="post-50246-score" class="comment-score"></div><div class="comment-text"><p>No. I am saying that no <em>changes</em> are made at all, and I am saying that "piping the output to another application on a common command line" has nothing to do with it either. By specifying command line parameters to tshark, you are not modifying environmental values of the shell (which another application could look at) but merely controlling the behaviour of that tshark instance alone.</p><p>I am also saying that there is no way to associate any individual <code>decode as</code> rules to a particular capture file, which is what I suppose you want to achieve. You can define a set of static <code>decode as</code> rules in the basic preferences profile and/or additional preferences profiles you can switch among, but the rule set from the chosen profile will be used to any capture file, not just to a particular one.</p><p>Without the <code>-w filename</code> option, tshark's output is textual. With that option, its output is in a pcapng binary format, whose structure provides no room for specification of any dissection rules.</p><p>What you tell tshark is:</p><ol><li><p>what dissectors to use for specific packets on top / instead of the default ones. This is the equivalent of manual <code>Decode as...</code> setting in Wireshark.</p></li><li><p>which packets to let through to the output, using the "display filter" and/or "capture filter" expressions. This is a direct equivalent of capture filter and display filter in Wireshark.</p></li><li><p>only if the specified output type is textual, i.e. if <code>-w</code> is not specified: which information from the packets elected by the display filter and in what form to display in textual form.</p></li></ol><p>If you would use <code>-w -</code> to tell tshark that the format of the output shall be pcapng but stdout shall be used, and pipe that output to another instance of tshark (or to Wireshark), that other instance of tshark would <em>not</em> inherit the settings from the first one.</p></div><div id="comment-50246-info" class="comment-info"><span class="comment-age">(16 Feb '16, 13:22)</span> sindy</div></div><span id="50247"></span><div id="comment-50247" class="comment"><div id="post-50247-score" class="comment-score"></div><div class="comment-text"><p>When I run "tshark -r file.pcap -o rtp.heuristic_rtp" it does indeed output the decoded, dynamic payload packets. But this is only during that thread of execution, so it is necessary to pipe the output where I want it immediately. But you are correct</p></div><div id="comment-50247-info" class="comment-info"><span class="comment-age">(16 Feb '16, 14:50)</span> testname0110</div></div></div><div id="comment-tools-50228" class="comment-tools"></div><div class="clear"></div><div id="comment-50228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50245"></span>

<div id="answer-container-50245" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50245-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Back to the basics. Wireshark makes interpretations based on its knowledge on how network frames are composed. Therefore we start at the bottom.</p><p>For most common network frames the datalinktype is Ethernet. Therefore the (generic) frame dissector hands the received frame (read form the pcap file) to the ethernet dissector. This reads the beginning of the frame and decides it contains an IP packet, and hands the remainder to the IP dissector. The IP dissector decides it contains an UDP payload, and hands the remainder to the UDP dissector.</p><p>The UDP dissector now has a problem. The port number in the dissector doesn't uniformly identify the payload type, so it has to try to find out where to hand the payload another way. Sometimes there are other protocols in the capture which tell something (think SIP/SDP for example), sometimes the payload itself has a 'magic' value to identify the payload type.</p><p>For RTP there is very little to go on, unless an external signalling protocol identifies gives you the port numbers, the payload doesn't give you much to go on. That's where the option 'decode as' and rtp_udp preference come into play. These allow the operator to force interpretation of the UDP payload as RTP, because of the high probability of false positive identification of random UDP payload as RTP.</p><p>So, the capture file just contains network frames, it's the interpretation Wireshark makes of them that shows RTP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '16, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-50245" class="comments-container"></div><div id="comment-tools-50245" class="comment-tools"></div><div class="clear"></div><div id="comment-50245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

