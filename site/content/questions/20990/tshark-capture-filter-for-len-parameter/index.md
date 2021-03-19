+++
type = "question"
title = "tshark capture filter for len parameter"
description = '''How do I set a capture filter in tshark so that only packets with len &amp;gt; 0 would be registered? I tried using greater and less commands but it didn&#x27;t work.'''
date = "2013-05-06T12:00:00Z"
lastmod = "2013-05-06T15:53:00Z"
weight = 20990
keywords = [ "filter", "capture", "tshark" ]
aliases = [ "/questions/20990" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [tshark capture filter for len parameter](/questions/20990/tshark-capture-filter-for-len-parameter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20990-score" class="post-score" title="current number of votes">0</div><span id="post-20990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I set a capture filter in tshark so that only packets with len &gt; 0 would be registered? I tried using greater and less commands but it didn't work.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '13, 12:00</strong></p><img src="https://secure.gravatar.com/avatar/61fe69c7740ccae4bdce2448e31c2f48?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Loco1989&#39;s gravatar image" /><p><span>Loco1989</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Loco1989 has no accepted answers">0%</span></p></div></div><div id="comments-container-20990" class="comments-container"></div><div id="comment-tools-20990" class="comment-tools"></div><div class="clear"></div><div id="comment-20990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20993"></span>

<div id="answer-container-20993" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20993-score" class="post-score" title="current number of votes">1</div><span id="post-20993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Loco1989 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From your comment on <span>@joemc</span>'s answer it turns out you mean the length of the TCP payload. In a display filter this is available as "tcp.len==0", so if you don't want to see TCP frames with no payload, then you can use "tcp.len&gt;0"</p><p>But you are looking for a capture filter, this is a little more complicated. This is because there is no field in the TCP header for the payload length. There is only a field for the length of the TCP header. However, in the IP header, there is a field "total length", which includes the length of the IP header and the IP payload (which is off course the sum of TCP header length and TCP payload length).</p><p>In short "IP total length = IP header length + TCP header length + TCP payload length" which results in:</p><pre><code>TCP payload length = IP total length - IP header length - TCP header length</code></pre><p>Now we need to create capture filters for each part:</p><pre><code>IP total length ==&gt; ip[2:2]
IP header length ==&gt; (ip[0]&amp;0x0f) &lt;&lt; 2
TCP header length ==&gt; (tcp[12]&amp;0xf0) &gt;&gt; 2</code></pre><p>Resulting in a capture filter of:</p><pre><code>ip[2:2] - ((ip[0]&amp;0x0f) &lt;&lt; 2) - ((tcp[12]&amp;0xf0) &gt;&gt; 2) &gt; 0</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '13, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20993" class="comments-container"><span id="20994"></span><div id="comment-20994" class="comment"><div id="post-20994-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much, it works exactly like it should! I would never come up with it myself... I'm not familiar with these commands for getting particular lengths but after your explanation at least I know in general what's going on and why. You helped me a lot, thanks again :)</p></div><div id="comment-20994-info" class="comment-info"><span class="comment-age">(06 May '13, 15:53)</span> <span class="comment-user userinfo">Loco1989</span></div></div></div><div id="comment-tools-20993" class="comment-tools"></div><div class="clear"></div><div id="comment-20993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20991"></span>

<div id="answer-container-20991" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20991-score" class="post-score" title="current number of votes">0</div><span id="post-20991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What length are you talking about? You can't have a 0 length frame. You can use tshark -R "frame.len &gt; 256" to target specific frames, greater than 256 in this example. But "frame.len &gt; 0" is the same as capturing everything. Are you talking about a different protocol layer?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '13, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/9681c8a3b1c4620c300ab9e3fdce439b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joemc&#39;s gravatar image" /><p><span>joemc</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joemc has no accepted answers">0%</span></p></div></div><div id="comments-container-20991" class="comments-container"><span id="20992"></span><div id="comment-20992" class="comment"><div id="post-20992-score" class="comment-score"></div><div class="comment-text"><p>I'm not really sure myself, sorry I'm such a beginner here... Well, when I use the regular Wireshark GUI there is that column called 'Info', and there are displayed some kind of parameters like Seq, Ack, Win, Len. Some of the captured packets are described with Len = 0. I want to filter out these packets.</p></div><div id="comment-20992-info" class="comment-info"><span class="comment-age">(06 May '13, 13:54)</span> <span class="comment-user userinfo">Loco1989</span></div></div></div><div id="comment-tools-20991" class="comment-tools"></div><div class="clear"></div><div id="comment-20991-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

