+++
type = "question"
title = "Live captures do not support two-pass analysis"
description = '''I&#x27;m using this command: tshark -i wlan0 -I &#92;  -o wlan.enable_decryption:TRUE &#92;  -2 -R &quot;ip and !ip.src == 192.168.0.0/24&quot; &#92;  -T fields -e wlan.ra -e ip.src -e ip.len  Where &quot;and&quot; is actually &quot;&amp;amp;&amp;amp;&quot;. This works with tshark v. 1.10, but v. 1.15 says: Live captures do not support two-pass analysis...'''
date = "2015-04-22T00:50:00Z"
lastmod = "2015-04-22T06:53:00Z"
weight = 41658
keywords = [ "capture-filter", "tshark", "display-filter" ]
aliases = [ "/questions/41658" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Live captures do not support two-pass analysis](/questions/41658/live-captures-do-not-support-two-pass-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41658-score" class="post-score" title="current number of votes">0</div><span id="post-41658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using this command:</p><pre><code>tshark -i wlan0 -I \
        -o wlan.enable_decryption:TRUE \
        -2 -R &quot;ip and !ip.src == 192.168.0.0/24&quot; \
        -T fields -e wlan.ra -e ip.src -e ip.len</code></pre><p>Where "and" is actually "&amp;&amp;". This works with tshark v. 1.10, but v. 1.15 says:</p><pre><code>Live captures do not support two-pass analysis</code></pre><p>So I started to try ostensibly equivalent capture filters, but failed right away -- the <code>ip.src</code> and <code>ip.len</code> fields aren't shown even with just plain <code>-f ip</code>.</p><p>How can I get this functionality of v. 1.10 in the newer 1.15?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '15, 00:50</strong></p><img src="https://secure.gravatar.com/avatar/abf01b6006996f947014ff671ba4151b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mk27&#39;s gravatar image" /><p><span>mk27</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mk27 has no accepted answers">0%</span></p></div></div><div id="comments-container-41658" class="comments-container"><span id="41661"></span><div id="comment-41661" class="comment"><div id="post-41661-score" class="comment-score"></div><div class="comment-text"><p>1.15? Where did you get that version from?</p></div><div id="comment-41661-info" class="comment-info"><span class="comment-age">(22 Apr '15, 01:59)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-41658" class="comment-tools"></div><div class="clear"></div><div id="comment-41658-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41666"></span>

<div id="answer-container-41666" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41666-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41666-score" class="post-score" title="current number of votes">1</div><span id="post-41666-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mk27 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Why the desire for two-pass analysis anyway? Dissecting IP and the IP sources address does not need it, neither does the IP length. So I would suggest skipping the '-2' parameter and check your results.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '15, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-41666" class="comments-container"><span id="41683"></span><div id="comment-41683" class="comment"><div id="post-41683-score" class="comment-score"></div><div class="comment-text"><p><code>tshark: -R without -2 is deprecated</code> ...I had thought it plain would not work earlier, so I guess that is fine.</p></div><div id="comment-41683-info" class="comment-info"><span class="comment-age">(22 Apr '15, 06:37)</span> <span class="comment-user userinfo">mk27</span></div></div><span id="41684"></span><div id="comment-41684" class="comment"><div id="post-41684-score" class="comment-score"></div><div class="comment-text"><p>And <code>-Y</code> works. Perhaps I was using a different filter earlier and it did not but I cannot reproduce that now. Sorry for the confusion!</p></div><div id="comment-41684-info" class="comment-info"><span class="comment-age">(22 Apr '15, 06:53)</span> <span class="comment-user userinfo">mk27</span></div></div></div><div id="comment-tools-41666" class="comment-tools"></div><div class="clear"></div><div id="comment-41666-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

