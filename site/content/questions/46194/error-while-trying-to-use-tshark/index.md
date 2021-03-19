+++
type = "question"
title = "error while trying to use tshark"
description = '''Error FIT was expected in this contact Command I gave C:&#92;Program Files (x86)&#92;Wireshark&amp;gt;tshark -r C:&#92;Users&#92;Karnail.Home-Notebook&#92;Documents&#92;MS - FIT&#92;CYB5675&#92;Week 3&#92;datasets&#92;lbl-internal.20050106-1323.port025.dump.anon -R frame.sequence eq &#92;&quot;tcp.flags.syn==1 &amp;amp;&amp;amp; tcp.flags.ack==0&quot;  What Am I t...'''
date = "2015-09-27T06:52:00Z"
lastmod = "2015-09-27T11:20:00Z"
weight = 46194
keywords = [ "tshark" ]
aliases = [ "/questions/46194" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [error while trying to use tshark](/questions/46194/error-while-trying-to-use-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46194-score" class="post-score" title="current number of votes">0</div><span id="post-46194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Error FIT was expected in this contact Command I gave</p><pre><code>C:\Program Files (x86)\Wireshark&gt;tshark -r C:\Users\Karnail.Home-Notebook\Documents\MS - FIT\CYB5675\Week 3\datasets\lbl-internal.20050106-1323.port025.dump.anon -R frame.sequence eq \&quot;tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0&quot;</code></pre><p>What Am I trying to do? I want to list all the packets from a PCAP file where syn=1 and ack=0 i.e. half open port scan.</p><p>Error I get is Error FIT was expected in this contact</p><p>Please help me resolve it.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '15, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/8bf0038eaf08659c0440e844f5e81369?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karnails&#39;s gravatar image" /><p><span>karnails</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karnails has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Sep '15, 10:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-46194" class="comments-container"></div><div id="comment-tools-46194" class="comment-tools"></div><div class="clear"></div><div id="comment-46194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46196"></span>

<div id="answer-container-46196" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46196-score" class="post-score" title="current number of votes">1</div><span id="post-46196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="karnails has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'll need to fix your quoting because the file path has spaces, and then your read filter is incorrect. Try this:</p><p><code>tshark -r "C:\Users\Karnail.Home-Notebook\Documents\MS - FIT\CYB5675\Week 3\datasets\lbl-internal.20050106-1323.port025.dump.anon" -Y "tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0"</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '15, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-46196" class="comments-container"><span id="46197"></span><div id="comment-46197" class="comment"><div id="post-46197-score" class="comment-score"></div><div class="comment-text"><p>Thanks How do I output of the command above (one that you fixed) to a file, say csv?</p></div><div id="comment-46197-info" class="comment-info"><span class="comment-age">(27 Sep '15, 11:02)</span> <span class="comment-user userinfo">karnails</span></div></div><span id="46198"></span><div id="comment-46198" class="comment"><div id="post-46198-score" class="comment-score"></div><div class="comment-text"><p>To redirect to a file, just use normal shell redirection, e.g. <code>&gt; myfile.txt</code>.</p><p>To make a csv, look at the <code>-T fields -e field.name1 -e field.name2 ...</code> options, along with <code>"-E separator=,"</code>, e.g. to display the frame number, ip.source and ip.destination use:</p><p><code>... -T fields -e frame.number -e ip.src -e ip.dst -E "separator=," &gt; myfile.csv</code></p><p>Field names can be found in Wireshark by selecting the field of interest in the packet details tree and looking at the field name in the status bar.</p><p>You can see the options on the tshark man <a href="https://www.wireshark.org/docs/man-pages/tshark.html">page</a>.</p></div><div id="comment-46198-info" class="comment-info"><span class="comment-age">(27 Sep '15, 11:20)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-46196" class="comment-tools"></div><div class="clear"></div><div id="comment-46196-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

