+++
type = "question"
title = "reconstructing HTTP object"
description = '''Hello, Is there any method to reconstruct HTTP objects using tshark (not wireshark)? Otherwise, could you tell me any other tools to do this? Thanks. '''
date = "2013-02-18T05:33:00Z"
lastmod = "2013-02-18T08:03:00Z"
weight = 18704
keywords = [ "http", "tshark" ]
aliases = [ "/questions/18704" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [reconstructing HTTP object](/questions/18704/reconstructing-http-object)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18704-score" class="post-score" title="current number of votes">0</div><span id="post-18704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, Is there any method to reconstruct HTTP objects using tshark (not wireshark)? Otherwise, could you tell me any other tools to do this?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '13, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/2c33bce451fd8dc3844b351b798cbee1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fates&#39;s gravatar image" /><p><span>fates</span><br />
<span class="score" title="35 reputation points">35</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fates has no accepted answers">0%</span></p></div></div><div id="comments-container-18704" class="comments-container"></div><div id="comment-tools-18704" class="comment-tools"></div><div class="clear"></div><div id="comment-18704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18705"></span>

<div id="answer-container-18705" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18705-score" class="post-score" title="current number of votes">1</div><span id="post-18705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there any method to reconstruct HTTP objects using tshark</p></blockquote><p>I guess you are talking about an <strong>export</strong> of 'objects' transmitted via HTTP (files, videos, images, etc.). If so, then there is no easy way to do that in tshark, as there is no such functionality built in. As you are asking for tshark (<strong>not</strong> Wireshark) I assume you want to automate things, right?</p><p>If so, these tools may or may not be interesting for you:</p><blockquote><p><code>https://isc.sans.edu/diary/Tools+for+extracting+files+from+pcaps/6961</code><br />
</p></blockquote><p>For scripting purposes, <strong><a href="http://justniffer.sourceforge.net/#!/justniffer_grab_http_traffic">justsniffer</a> (Linux)</strong> or <strong><a href="http://www.cockos.com/assniffer/">assniffer</a> (Windows)</strong> are probably better tools to extract HTTP data 'objects'.</p><p>BTW: Additionally you might be interested in my answer to the following question:</p><blockquote><p><code>http://ask.wireshark.org/questions/15560/headless-automate-export-object-when-capturing-packeting</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '13, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Feb '13, 08:02</strong> </span></p></div></div><div id="comments-container-18705" class="comments-container"><span id="18706"></span><div id="comment-18706" class="comment"><div id="post-18706-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt. I'll try it. :)</p></div><div id="comment-18706-info" class="comment-info"><span class="comment-age">(18 Feb '13, 08:01)</span> <span class="comment-user userinfo">fates</span></div></div><span id="18707"></span><div id="comment-18707" class="comment"><div id="post-18707-score" class="comment-score"></div><div class="comment-text"><p>Good luck!</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-18707-info" class="comment-info"><span class="comment-age">(18 Feb '13, 08:03)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-18705" class="comment-tools"></div><div class="clear"></div><div id="comment-18705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

