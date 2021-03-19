+++
type = "question"
title = "packet count"
description = '''How to count the number of &quot;syn&quot;, &quot;syn+ack&quot;, and &quot;ack&quot; packets transferred in each second for some hours. I need to build a time series on that. Thanks in advance Varun'''
date = "2014-06-11T03:08:00Z"
lastmod = "2014-06-14T05:35:00Z"
weight = 33638
keywords = [ "sniffing", "packet-capture", "tcpdump", "tcp" ]
aliases = [ "/questions/33638" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [packet count](/questions/33638/packet-count)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33638-score" class="post-score" title="current number of votes">0</div><span id="post-33638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to count the number of "syn", "syn+ack", and "ack" packets transferred in each second for some hours. I need to build a time series on that. Thanks in advance</p><p>Varun</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sniffing" rel="tag" title="see questions tagged &#39;sniffing&#39;">sniffing</span> <span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '14, 03:08</strong></p><img src="https://secure.gravatar.com/avatar/85b097036fe5cccc1c8e21fe3da3c781?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Varun%20Tharol&#39;s gravatar image" /><p><span>Varun Tharol</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Varun Tharol has no accepted answers">0%</span></p></div></div><div id="comments-container-33638" class="comments-container"><span id="33639"></span><div id="comment-33639" class="comment"><div id="post-33639-score" class="comment-score"></div><div class="comment-text"><p>do you mean "all ACK packets" or just the ones that are part of a TCP handshake?</p></div><div id="comment-33639-info" class="comment-info"><span class="comment-age">(11 Jun '14, 03:18)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="33687"></span><div id="comment-33687" class="comment"><div id="post-33687-score" class="comment-score"></div><div class="comment-text"><p>The ones that are part of a TCP handshake.</p></div><div id="comment-33687-info" class="comment-info"><span class="comment-age">(12 Jun '14, 01:21)</span> <span class="comment-user userinfo">Varun Tharol</span></div></div></div><div id="comment-tools-33638" class="comment-tools"></div><div class="clear"></div><div id="comment-33638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33658"></span>

<div id="answer-container-33658" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33658-score" class="post-score" title="current number of votes">1</div><span id="post-33658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Varun Tharol has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the IO graph for that</p><blockquote><p>Statistics -&gt; IO Graph</p></blockquote><p>Then use the following filters</p><p><strong>Graph1:</strong> <code>tcp.flags eq 0x02</code> (SYN)<br />
<strong>Graph2:</strong> <code>tcp.flags eq 0x12</code> (SYN-ACK)<br />
<strong>Graph3:</strong> <code>tcp.flags.ack eq 1 and tcp.seq eq 1 and tcp.ack eq 1 and tcp.len eq 0</code> (ACK)</p><p>The last filter is a bit long (maybe there is a better one) and it will only work if you have enabled relative sequence numbers for the TCP protocol (default setting in Wireshark).</p><p>Let Wireshark draw the graphs (X-Axis tick interval 1 second) and then click on the 'Copy' button. This will copy the values for the three graphs into the clipboard from where you can copy it to a spreadsheet or an editor.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '14, 10:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-33658" class="comments-container"><span id="33686"></span><div id="comment-33686" class="comment"><div id="post-33686-score" class="comment-score"></div><div class="comment-text"><p>It works. Thank you very much brother.</p></div><div id="comment-33686-info" class="comment-info"><span class="comment-age">(12 Jun '14, 01:17)</span> <span class="comment-user userinfo">Varun Tharol</span></div></div><span id="33698"></span><div id="comment-33698" class="comment"><div id="post-33698-score" class="comment-score"></div><div class="comment-text"><p>good!</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-33698-info" class="comment-info"><span class="comment-age">(12 Jun '14, 04:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="33800"></span><div id="comment-33800" class="comment"><div id="post-33800-score" class="comment-score"></div><div class="comment-text"><p>Sure.......</p></div><div id="comment-33800-info" class="comment-info"><span class="comment-age">(14 Jun '14, 05:35)</span> <span class="comment-user userinfo">Varun Tharol</span></div></div></div><div id="comment-tools-33658" class="comment-tools"></div><div class="clear"></div><div id="comment-33658-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

