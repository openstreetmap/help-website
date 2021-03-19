+++
type = "question"
title = "Filter udp frame by bit instead of byte"
description = '''We have built a custom dissector for udp, and would like to be able to filter on specific bits rather than bytes. Is this possible? I believe it may be a combination of frame slicing and bitmask and, but have been unsuccessful so far. '''
date = "2014-08-19T14:39:00Z"
lastmod = "2014-08-27T17:00:00Z"
weight = 35598
keywords = [ "filter", "frame", "dissector", "bit" ]
aliases = [ "/questions/35598" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Filter udp frame by bit instead of byte](/questions/35598/filter-udp-frame-by-bit-instead-of-byte)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35598-score" class="post-score" title="current number of votes">0</div><span id="post-35598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have built a custom dissector for udp, and would like to be able to filter on specific bits rather than bytes. Is this possible? I believe it may be a combination of frame slicing and bitmask and, but have been unsuccessful so far.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-frame" rel="tag" title="see questions tagged &#39;frame&#39;">frame</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-bit" rel="tag" title="see questions tagged &#39;bit&#39;">bit</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '14, 14:39</strong></p><img src="https://secure.gravatar.com/avatar/40aae7ab1a30c4c2d4bbece83599857a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hls&#39;s gravatar image" /><p><span>hls</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hls has one accepted answer">100%</span></p></div></div><div id="comments-container-35598" class="comments-container"></div><div id="comment-tools-35598" class="comment-tools"></div><div class="clear"></div><div id="comment-35598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35779"></span>

<div id="answer-container-35779" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35779-score" class="post-score" title="current number of votes">2</div><span id="post-35779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hls has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, this is possible, but whether by design or mistake, it's certainly not always intuitive. As you mentioned, you would use a combination of frame slicing and bitmask operators.</p><p>For example, if you wanted to test if the least significant bit of the first UDP byte was set, you could use: <code>     udp[0] &amp; 1</code></p><p>If you wanted to test if the least significant bit was set and the most significant bit was set, you could NOT use this though: <code>     udp[0] &amp; 81</code></p><p>The reason you can't use that is because it will match packets where <em>either</em> the most signifcant bit is set or the least significant bit is set, but not necessarily packets where both bits are set. In order to test that both bits are set, the intuitive way would be to use something like follows, which unfortunately you can't do because Wireshark's display filter syntax apparently doesn't support this: <code>     (udp[0] &amp; 81) == 81</code></p><p>Therefore, the way to accomplish this is to test each bit individually using something like so: <code>     (udp[0] &amp; 80) &amp;&amp; (udp[0] &amp; 1)</code></p><p>And if you wanted to test if a bit is <strong>NOT</strong> set, then you can use the <code>!</code> operator. For example, to test that the most significant bit is set and the least significant bit is not set, use: <code>     (udp[0] &amp; 80) &amp;&amp; !(udp[0] &amp; 1)</code></p><p>This can be a pain to write if you have a lot of bits to test, but at least you can save your filter and avoid having to retype this every time. A <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChDisplayFilterMacrosSection.html">display filter macro</a> might also be useful here as well.</p><p>See also the <strong>Bit field operations</strong> section of the <a href="https://www.wireshark.org/docs/man-pages/wireshark-filter.html">Wireshark filter syntax and reference</a> page.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '14, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Aug '14, 07:42</strong> </span></p></div></div><div id="comments-container-35779" class="comments-container"><span id="35823"></span><div id="comment-35823" class="comment"><div id="post-35823-score" class="comment-score"></div><div class="comment-text"><p>Thank you! This seems to be working, even though it could be a slight pain, it's better than nothing! Thanks again</p></div><div id="comment-35823-info" class="comment-info"><span class="comment-age">(27 Aug '14, 17:00)</span> <span class="comment-user userinfo">hls</span></div></div></div><div id="comment-tools-35779" class="comment-tools"></div><div class="clear"></div><div id="comment-35779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

