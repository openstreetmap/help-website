+++
type = "question"
title = "Get reassembled information with command line tools"
description = '''Hi, I tested all the tools (rawshark, editcap), even i used the libpcap api to solve my problem but i can&#x27;t. The thing is that i have a pcap file with diameter frames inside. Sometimes there are reassembled packets. The only way to get the whole diameter packet is by mean shell scripting over the &quot;t...'''
date = "2015-03-27T06:08:00Z"
lastmod = "2015-03-28T11:18:00Z"
weight = 40935
keywords = [ "rawshark", "reassembled", "editcap", "tshark" ]
aliases = [ "/questions/40935" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Get reassembled information with command line tools](/questions/40935/get-reassembled-information-with-command-line-tools)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40935-score" class="post-score" title="current number of votes">0</div><span id="post-40935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I tested all the tools (rawshark, editcap), even i used the libpcap api to solve my problem but i can't. The thing is that i have a pcap file with diameter frames inside. Sometimes there are reassembled packets. The only way to get the whole diameter packet is by mean shell scripting over the "tshark -r -x" output, but this is not robust because this script is very fixed to the libpcap system version (which causes different text outputs).</p><p>I would like to use c program, editpcap, rawshark or whatever, but i only obtain the incomplete frame which does not contain the whole diameter message.</p><p>Summing up, in my pcap example i have this frames:</p><pre><code>  1 1427215933.697904 192.168.14.42 -&gt; 192.168.12.40 DIAMETER 498 cmd=Credit-Control Request(272) flags=R--- appl=3GPP Gx(16777238) h2h=4e6e6 e2e=bd986 | 
  3 1427215934.449523 192.168.12.40 -&gt; 192.168.14.42 DIAMETER 358 cmd=Credit-Control Answer(272) flags=---- appl=3GPP Gx(16777238) h2h=4e6e6 e2e=bd986 | 
  6 1427215934.456204 192.168.14.42 -&gt; 192.168.12.40 DIAMETER 638 cmd=AA Request(265) flags=R--- appl=3GPP Rx(16777236) h2h=c73c3 e2e=4cee4 | 
  8 1427215935.123559 192.168.12.40 -&gt; 192.168.14.42 DIAMETER 314 cmd=AA Answer(265) flags=---- appl=3GPP Rx(16777236) h2h=c73c3 e2e=4cee4 | </code></pre><p>The 6th frame is the incomplete one. With tshark -x you could see the whole information: frame block and reassembled completed block:</p><pre><code>Reassembled TCP (1972 bytes):

0000  01 00 07 b4 80 00 01 09 01 00 00 14 00 0c 73 c3   ..............s.
0010  00 04 ce e4 00 00 01 07 40 00 00 42 74 63 5f 30   [email protected]_0
0020  31 5f 46 75 6c 6c 41 56 50 73 3b 61 66 4e 6f 64   1_FullAVPs;afNod
0030  65 48 6f 73 74 6e 61 6d 65 2e 61 66 4e 6f 64 65   eHostname.afNode
...</code></pre><p>That's the useful section for me, because inside it i have the complete diameter message.</p><p>If you execute 'editcap my.pcap 6.pcap -r 6', you will have the data but not completed, only gets the main frame, not the reassembled one. The same happens with all other tools. Only shell scripting solves my problem but i don't like this solution (not robunst as i said).</p><p>Could you help me ? Thanks a lot BRs</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rawshark" rel="tag" title="see questions tagged &#39;rawshark&#39;">rawshark</span> <span class="post-tag tag-link-reassembled" rel="tag" title="see questions tagged &#39;reassembled&#39;">reassembled</span> <span class="post-tag tag-link-editcap" rel="tag" title="see questions tagged &#39;editcap&#39;">editcap</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '15, 06:08</strong></p><img src="https://secure.gravatar.com/avatar/3d8ccf5c026cc90f0eb91fda75e00f7e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eramos&#39;s gravatar image" /><p><span>eramos</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eramos has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Mar '15, 16:12</strong> </span></p></div></div><div id="comments-container-40935" class="comments-container"></div><div id="comment-tools-40935" class="comment-tools"></div><div class="clear"></div><div id="comment-40935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40937"></span>

