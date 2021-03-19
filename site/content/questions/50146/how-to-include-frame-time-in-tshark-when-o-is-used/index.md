+++
type = "question"
title = "how to include frame time in tshark when -O is used"
description = '''What option can I use to add frame time into following output? lab@ubuntu:~# tshark -ni bond0 -O tcp Capturing on &#x27;bond0&#x27; Frame 1: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) on interface 0 Ethernet II, Src: f0:1c:2d:43:ee:27 (f0:1c:2d:43:ee:27), Dst: 5c:b9:01:8b:6f:3c (5c:b9:01:8b:6f:...'''
date = "2016-02-12T07:13:00Z"
lastmod = "2016-02-12T07:42:00Z"
weight = 50146
keywords = [ "tshark" ]
aliases = [ "/questions/50146" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to include frame time in tshark when -O is used](/questions/50146/how-to-include-frame-time-in-tshark-when-o-is-used)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50146-score" class="post-score" title="current number of votes">0</div><span id="post-50146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What option can I use to add frame time into following output?</p><pre><code>[email protected]:~# tshark -ni bond0 -O tcp
Capturing on &#39;bond0&#39;
Frame 1: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) on interface 0
Ethernet II, Src: f0:1c:2d:43:ee:27 (f0:1c:2d:43:ee:27), Dst: 5c:b9:01:8b:6f:3c (5c:b9:01:8b:6f:3c)
Internet Protocol Version 4, Src: 172.222.19.201 (172.222.19.201), Dst: 172.222.76.4 (172.222.76.4)
Transmission Control Protocol, Src Port: 8086 (8086), Dst Port: 54040 (54040), Seq: 1, Ack: 1, Len: 0
    Source port: 8086 (8086)
    Destination port: 54040 (54040)
    [Stream index: 0]</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '16, 07:13</strong></p><img src="https://secure.gravatar.com/avatar/b7590de43adb375f2d9c6ba1f98b72cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yacare&#39;s gravatar image" /><p><span>yacare</span><br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yacare has no accepted answers">0%</span></p></div></div><div id="comments-container-50146" class="comments-container"></div><div id="comment-tools-50146" class="comment-tools"></div><div class="clear"></div><div id="comment-50146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50153"></span>

<div id="answer-container-50153" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50153-score" class="post-score" title="current number of votes">2</div><span id="post-50153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try using <code>-P</code>. If your Wireshark columns include timestamps, they'll be displayed along with all the other columns. If you <strong>only</strong> want the frame time in the summary, then you'll have to explicitly specify the columns using the <code>-o gui.column.format</code> option, such as:</p><pre><code>tshark -ni bond0 -O tcp -P -o gui.column.format:&#39;&quot;Time&quot;, &quot;%t&quot;&#39;</code></pre><p>... or on Windows:</p><pre><code>tshark.exe -ni bond0 -O tcp -P -o gui.column.format:&quot;\&quot;Time\&quot;, \&quot;%t\&quot;&quot;</code></pre><p>You can see the column formats by running, <code>tshark -G column-formats</code>. You can also see your existing Wireshark columns by looking in your <em>preferences</em> file for <code>gui.column.format</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '16, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Feb '16, 07:41</strong> </span></p></div></div><div id="comments-container-50153" class="comments-container"><span id="50154"></span><div id="comment-50154" class="comment"><div id="post-50154-score" class="comment-score"></div><div class="comment-text"><p>Nice! It works.</p><p>Thanks Cmaynard.</p></div><div id="comment-50154-info" class="comment-info"><span class="comment-age">(12 Feb '16, 07:42)</span> <span class="comment-user userinfo">yacare</span></div></div></div><div id="comment-tools-50153" class="comment-tools"></div><div class="clear"></div><div id="comment-50153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50147"></span>

<div id="answer-container-50147" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50147-score" class="post-score" title="current number of votes">1</div><span id="post-50147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You cannot show frame time alone (because <code>-T fields -e frame.time</code> overrides the <code>-O</code> values), but you can use <code>-O "tcp,frame"</code> and get the whole frame pseudo-header.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '16, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50147" class="comments-container"><span id="50151"></span><div id="comment-50151" class="comment"><div id="post-50151-score" class="comment-score"></div><div class="comment-text"><p>Thanks Sindy. That is what I saw. -T overrides -O. -O frame displays the entire frame pseudo header. Was wondering if any option to just print out the frame arrival time along with output specified with -O.</p></div><div id="comment-50151-info" class="comment-info"><span class="comment-age">(12 Feb '16, 07:26)</span> <span class="comment-user userinfo">yacare</span></div></div></div><div id="comment-tools-50147" class="comment-tools"></div><div class="clear"></div><div id="comment-50147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

