+++
type = "question"
title = "Analysing USB traffic"
description = '''I&#x27;ve captured USB traffic using Wireshark, but I&#x27;m finding it difficult to analyse. Most of my useful data lies in hundreds of URB_BULK in/out packets (too many to browse through one by one). I&#x27;m specifically interested in the actual data sent over USB, not the headers. For TCP/IP data, I&#x27;ve found t...'''
date = "2012-05-16T09:15:00Z"
lastmod = "2012-05-17T13:47:00Z"
weight = 11054
keywords = [ "usb" ]
aliases = [ "/questions/11054" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Analysing USB traffic](/questions/11054/analysing-usb-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11054-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">2</div></div></td><td><div id="item-right"><div class="question-body"><p>I've captured USB traffic using Wireshark, but I'm finding it difficult to analyse. Most of my useful data lies in hundreds of URB_BULK in/out packets (too many to browse through one by one). I'm specifically interested in the actual data sent over USB, not the headers.</p><p>For TCP/IP data, I've found the "Follow TCP stream" function very useful to view the entire "coversation" between the host and the client, but there doesn't seem to be anything similar for USB.</p><p>What is the best way to view the entire "conversation" of all the USB data?</p><p>My best solution so far is to use <code>tshark -x -r mydata.pcap</code> to dump the file, then I get something like the following:</p><pre><code>460  11.863947         host -&gt; 3.1          USB 64 URB_BULK in

0000  00 f6 94 c0 00 88 ff ff 53 03 81 03 06 00 2d 3c   ........S.....-&lt;
0010  ad c8 b3 4f 00 00 00 00 96 a8 0c 00 8d ff ff ff   ...O............
0020  00 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0030  00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00   ................

461  11.864934          3.1 -&gt; host         USB 77 URB_BULK in

0000  00 f6 94 c0 00 88 ff ff 43 03 81 03 06 00 2d 00   ........C.....-.
0010  ad c8 b3 4f 00 00 00 00 71 ac 0c 00 00 00 00 00   ...O....q.......
0020  0d 00 00 00 0d 00 00 00 00 00 00 00 00 00 00 00   ................
0030  00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00   ................
0040  a4 09 50 60 00 00 00 00 00 ff ff 09 94            ..P`.........</code></pre></div><div id="question-tags" class="tags-container tags">usb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '12, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/e15028f4cfbbdf1c2b42bd5abb326ecc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ralf%20Kistner&#39;s gravatar image" /><p>Ralf Kistner<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ralf Kistner has one accepted answer">100%</span></p></div></div><div id="comments-container-11054" class="comments-container"></div><div id="comment-tools-11054" class="comment-tools"></div><div class="clear"></div><div id="comment-11054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11115"></span>

<div id="answer-container-11115" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11115-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>These are the steps I followed to make the data usable:</p><ol><li><p><strong>Filter out the irrelevant data.</strong> Kurt's answer helped a lot here. Select a message, find a field you need to filter on, right-click on the field and select "Apply as Filter". To filter on multiple fields, join them with <code>and</code>. In my case I was only interested in fields containing data, and only from a single device, so my filter looks like this:</p><pre><code>usb.data_flag == &quot;present (0)&quot; &amp;&amp; usb.device_address == 3</code></pre><p>As I only monitored a single bus, I did not need to filter out the bus.</p></li><li><p><strong>Display useful columns.</strong> The default columns are not extremely useful, so I changed them to the following. The important one here is the "Leftover Capture Data".</p><pre><code>No.  (default column)
Time  (default column)
Source  (default column)
Data length [bytes] (instead of length)
Leftover Capture Data (the actual data as hex)</code></pre><p>To remove the redundant default columns, simply right-click and select remove. To add more columns, find the relevant field in the packet details, right click and select "Apply Column".</p></li><li><p>(Optional) <strong>Export as text file.</strong> Once the filters and columns are configured, the data can be exported to a nice text format, to allow for easy search and copy/paste functionality. File -&gt; Export -&gt; as "Plain Text" file. Select "Displayed" instead of "Captured" to use the filters. Select only "Packet summary line" and not "Packet details" or "Packet bytes" for a nice and compact format. My output now looks as follows, containing only the relevant output:</p><pre><code>No.     Time        Source                Data length [bytes] Leftover Capture Data
     29 3.568506    host                  8                   a402440003e10000
     30 3.568930    3.1                   7                   a40340004400a3
     33 3.570528    host                  8                   a402450041a20000
     35 3.571931    3.1                   7                   a40340004500a2</code></pre></li></ol><p><em>Disclaimer: I know little about USB, so this might not be useful in the general case. In my case I'm only interested in the data (payload) sent with URB_BULK, and not any other data or headers.</em></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '12, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/e15028f4cfbbdf1c2b42bd5abb326ecc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ralf%20Kistner&#39;s gravatar image" /><p>Ralf Kistner<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ralf Kistner has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 May '12, 14:13</p></div></div><div id="comments-container-11115" class="comments-container"></div><div id="comment-tools-11115" class="comment-tools"></div><div class="clear"></div><div id="comment-11115-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11059"></span>

<div id="answer-container-11059" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11059-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could (display) filter on the device and bus ID:</p><blockquote><p><code>usb.device_address eq 8 and usb.bus_id eq 1</code></p></blockquote><p>This will show only the communication between that devive and the host.</p><blockquote><p><code>What is the best way to view the entire "conversation" of all the USB data?</code></p></blockquote><p>Do you mean a text representation of the exchanged data? If yes, then there is nothing I know of.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '12, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 May '12, 11:11</p></div></div><div id="comments-container-11059" class="comments-container"><span id="11064"></span><div id="comment-11064" class="comment"><div id="post-11064-score" class="comment-score"></div><div class="comment-text"><p>Thanks, the filter helps cutting away some of the non-relevant data at least. Is there a filter to only show the URB_BULK in/out data?</p><p>Yes, I mean viewing the exchanged data (excluding headers) in hex and/or ASCII format.</p></div><div id="comment-11064-info" class="comment-info"><span class="comment-age">(16 May '12, 13:36)</span> Ralf Kistner</div></div><span id="11072"></span><div id="comment-11072" class="comment"><div id="post-11072-score" class="comment-score">1</div><div class="comment-text"><blockquote><p><code>Is there a filter to only show the URB_BULK in/out data?</code></p></blockquote><p>Just open a USB packet and select any item. You will see the display filter in the status line at the bottom of the window. With that you should be able to build any filter you need.</p></div><div id="comment-11072-info" class="comment-info"><span class="comment-age">(16 May '12, 15:48)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-11059" class="comment-tools"></div><div class="clear"></div><div id="comment-11059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

