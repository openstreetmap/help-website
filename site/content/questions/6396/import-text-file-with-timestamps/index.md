+++
type = "question"
title = "Import text file with timestamps"
description = '''Do you have an example of a text file for importing that has timestamps in the text file? I have tried the following with the %S format for Date/Time but the timestamp for all frames is displayed as 0.000000 in WireShark.  0.000200  0000 e0 9f 97 1c  0004 20 5c 66 ae  0008 19 d1 a6 80  000c 08 00 45...'''
date = "2011-09-15T08:40:00Z"
lastmod = "2011-09-16T00:56:00Z"
weight = 6396
keywords = [ "import", "text", "timestamp" ]
aliases = [ "/questions/6396" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Import text file with timestamps](/questions/6396/import-text-file-with-timestamps)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6396-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Do you have an example of a text file for importing that has timestamps in the text file? I have tried the following with the %S format for Date/Time but the timestamp for all frames is displayed as 0.000000 in WireShark.</p><pre><code> 0.000200
 0000 e0 9f 97 1c
 0004 20 5c 66 ae
 0008 19 d1 a6 80
 000c 08 00 45 00
 0010 00 99 00 00
 0014 40 00 ff 06
 0018 a8 7f 85 2d
 001c f7 e1 b5 d6
 0020 9f f9 01 da
 0024 01 da 00 00
 0028 00 00 00 00
 002c 00 00 50 18
 0030 ff ff 27 e2
 0034 00 00 55 5c
 0038 03 96 8f 9a
 003c a1 f8 73 69
 0.000400 
 0000 66 ae 19 d1
 0004 a6 80 e0 9f
 0008 97 1c 20 5c
 000c 08 00 45 00
 0010 00 a9 00 00
 0014 40 00 ff 06
 0018 a8 6f b5 d6
 001c 9f f9 85 2d
 0020 f7 e1 01 da
 0024 01 da 00 00
 0028 00 00 00 00
 002c 00 00 50 18
 0030 ff ff d0 67
 0034 00 00 58 32
 0038 bc 86 e9 cb
 003c 82 2f 0d 57
 0.000600 
 0000 e0 9f 97 1c
 0004 20 5c 66 ae
 0008 19 d1 a6 80
 000c 08 00 45 00
 0010 00 ab 00 00
 0014 40 00 ff 06
 0018 a8 6d 85 2d
 001c f7 e1 b5 d6
 0020 9f f9 01 da
 0024 01 da 00 00
 0028 00 71 00 00
 002c 00 00 50 18
 0030 ff ff f8 08
 0034 00 00 9c b0
 0038 16 e9 06 24
 003c c5 fa f1 e7</code></pre></div><div id="question-tags" class="tags-container tags">import text timestamp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '11, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/c167cb677627582928b64e41ff1894a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kevinj&#39;s gravatar image" /><p>kevinj<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kevinj has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Sep '11, 14:56</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-6396" class="comments-container"></div><div id="comment-tools-6396" class="comment-tools"></div><div class="clear"></div><div id="comment-6396-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="6404"></span>

<div id="answer-container-6404" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6404-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can add date and time (but I don't know how to add microseconds).<br />
<br />
Copy and save this as dump</p><pre><code>2011-09-01 00:00:02
0000 e0 9f 97 1c 20 5c 66 ae 19 d1 a6 80 08 00 45 00 
0010 00 99 00 00 40 00 ff 06 a8 7f 85 2d f7 e1 b5 d6 
0020 9f f9 01 da 01 da 00 00 00 00 00 00 00 00 50 18 
0030 ff ff 27 e2 00 00 55 5c 03 96 8f 9a a1 f8 73 69 
2011-09-01 00:00:04 
0000 66 ae 19 d1 a6 80 e0 9f 97 1c 20 5c 08 00 45 00 
0010 00 a9 00 00 40 00 ff 06 a8 6f b5 d6 9f f9 85 2d 
0020 f7 e1 01 da 01 da 00 00 00 00 00 00 00 00 50 18 
0030 ff ff d0 67 00 00 58 32 bc 86 e9 cb 82 2f 0d 57 
2011-09-01 00:00:06 
0000 e0 9f 97 1c 20 5c 66 ae 19 d1 a6 80 08 00 45 00 
0010 00 ab 00 00 40 00 ff 06 a8 6d 85 2d f7 e1 b5 d6 
0020 9f f9 01 da 01 da 00 00 00 71 00 00 00 00 50 18 
0030 ff ff f8 08 00 00 9c b0 16 e9 06 24 c5 fa f1 e7</code></pre>Run:<br />
$ text2pcap -t "%Y-%m-%d %H:%M:%S" dump dump.pcap<br />
Input from: dump<br />
Output to: dump.pcap<br />
Wrote packet of 64 bytes at 0<br />
Wrote packet of 64 bytes at 64<br />
Wrote packet of 63 bytes at 128<br />
Read 3 potential packets, wrote 3 packets<br />
</div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '11, 12:06</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-6404" class="comments-container"><span id="6410"></span><div id="comment-6410" class="comment"><div id="post-6410-score" class="comment-score">1</div><div class="comment-text"><p>Or go to Wireshark directly.</p><p>Menu File|Import, select file name, check Data/Time and enter format string "%F %T" (which is equivalent to %Y-%m-%d %H:%M:%S). Click Ok and your done.</p></div><div id="comment-6410-info" class="comment-info"><span class="comment-age">(16 Sep '11, 00:49)</span> Jaap ♦</div></div></div><div id="comment-tools-6404" class="comment-tools"></div><div class="clear"></div><div id="comment-6404-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6411"></span>

