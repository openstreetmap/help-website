+++
type = "question"
title = "Length of LLC filter"
description = '''What is the filter string to capture packets with specific length for their LLC? In order to find packets that the LLC exist in them, the diplay filter is simply &quot;llc&quot;. But how to contrive from that a filter for its length?  Edit #1 (18 May 2014 07:14 UTC): The LLC is 8 bytes in length. Here&#x27;s an ex...'''
date = "2014-05-15T08:25:00Z"
lastmod = "2014-05-17T23:41:00Z"
weight = 32831
keywords = [ "llc" ]
aliases = [ "/questions/32831" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Length of LLC filter](/questions/32831/length-of-llc-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32831-score" class="post-score" title="current number of votes">0</div><span id="post-32831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the filter string to capture packets with specific length for their LLC?</p><p>In order to find packets that the LLC exist in them, the diplay filter is simply "llc".<br />
But how to contrive from that a filter for its length?</p><hr /><p>Edit #1 (18 May 2014 07:14 UTC):</p><p>The LLC is 8 bytes in length. Here's an example of such LLC header (in PDML format): <a href="http://pastebin.com/MKNy77Qa">http://pastebin.com/MKNy77Qa</a></p><p>Indeed, we're talking about WiFi packets. Sorry for omitting this detail.<br />
</p><p>The filter <code>llc.control.ftype == "Unnumbered frame"</code> seems to work despite that it's a WiFi packet. Can I rely on it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-llc" rel="tag" title="see questions tagged &#39;llc&#39;">llc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '14, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/d7bc992d0b3f0e2db1bf0eec41ba32dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dor_lan&#39;s gravatar image" /><p><span>Dor_lan</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dor_lan has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 May '14, 23:30</strong> </span></p></div></div><div id="comments-container-32831" class="comments-container"></div><div id="comment-tools-32831" class="comment-tools"></div><div class="clear"></div><div id="comment-32831-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32864"></span>

<div id="answer-container-32864" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32864-score" class="post-score" title="current number of votes">1</div><span id="post-32864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dor_lan has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I presume, from "the display filter is simply "llc"", that by "LLC" you mean the IEEE 802.2 LLC.</p><p>If so, then the LLC header is either 3 or 4 bytes long. If you want packets with a 3-byte header (which is almost all of them), you want unnumbered frames; if you want packets with a 4-byte header, you want non-unnumbered frames.</p><p>If by "capture packets" you mean "capture packets", i.e. you don't want Wireshark to even <em>see</em> those packets, the capture filter for packets with a 3-byte LLC header would, for Ethernet, be</p><pre><code>ether[12:2] &lt;= 1500 &amp;&amp; (ether[16] &amp; 0x03) == 0x03</code></pre><p>where the first test checks that the type/length field in the Ethernet header has a value &lt;= 1500 and thus is a length field - meaning that what follows should be an 802.2 LLC header - and the second test checks that the type in the control field of the LLC header is "unnumbered".</p><p>To check for packets with a 4-byte LLC header, do</p><pre><code>ether[12:2] &lt;= 1500 &amp;&amp; (ether[16] &amp; 0x03) != 0x03</code></pre><p>For other network types, such as Wi-Fi, it'd be different - and somewhat complicated, assuming it's even possible, given that the link-layer header is variable-length. libpcap <em>should</em> really support filters for checking for LLC frame types, but it currently doesn't; I'll look at adding that (but that won't help until it shows up in a libpcap/WinPcap release and you have that version of libpcap/WinPcap on your system, with Wireshark using it).</p><p>If you've already captured the packets, and you only want to see the ones with a 3-byte LLC header, the display filter is</p><pre><code>llc.control.ftype == &quot;Unnumbered frame&quot;</code></pre><p>and for the ones with a 4-byte LLC header, it's</p><pre><code>llc.control.ftype != &quot;Unnumbered frame&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '14, 15:49</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-32864" class="comments-container"><span id="32867"></span><div id="comment-32867" class="comment"><div id="post-32867-score" class="comment-score"></div><div class="comment-text"><p>Indeed it's a WiFi packet. Would the last 2 filters work anyway? Please see me Edit. Thx!</p></div><div id="comment-32867-info" class="comment-info"><span class="comment-age">(17 May '14, 23:31)</span> <span class="comment-user userinfo">Dor_lan</span></div></div><span id="32868"></span><div id="comment-32868" class="comment"><div id="post-32868-score" class="comment-score"></div><div class="comment-text"><p>Yes, the <em>display</em> filters will work.</p></div><div id="comment-32868-info" class="comment-info"><span class="comment-age">(17 May '14, 23:41)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-32864" class="comment-tools"></div><div class="clear"></div><div id="comment-32864-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32840"></span>

<div id="answer-container-32840" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32840-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32840-score" class="post-score" title="current number of votes">1</div><span id="post-32840-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is no length field in the LLC headers - at least not the one that I found so far. you could filter on eth.len if the LLC frames are flowing over ethernet and - given the LLC header itself is 3 bytes in size - substract 3</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '14, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-32840" class="comments-container"></div><div id="comment-tools-32840" class="comment-tools"></div><div class="clear"></div><div id="comment-32840-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

