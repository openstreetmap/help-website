+++
type = "question"
title = "Use last dissector data"
description = '''Hi, I´m developing a plugin for TUP, and to decode the CIC field i need to use the last byte from the previous dissector (MTP3 in my case), as it´s last four bits are part of the 12 bit CIC field from my TUP messages.. I need to , somehow, &quot;share&quot; this last byte between the dissectors How can i do t...'''
date = "2013-05-17T10:15:00Z"
lastmod = "2013-05-21T10:43:00Z"
weight = 21231
keywords = [ "tup", "chained-dissector", "mtp3" ]
aliases = [ "/questions/21231" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Use last dissector data](/questions/21231/use-last-dissector-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21231-score" class="post-score" title="current number of votes">0</div><span id="post-21231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I´m developing a plugin for TUP, and to decode the CIC field i need to use the last byte from the previous dissector (MTP3 in my case), as it´s last four bits are part of the 12 bit CIC field from my TUP messages.. I need to , somehow, "share" this last byte between the dissectors How can i do that?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tup" rel="tag" title="see questions tagged &#39;tup&#39;">tup</span> <span class="post-tag tag-link-chained-dissector" rel="tag" title="see questions tagged &#39;chained-dissector&#39;">chained-dissector</span> <span class="post-tag tag-link-mtp3" rel="tag" title="see questions tagged &#39;mtp3&#39;">mtp3</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '13, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/41cae5c8111115b7c81a5d2f5a624c14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Renan&#39;s gravatar image" /><p><span>Renan</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Renan has no accepted answers">0%</span></p></div></div><div id="comments-container-21231" class="comments-container"></div><div id="comment-tools-21231" class="comment-tools"></div><div class="clear"></div><div id="comment-21231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21232"></span>

<div id="answer-container-21232" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21232-score" class="post-score" title="current number of votes">1</div><span id="post-21232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Renan has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A common way to solve this problem is to store the needed value in the "private_data" field of pinfo. For example the MTP3 dissector <em>used to</em> do this to pass the SI down to subdissectors:</p><pre><code>/* Store the SI so that subidissectors know what SI this msg is */   
*pd_save = pinfo-&gt;private_data;      
pinfo-&gt;private_data = GUINT_TO_POINTER(sio &amp; SERVICE_INDICATOR_MASK);</code></pre><p>(A better solution to passing the SI was found and implemented in <a href="https://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=45788">r45788</a>. That means the private_data field could be used for passing the SLS to TUP.)</p><p>A newer (and probably better) way to solve this problem is to pass the data directly. This could be done by calling <code>dissector_try_uint_new()</code> in packet-mtp3.c (and passing the SLS as the 'data' argument) and then using the (now normally unused) 'data' parameter of new-style dissectors (<code>new_dissector_</code>t) and heuristic dissectors.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '13, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-21232" class="comments-container"><span id="21349"></span><div id="comment-21349" class="comment"><div id="post-21349-score" class="comment-score"></div><div class="comment-text"><p>[Original comment moved to the new question.]</p><p>Also: this is a Q&amp;A site not a forum so if an answer answers your question, please mark the answer as accepted (by checking the checkbox next to the answer).</p></div><div id="comment-21349-info" class="comment-info"><span class="comment-age">(21 May '13, 10:43)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-21232" class="comment-tools"></div><div class="clear"></div><div id="comment-21232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

