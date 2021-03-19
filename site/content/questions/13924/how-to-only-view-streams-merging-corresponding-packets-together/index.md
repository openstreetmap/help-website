+++
type = "question"
title = "How to only view streams, merging corresponding packets together"
description = '''Is there a way to see only a list of streams, without every single packet separately, like in HttpFox, e.g. HTTP localip:12345 -&amp;gt; www.example.org:80 GET /index.html HTTP localip:12346 -&amp;gt; www.example.org:80 POST /example-form a=b&amp;amp;x=y SMTP localip:12347 -&amp;gt; mail.example.org:25 LOGIN user:p...'''
date = "2012-08-28T02:18:00Z"
lastmod = "2012-08-28T05:53:00Z"
weight = 13924
keywords = [ "streams", "http", "tcp", "wireshark" ]
aliases = [ "/questions/13924" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to only view streams, merging corresponding packets together](/questions/13924/how-to-only-view-streams-merging-corresponding-packets-together)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13924-score" class="post-score" title="current number of votes">0</div><span id="post-13924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to see only a list of streams, without every single packet separately, like in HttpFox, e.g.</p><pre><code>HTTP localip:12345 -&gt; www.example.org:80  GET /index.html
HTTP localip:12346 -&gt; www.example.org:80  POST /example-form   a=b&amp;x=y
SMTP localip:12347 -&gt; mail.example.org:25 LOGIN user:password, MAIL: [email protected]example.org -&gt; [email protected]example.org
SSH  localip:12348 -&gt; ssh.example.org:22</code></pre><p>And clicking on a stream should show the corresponding packets or the stream content.</p><p>I tried "follow tcp stream", but that shows only one, and "export objects\http", but that is only for http...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-streams" rel="tag" title="see questions tagged &#39;streams&#39;">streams</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '12, 02:18</strong></p><img src="https://secure.gravatar.com/avatar/a40764e17b8f967052f9600079692f16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BeniBela&#39;s gravatar image" /><p><span>BeniBela</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BeniBela has no accepted answers">0%</span></p></div></div><div id="comments-container-13924" class="comments-container"></div><div id="comment-tools-13924" class="comment-tools"></div><div class="clear"></div><div id="comment-13924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13926"></span>

<div id="answer-container-13926" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13926-score" class="post-score" title="current number of votes">1</div><span id="post-13926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="BeniBela has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can get a list of all conversations/streams by looking at the conversation statisticsin the statistics menu (and in the conversation list at the TCP tab), and look at individual streams by right-clicking on a line and applying a filter A &lt;-&gt; B.</p><p>If you want your packet list to show interesting stuff you'll need to build a more or less complicated filter. For example a simple "http.request.method" could show you the http requests, but you'd need to add similar filter expressions for all other protocols.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '12, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Aug '12, 02:27</strong> </span></p></div></div><div id="comments-container-13926" class="comments-container"><span id="13928"></span><div id="comment-13928" class="comment"><div id="post-13928-score" class="comment-score"></div><div class="comment-text"><p>That's nice. But why is it called "statistics"? It sounds like it only show some summaries. And why is the list cleared and regenerated, every time you select a filter/follow a stream? And it is annoying that you need to click/select 4 times to change the filter.</p></div><div id="comment-13928-info" class="comment-info"><span class="comment-age">(28 Aug '12, 03:23)</span> <span class="comment-user userinfo">BeniBela</span></div></div><span id="13929"></span><div id="comment-13929" class="comment"><div id="post-13929-score" class="comment-score"></div><div class="comment-text"><p>Probably because it is a statistical listing of conversations with bytes/packets/bps etc. I agree that the refiltering process is painful, but at the moment there is no way around it...</p></div><div id="comment-13929-info" class="comment-info"><span class="comment-age">(28 Aug '12, 04:59)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="13931"></span><div id="comment-13931" class="comment"><div id="post-13931-score" class="comment-score"></div><div class="comment-text"><p>But the list does change. There is no need to refilter, if it is set to ignore the filters</p></div><div id="comment-13931-info" class="comment-info"><span class="comment-age">(28 Aug '12, 05:53)</span> <span class="comment-user userinfo">BeniBela</span></div></div></div><div id="comment-tools-13926" class="comment-tools"></div><div class="clear"></div><div id="comment-13926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

