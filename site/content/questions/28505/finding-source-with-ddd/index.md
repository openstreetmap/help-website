+++
type = "question"
title = "Finding source with DDD"
description = '''I&#x27;ve build wireshark, and can start it up using ddd using the recommended method through libtool &quot;libtool --mode=execute ddd ./wireshark&quot;. If I click File &amp;gt; Open Source, it displays a list of .c and .h files, but not all of the files in the project. In particular, I&#x27;m looking to debug a dissector...'''
date = "2013-12-31T13:49:00Z"
lastmod = "2014-01-03T08:21:00Z"
weight = 28505
keywords = [ "debug", "dissector", "ddd" ]
aliases = [ "/questions/28505" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Finding source with DDD](/questions/28505/finding-source-with-ddd)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28505-score" class="post-score" title="current number of votes">0</div><span id="post-28505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've build wireshark, and can start it up using ddd using the recommended method through libtool "libtool --mode=execute ddd ./wireshark". If I click File &gt; Open Source, it displays a list of .c and .h files, but not all of the files in the project. In particular, I'm looking to debug a dissector. I've tried to add ./epan/dissectors/ to the search path, but that has not helped. How can I tell ddd to look/open source files in the dissectors directory?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-debug" rel="tag" title="see questions tagged &#39;debug&#39;">debug</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-ddd" rel="tag" title="see questions tagged &#39;ddd&#39;">ddd</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '13, 13:49</strong></p><img src="https://secure.gravatar.com/avatar/7007cec142da24944948b806c663c76d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maplante&#39;s gravatar image" /><p><span>maplante</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maplante has no accepted answers">0%</span></p></div></div><div id="comments-container-28505" class="comments-container"></div><div id="comment-tools-28505" class="comment-tools"></div><div class="clear"></div><div id="comment-28505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28537"></span>

<div id="answer-container-28537" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28537-score" class="post-score" title="current number of votes">1</div><span id="post-28537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="maplante has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Run the program up to main(), then the shared objects are loaded, such as 'epan' which contains the dissectors.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '14, 15:41</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-28537" class="comments-container"><span id="28552"></span><div id="comment-28552" class="comment"><div id="post-28552-score" class="comment-score"></div><div class="comment-text"><p>That worked.</p><p>Thanks!</p><p>(Converted to a comment as per the way ask.wireshark works; Please see the FAQ).</p></div><div id="comment-28552-info" class="comment-info"><span class="comment-age">(03 Jan '14, 08:21)</span> <span class="comment-user userinfo">maplante</span></div></div></div><div id="comment-tools-28537" class="comment-tools"></div><div class="clear"></div><div id="comment-28537-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

