+++
type = "question"
title = "Does Mapnik renders the relation with type=bridge?"
description = '''Today I was looking at the following case:   These 3 bridges are supposed to be only one. I searched around the wiki, and found a page that linked to a proposal that described a solution. It seems like this proposal was never voted on... However currently it is used 3576 times according to taginfo. ...'''
date = "2014-02-10T21:14:00Z"
lastmod = "2014-02-11T07:28:00Z"
weight = 30599
keywords = [ "bridge", "relation", "renderer", "mapnik" ]
aliases = [ "/questions/30599" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Does Mapnik renders the relation with type=bridge?](/questions/30599/does-mapnik-renders-the-relation-with-typebridge)

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
<span id="post-30599-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30599-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30599-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Today I was looking at the following case:</p>
<p><img src="/upfiles/bridge.png" alt="alt text" /></p>
<p>These 3 bridges are supposed to be only one. I searched around the wiki, and found <a href="https://wiki.openstreetmap.org/wiki/Relation:bridge">a page</a> that linked to a proposal that described a solution. It seems like this proposal was never voted on... However <a href="http://taginfo.openstreetmap.org/tags/?key=type&amp;value=bridge">currently it is used 3576 times according to taginfo</a>. Turns out it's probably because it's officially supported by JOSM.</p>
<p>So I <a href="https://www.openstreetmap.org/relation/3503937">tried using this relation type</a>, but with no success.</p>
<p>Am I doing something wrong, or is it really not rendered by Mapnik currently?</p>
<p>Thanks</p>
<p>PS: to clarify, the renderer should be rendering this as one bridge, not three how it's shown in the screenshot.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-renderer" rel="tag" title="see questions tagged &#39;renderer&#39;">renderer</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '14, 21:14</strong></p>
<img src="https://secure.gravatar.com/avatar/704f28429974bab1704a7535eb8a5734?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jgpacker&#39;s gravatar image" />
<p><span>jgpacker</span><br />
<span class="score" title="236 reputation points">236</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jgpacker has one accepted answer">10%</span></p>
</img>
</div>
</div>
<div id="comments-container-30599" class="comments-container">
&#10;</div>
<div id="comment-tools-30599" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30599-form-container" class="comment-form-container">
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

<span id="30604"></span>

<div id="answer-container-30604" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30604-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30604-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30604-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jgpacker has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Bridge relations are not drawn by the current OSM Carto style sheet used for the map on www.openstreetmap.org.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '14, 22:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-30604" class="comments-container">
<span id="30617"></span>
<div id="comment-30617" class="comment">
<div id="post-30617-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Nevertheless it is still worth to add them because they avoid the duplication of tags like name, operator, length etc. And of course it is possible that they will be rendered some day.</p>
</div>
<div id="comment-30617-info" class="comment-info">
<span class="comment-age">(11 Feb '14, 07:28)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30604" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30604-form-container" class="comment-form-container">
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

