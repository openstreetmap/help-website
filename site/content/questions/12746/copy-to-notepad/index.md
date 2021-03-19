+++
type = "question"
title = "Copy to notepad"
description = '''Hi, If i want to copy multiple rows to textfile ctrl or shift pressed in doesn&#x27;t work. what is the easiest way to copy specific rows to a textfile?'''
date = "2012-07-16T04:43:00Z"
lastmod = "2017-01-05T03:16:00Z"
weight = 12746
keywords = [ "notepad" ]
aliases = [ "/questions/12746" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Copy to notepad](/questions/12746/copy-to-notepad)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12746-score" class="post-score" title="current number of votes">2</div><span id="post-12746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>If i want to copy multiple rows to textfile ctrl or shift pressed in doesn't work. what is the easiest way to copy specific rows to a textfile?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-notepad" rel="tag" title="see questions tagged &#39;notepad&#39;">notepad</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '12, 04:43</strong></p><img src="https://secure.gravatar.com/avatar/b307aedf12ca75ee1da5ec114fa2028e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ivan&#39;s gravatar image" /><p><span>Ivan</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ivan has no accepted answers">0%</span></p></div></div><div id="comments-container-12746" class="comments-container"></div><div id="comment-tools-12746" class="comment-tools"></div><div class="clear"></div><div id="comment-12746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12748"></span>