<div id="answer-container-40937" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40937-score" class="post-score" title="current number of votes">0</div><span id="post-40937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Seems as though you need full dissection of packets (since reassembly needs to take place) so editcap is out. tshark (with the two-pass option for recent versions) would be required. If you need to be able to machine process the output select one of the non-human output text formats, in your case PDML, and parse the desired content from there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '15, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-40937" class="comments-container"><span id="40940"></span><div id="comment-40940" class="comment"><div id="post-40940-score" class="comment-score"></div><div class="comment-text"><p>Regarding two.pass, i suppose you talk about '-2' option:</p><pre><code>PCAP2HEX&gt; tshark -x -r my.pcap 2&gt;/dev/null &gt; normal.txt
PCAP2HEX&gt; tshark -2 -x -r my.pcap 2&gt;/dev/null &gt; two-pass.txt
PCAP2HEX&gt; diff normal.txt  two-pass.txt </code></pre><p>It seems to have the same result.</p><p>Regarding pdml (adding '-T pdml' to the tshark command line), it seems that my pcap cannot achieve it: tshark: Raw packet hex data can only be printed as text or PostScript</p><p>Perhaps, is there any sample code (i couldn't find) for such full dissection. In my code, i use pcap_open_offline and pcap_next.</p></div><div id="comment-40940-info" class="comment-info"><span class="comment-age">(27 Mar '15, 08:39)</span> <span class="comment-user userinfo">eramos</span></div></div><span id="40945"></span><div id="comment-40945" class="comment"><div id="post-40945-score" class="comment-score"></div><div class="comment-text"><p>What version of wireshark are you working with? If the file is loaded into wireshark does reassembly work then? If there is duplicate mmessages or outoforder ones reassembly sometimes fail.</p></div><div id="comment-40945-info" class="comment-info"><span class="comment-age">(27 Mar '15, 10:22)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="40948"></span><div id="comment-40948" class="comment"><div id="post-40948-score" class="comment-score"></div><div class="comment-text"><p>Wireshark works well. It reassembles all correctly. But I need to process the pcap externally, no gui tools involved. I tested tshark adding '-e tcp.segment' and my frame #6 involves #5 and #6 itself. I could join rawshark hex output for such frames, detect some diameter pattern (for example hop by hop followed by end to end) and then build the message by mean shell scripting. But I would prefer to have a c program prototype or any special option (for tshark, rawshark, whatever) that I currently ignore. Probably this option is not implemented.</p></div><div id="comment-40948-info" class="comment-info"><span class="comment-age">(27 Mar '15, 14:44)</span> <span class="comment-user userinfo">eramos</span></div></div></div><div id="comment-tools-40937" class="comment-tools"></div><div class="clear"></div><div id="comment-40937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40959"></span>

<div id="answer-container-40959" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40959-score" class="post-score" title="current number of votes">0</div><span id="post-40959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Finally, I made a safer script based in rawshark/tshark but not processing tshark -x output. Then it works for different libpcap versions (at least those that i tested).</p><p>The script is easy to adapt to another protocols using corresponding length fields and filters (see <a href="https://www.wireshark.org/docs/dfref">https://www.wireshark.org/docs/dfref</a> ).</p><p>Feel free to use if you consider useful: <a href="http://redmine.teslayout.com/projects/anna-suite/repository/revisions/master/entry/example/diameter/launcher/resources/pcap2diameterHex.sh">http://redmine.teslayout.com/projects/anna-suite/repository/revisions/master/entry/example/diameter/launcher/resources/pcap2diameterHex.sh</a></p><p>Anyway, it would be very helpful to have any option in wireshark tools to ease this kind of work. Then, if you know, please tell me.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '15, 11:18</strong></p><img src="https://secure.gravatar.com/avatar/3d8ccf5c026cc90f0eb91fda75e00f7e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eramos&#39;s gravatar image" /><p><span>eramos</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eramos has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Mar '15, 11:19</strong> </span></p></div></div><div id="comments-container-40959" class="comments-container"></div><div id="comment-tools-40959" class="comment-tools"></div><div class="clear"></div><div id="comment-40959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

