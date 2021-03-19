+++
type = "question"
title = "How do you capture RTP packets?"
description = '''I&#x27;m trying to capture RTP streams. When I use rtp as a packet filter Wireshark says &quot;Invalid capture filter: &quot;rtp&quot;!&quot; What port does RTP use?'''
date = "2010-09-08T09:39:00Z"
lastmod = "2010-09-14T04:47:00Z"
weight = 11
keywords = [ "capture-filter", "rtp" ]
aliases = [ "/questions/11" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How do you capture RTP packets?](/questions/11/how-do-you-capture-rtp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to capture RTP streams. When I use <code>rtp</code> as a packet filter Wireshark says "Invalid capture filter: "rtp"!" What port does RTP use?</p></div><div id="question-tags" class="tags-container tags">capture-filter rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Sep '10, 09:39</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Sep '10, 11:47</p></div></div><div id="comments-container-11" class="comments-container"></div><div id="comment-tools-11" class="comment-tools"></div><div class="clear"></div><div id="comment-11-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="37"></span>

<div id="answer-container-37" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>RTP port numbers are usually dynamically assigned. You can use something like this to get close enough in most cases:</p><pre><code>udp[1] &amp; 1 != 1 &amp;&amp; udp[3] &amp; 1 != 1 &amp;&amp; udp[8] &amp; 0x80 == 0x80 &amp;&amp; length &lt; 250</code></pre><p>It does the following:</p><ul><li><code>udp[1] &amp; 1 != 1 &amp;&amp; udp[3] &amp; 1 != 1</code> - even source and destination UDP ports</li><li><code>udp[8] &amp; 0x80 == 0x80</code> - a valid RTP version</li><li><code>length &lt; 250</code> - look for small packets.</li></ul><p>This will capture any non-RTP traffic that happens to match the filter (such as DNS) but it will capture all RTP packets in many environments.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '10, 19:23</strong></p><img src="https://secure.gravatar.com/avatar/617af6ab029cb379ad0ca71495f94df9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Test%20User%201&#39;s gravatar image" /><p>Test User 1<br />
<span class="score" title="141 reputation points">141</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Test User 1 has 2 accepted answers">40%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Sep '10, 19:41</p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span></p></div></div><div id="comments-container-37" class="comments-container"></div><div id="comment-tools-37" class="comment-tools"></div><div class="clear"></div><div id="comment-37-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54"></span>

<div id="answer-container-54" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This likely (hopefully) causes RTP session establishment signaling to be filtered out, so make sure to set '<em>Try to decode RTP outside of conversations</em>' in the RTP dissector preferences. Otherwise you'll only see UDP packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '10, 03:49</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-54" class="comments-container"></div><div id="comment-tools-54" class="comment-tools"></div><div class="clear"></div><div id="comment-54-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56"></span>

<div id="answer-container-56" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It could even be</p><pre><code>udp[8] &amp; 0xC0 == 0x80</code></pre><p>to check for a valid RTP version (2).</p><p>The length could be tuned even further, starting at 225 for untagged 20 ms G.711 audio @ 8kbps, adding 80 bytes per 10 ms extra. Other features (SRTP, RTP extensions) and other codecs (G722, G729, etc) require other sizes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '10, 04:47</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-56" class="comments-container"></div><div id="comment-tools-56" class="comment-tools"></div><div class="clear"></div><div id="comment-56-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

