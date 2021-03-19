+++
type = "question"
title = "get most common sender of packets in a trace file"
description = '''I am trying to find out the host that has sent the most TCP packets in a trace file, regardless of destination. Is there a way to do that with Wireshark?'''
date = "2012-11-27T20:56:00Z"
lastmod = "2012-11-28T17:31:00Z"
weight = 16365
keywords = [ "filter", "ip", "tcp" ]
aliases = [ "/questions/16365" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [get most common sender of packets in a trace file](/questions/16365/get-most-common-sender-of-packets-in-a-trace-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16365-score" class="post-score" title="current number of votes">0</div><span id="post-16365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to find out the host that has sent the most TCP packets in a trace file, regardless of destination. Is there a way to do that with Wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '12, 20:56</strong></p><img src="https://secure.gravatar.com/avatar/1be285a38167733089ad79d28cf2d82e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user9909&#39;s gravatar image" /><p><span>user9909</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user9909 has no accepted answers">0%</span></p></div></div><div id="comments-container-16365" class="comments-container"></div><div id="comment-tools-16365" class="comment-tools"></div><div class="clear"></div><div id="comment-16365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16368"></span>

<div id="answer-container-16368" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16368-score" class="post-score" title="current number of votes">2</div><span id="post-16368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="user9909 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, there is:</p><ol><li>Set the display filter to "tcp" and click "apply"</li><li>Go to "Statistics -&gt; Endpoints"</li><li>Select "Limit to display filter"</li><li>Click on the "IPv4" tab</li><li>Click on "Tx Bytes" twice to sort reversely on transmitted bytes</li></ol><p>Then you may use "Copy" to export the results in CSV to the clipboard...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '12, 23:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-16368" class="comments-container"><span id="16385"></span><div id="comment-16385" class="comment"><div id="post-16385-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much! That's exactly what I needed</p></div><div id="comment-16385-info" class="comment-info"><span class="comment-age">(28 Nov '12, 06:04)</span> <span class="comment-user userinfo">user9909</span></div></div><span id="16397"></span><div id="comment-16397" class="comment"><div id="post-16397-score" class="comment-score"></div><div class="comment-text"><p>Is there a way to use the Endpoints IPv4 tab to display only the src ips instead of src + dest ips in the statistics?</p></div><div id="comment-16397-info" class="comment-info"><span class="comment-age">(28 Nov '12, 11:19)</span> <span class="comment-user userinfo">user9909</span></div></div><span id="16399"></span><div id="comment-16399" class="comment"><div id="post-16399-score" class="comment-score"></div><div class="comment-text"><p>That's not possible. Then you need to cook something up with tshark and some scripting. If you are just interested in the count of packets, you can use:</p><pre><code>tshark -r &lt;file&gt; -R tcp -T fields -e ip.src | sort | uniq -c</code></pre><p>If you want the top 10, you can add:</p><pre><code>... | sort -rn | head</code></pre><p>(if you're on windows, you can use powershell for similar commands or install cygwin to get a bash shell)</p></div><div id="comment-16399-info" class="comment-info"><span class="comment-age">(28 Nov '12, 11:44)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="16402"></span><div id="comment-16402" class="comment"><div id="post-16402-score" class="comment-score"></div><div class="comment-text"><p>The PowerShell equivalents would be:</p><p><code>tshark -r &lt;file&gt; -R tcp -T fields -e "ip.src" | Sort-Object -Unique | Measure-Object</code></p><p>and:</p><p><code>... | Group-Object | Sort-Object -Descending | Select-Object -First 10</code></p></div><div id="comment-16402-info" class="comment-info"><span class="comment-age">(28 Nov '12, 12:39)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="16409"></span><div id="comment-16409" class="comment"><div id="post-16409-score" class="comment-score"></div><div class="comment-text"><p>Fantastic, thanks guys</p></div><div id="comment-16409-info" class="comment-info"><span class="comment-age">(28 Nov '12, 17:31)</span> <span class="comment-user userinfo">user9909</span></div></div></div><div id="comment-tools-16368" class="comment-tools"></div><div class="clear"></div><div id="comment-16368-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

