+++
type = "question"
title = "Add ip.addr to a pre-defined display filter quickly"
description = '''Hey there, I have a predefined filter which looks approximately like ((http or dns or sip) and ((ip.addr == 1.2.3.0/24) or (ip.addr == 2.3.4.0/24) or (dns contains &quot;abcdef&quot;) or (dns contains &quot;ddjdjdjd&quot;))  Basically the IP ranges are SIP and config servers that are contacted. On the interface I&#x27;m tra...'''
date = "2016-05-11T14:09:00Z"
lastmod = "2016-05-11T23:07:00Z"
weight = 52448
keywords = [ "gui", "display-filter" ]
aliases = [ "/questions/52448" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Add ip.addr to a pre-defined display filter quickly](/questions/52448/add-ipaddr-to-a-pre-defined-display-filter-quickly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52448-score" class="post-score" title="current number of votes">0</div><span id="post-52448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey there,</p><p>I have a predefined filter which looks approximately like</p><pre><code>((http or dns or sip) and  ((ip.addr == 1.2.3.0/24) or (ip.addr == 2.3.4.0/24) or (dns contains &quot;abcdef&quot;) or (dns contains &quot;ddjdjdjd&quot;))</code></pre><p>Basically the IP ranges are SIP and config servers that are contacted. On the interface I'm tracing there will be a lot of clients that will try to do exactly what I'm filtering for and thus I only like to have the traffic which matches this rule AND my own client IP address.</p><p>I have a button that applies this filter as a predefined display filter.</p><p>I then usually add the client IP (which I read from the clients UI or I see it appearing in the list, or both) by adding "AND ip.addr == clientip".</p><p>However it would save me some minutes per day and maybe some hours per year if i could simply add the IP to the filter by performing a click on a packet from my client that appears in the trace.</p><p>I know there is "prepare filter" -&gt; "and". But it will either (depending on what IP I selected) add "ip.dst" or "ip.src".</p><p>That will either hide away the packets coming back from the server or the ones that the client sent itself.</p><p>Is there an elegant way to solve this?</p><p>TL;DR: have a predefined filter that needs to be combined with "AND ip.addr == $selected-client-ip", how to do it easily?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gui" rel="tag" title="see questions tagged &#39;gui&#39;">gui</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '16, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/6a957b4a3140d9da1c17d8612db6d949?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aslmx&#39;s gravatar image" /><p><span>aslmx</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aslmx has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 May '16, 14:45</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-52448" class="comments-container"></div><div id="comment-tools-52448" class="comment-tools"></div><div class="clear"></div><div id="comment-52448-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52452"></span>

<div id="answer-container-52452" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52452-score" class="post-score" title="current number of votes">1</div><span id="post-52452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aslmx has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go into preferences, select "Protocols", check "Display hidden protocol items".</p><p>Then go back to your capture and do the same "Prepare filter" -&gt; "...and Selected" trick, but now use it on the previously hidden field ip.host.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '16, 14:48</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-52452" class="comments-container"><span id="52459"></span><div id="comment-52459" class="comment"><div id="post-52459-score" class="comment-score"></div><div class="comment-text"><p>Thanks. This is what i was looking for. What a pity it has been hidden so carefully...</p></div><div id="comment-52459-info" class="comment-info"><span class="comment-age">(11 May '16, 23:07)</span> <span class="comment-user userinfo">aslmx</span></div></div></div><div id="comment-tools-52452" class="comment-tools"></div><div class="clear"></div><div id="comment-52452-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

