+++
type = "question"
title = "Nodes with twice an attribute"
description = '''Hello, I noticed that some nodes have the name attribute twice (with varying case). For exemple the node 2624350260 has attribute &#x27;name&#x27; and attribute &#x27;Name&#x27;. This brings two questions :  Are attribute names case sensitive ? Can a node have the same attribute more than once ?  Thanks'''
date = "2016-09-13T10:39:00Z"
lastmod = "2016-09-13T11:05:00Z"
weight = 52031
keywords = [ "node", "attributes" ]
aliases = [ "/questions/52031" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nodes with twice an attribute](/questions/52031/nodes-with-twice-an-attribute)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52031-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I noticed that some nodes have the name attribute twice (with varying case). For exemple the node 2624350260 has attribute 'name' and attribute 'Name'.</p>
<p>This brings two questions :</p>
<ul>
<li>Are attribute names case sensitive ?</li>
<li>Can a node have the same attribute more than once ?</li>
</ul>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-attributes" rel="tag" title="see questions tagged &#39;attributes&#39;">attributes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '16, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/92c44e45a6d5fee06626f386d830dfde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="doubret&#39;s gravatar image" />
<p><span>doubret</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="doubret has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Sep '16, 10:40</strong> </span></p>
</div>
</div>
<div id="comments-container-52031" class="comments-container">
&#10;</div>
<div id="comment-tools-52031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52031-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52032"></span>

<div id="answer-container-52032" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52032-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="doubret has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Tags">Tags</a> are case-sensitive. This means that <em>name</em> and <em>Name</em> are not the same. Also, each tag can only exist once for each <a href="https://wiki.openstreetmap.org/wiki/Elements">element</a>. So each element can only have a single <em>name</em> tag.</p>
<p>Keys should be kept in lowercase. Thus <em>Name</em> will not be interpreted by any popular tool, i.e. it won't get rendered, it won't be used for searching and so on. As far as I know there is not a single popular key that contains any uppercase latter, except for "FIXME". Most of the tags starting with an uppercase letter are just a mistake, either made by a human being while editing tags by hand or caused by some badly written (import) tool. Yet they might contain valuable information, so only remove/fix them if you really know what you are doing. Ideally try to contact the author.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '16, 10:51</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Sep '16, 10:53</strong> </span></p>
</div>
</div>
<div id="comments-container-52032" class="comments-container">
<span id="52033"></span>
<div id="comment-52033" class="comment">
<div id="post-52033-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thank you. I will not remove anything, don't worry. I'll try to contact the authors.</p>
</div>
<div id="comment-52033-info" class="comment-info">
<span class="comment-age">(13 Sep '16, 11:05)</span> <span class="comment-user userinfo">doubret</span>
</div>
</div>
</div>
<div id="comment-tools-52032" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52032-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

