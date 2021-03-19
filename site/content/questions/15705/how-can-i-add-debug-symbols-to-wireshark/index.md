+++
type = "question"
title = "How can i add debug symbols to wireshark?"
description = '''I am debugging wireshark using gdb. How can i add debug symbols to wireshark?'''
date = "2012-11-08T04:14:00Z"
lastmod = "2012-11-12T00:28:00Z"
weight = 15705
keywords = [ "gdb" ]
aliases = [ "/questions/15705" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can i add debug symbols to wireshark?](/questions/15705/how-can-i-add-debug-symbols-to-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15705-score" class="post-score" title="current number of votes">0</div><span id="post-15705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am debugging wireshark using gdb. How can i add debug symbols to wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gdb" rel="tag" title="see questions tagged &#39;gdb&#39;">gdb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '12, 04:14</strong></p><img src="https://secure.gravatar.com/avatar/b0ed262c234b0aa9fae2e5b2d51b14c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Akhil&#39;s gravatar image" /><p><span>Akhil</span><br />
<span class="score" title="53 reputation points">53</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Akhil has no accepted answers">0%</span></p></div></div><div id="comments-container-15705" class="comments-container"></div><div id="comment-tools-15705" class="comment-tools"></div><div class="clear"></div><div id="comment-15705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15788"></span>

<div id="answer-container-15788" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15788-score" class="post-score" title="current number of votes">0</div><span id="post-15788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Akhil has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As you would do with any other program, by adding option '-g' to the gcc compiler.</p><blockquote><p><code>gcc -g</code><br />
</p></blockquote><p>However, you don't have to care about that, as the standard build process will add '-g' to the CFLAGS variable and thus your compiled binary will have debug symbols, unless you change the build process.</p><p>You can check if there are debug symbols with the following command:</p><blockquote><p><code>nm --debug-syms wireshark/.libs/wireshark</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '12, 03:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Nov '12, 03:56</strong> </span></p></div></div><div id="comments-container-15788" class="comments-container"><span id="15791"></span><div id="comment-15791" class="comment"><div id="post-15791-score" class="comment-score"></div><div class="comment-text"><p>The <code>nm</code> command will work only if the <code>nm</code> on the system is the GNU binutils version of <code>nm</code> or a compatible version; not all versions of <code>nm</code> support the <code>--debug-syms</code> option.</p></div><div id="comment-15791-info" class="comment-info"><span class="comment-age">(10 Nov '12, 17:20)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="15810"></span><div id="comment-15810" class="comment"><div id="post-15810-score" class="comment-score"></div><div class="comment-text"><p>The output of the command nm --debug-syms wireshark/.libs/wireshark is as follows:</p><pre><code>00000000005206a0 T pcap_findalldevs
000000000052f360 T pcap_fopen_offline
0000000000530430 T pcap_free
0000000000520df0 T pcap_free_datalinks
0000000000521980 T pcap_freealldevs
0000000000522600 T pcap_freecode
0000000000530400 T pcap_get_debug
0000000000520c30 T pcap_get_selectable_fd</code></pre><p>What does that mean: debug symbols present or not?</p></div><div id="comment-15810-info" class="comment-info"><span class="comment-age">(11 Nov '12, 20:04)</span> <span class="comment-user userinfo">Akhil</span></div></div><span id="15812"></span><div id="comment-15812" class="comment"><div id="post-15812-score" class="comment-score"></div><div class="comment-text"><p>debug symbols present</p></div><div id="comment-15812-info" class="comment-info"><span class="comment-age">(11 Nov '12, 22:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="15813"></span><div id="comment-15813" class="comment"><div id="post-15813-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt</p></div><div id="comment-15813-info" class="comment-info"><span class="comment-age">(12 Nov '12, 00:28)</span> <span class="comment-user userinfo">Akhil</span></div></div></div><div id="comment-tools-15788" class="comment-tools"></div><div class="clear"></div><div id="comment-15788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

