+++
type = "question"
title = "How do I get the default output of TShark as a CSV?"
description = '''I am not sure where i need to go to find the answer to my question. So if there is a link i missed please let me know. I dont mind trying to figure it out. But will gladly accept an answer too.  I am trying to save the output of this command to a CSV file preferably. saving straight to the csv is id...'''
date = "2016-01-09T19:55:00Z"
lastmod = "2016-01-09T20:59:00Z"
weight = 49040
keywords = [ "output", "csv", "columns", "file" ]
aliases = [ "/questions/49040" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How do I get the default output of TShark as a CSV?](/questions/49040/how-do-i-get-the-default-output-of-tshark-as-a-csv)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49040-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am not sure where i need to go to find the answer to my question. So if there is a link i missed please let me know. I dont mind trying to figure it out. But will gladly accept an answer too.</p><p>I am trying to save the output of this command to a CSV file preferably. saving straight to the csv is ideal as opening a pcap file and converting regularly does not sound fun either.</p><p>The command i am trying to replicate is:</p><p>tshark -i wlan1 subtype probereq</p><p>I have tried using command tshark -i wlan1 subtype probereq -V &gt;testout.txt</p></div><div id="question-tags" class="tags-container tags">output csv columns file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jan '16, 19:55</strong></p><img src="https://secure.gravatar.com/avatar/f0ee17843209dc930192e53d9e5ac078?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thegeneral&#39;s gravatar image" /><p>thegeneral<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thegeneral has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jan '16, 21:03</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-49040" class="comments-container"></div><div id="comment-tools-49040" class="comment-tools"></div><div class="clear"></div><div id="comment-49040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49045"></span>

<div id="answer-container-49045" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49045-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I assume from</p><blockquote><p>The command i am trying to replicate is:</p><p>tshark -i wlan1 subtype probereq</p></blockquote><p>that you want the columns that <code>tshark -i wlan1 subtype probereq</code> prints out to be written to a file as a CSV, i.e. with commas between the column values.</p><p>There's not a simple way to do that <em>directly</em>, but you can ask TShark to print various values from the packet with commas between them. If you want the standard set of columns, you could, at least with newer versions of Wireshark, do</p><pre><code>tshark -i wlan1 -T fields -E separator=, -E quote=d -e _ws.col.No. -e _ws.col.Time -e _ws.col.Source -e _ws.col.Destination -e _ws.col.Protocol -e _ws.col.Length -e _ws.col.Info subtype probereq</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '16, 20:59</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jan '16, 00:40</p></div></div><div id="comments-container-49045" class="comments-container"><span id="49196"></span><div id="comment-49196" class="comment"><div id="post-49196-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the help. This is getting the results i am looking for. But now the issue is writing those results to a file.</p><p>When i add -w testfile.txt it just prints to screen but nothing in the file. same with -w -v &gt;testfile.txt</p><p>Any advise on writing the results to a capture file?</p></div><div id="comment-49196-info" class="comment-info"><span class="comment-age">(13 Jan '16, 21:50)</span> thegeneral</div></div><span id="49197"></span><div id="comment-49197" class="comment"><div id="post-49197-score" class="comment-score"></div><div class="comment-text"><p><code>-w</code> specifies to what file the <em>raw captured data</em> should be written. It is always an error to use <code>-w</code> with a file whose name ends in <code>.txt</code>, because TShark (and dumpcap, and tcpdump) do <em>not</em> write out raw captures as text.</p><p>If you don't need the raw packet file (to read later with Wireshark or tcpdump or some other program that can read pcap or pcapng files), then don't specify <code>-w</code> at all, just run tshark with the output redirected to the file, and no <code>-w</code>:</p><pre><code>tshark -i wlan1 -T fields -E separator=, -E quote=d -e _ws.col.No. -e _ws.col.Time -e _ws.col.Source -e _ws.col.Destination -e _ws.col.Protocol -e _ws.col.Length -e _ws.col.Info subtype probereq &gt;testfile.txt</code></pre></div><div id="comment-49197-info" class="comment-info"><span class="comment-age">(13 Jan '16, 21:54)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-49045" class="comment-tools"></div><div class="clear"></div><div id="comment-49045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

