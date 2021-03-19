+++
type = "question"
title = "how do I extract an MPEG stream from a wireshark capture file (.pcap) and convert that data to &quot;.ts&quot; format (transport stream)"
description = '''hi i have captured network stream via wireshark tool and this stream is in .pcap file format and i want to convert this format to Ts format. how i will convert.'''
date = "2013-11-12T01:37:00Z"
lastmod = "2013-11-15T10:20:00Z"
weight = 26868
keywords = [ "capture" ]
aliases = [ "/questions/26868" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how do I extract an MPEG stream from a wireshark capture file (.pcap) and convert that data to ".ts" format (transport stream)](/questions/26868/how-do-i-extract-an-mpeg-stream-from-a-wireshark-capture-file-pcap-and-convert-that-data-to-ts-format-transport-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26868-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi i have captured network stream via wireshark tool and this stream is in .pcap file format and i want to convert this format to Ts format. how i will convert.</p></div><div id="question-tags" class="tags-container tags">capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '13, 01:37</strong></p><img src="https://secure.gravatar.com/avatar/193a682dd21ed6ce9f338159e3f9a2a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="COOLpa&#39;s gravatar image" /><p>COOLpa<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="COOLpa has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Nov '13, 04:45</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-26868" class="comments-container"><span id="26875"></span><div id="comment-26875" class="comment"><div id="post-26875-score" class="comment-score"></div><div class="comment-text"><p>do you mind to tell us what the .ts format is?</p></div><div id="comment-26875-info" class="comment-info"><span class="comment-age">(12 Nov '13, 03:49)</span> Kurt Knochner ♦</div></div><span id="26877"></span><div id="comment-26877" class="comment"><div id="post-26877-score" class="comment-score"></div><div class="comment-text"><p>transport stream</p></div><div id="comment-26877-info" class="comment-info"><span class="comment-age">(12 Nov '13, 04:06)</span> COOLpa</div></div><span id="26879"></span><div id="comment-26879" class="comment"><div id="post-26879-score" class="comment-score"></div><div class="comment-text"><p>never heard of that. What kind of sniffer uses that format?</p></div><div id="comment-26879-info" class="comment-info"><span class="comment-age">(12 Nov '13, 04:09)</span> Kurt Knochner ♦</div></div><span id="26887"></span><div id="comment-26887" class="comment"><div id="post-26887-score" class="comment-score"></div><div class="comment-text"><p>I think the OP is trying to extract an MPEG video stream from a network capture.</p></div><div id="comment-26887-info" class="comment-info"><span class="comment-age">(12 Nov '13, 04:32)</span> grahamb ♦</div></div><span id="26888"></span><div id="comment-26888" class="comment"><div id="post-26888-score" class="comment-score"></div><div class="comment-text"><p>yes MPEG transport stream</p></div><div id="comment-26888-info" class="comment-info"><span class="comment-age">(12 Nov '13, 04:37)</span> COOLpa</div></div><span id="26889"></span><div id="comment-26889" class="comment not_top_scorer"><div id="post-26889-score" class="comment-score"></div><div class="comment-text"><p>Ah, sounds reasonable, now that you mention it :-) I was mislead by the word 'convert'.</p></div><div id="comment-26889-info" class="comment-info"><span class="comment-age">(12 Nov '13, 04:37)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26868" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-26868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27037"></span>

<div id="answer-container-27037" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27037-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In Wireshark, load your pcap file, then choose: <code>File -&gt; Export Objects -&gt; HTTP -&gt; [Select the audio/mpeg file of interest] -&gt; Save As -&gt; filename.mpeg</code>.</p><p>From there, use any external software of your choice capable of performing the conversion from .mpeg to .ts. For example, using the <a href="http://www.videolan.org/">VLC media player</a>, you would choose: <code>Media -&gt; Convert/Save -&gt; Add... -&gt; filename.mpeg -&gt; Convert/Save -&gt; Profile: Video - H.264 + MP3 (TS), Destination file: filename.ts -&gt; Start</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Nov '13, 10:20</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-27037" class="comments-container"></div><div id="comment-tools-27037" class="comment-tools"></div><div class="clear"></div><div id="comment-27037-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

