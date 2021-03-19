+++
type = "question"
title = "How do you filter based on protocol?"
description = '''I added my own dissector to wireshark and compiled everything. I want to filter the packets so it only captures the ones that register as the &quot;CDMI&quot; protocol. The protocol is an extension to HTTP on port 80 if that helps.'''
date = "2011-02-10T10:49:00Z"
lastmod = "2011-02-11T14:23:00Z"
weight = 2276
keywords = [ "filter", "protocol", "filters", "custom" ]
aliases = [ "/questions/2276" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do you filter based on protocol?](/questions/2276/how-do-you-filter-based-on-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2276-score" class="post-score" title="current number of votes">0</div><span id="post-2276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I added my own dissector to wireshark and compiled everything. I want to filter the packets so it only captures the ones that register as the "CDMI" protocol.</p><p>The protocol is an extension to HTTP on port 80 if that helps.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-filters" rel="tag" title="see questions tagged &#39;filters&#39;">filters</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '11, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/3d3535b19a6debac9e2b855465a2027b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rodayo&#39;s gravatar image" /><p><span>Rodayo</span><br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rodayo has no accepted answers">0%</span></p></div></div><div id="comments-container-2276" class="comments-container"></div><div id="comment-tools-2276" class="comment-tools"></div><div class="clear"></div><div id="comment-2276-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2279"></span>

<div id="answer-container-2279" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2279-score" class="post-score" title="current number of votes">0</div><span id="post-2279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Capture filters have no knowledge about dissectors but are based on the BPF filtering rules. This is done to make them fast and safe to run in the kernel.</p><p>How is your "CDMI" protocol an extension to HTTP? Does it use it's own methods instead of GET/POST? Or does it run on top of HTTP?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '11, 16:23</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2279" class="comments-container"><span id="2288"></span><div id="comment-2288" class="comment"><div id="post-2288-score" class="comment-score"></div><div class="comment-text"><p>There will be an extra along with the HTTP ones:</p><p>...</p><p>X-CDMI-Specification-Version: 1.0 { ... }</p><p>...</p><p>But I figured this out yesterday, lol. Thanks anyways.</p></div><div id="comment-2288-info" class="comment-info"><span class="comment-age">(11 Feb '11, 14:23)</span> <span class="comment-user userinfo">Rodayo</span></div></div></div><div id="comment-tools-2279" class="comment-tools"></div><div class="clear"></div><div id="comment-2279-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

