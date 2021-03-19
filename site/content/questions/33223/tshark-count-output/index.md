+++
type = "question"
title = "tshark count output"
description = '''In the following version... TShark 1.10.7 (v1.10.7-0-g6b931a1 from master-1.10) Is this expected?  sudo /usr/local/bin/tshark -n -q -r cdp-01-ccc-2014-05-21-accounting-and-accepts.cap -z io,stat,0,&quot;COUNT(radius.code)radius.code&quot; &#x27;radius.code==2&#x27;  ============================================ | IO Sta...'''
date = "2014-05-30T12:52:00Z"
lastmod = "2014-05-31T07:19:00Z"
weight = 33223
keywords = [ "count", "tshark" ]
aliases = [ "/questions/33223" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark count output](/questions/33223/tshark-count-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33223-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In the following version...</p><p>TShark 1.10.7 (v1.10.7-0-g6b931a1 from master-1.10)</p><p>Is this expected?</p><pre><code>sudo /usr/local/bin/tshark -n -q -r cdp-01-ccc-2014-05-21-accounting-and-accepts.cap -z io,stat,0,&quot;COUNT(radius.code)radius.code&quot; &#39;radius.code==2&#39;

============================================
| IO Statistics                            |
|                                          |
| Interval size:   407.0 secs (dur)        |
| Col 1: Frames and bytes                  |
|     2: COUNT(radius.code)radius.code     |
|------------------------------------------|
|                |1                |2      |
| Interval       | Frames |  Bytes | COUNT |
|------------------------------------------|
| 0.0 &lt;&gt; 86307.0 |     59 |  22868 |    59 |
============================================

sudo /usr/local/bin/tshark -n -r cdp-01-ccc-2014-05-21-accounting-and-accepts.cap -z io,stat,0,&quot;COUNT(radius.code)radius.code&quot; &#39;radius.code==2&#39; | grep Access-Accept | wc -l 1618</code></pre><p>Why is there such a difference in counts and what should it be?</p></div><div id="question-tags" class="tags-container tags">count tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '14, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/f7258bc33d2e127dab5be103bb72d8e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="loner_t&#39;s gravatar image" /><p>loner_t<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="loner_t has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 May '14, 13:46</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-33223" class="comments-container"></div><div id="comment-tools-33223" class="comment-tools"></div><div class="clear"></div><div id="comment-33223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33232"></span>

<div id="answer-container-33232" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33232-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Why is there such a difference in counts and what should it be?</p></blockquote><p>because you are using <strong>-q</strong> (be quiet) in the first case, which tells tshark to <strong>not</strong> print a line for every packet in the capture file. As you did not use <strong>-q</strong> in the second case, you are getting a much larger number of lines, one per frame in the pcap file. That's totally expected behavior. See the man page of tshark.</p><blockquote><p><a href="http://www.wireshark.org/docs/man-pages/tshark.html">http://www.wireshark.org/docs/man-pages/tshark.html</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '14, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-33232" class="comments-container"><span id="33234"></span><div id="comment-33234" class="comment"><div id="post-33234-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Kurt. The reason for not using -q in second one was to see and count of actual packets with radius.code==2.</p><p>Also, even though my interval is set to 0 in both cases, tshark uses 407.0 seconds as an interval. The man page says, if interval is set to 0, the count function is over the entire duration of the capture, which in my specific case is roughly 24 hours.</p><p>Am I interpreting the man page correctly? The goal is to count the number of packets with radius.code==2 accurately.</p></div><div id="comment-33234-info" class="comment-info"><span class="comment-age">(31 May '14, 08:08)</span> loner_t</div></div><span id="33250"></span><div id="comment-33250" class="comment"><div id="post-33250-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The goal is to count the number of packets with radius.code==2 accurately</p></blockquote><p>Then please try this (not tested):</p><blockquote><p>tshark -nr cdp-01-ccc-2014-05-21-accounting-and-accepts.cap -Y "radius.code==2" | grep Access-Accept | wc -l</p></blockquote></div><div id="comment-33250-info" class="comment-info"><span class="comment-age">(01 Jun '14, 15:56)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-33232" class="comment-tools"></div><div class="clear"></div><div id="comment-33232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

