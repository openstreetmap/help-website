+++
type = "question"
title = "filter 1second fragment with the tshark"
description = '''Hello. When I try to extract like this: tshark -r $suff.pcap.gz -R &quot;frame.time_relative &amp;lt;= 1&quot; -2 -q -w $host4dump.1sec.cap  I get what I want except for the fact that each packet has a time value 0.000000000(Jan 1, 1970 03:00:00.000000000).  What should I do to extract it properly? Is there anoth...'''
date = "2015-07-10T22:44:00Z"
lastmod = "2015-07-11T09:50:00Z"
weight = 44070
keywords = [ "timestamp", "console", "tshark", "display-filter" ]
aliases = [ "/questions/44070" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [filter 1second fragment with the tshark](/questions/44070/filter-1second-fragment-with-the-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44070-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello.</p><p>When I try to extract like this:</p><pre><code>tshark -r $suff.pcap.gz -R &quot;frame.time_relative &lt;= 1&quot; -2 -q -w $host4dump.1sec.cap</code></pre><p>I get what I want except for the fact that each packet has a time value 0.000000000(Jan 1, 1970 03:00:00.000000000).</p><p>What should I do to extract it properly? Is there another way to extract 1 second piece of a dump using non-interactive console (within a script)?</p></div><div id="question-tags" class="tags-container tags">timestamp console tshark display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '15, 22:44</strong></p><img src="https://secure.gravatar.com/avatar/757f09b44d22198faf9a42110c95e01c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rusyarr&#39;s gravatar image" /><p>rusyarr<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rusyarr has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jul '15, 22:50</p></div></div><div id="comments-container-44070" class="comments-container"></div><div id="comment-tools-44070" class="comment-tools"></div><div class="clear"></div><div id="comment-44070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="44071"></span>

<div id="answer-container-44071" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44071-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>tshark -r $suff.pcap.gz -Y "frame.time_relative &lt;= 1" -q -w $host4dump.1sec.cap</code> did the trick.</p><p>So the question alters What's the difference beetween -R -2 and Y? Because only gathered statistics with -R option corresponds the statistics in wireshark. I mean eg statistics like this:</p><pre><code>tshark -r $suff.pcap.gz -R &quot;frame.time_relative &lt;= 1&quot; -2 -q -z smpp_commands,tree &gt;&gt; $suff.txt</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '15, 23:55</strong></p><img src="https://secure.gravatar.com/avatar/757f09b44d22198faf9a42110c95e01c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rusyarr&#39;s gravatar image" /><p>rusyarr<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rusyarr has no accepted answers">0%</span></p></div></div><div id="comments-container-44071" class="comments-container"></div><div id="comment-tools-44071" class="comment-tools"></div><div class="clear"></div><div id="comment-44071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="44074"></span>

<div id="answer-container-44074" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44074-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For your original question:</p><p>What tshark/wireshark version are you running? I tried that command and did not get a time value of 0. (if by "time value" you mean Arrival Time or Epoch Time)</p><p>Can you post your capture file somewhere?</p><hr /><p>For your second question of what the difference is between <code>-R -2</code> and <code>-Y</code>:</p><p>For both Wireshark and tshark, when they read the contents of a capture file they build an internal list of the frames (i.e., packets) in it. When you apply a <strong>display</strong> filter, it filters out packets from that list, to only show you the things that matched the display filter. With a display filter applied, the frame numbers (packet numbers) you see in the left-most column will likely not be sequential, but will instead only be for the packets that matched the display filter. When you clear that display filter, all the frames show up again (in Wireshark obviously, since in tshark you can't clear it afterwards since there is no "afterwards").</p><p>But both Wireshark and tshark also support a <strong>read</strong> filter. A read filter is the same syntax/mechanics as a <strong>display</strong> filter, but is applied to the frames/packets in the capture file <em>before</em> they are put in that list, and only the packets which match the read filter are added to that list at all. Because it's applied before they're added to the list, the frame numbers you see will now be sequential, because the frame number is based on the position in the list, and only the packets that matched the read filter are in that list.</p><p>In tshark, the <code>-R</code> option is for a <strong>read</strong> filter, and the <code>-Y</code> option is for a <strong>display</strong> filter. In Wireshark, when you click on the "Open" button (or menu File-&gt;Open) to open a new file, in the Open-file dialog window you'll see a "Filter" text box where you can put a filter-type string - that's a <strong>read</strong> filter; whereas the one on the top of the GUI in the toolbar is a <strong>display</strong> filter.</p><p>The <code>-2</code> option tells tshark to process the packets twice. This is necessary to handle some scenarios, like fragmented packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '15, 09:50</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-44074" class="comments-container"><span id="44120"></span><div id="comment-44120" class="comment"><div id="post-44120-score" class="comment-score"></div><div class="comment-text"><p>Tx, Hadriel! Everything has become clear now!</p></div><div id="comment-44120-info" class="comment-info"><span class="comment-age">(14 Jul '15, 00:51)</span> rusyarr</div></div></div><div id="comment-tools-44074" class="comment-tools"></div><div class="clear"></div><div id="comment-44074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

