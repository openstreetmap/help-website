+++
type = "question"
title = "search in uncompressed packet bytes"
description = '''I&#x27;ve captured some http packets and want to find out which ones contain some string. I use &quot;Edit-&amp;gt;Find Packet&quot; with &quot;Packet bytes&quot; option selected, but it doesn&#x27;t find anything because the data is compressed (Content-Encoding: gzip). When I search in &quot;Packet details&quot;, it doesn&#x27;t find everything b...'''
date = "2011-10-08T11:56:00Z"
lastmod = "2011-10-09T13:32:00Z"
weight = 6809
keywords = [ "search", "find", "uncompressed" ]
aliases = [ "/questions/6809" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [search in uncompressed packet bytes](/questions/6809/search-in-uncompressed-packet-bytes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6809-score" class="post-score" title="current number of votes">0</div><span id="post-6809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've captured some http packets and want to find out which ones contain some string. I use "Edit-&gt;Find Packet" with "Packet bytes" option selected, but it doesn't find anything because the data is compressed (Content-Encoding: gzip). When I search in "Packet details", it doesn't find everything because some lines are too long and get truncated.</p><p>Is there any way to search in uncompressed packet bytes?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-find" rel="tag" title="see questions tagged &#39;find&#39;">find</span> <span class="post-tag tag-link-uncompressed" rel="tag" title="see questions tagged &#39;uncompressed&#39;">uncompressed</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '11, 11:56</strong></p><img src="https://secure.gravatar.com/avatar/ab98fa290b92c97a4ad74b9b81b9ea36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="humanista&#39;s gravatar image" /><p><span>humanista</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="humanista has no accepted answers">0%</span></p></div></div><div id="comments-container-6809" class="comments-container"></div><div id="comment-tools-6809" class="comment-tools"></div><div class="clear"></div><div id="comment-6809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6810"></span>

<div id="answer-container-6810" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6810-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6810-score" class="post-score" title="current number of votes">2</div><span id="post-6810-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="humanista has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My first suggestion would have been to use "http contains &lt;xxx&gt;", but "http" only points to the compressed data. Digging a little deeper gives me a second suggestion that does seem to work. The uncompressed data is put in a new TVB and in the packet-details pane the dissection is listed under "data-text-lines". So you can use the (search or display) filter:</p><pre><code>http and data-text-lines contain &quot;&lt;XXX&gt;&quot;</code></pre><p>Hope this works for you!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '11, 00:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6810" class="comments-container"><span id="6815"></span><div id="comment-6815" class="comment"><div id="post-6815-score" class="comment-score"></div><div class="comment-text"><p>'http and data-text-lines contains "string"' works perfectly. Thank you very much!</p></div><div id="comment-6815-info" class="comment-info"><span class="comment-age">(09 Oct '11, 10:41)</span> <span class="comment-user userinfo">humanista</span></div></div><span id="6816"></span><div id="comment-6816" class="comment"><div id="post-6816-score" class="comment-score"></div><div class="comment-text"><p>(converted your "answer" to a "comment" please see the FAQ for details)</p></div><div id="comment-6816-info" class="comment-info"><span class="comment-age">(09 Oct '11, 13:32)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-6810" class="comment-tools"></div><div class="clear"></div><div id="comment-6810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

