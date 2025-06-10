+++
type = "question"
title = "What are the entities searched by Nominatim? (cannot find relation type=tunnel)"
description = '''I was searching for this relation by name, but Nominatim finds no results: http://www.openstreetmap.org/relation/5519843#map=15/50.1009/14.4076 - however it seems that Nominatim should be able to search in relations as well. (Note that the ways inside this relation have their own, different names, a...'''
date = "2015-12-04T14:28:00Z"
lastmod = "2015-12-07T10:03:00Z"
weight = 46974
keywords = [ "search", "nominatim", "relation" ]
aliases = [ "/questions/46974" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What are the entities searched by Nominatim? (cannot find relation type=tunnel)](/questions/46974/what-are-the-entities-searched-by-nominatim-cannot-find-relation-typetunnel)

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
<span id="post-46974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46974-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was searching for this relation by name, but Nominatim finds no results: <a href="http://www.openstreetmap.org/relation/5519843#map=15/50.1009/14.4076">http://www.openstreetmap.org/relation/5519843#map=15/50.1009/14.4076</a> - however it seems that Nominatim should be able to <a href="https://help.openstreetmap.org/questions/45347/nominatim-should-search-relations">search in relations</a> as well.</p>
<p>(Note that the ways inside this relation have their own, different names, and the relation itself has been named and alt_named this way for many months now.)</p>
<p>Neither the <a href="http://wiki.openstreetmap.org/wiki/Nominatim/FAQ">FAQ</a> nor the <a href="http://wiki.openstreetmap.org/wiki/Nominatim">documentation</a> mentions what entities are included/excluded from search, in other words, what specifically is searched. If it's a problem with this specific entity, is there a way to fix it? Or, if <code>type=tunnel</code> is not searched, where do I find out what relation types <em>are</em> searchable?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Dec '15, 14:28</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Dec '15, 10:04</strong> </span></p>
</div>
</div>
<div id="comments-container-46974" class="comments-container">
&#10;</div>
<div id="comment-tools-46974" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46974-form-container" class="comment-form-container">
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

<span id="47002"></span>

<div id="answer-container-47002" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47002-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Piskvor has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Producing a negative list for Nominatim would likely be an endless task, undoubtably it works with a positive list and relations of type tunnel are likely simply not included at this point in time (the same as bridge and site relations).</p>
<p>Particularly given that the addition of tunnel relations seem to be a stealth edit here <a href="http://wiki.openstreetmap.org/w/index.php?title=Key:tunnel&amp;oldid=1082393">http://wiki.openstreetmap.org/w/index.php?title=Key:tunnel&amp;oldid=1082393</a> and as you can see only a tiny number of objects are actually tagged that way.</p>
<p>Naturally there is nothing stoping you from asking for support.</p>
<p>PS: relevant code <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/output-gazetteer.cpp">https://github.com/openstreetmap/osm2pgsql/blob/master/output-gazetteer.cpp</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '15, 07:51</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Dec '15, 10:06</strong> </span></p>
</div>
</div>
<div id="comments-container-47002" class="comments-container">
<span id="47025"></span>
<div id="comment-47025" class="comment">
<div id="post-47025-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I see that the "relevant code" link answers my question "what names <em>does</em> Nominatim search", which is what I was looking for. Thanks a lot!</p>
</div>
<div id="comment-47025-info" class="comment-info">
<span class="comment-age">(07 Dec '15, 10:03)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
</div>
<div id="comment-tools-47002" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47002-form-container" class="comment-form-container">
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

