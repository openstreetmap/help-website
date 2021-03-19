+++
type = "question"
title = "How to write a dissector for a protocol that runs on top of TCP?"
description = '''void proto_reg_handoff_foo(void) {  static dissector_handle_t foo_handle;   foo_handle = create_dissector_handle(dissect_foo, proto_foo);  dissector_add_uint(&quot;udp.port&quot;, FOO_PORT, foo_handle); }  Here, shall i change &quot;udp.port&quot; as &quot;tcp.port&quot; for my tcp based application layer protocol dissector?'''
date = "2011-11-11T17:27:00Z"
lastmod = "2011-11-12T14:44:00Z"
weight = 7388
keywords = [ "development", "dissector" ]
aliases = [ "/questions/7388" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to write a dissector for a protocol that runs on top of TCP?](/questions/7388/how-to-write-a-dissector-for-a-protocol-that-runs-on-top-of-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7388-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7388-score" class="post-score" title="current number of votes">0</div><span id="post-7388-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>void
proto_reg_handoff_foo(void)
{
    static dissector_handle_t foo_handle;

    foo_handle = create_dissector_handle(dissect_foo, proto_foo);
    dissector_add_uint(&quot;udp.port&quot;, FOO_PORT, foo_handle);
}</code></pre><p>Here, shall i change "udp.port" as "tcp.port" for my tcp based application layer protocol dissector?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '11, 17:27</strong></p><img src="https://secure.gravatar.com/avatar/01febacc45af8ecf743c4f575d428326?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JK7&#39;s gravatar image" /><p><span>JK7</span><br />
<span class="score" title="31 reputation points">31</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JK7 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Nov '11, 13:29</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-7388" class="comments-container"></div><div id="comment-tools-7388" class="comment-tools"></div><div class="clear"></div><div id="comment-7388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7392"></span>

<div id="answer-container-7392" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7392-score" class="post-score" title="current number of votes">0</div><span id="post-7392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, that should be all that's required.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '11, 00:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-7392" class="comments-container"></div><div id="comment-tools-7392" class="comment-tools"></div><div class="clear"></div><div id="comment-7392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7397"></span>

<div id="answer-container-7397" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7397-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7397-score" class="post-score" title="current number of votes">0</div><span id="post-7397-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>UDP is a packet-oriented protocol, so packets for a protocol running atop UDP usually have a one-to-one correspondence with UDP packets.</p><p>TCP is a byte-stream oriented protocol, so packets for a protocol running atop TCP have to put their own packet boundaries into the byte stream, with, for example, a packet size field.</p><p>Dissectors for protocols running atop TCP just get handed TCP segment data, with no guarantee that they're being handed exactly one packet or that they're being handed all of the data in a packet. The dissector would have to handle that itself.</p><p>Depending on how your protocol does that, you might, for example, be able to use <code>tcp_dissect_pdus()</code> to do all the work. How does your protocol divide the byte stream into packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '11, 13:27</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7397" class="comments-container"><span id="7398"></span><div id="comment-7398" class="comment"><div id="post-7398-score" class="comment-score"></div><div class="comment-text"><p>I think the OP is asking the question as the Developers Guide shows the "FOO" dissector as running atop UDP as per the example the OP has posted.</p><p>Your points are all worth noting though.</p></div><div id="comment-7398-info" class="comment-info"><span class="comment-age">(12 Nov '11, 14:44)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-7397" class="comment-tools"></div><div class="clear"></div><div id="comment-7397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

