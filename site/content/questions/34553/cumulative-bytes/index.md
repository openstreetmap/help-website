+++
type = "question"
title = "Cumulative Bytes"
description = '''Hello, I want to apply a filter so i can search for packets with certain cumulative bytes. I know how to add a column with this information (preference-&amp;gt; columns) but I don&#x27;t know what is the command for the filter. For example I want to know all the packets that have more than x cumulative bytes...'''
date = "2014-07-10T04:38:00Z"
lastmod = "2014-07-10T04:38:00Z"
weight = 34553
keywords = [ "filter", "statistics", "packets", "tshark", "wireshark" ]
aliases = [ "/questions/34553" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cumulative Bytes](/questions/34553/cumulative-bytes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34553-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I want to apply a filter so i can search for packets with certain cumulative bytes. I know how to add a column with this information (preference-&gt; columns) but I don't know what is the command for the filter. For example I want to know all the packets that have more than x cumulative bytes. A filter that I can use like a frame.time_relative filter.</p><p>The point is that this must be a filter, not a graphic method, because later on I will need to implement this in a perl script (so i will have to use tshark) and extract those informations to a file (i.e. -e frame.time_relative or -e rtp.seq).</p><p>Concerned beginner</p></div><div id="question-tags" class="tags-container tags">filter statistics packets tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '14, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/d37010d6d63374fe35a5fcfba121dedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anhtuan&#39;s gravatar image" /><p>anhtuan<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anhtuan has no accepted answers">0%</span></p></div></div><div id="comments-container-34553" class="comments-container"><span id="34554"></span><div id="comment-34554" class="comment"><div id="post-34554-score" class="comment-score"></div><div class="comment-text"><p>can you please define 'more than x cumulative bytes' in an example?</p></div><div id="comment-34554-info" class="comment-info"><span class="comment-age">(10 Jul '14, 04:40)</span> Kurt Knochner ♦</div></div><span id="34555"></span><div id="comment-34555" class="comment"><div id="post-34555-score" class="comment-score"></div><div class="comment-text"><p>For example I can use a frame.time_relative &gt; 10. In a similar way I want to use a filter to know from which packet the cumulative number of bytes is higher than x. Moreover later i will need to extract the entire column with cumulative bytes information so the name of the filter is essential for me.</p></div><div id="comment-34555-info" class="comment-info"><span class="comment-age">(10 Jul '14, 04:49)</span> anhtuan</div></div><span id="34556"></span><div id="comment-34556" class="comment"><div id="post-34556-score" class="comment-score"></div><div class="comment-text"><p>As I said: can you please define 'more than x cumulative bytes' <strong>in an example</strong>?</p></div><div id="comment-34556-info" class="comment-info"><span class="comment-age">(10 Jul '14, 04:50)</span> Kurt Knochner ♦</div></div><span id="34557"></span><div id="comment-34557" class="comment"><div id="post-34557-score" class="comment-score"></div><div class="comment-text"><p>"rtp.ssrc = 0x176EF98C and CUMULATIVE_BYTES &gt; 30000". This is an example.</p></div><div id="comment-34557-info" class="comment-info"><span class="comment-age">(10 Jul '14, 04:54)</span> anhtuan</div></div><span id="34558"></span><div id="comment-34558" class="comment"><div id="post-34558-score" class="comment-score"></div><div class="comment-text"><p>O.K. let me rephrase it: What exactly are <strong>cumulative</strong> bytes for you?</p></div><div id="comment-34558-info" class="comment-info"><span class="comment-age">(10 Jul '14, 04:56)</span> Kurt Knochner ♦</div></div><span id="34559"></span><div id="comment-34559" class="comment not_top_scorer"><div id="post-34559-score" class="comment-score"></div><div class="comment-text"><p>if you will go to wireshark -&gt; edit -&gt; preferences -&gt; columns than there is a column with a field type "cumulative bytes". It's a number of bytes that have been "transmited" up till that packet.</p></div><div id="comment-34559-info" class="comment-info"><span class="comment-age">(10 Jul '14, 05:02)</span> anhtuan</div></div></div><div id="comment-tools-34553" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-34553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

