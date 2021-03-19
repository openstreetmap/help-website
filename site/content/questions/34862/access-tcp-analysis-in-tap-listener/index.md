+++
type = "question"
title = "Access TCP analysis in tap listener"
description = '''I am trying to write a tap for TCP with access to Wireshark&#x27;s analysis (such as which frame the current packet is acknowledging. It seems relatively straight forward to do this in Lua with something like: acksframe = Field.new(&quot;tcp.analysis.acks_frame&quot;) ack = acksframe()  However I have not worked o...'''
date = "2014-07-23T16:29:00Z"
lastmod = "2014-07-27T16:58:00Z"
weight = 34862
keywords = [ "c", "tap", "c++" ]
aliases = [ "/questions/34862" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Access TCP analysis in tap listener](/questions/34862/access-tcp-analysis-in-tap-listener)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34862-score" class="post-score" title="current number of votes">0</div><span id="post-34862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to write a tap for TCP with access to Wireshark's analysis (such as which frame the current packet is acknowledging.</p><p>It seems relatively straight forward to do this in Lua with something like:</p><pre><code>acksframe = Field.new(&quot;tcp.analysis.acks_frame&quot;)
ack = acksframe()</code></pre><p>However I have not worked out how to do this in a tap written in C/C++.</p><p>From what I understand, I have access to the following information in a TCP tap:</p><ul><li><code>packet_info</code>: generic packet information</li><li><code>epan_dissect</code>: overall structure of the packet (layers and pointers to corresponding data)</li><li><code>tcpheader</code>: the fields of the TCP header</li></ul><p>None of these seems to have the TCP analysis information available in the Lua tap. <code>tcpheader</code> contains the basics such as <code>seq</code> and <code>ack</code> fields, however I am hoping to leverage Wireshark's analysis rather than trying to re-implement this myself.</p><p>How can I access Wireshark's TCP analysis from a tap listener written in C?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-c" rel="tag" title="see questions tagged &#39;c&#39;">c</span> <span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span> <span class="post-tag tag-link-c++" rel="tag" title="see questions tagged &#39;c++&#39;">c++</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jul '14, 16:29</strong></p><img src="https://secure.gravatar.com/avatar/6c2d45fd9e805840e1637c06976cc3d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wainwright&#39;s gravatar image" /><p><span>wainwright</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wainwright has no accepted answers">0%</span></p></div></div><div id="comments-container-34862" class="comments-container"></div><div id="comment-tools-34862" class="comment-tools"></div><div class="clear"></div><div id="comment-34862-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34934"></span>

<div id="answer-container-34934" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34934-score" class="post-score" title="current number of votes">0</div><span id="post-34934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In order to access these fields you must ask for them by creating a tap filter when calling <code>register_tap_listener</code>.</p><p>For example, to ask for <code>tcp.analysis.acks_frame</code>, you would set up a filter such as:</p><p><code>"frame || tcp.analysis.acks_frame"</code></p><p>which you would pass as the 3rd argument to <code>register_tap_listener</code>.</p><p>If the tap is registered with the filter, the data can be found in the protocol tree provided in the <code>epan_dissect_t</code> pointer passed as the 3rd argument to your packet callback.</p><p>Note that this requires you to have a filter (performance hit) even if you are willing to receive all packets. There may be a better way where you can request that those fields are filled, without having to filter packets, but I am not aware of it.</p></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '14, 16:58</strong></p><img src="https://secure.gravatar.com/avatar/6c2d45fd9e805840e1637c06976cc3d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wainwright&#39;s gravatar image" /><p><span>wainwright</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wainwright has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jul '14, 17:04</strong> </span></p></div></div><div id="comments-container-34934" class="comments-container"></div><div id="comment-tools-34934" class="comment-tools"></div><div class="clear"></div><div id="comment-34934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

