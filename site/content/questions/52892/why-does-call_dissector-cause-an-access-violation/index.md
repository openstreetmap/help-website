+++
type = "question"
title = "Why does call_dissector() cause an Access Violation?"
description = '''In my c++ project,use call_dissector() to decode the s1ap data, in most time, it works fine. but if the s1ap contains NAS info, the exception &quot;Access Violation&quot; occurs. code: epan_dissect_t *edtt....(initials) dissector_handle_t handle = find_dissector(&quot;s1ap&quot;); call_dissector(handle, edtt-&amp;gt;tvb, &amp;...'''
date = "2016-05-24T20:05:00Z"
lastmod = "2016-05-26T17:38:00Z"
weight = 52892
keywords = [ "lte" ]
aliases = [ "/questions/52892" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why does call\_dissector() cause an Access Violation?](/questions/52892/why-does-call_dissector-cause-an-access-violation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52892-score" class="post-score" title="current number of votes">0</div><span id="post-52892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In my c++ project,use call_dissector() to decode the s1ap data, in most time, it works fine. but if the s1ap contains NAS info, the exception "Access Violation" occurs. code:</p><pre><code>epan_dissect_t *edtt....(initials)
dissector_handle_t handle = find_dissector(&quot;s1ap&quot;);
call_dissector(handle, edtt-&gt;tvb, &amp;edtt-&gt;pi, edtt-&gt;tree);</code></pre><p>the sample s1ap data(hex)</p><pre><code>000b405c00000300000005c0065077e100080003400260001a00454427478345a50607623b09013801010891683108200545f2002b6013a1015618939153768974f200084170902171242314050003d90202006b00610064006500610049006f</code></pre><p>Anyone can help me? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lte" rel="tag" title="see questions tagged &#39;lte&#39;">lte</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '16, 20:05</strong></p><img src="https://secure.gravatar.com/avatar/817e70fd454be6f59a1b0ab5e2d03d3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="garport&#39;s gravatar image" /><p><span>garport</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="garport has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 May '16, 02:47</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-52892" class="comments-container"><span id="52900"></span><div id="comment-52900" class="comment"><div id="post-52900-score" class="comment-score"></div><div class="comment-text"><p>It would be helpful if you were indicating us which Wireshark version you are using, and if the S1AP PDU was complete (when I try to decode the one posted above it appears to be truncated: the ASN.1 PER string indicates that the NAS PDU should be 68 bytes long but only 4 bytes are present).</p></div><div id="comment-52900-info" class="comment-info"><span class="comment-age">(25 May '16, 02:45)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="52938"></span><div id="comment-52938" class="comment"><div id="post-52938-score" class="comment-score"></div><div class="comment-text"><p>version: Wireshark 2.0.2 64bit Sorry about the sample data: two '0x' mixed in The sample data is only the s1ap pdu message and NOT include any headers. Thanks for help.</p></div><div id="comment-52938-info" class="comment-info"><span class="comment-age">(25 May '16, 17:55)</span> <span class="comment-user userinfo">garport</span></div></div><span id="52949"></span><div id="comment-52949" class="comment"><div id="post-52949-score" class="comment-score"></div><div class="comment-text"><p>When you say "my c++ project" do you mean a C++ addition to Wireshark, or an external project using libwireshark?</p></div><div id="comment-52949-info" class="comment-info"><span class="comment-age">(26 May '16, 02:35)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="52978"></span><div id="comment-52978" class="comment"><div id="post-52978-score" class="comment-score"></div><div class="comment-text"><p>an external project using libwireshark</p></div><div id="comment-52978-info" class="comment-info"><span class="comment-age">(26 May '16, 17:38)</span> <span class="comment-user userinfo">garport</span></div></div></div><div id="comment-tools-52892" class="comment-tools"></div><div class="clear"></div><div id="comment-52892-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52953"></span>

<div id="answer-container-52953" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52953-score" class="post-score" title="current number of votes">0</div><span id="post-52953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Decoding this PDU with standard Wireshark 2.0.2 64 bits on Windows does not trigger any exception.</p><p>As you seem to call libwireshark from your own source code, the best way to move forward is probably to investigate this yourself with a debugger. The Windows debugging symbols (assuming you are using Windows) can be found <a href="https://www.wireshark.org/download/win64/all-versions/">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '16, 04:37</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-52953" class="comments-container"></div><div id="comment-tools-52953" class="comment-tools"></div><div class="clear"></div><div id="comment-52953-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

