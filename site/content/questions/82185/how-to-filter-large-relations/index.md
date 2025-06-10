+++
type = "question"
title = "How to filter large relations"
description = '''Dear OSM community, I&#x27;m having problems with large relations. Mostly coastlines, seas or oceans (e.g. https://www.openstreetmap.org/relation/4497545). They cause problems when I try to segment large map tiles because they are not split apart if I keep relations together, causing quite high nodes cou...'''
date = "2021-10-15T18:09:00Z"
lastmod = "2021-10-15T18:57:00Z"
weight = 82185
keywords = [ "filter", "filtering", "osmfilter", "relations" ]
aliases = [ "/questions/82185" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter large relations](/questions/82185/how-to-filter-large-relations)

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
<span id="post-82185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82185-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear OSM community,</p>
<p>I'm having problems with large relations. Mostly coastlines, seas or oceans (e.g. <a href="https://www.openstreetmap.org/relation/4497545">https://www.openstreetmap.org/relation/4497545</a>). They cause problems when I try to segment large map tiles because they are not split apart if I keep relations together, causing quite high nodes counts per split.</p>
<p>My question is: Is there some way to filter out such big relations using osm filter or similar commandline tools? Is anyone else having problems with this, and how did you address this problem?</p>
<p>Best regards, David</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Oct '21, 18:09</strong></p>
<img src="https://secure.gravatar.com/avatar/25016c1d96c37605cbea2c856055e065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gemons&#39;s gravatar image" />
<p><span>Gemons</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gemons has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82185" class="comments-container">
&#10;</div>
<div id="comment-tools-82185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82185-form-container" class="comment-form-container">
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

<span id="82186"></span>

<div id="answer-container-82186" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82186-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With osmosis you can do regional cuts using the <code>clipIncompleteEntities=true</code> option. This will then remove all nodes outside of the region, and modify ways that lie partly in and partly outside the region to only refer to the nodes inside. The same for relations.</p>
<p>However this process can lead to invalid geometries, so a large forest multipolygon that extends outside of your area might not be contained at all.</p>
<p>(These large water bodies are a pet peeve of mine, I think they misrepresent the facts, are solely created to have nice labels on the map, and should be deleted and replaced by a node in the middle.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Oct '21, 18:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-82186" class="comments-container">
<span id="82187"></span>
<div id="comment-82187" class="comment">
<div id="post-82187-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the fast reply. I tried to clip relations at the bounding box of my map tiles, but as you mentioned I also saw that this sometimes produces weird results. E.g. one time I had a U-shaped forest. After clipping it was not clear anymore where inside and outside of the forest was.</p>
<p>I think if there is no existing solution to filter a relation by node count (or member count could be enough as well) I will have to implement some filter like that on my own inside the program logic.</p>
<p>I hope that the overall number of relations filtered out due to this will be low enough such that I can manually evaluate if the relations that were thrown away should really be thrown away.</p>
</div>
<div id="comment-82187-info" class="comment-info">
<span class="comment-age">(15 Oct '21, 18:44)</span> <span class="comment-user userinfo">Gemons</span>
</div>
</div>
<span id="82188"></span>
<div id="comment-82188" class="comment">
<div id="post-82188-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Question is, what are you splitting the map for? IF you were to convert OSM data into geometries first (e.g. import into PostgreSQL) then you could split that nicely and cut large areas into smaller areas along the boundaries. Or use vector tiles. But I can't tell you if that will work for your use case since I don't know enough about that.</p>
</div>
<div id="comment-82188-info" class="comment-info">
<span class="comment-age">(15 Oct '21, 18:48)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="82189"></span>
<div id="comment-82189" class="comment">
<div id="post-82189-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm currently working on a map that only shows the type of environment. E.g. forest, water, meadow ... For this I merge multiple tag groups describing the envrionment into 11 environment groups. Then I import the map data into e.g. Python or Matlab and process the geometry. The code I have only works good on smaller map tiles ans the merging of polygons becomes quite expensive when the polygons become larger. Therefore, I split the map into smaller tiles upfront and process the tiles one by one. Ideally I will do this for the whole world map, mich means it should run automated as much as possible.</p>
</div>
<div id="comment-82189-info" class="comment-info">
<span class="comment-age">(15 Oct '21, 18:57)</span> <span class="comment-user userinfo">Gemons</span>
</div>
</div>
</div>
<div id="comment-tools-82186" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82186-form-container" class="comment-form-container">
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

