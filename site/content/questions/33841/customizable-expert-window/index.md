+++
type = "question"
title = "Customizable Expert Window"
description = '''Considering some traffic is more important to some than others. Is the expert window customizable to capture errors that we see as more serious than others that are predefined?'''
date = "2014-06-15T13:39:00Z"
lastmod = "2014-06-15T14:52:00Z"
weight = 33841
keywords = [ "expert" ]
aliases = [ "/questions/33841" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Customizable Expert Window](/questions/33841/customizable-expert-window)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33841-score" class="post-score" title="current number of votes">0</div><span id="post-33841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Considering some traffic is more important to some than others. Is the expert window customizable to capture errors that we see as more serious than others that are predefined?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-expert" rel="tag" title="see questions tagged &#39;expert&#39;">expert</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '14, 13:39</strong></p><img src="https://secure.gravatar.com/avatar/0e87784831cbde17a6f9849609360d94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ciscokid1701d&#39;s gravatar image" /><p><span>ciscokid1701d</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ciscokid1701d has no accepted answers">0%</span></p></div></div><div id="comments-container-33841" class="comments-container"></div><div id="comment-tools-33841" class="comment-tools"></div><div class="clear"></div><div id="comment-33841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33843"></span>

<div id="answer-container-33843" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33843-score" class="post-score" title="current number of votes">0</div><span id="post-33843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is the expert window customizable</p></blockquote><p>No. What is added to the expert info, is hard coded into the dissectors. If you want to change that behavior, you'll have to change the code of each and every dissector that adds expert info. Alternatively you could modify the 'expert' functions that are called by the dissectors and implement some kind of filtering system that is configurable through the GUI. In either case, you'll have to change the source code.</p><p>A totally different alternative is to ignore the expert info window and to <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChCustColorizationSection.html">build your own coloring rules</a>, based on the content of the expert fields</p><ul><li>expert.message</li><li>expert.group</li><li>expert.severity</li></ul><p>See also my answer to a similar question</p><blockquote><p><a href="http://ask.wireshark.org/questions/33842/modifying-the-expert">http://ask.wireshark.org/questions/33842/modifying-the-expert</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '14, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jun '14, 14:55</strong> </span></p></div></div><div id="comments-container-33843" class="comments-container"><span id="33854"></span><div id="comment-33854" class="comment"><div id="post-33854-score" class="comment-score"></div><div class="comment-text"><p>there is one dissector (I could find) that has some configurable preferences. packet-ncp.c. For the rest, my answer above still applies.</p><p>packet-ncp.c checks the following preferences.</p><pre><code># Whether the NCP dissector should echo the NDS Entry ID to name resolves to the expert table.
#ncp.eid_2_expert: TRUE
# Whether the NCP dissector should echo NCP connection information to the expert table.
#ncp.connection_2_expert: FALSE
# Whether the NCP dissector should echo protocol errors to the expert table.
#ncp.error_2_expert: TRUE
# Whether the NCP dissector should echo server information to the expert table.
#ncp.server_2_expert: TRUE
# Whether the NCP dissector should echo file open/close/oplock information to the expert table.
#ncp.file_2_expert: FALSE</code></pre></div><div id="comment-33854-info" class="comment-info"><span class="comment-age">(15 Jun '14, 14:52)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-33843" class="comment-tools"></div><div class="clear"></div><div id="comment-33843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

