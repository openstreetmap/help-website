+++
type = "question"
title = "Memory Leak in 1.6.8?"
description = '''I am performing an SNA trace (capture filter is &quot;not ip &amp;amp;&amp;amp; not arp &amp;amp;&amp;amp; not ether proto 0x8805 &amp;amp;&amp;amp; not ether proto 0x8806 &amp;amp;&amp;amp; not ether proto 0x0800&quot;). I am collecting about 10 packets per minute; the last trace file was ~32KB -- small capture data! Running on Win XP SP3 ...'''
date = "2012-05-25T15:21:00Z"
lastmod = "2012-05-29T06:57:00Z"
weight = 11359
keywords = [ "windows", "leak", "wireshark", "memory" ]
aliases = [ "/questions/11359" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Memory Leak in 1.6.8?](/questions/11359/memory-leak-in-168)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11359-score" class="post-score" title="current number of votes">0</div><span id="post-11359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am performing an SNA trace (capture filter is "not ip &amp;&amp; not arp &amp;&amp; not ether proto 0x8805 &amp;&amp; not ether proto 0x8806 &amp;&amp; not ether proto 0x0800"). I am collecting about 10 packets per minute; the last trace file was ~32KB -- small capture data!</p><p>Running on Win XP SP3 with latest patches. 1GB RAM, P4 2.66 CPU.</p><p>I am seeing the wireshark.exe's allocated memory rising at about 2MB / 10 seconds until the process crashes at around 1GB. I can see the system allocated memory graph climb up steadily until the crash every time.</p><p>I am trying 1.4 now to see if it has the same problem.</p><p>Is there anything I can collect for you to help you find the leak?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-leak" rel="tag" title="see questions tagged &#39;leak&#39;">leak</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '12, 15:21</strong></p><img src="https://secure.gravatar.com/avatar/63a64748d33d55a231a98e2988eaf238?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BobbyW&#39;s gravatar image" /><p><span>BobbyW</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BobbyW has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 May '12, 15:22</strong> </span></p></div></div><div id="comments-container-11359" class="comments-container"><span id="11364"></span><div id="comment-11364" class="comment"><div id="post-11364-score" class="comment-score"></div><div class="comment-text"><p>Running the same trace / filter on 1.4.13, it has been sitting at 60MB allocated for 30 minutes now ... I think 1.6.8 definitely has a leak.</p></div><div id="comment-11364-info" class="comment-info"><span class="comment-age">(25 May '12, 16:31)</span> <span class="comment-user userinfo">BobbyW</span></div></div></div><div id="comment-tools-11359" class="comment-tools"></div><div class="clear"></div><div id="comment-11359-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11415"></span>

<div id="answer-container-11415" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11415-score" class="post-score" title="current number of votes">2</div><span id="post-11415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><em>Is there anything I can collect for you to help you find the leak?</em></p><p>I would suggest collecting as many packets as you can using the same capture filter as you did previously, namely, "<code>not ip &amp;&amp; not arp &amp;&amp; not ether proto 0x8805 &amp;&amp; not ether proto 0x8806 &amp;&amp; not ether proto 0x0800</code>", but stop capturing shortly before you run out of memory. Then save the resulting packets to a capture file, open a <a href="https://bugs.wireshark.org/bugzilla/">bug report</a>, and attach the capture file to it so someone can use it to help analyze what's going on and hopefully provide a fix, if possible.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '12, 18:12</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-11415" class="comments-container"><span id="11442"></span><div id="comment-11442" class="comment"><div id="post-11442-score" class="comment-score">1</div><div class="comment-text"><p>Even if Wireshark does crash, the temporary should still be around; you could use that to attach to a bug report. See the <a href="http://www.wireshark.org/faq.html#q7.12">Q7.12</a> in the FAQ.</p></div><div id="comment-11442-info" class="comment-info"><span class="comment-age">(29 May '12, 06:57)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-11415" class="comment-tools"></div><div class="clear"></div><div id="comment-11415-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

