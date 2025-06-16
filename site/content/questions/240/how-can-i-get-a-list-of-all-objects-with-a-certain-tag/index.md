+++
type = "question"
title = "How can I get a list of all objects with a certain tag?"
description = '''Xapi will give me such a list, but I have to download the objects themselves. For relations it&#x27;s even worse: xapi not only gives you the relations but all the elements. So how would I get, for instance, a list of all relations with network=US:US?'''
date = "2010-07-16T06:11:00Z"
lastmod = "2010-07-16T23:50:00Z"
weight = 240
keywords = [ "list", "xapi", "tagging" ]
aliases = [ "/questions/240" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I get a list of all objects with a certain tag?](/questions/240/how-can-i-get-a-list-of-all-objects-with-a-certain-tag)

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
<span id="post-240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-240-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Xapi will give me such a list, but I have to download the objects themselves. For relations it's even worse: xapi not only gives you the relations but all the elements.</p>
<p>So how would I get, for instance, a list of all relations with network=US:US?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-list" rel="tag" title="see questions tagged &#39;list&#39;">list</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '10, 06:11</strong></p>
<img src="https://secure.gravatar.com/avatar/0c334b9f230e39c1e73a2b0322a23fb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NE2&#39;s gravatar image" />
<p><span>NE2</span><br />
<span class="score" title="1359 reputation points"><span>1.4k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NE2 has one accepted answer">9%</span></p>
</div>
</div>
<div id="comments-container-240" class="comments-container">
&#10;</div>
<div id="comment-tools-240" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-240-form-container" class="comment-form-container">
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

<span id="247"></span>

<div id="answer-container-247" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-247-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-247-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-247-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The API has a search method that you can use for this. The request to use in your example would look like this:</p>
<p><a href="http://api.openstreetmap.org/api/0.6/relations/search?type=network&amp;value=US:US">http://api.openstreetmap.org/api/0.6/relations/search?type=network&amp;value=US:US</a></p>
<p>This is little known and little used because unlike XAPI, it does not support bounding box queries so you will always find all objects, world-wide, that match your request. (The same request works for ways or nodes if you replace "relations" accordingly in the query.)</p>
<p>This query will return the matching objects, but not referenced objects (i.e. no nodes in ways or members in relations).</p>
<p>The request is documented on the <a href="https://wiki.openstreetmap.org/wiki/API_v0.5#Searching_for_Objects_by_Tag">Wiki</a> but for some reason it has not made it onto the API 0.6 page.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '10, 07:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-247" class="comments-container">
<span id="255"></span>
<div id="comment-255" class="comment">
<div id="post-255-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Exactly what I wanted. Thanks :)</p>
</div>
<div id="comment-255-info" class="comment-info">
<span class="comment-age">(16 Jul '10, 10:52)</span> <span class="comment-user userinfo">NE2</span>
</div>
</div>
<span id="281"></span>
<div id="comment-281" class="comment">
<div id="post-281-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Now wait a second. I don't remember what happened yesterday, but I downloaded that query today and it's incomplete. For example, <span>relation 112245</span> is missing.</p>
</div>
<div id="comment-281-info" class="comment-info">
<span class="comment-age">(16 Jul '10, 23:50)</span> <span class="comment-user userinfo">NE2</span>
</div>
</div>
</div>
<div id="comment-tools-247" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-247-form-container" class="comment-form-container">
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

