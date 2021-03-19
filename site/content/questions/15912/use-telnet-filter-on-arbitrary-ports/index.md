+++
type = "question"
title = "Use telnet filter on arbitrary ports?"
description = '''Is it possible to apply Wireshark&#x27;s telnet data filter to any ports other than 23? I&#x27;ve been trying to analyse traffic to several non-standard ports and I haven&#x27;t been able to get it working.'''
date = "2012-11-14T13:49:00Z"
lastmod = "2012-11-14T15:05:00Z"
weight = 15912
keywords = [ "filter", "port", "telnet" ]
aliases = [ "/questions/15912" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Use telnet filter on arbitrary ports?](/questions/15912/use-telnet-filter-on-arbitrary-ports)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15912-score" class="post-score" title="current number of votes">0</div><span id="post-15912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to apply Wireshark's telnet data filter to any ports other than 23? I've been trying to analyse traffic to several non-standard ports and I haven't been able to get it working.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-telnet" rel="tag" title="see questions tagged &#39;telnet&#39;">telnet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '12, 13:49</strong></p><img src="https://secure.gravatar.com/avatar/fea37059f7c6c66fa41f9a9fc78e1ebc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rarkham&#39;s gravatar image" /><p><span>rarkham</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rarkham has no accepted answers">0%</span></p></div></div><div id="comments-container-15912" class="comments-container"></div><div id="comment-tools-15912" class="comment-tools"></div><div class="clear"></div><div id="comment-15912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15914"></span>

<div id="answer-container-15914" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15914-score" class="post-score" title="current number of votes">3</div><span id="post-15914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rarkham has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to tell Wireshark, that the other port is to be decoded as telnet.</p><p>Example: The telnet server accepts connections on port 2323.</p><p>In Wireshark select a packet from the conversation on port 2323. Right click on that packet and select:</p><blockquote><p><code>Decode As -&gt; Transport -&gt; TCP Destination (2323)</code><br />
</p></blockquote><p>From the list of protocols select TELNET. Click on OK.</p><p>Now the display filter <strong>telnet.data</strong> will also match on port 2323.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '12, 14:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Nov '12, 14:18</strong> </span></p></div></div><div id="comments-container-15914" class="comments-container"><span id="15916"></span><div id="comment-15916" class="comment"><div id="post-15916-score" class="comment-score"></div><div class="comment-text"><p>That's exactly what I needed, thank you!</p></div><div id="comment-15916-info" class="comment-info"><span class="comment-age">(14 Nov '12, 15:05)</span> <span class="comment-user userinfo">rarkham</span></div></div></div><div id="comment-tools-15914" class="comment-tools"></div><div class="clear"></div><div id="comment-15914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

