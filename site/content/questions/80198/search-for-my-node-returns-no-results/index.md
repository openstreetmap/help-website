+++
type = "question"
title = "Search for my node returns no results"
description = '''Hello, Six mounths ago I added &quot;Cocott&#x27;arium de Neuville&quot; - node 8180288803 and I am not able to find it using OSM search. It is a public facility. Nominatim can not find it by name nor ID, and a reverse search returns a nearest structure but not the node itself. Do I need to do something more? Than...'''
date = "2021-05-16T22:34:00Z"
lastmod = "2021-05-17T01:23:00Z"
weight = 80198
keywords = [ "search", "nominatim", "nodes" ]
aliases = [ "/questions/80198" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Search for my node returns no results](/questions/80198/search-for-my-node-returns-no-results)

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
<span id="post-80198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80198-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>Six mounths ago I added <a href="https://www.openstreetmap.org/way/943667334" title="Cocott&#39;arium de Neuville">"Cocott'arium de Neuville" - node 8180288803</a> and I am not able to find it using OSM search. It is a public facility.</p>
<p>Nominatim can not find it by name nor ID, and a reverse search returns <a href="https://nominatim.openstreetmap.org/ui/reverse.html?lat=49.0128850&amp;lon=2.0621438&amp;zoom=18" title="Ehpad Château de Neuville">a nearest structure</a> but not the node itself.</p>
<p>Do I need to do something more?</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 May '21, 22:34</strong></p>
<img src="https://secure.gravatar.com/avatar/170abfdafc9ab5d262fe209f623148a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chtio&#39;s gravatar image" />
<p><span>Chtio</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chtio has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 May '21, 01:25</strong> </span></p>
</div>
</div>
<div id="comments-container-80198" class="comments-container">
&#10;</div>
<div id="comment-tools-80198" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80198-form-container" class="comment-form-container">
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

<span id="80199"></span>

<div id="answer-container-80199" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80199-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-80199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Chtio has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim (searchbox on openstreetmap.org) doesn't import places with tag <code>attraction=animal</code> <a href="https://taginfo.openstreetmap.org/projects/nominatim#tags">https://taginfo.openstreetmap.org/projects/nominatim#tags</a> Nominatim imports a lot of types of (named) places but not all. The main factor is if users use it for addresses or navigation.</p>
<p>It does import places tagged <code>tourism=*</code> but I can't tell if this place is also a tourist attraction. <a href="https://wiki.openstreetmap.org/wiki/Tag:tourism%3Dattraction">https://wiki.openstreetmap.org/wiki/Tag:tourism%3Dattraction</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '21, 23:25</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-80199" class="comments-container">
<span id="80200"></span>
<div id="comment-80200" class="comment">
<div id="post-80200-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are right, it should have the tourism:attraction tag. I hesitated with the farmyard=poultry tag but the place also has educational and touristic puposes. Thank you for your help!</p>
</div>
<div id="comment-80200-info" class="comment-info">
<span class="comment-age">(17 May '21, 01:23)</span> <span class="comment-user userinfo">Chtio</span>
</div>
</div>
</div>
<div id="comment-tools-80199" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80199-form-container" class="comment-form-container">
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