<div id="answer-container-12748" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12748-score" class="post-score" title="current number of votes">1</div><span id="post-12748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Mark the packtes (CRTL-M) you need, then print them to a text file:</p><blockquote><p><code>File -&gt; Print -&gt; Plain Text</code><br />
</p></blockquote><p>Select the following options:</p><ul><li>Output to file (e.g. wireshark.out)</li><li>Marked packets only (Packet range)</li><li>Packet summary line (Packet Format)</li></ul><p>Then open the output file in an editor.</p><p>Alternatively, you can use tshark</p><blockquote><p><code>tshark -r input.cap -T fields -e ip.src -e ip.dst -e &lt;whatever_field_you_like&gt; -E header=y -E separator=;</code></p></blockquote><p>See <code>tshark -G</code> for a list of available fields. You can also select in Wireshark and it will show the field name in the status line at the bottom (TCP Source Port - tcp.srcport)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '12, 05:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-12748" class="comments-container"><span id="17110"></span><div id="comment-17110" class="comment"><div id="post-17110-score" class="comment-score"></div><div class="comment-text"><p>Works fine. But is that really the "<em>easiest way</em>"? That would be ridiculous, why can't you just select everything (with something like ctrl+a, shift+arrows, mouse, ...) and press ctrl+c?</p></div><div id="comment-17110-info" class="comment-info"><span class="comment-age">(20 Dec '12, 12:30)</span> <span class="comment-user userinfo">BeniBela</span></div></div><span id="17111"></span><div id="comment-17111" class="comment"><div id="post-17111-score" class="comment-score"></div><div class="comment-text"><blockquote><p>why can't you just select everything (with something like ctrl+a, shift+arrows, mouse, ...) and press ctrl+c?</p></blockquote><p>because it is not yet implemented ;-)</p></div><div id="comment-17111-info" class="comment-info"><span class="comment-age">(20 Dec '12, 12:45)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17122"></span><div id="comment-17122" class="comment"><div id="post-17122-score" class="comment-score"></div><div class="comment-text"><p>And implimenting it isn't trivial.</p></div><div id="comment-17122-info" class="comment-info"><span class="comment-age">(20 Dec '12, 23:39)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="17135"></span><div id="comment-17135" class="comment"><div id="post-17135-score" class="comment-score"></div><div class="comment-text"><p><span>@Anders</span>: But it looks like a trivial GUI thingy</p></div><div id="comment-17135-info" class="comment-info"><span class="comment-age">(21 Dec '12, 08:34)</span> <span class="comment-user userinfo">BeniBela</span></div></div><span id="17140"></span><div id="comment-17140" class="comment"><div id="post-17140-score" class="comment-score"></div><div class="comment-text"><p>It's probably 'easy' for the currently selected packet, as there is already such a function, just not available via CTRL-C (windows).</p><blockquote><p><code>right click -&gt; Copy -&gt; Summary (Text)</code><br />
</p></blockquote><p>That's not the full packet detail, but that could be made a configurable option. So, implementing that would be 'quite easy'.</p><p>However: I don't know how hard it would be to implement 'multi-select' in the packet list view?</p><p>Can anyone of the GTK experts please jump in?</p></div><div id="comment-17140-info" class="comment-info"><span class="comment-age">(21 Dec '12, 09:43)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17151"></span><div id="comment-17151" class="comment not_top_scorer"><div id="post-17151-score" class="comment-score"></div><div class="comment-text"><blockquote><p><span></span><span>@Anders</span>: But it looks like a trivial GUI thingy<br />
</p></blockquote><p>Feel free to implement it :-)</p></div><div id="comment-17151-info" class="comment-info"><span class="comment-age">(21 Dec '12, 13:57)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="58504"></span><div id="comment-58504" class="comment not_top_scorer"><div id="post-58504-score" class="comment-score"></div><div class="comment-text"><p>I know this is an older post but I was wondering if anyone had found a workaround to the hours spent: - Right-click - Copy - ...as Printable Text ...when you have hundreds (maybe thousands) of packets to copy as printable text and dump into a text editor. Thanks</p></div><div id="comment-58504-info" class="comment-info"><span class="comment-age">(04 Jan '17, 10:06)</span> <span class="comment-user userinfo">Lars</span></div></div><span id="58511"></span><div id="comment-58511" class="comment not_top_scorer"><div id="post-58511-score" class="comment-score"></div><div class="comment-text"><p>Have you tried:</p><p>File / Export Packet Dissections / as "Plain Text" File</p></div><div id="comment-58511-info" class="comment-info"><span class="comment-age">(04 Jan '17, 11:26)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="58515"></span><div id="comment-58515" class="comment not_top_scorer"><div id="post-58515-score" class="comment-score"></div><div class="comment-text"><p>I did try that, and print as plain text. The problem is that it is SNMP and I do not need to SNMP long-form OID info that is displays. I need the Human Readable Alarm Data that is shown when you right-click on a packet, Copy, ....as Printable Text.</p><p>Here is what printing packet dissections of 49 sorted packets produces...I just show one:</p><pre><code>No.     Time                          Source                Destination           Protocol Length Info
   3440 2016-12-05 11:41:17.652442    sourceipaddr          destipaddr             SNMP     571    snmpV2-trap 1.3.6.1.2.1.1.3.0 1.3.6.1.6.3.1.1.4.1.0 1.3.6.1.4.1.562.29.6.2.1 1.3.6.1.4.1.562.29.6.2.2 1.3.6.1.4.1.562.29.6.2.3 1.3.6.1.4.1.562.29.6.1.1.1.1 1.3.6.1.4.1.562.29.6.1.1.1.2 1.3.6.1.4.1.562.29.6.1.1.1.3 1.3.6.1.4.1.562.29.6.1.1.1.4 1.3.6.1.4.1.562.29.6.1.1.1.5 1.3.6.1.4.1.562.29.6.1.1.1.6 1.3.6.1.4.1.562.29.6.1.1.1.7 1.3.6.1.4.1.562.68.11.1.1.1 1.3.6.1.4.1.562.68.11.1.1.2 1.3.6.1.4.1.562.68.11.1.1.3 1.3.6.1.4.1.562.68.11.1.1.4 1.3.6.1.4.1.562.68.11.1.1.6 1.3.6.1.6.3.1.1.4.3.0
Frame 3440: 571 bytes on wire (4568 bits), 571 bytes captured (4568 bits) on interface 0
Ethernet II, Src: CiscoInc_af:97:01 (a8:0c:0d:af:97:01), Dst: Microsof_0e:23:0d (00:15:5d:0e:23:0d)
Internet Protocol Version 4, Src: 10.3.148.211, Dst: 10.64.14.133
User Datagram Protocol, Src Port: 1097, Dst Port: 162
Simple Network Management Protocol</code></pre><p>Doing a Right-Click, Copy, ...as Printable Text, and then pasting into NotePad++, produces this:</p><pre><code>]#
E-:H~D
@I 0
sysadmin00+CVH0
+
+2.0+20+2)0-+2Optical Channel Power Transmit0
+20
+200g
+2VNODE11:CHMON-1-2-7-153504,OPT-OCH,NEND,TRMT,0000,000000,-17.60,000006,1-UNT,NA,1535.040
+2NA0
+2NA0
+20
+20+2D0+2D0+2DNODE110[email protected]
0+2D0
 + +2D</code></pre><p>I need the 4th and 7th lines in this output, although it is not always in the same line. I have thousands of packets to parse and capture in this way and strip away what I will call "the noise" and then use that data. Just the ability to perform a mass copy as printable text and dump into Notepad would save me a great deal of time.</p></div><div id="comment-58515-info" class="comment-info"><span class="comment-age">(04 Jan '17, 12:24)</span> <span class="comment-user userinfo">Lars</span></div></div><span id="58534"></span><div id="comment-58534" class="comment not_top_scorer"><div id="post-58534-score" class="comment-score"></div><div class="comment-text"><p>All the recent "answers" have been converted to a comments as that's how this site works. Please read the FAQ for more information.</p><p><span>@Lars</span>,</p><p>Attempting to parse Wireshark dissection of SNMP traffic seems to be an awfully long winded of going about this. Why not use an SNMP application to issue the specific SNMP requests you require and output the returned data in the format you require?</p></div><div id="comment-58534-info" class="comment-info"><span class="comment-age">(05 Jan '17, 03:16)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-12748" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-12748-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

