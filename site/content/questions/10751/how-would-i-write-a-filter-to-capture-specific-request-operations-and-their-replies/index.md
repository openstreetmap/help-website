+++
type = "question"
title = "How would I write a filter to capture specific request operations and their replies?"
description = '''Hi all - I&#x27;m trying to write a display filter that will filter certain specific operations and only their responses - is this possible? for example the current filter is: ((giop.request_op == &quot;reportStatus&quot;) || (giop.request_op == &quot;getStatus&quot;)|| (giop.request_op == &quot;newChanges&quot;)) || giop.exceptionid...'''
date = "2012-05-07T15:10:00Z"
lastmod = "2013-04-11T13:49:00Z"
weight = 10751
keywords = [ "display-filter", "wireshark" ]
aliases = [ "/questions/10751" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How would I write a filter to capture specific request operations and their replies?](/questions/10751/how-would-i-write-a-filter-to-capture-specific-request-operations-and-their-replies)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10751-score" class="post-score" title="current number of votes">0</div><span id="post-10751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all - I'm trying to write a display filter that will filter certain specific operations and only their responses - is this possible?</p><p>for example the current filter is:</p><pre><code>((giop.request_op == &quot;reportStatus&quot;) || (giop.request_op == &quot;getStatus&quot;)|| (giop.request_op == &quot;newChanges&quot;)) || giop.exceptionid</code></pre><p>Is there any way to include only the responses to these requests? In the case of the exception, I'd love it to throw the request that caused the exception, but I realise this would be potentially difficult. I'm really just trying to come up with the whole transactions without manually having to filter out all the unrelated responses. Thanks Scott</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '12, 15:10</strong></p><img src="https://secure.gravatar.com/avatar/c4a59238ef906285e110fa429a9a94b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott%20Harman&#39;s gravatar image" /><p><span>Scott Harman</span><br />
<span class="score" title="46 reputation points">46</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott Harman has one accepted answer">50%</span></p></div></div><div id="comments-container-10751" class="comments-container"></div><div id="comment-tools-10751" class="comment-tools"></div><div class="clear"></div><div id="comment-10751-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10756"></span>

<div id="answer-container-10756" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10756-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10756-score" class="post-score" title="current number of votes">1</div><span id="post-10756-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Scott Harman has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at <a href="http://wiki.wireshark.org/MATE">http://wiki.wireshark.org/MATE</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '12, 15:58</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-10756" class="comments-container"><span id="20300"></span><div id="comment-20300" class="comment"><div id="post-20300-score" class="comment-score">1</div><div class="comment-text"><p>Hi SYN-bit... I've finally gotten around to actually doing this... it's not elegant but it works really well</p><pre><code>Pdu giop_pdu Proto giop Transport tcp/ip {
        Extract giop_addr From ip.addr;
        Extract giop_port From tcp.port;
        Extract giop_type From giop.type;
        Extract giop_request_id From giop.request_id;
        Extract giop_request_op From giop.request_op;
};

Gop giop_req On giop_pdu Match (giop_addr, giop_addr, giop_port, giop_port,giop_request_id) {
        Start (giop_type = 0);
        Stop (giop_type = 1);
        Extra (giop_request_op);
};

Gog giop_session {
    Member giop_req(giop_addr, giop_addr, giop_port, giop_port,giop_request_id );
    Extra (giop_request_op);
};</code></pre><p>Now, I can capture all the transactions by filtering just on 'mate' which works perfectly! Equally - the display filter</p><pre><code>mate.giop_session.giop_request_op contains &quot;Placeholder&quot;</code></pre><p>Gives me all my Placeholder transactions and I can easily see the relationships</p></div><div id="comment-20300-info" class="comment-info"><span class="comment-age">(10 Apr '13, 21:31)</span> <span class="comment-user userinfo">Scott Harman</span></div></div><span id="20316"></span><div id="comment-20316" class="comment"><div id="post-20316-score" class="comment-score"></div><div class="comment-text"><p>Hi Scott, thank you for updating this question with your MATE code for others to learn from. I'm glad it worked out for you this way.</p><p>PS I converted your "answer" to a "comment" as that is how this site works best, please see the FAQ.</p></div><div id="comment-20316-info" class="comment-info"><span class="comment-age">(11 Apr '13, 02:56)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="20349"></span><div id="comment-20349" class="comment"><div id="post-20349-score" class="comment-score"></div><div class="comment-text"><p>Thanks very much - I can never work out which way to respond ;) I'm stoked that it works as well as it does - and now understand why you need to craft your own filters, as it takes a human brain to understand the relationships in the transactions.</p></div><div id="comment-20349-info" class="comment-info"><span class="comment-age">(11 Apr '13, 13:49)</span> <span class="comment-user userinfo">Scott Harman</span></div></div></div><div id="comment-tools-10756" class="comment-tools"></div><div class="clear"></div><div id="comment-10756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

