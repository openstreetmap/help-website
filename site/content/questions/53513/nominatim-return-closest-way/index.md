+++
type = "question"
title = "Nominatim return closest way"
description = '''Hi, I&#x27;m just wondering if it is possible to only return ways using the reverse geocode method from longitude and latitude.  I&#x27;m currently using the query http://nominatim.openstreetmap.org/reverse?format=json&amp;amp;lat=53.3533634&amp;amp;lon=-6.363978&amp;amp;osm_type=W.  This however still returns nodes if t...'''
date = "2016-12-13T00:15:00Z"
lastmod = "2016-12-13T07:47:00Z"
weight = 53513
keywords = [ "nominatim" ]
aliases = [ "/questions/53513" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim return closest way](/questions/53513/nominatim-return-closest-way)

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
<span id="post-53513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53513-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm just wondering if it is possible to only return ways using the reverse geocode method from longitude and latitude.</p>
<p>I'm currently using the query <a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=53.3533634&amp;lon=-6.363978&amp;osm_type=W.">http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=53.3533634&amp;lon=-6.363978&amp;osm_type=W.</a></p>
<p>This however still returns nodes if that's what the co-ordinates point to.</p>
<p>I was wondering if there is a method for finding the way based on the node id, if this is what gets returned based on the query.</p>
<p>Any help on the matter will be most appreciated. Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Dec '16, 00:15</strong></p>
<img src="https://secure.gravatar.com/avatar/644ca0e0330ed699a366d37c15678350?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shayD&#39;s gravatar image" />
<p><span>shayD</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shayD has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53513" class="comments-container">
<span id="53523"></span>
<div id="comment-53523" class="comment">
<div id="post-53523-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sounds like Overpass API is the better approach here, isn't it?</p>
</div>
<div id="comment-53523-info" class="comment-info">
<span class="comment-age">(13 Dec '16, 07:47)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53513" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53513-form-container" class="comment-form-container">
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

<span id="53515"></span>

<div id="answer-container-53515" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53515-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="shayD has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use the <code>zoom</code> parameter. For example <a href="http://nominatim.openstreetmap.org/reverse.php?format=html&amp;lat=53.3533634&amp;lon=-6.363978&amp;zoom=16">http://nominatim.openstreetmap.org/reverse.php?format=html&amp;lat=53.3533634&amp;lon=-6.363978&amp;zoom=16</a> (you want so change <code>format=html</code> into <code>format=json</code>)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '16, 00:56</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-53515" class="comments-container">
<span id="53516"></span>
<div id="comment-53516" class="comment">
<div id="post-53516-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the quick reply and the answer to the question, works perfect!</p>
</div>
<div id="comment-53516-info" class="comment-info">
<span class="comment-age">(13 Dec '16, 01:07)</span> <span class="comment-user userinfo">shayD</span>
</div>
</div>
</div>
<div id="comment-tools-53515" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53515-form-container" class="comment-form-container">
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

