+++
type = "question"
title = "How to filter only errors or bad tcp packets"
description = '''I want to apply only filter such as Bad TCP Checksum errors ICMP errors for wireshark. How can I achieve this.'''
date = "2015-04-29T12:07:00Z"
lastmod = "2015-04-29T12:17:00Z"
weight = 41947
keywords = [ "wireshark" ]
aliases = [ "/questions/41947" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter only errors or bad tcp packets](/questions/41947/how-to-filter-only-errors-or-bad-tcp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41947-score" class="post-score" title="current number of votes">0</div><span id="post-41947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to apply only filter such as</p><p>Bad TCP</p><p>Checksum errors</p><p>ICMP errors</p><p>for wireshark. How can I achieve this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '15, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/6197906c26d7ea36b7bdceb8de34248a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Devendra&#39;s gravatar image" /><p><span>Devendra</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Devendra has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Apr '15, 12:23</strong> </span></p></div></div><div id="comments-container-41947" class="comments-container"></div><div id="comment-tools-41947" class="comment-tools"></div><div class="clear"></div><div id="comment-41947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41948"></span>

<div id="answer-container-41948" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41948-score" class="post-score" title="current number of votes">0</div><span id="post-41948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>ICMP should be easy, just filter away echo request and reply (type 8 and 0). Unless you have funky stuff like address mask/timestamp requests that should only show problems. The best filter for this is</p><pre><code>(icmp.type &gt; 0 and icmp.type &lt; 8) or icmp.type &gt; 8</code></pre><p>Filtering for checksum errors doesn't make sense because you won't be able to capture real packets with checksum errors. They'd be dropped by your network card before you ever see them. See this blog post for more details: <a href="https://blog.packet-foo.com/2013/05/capturing-damaged-frames/">https://blog.packet-foo.com/2013/05/capturing-damaged-frames/</a></p><p>For bad TCP you could try to work with the filter</p><pre><code>tcp.analysis.flags</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '15, 12:17</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41948" class="comments-container"></div><div id="comment-tools-41948" class="comment-tools"></div><div class="clear"></div><div id="comment-41948-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