<div id="answer-container-6411" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6411-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Import time format is determent by <a href="http://linux.die.net/man/3/strftime">strftime(3)</a>, see also <a href="http://www.wireshark.org/docs/man-pages/text2pcap.html">man text2pcap</a> and <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChIOImportSection.html">User's Guide</a>.</p><p>Trick is to add a dot after the %S (or %T for that matter) specifier.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '11, 00:56</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-6411" class="comments-container"></div><div id="comment-tools-6411" class="comment-tools"></div><div class="clear"></div><div id="comment-6411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6399"></span>

<div id="answer-container-6399" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6399-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you mean using text2pcap to import text files with timestamp information, then this is not yet supported, although this was filed as <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1636">bug 1636</a> several years ago.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '11, 10:47</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-6399" class="comments-container"><span id="6416"></span><div id="comment-6416" class="comment"><div id="post-6416-score" class="comment-score"></div><div class="comment-text"><p>Based on the other answers, the bug you mentioned is no longer an issue (and should be closed).</p></div><div id="comment-6416-info" class="comment-info"><span class="comment-age">(16 Sep '11, 05:50)</span> bstn</div></div><span id="6417"></span><div id="comment-6417" class="comment"><div id="post-6417-score" class="comment-score"></div><div class="comment-text"><p>The bug was filed because text2pcap does not properly handle/parse capture files exported to text with packet summary and/or details information included. As far as I'm aware, this is still the case.</p></div><div id="comment-6417-info" class="comment-info"><span class="comment-age">(16 Sep '11, 07:06)</span> cmaynard ♦♦</div></div><span id="6418"></span><div id="comment-6418" class="comment"><div id="post-6418-score" class="comment-score"></div><div class="comment-text"><p>Ok. However, it's evident (from @joke's answer) that text2pcap <strong>does support</strong> importing text files with timestamp information.</p></div><div id="comment-6418-info" class="comment-info"><span class="comment-age">(16 Sep '11, 07:17)</span> bstn</div></div><span id="6419"></span><div id="comment-6419" class="comment"><div id="post-6419-score" class="comment-score"></div><div class="comment-text"><p>@bstn: the bug concerned is about writing out packet info from Wireshark into a text file, and later trying to import that. The Wireshark output does not adhere to <em>od -Ax -tx1</em> layout, for which text2pcap was made. The bug report should be an enhancement request.</p></div><div id="comment-6419-info" class="comment-info"><span class="comment-age">(16 Sep '11, 07:36)</span> Jaap ♦</div></div><span id="6421"></span><div id="comment-6421" class="comment"><div id="post-6421-score" class="comment-score"></div><div class="comment-text"><p>In my view, it's not an enhancement request because I feel that Wireshark's own tools should be able to inter-operate with each other. If Wireshark is able to export a pcap file to text, then Wireshark's text2pcap tool ought to be able to convert it back to exactly the same pcap file as the original. But if you feel strongly that it should be an enhancement, then feel free to change it.</p></div><div id="comment-6421-info" class="comment-info"><span class="comment-age">(16 Sep '11, 07:45)</span> cmaynard ♦♦</div></div><span id="6431"></span><div id="comment-6431" class="comment not_top_scorer"><div id="post-6431-score" class="comment-score"></div><div class="comment-text"><p>Enhancement or bug depends on the design goals. The manual page clearly states that text2pcap is intended to eat up octal dumps and spit out packet captures. It has some fancy stuff, like email comment marker digestion, #text2pcap inline directives and such. If it wouldn't do all this that would be a bug.</p><p>If we think the tool should be able to do more/something else then there's a addition/change in design goals. That's an enhancement.</p><p>Personally I don't care what this is called either way. As long as the tool does what people need it to do.</p></div><div id="comment-6431-info" class="comment-info"><span class="comment-age">(17 Sep '11, 02:58)</span> Jaap ♦</div></div><span id="6530"></span><div id="comment-6530" class="comment not_top_scorer"><div id="post-6530-score" class="comment-score"></div><div class="comment-text"><p>For what it's worth, I have reclassified <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1636">bug 1636</a> as an enhancement.</p></div><div id="comment-6530-info" class="comment-info"><span class="comment-age">(23 Sep '11, 13:34)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-6399" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-6399-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

