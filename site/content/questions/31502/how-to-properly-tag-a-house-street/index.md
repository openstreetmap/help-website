+++
type = "question"
title = "how to properly tag a house / street?"
description = '''So I tried to properly map a lot of a village nearby, but it seems that things are not alright as I can&#x27;t search for a house I mapped and have openstreetmap.org pull up the proper building. For instance this search  the building is tagged with: &quot;addr:housenumber 15&quot;, the street has &quot;name:Chemin de l...'''
date = "2014-03-12T20:30:00Z"
lastmod = "2014-03-13T09:57:00Z"
weight = 31502
keywords = [ "associatedstreet", "streetnames", "tagging", "nominatim" ]
aliases = [ "/questions/31502" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to properly tag a house / street?](/questions/31502/how-to-properly-tag-a-house-street)

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
<span id="post-31502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31502-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So I tried to properly map a lot of a village nearby, but it seems that things are not alright as I can't search for a house I mapped and have openstreetmap.org pull up the proper building.</p>
<p>For instance <span>this search</span></p>
<ul>
<li>the building is tagged with: "addr:housenumber 15",</li>
<li>the street has "name:Chemin de l'...",</li>
<li>the building is part of a relation "associatedStreet:Chemin de l'...", just like the address I'm looking up.</li>
</ul>
<p>I did this change several days ago, so I was expecting openstreetmap.org to have these tags.</p>
<p>Is there anything else that's required? What am I missing? Am I supposed to tag each individual house/building with "addr:street" ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-associatedstreet" rel="tag" title="see questions tagged &#39;associatedstreet&#39;">associatedstreet</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Mar '14, 20:30</strong></p>
<img src="https://secure.gravatar.com/avatar/1319bb23a775a30901c30ed448012183?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ma1&#39;s gravatar image" />
<p><span>ma1</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ma1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Mar '14, 09:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-31502" class="comments-container">
<span id="31504"></span>
<div id="comment-31504" class="comment">
<div id="post-31504-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does it work for older addresses? How are they tagged? The search DB update should not be a problem currently (see <span>FAQ</span>).</p>
</div>
<div id="comment-31504-info" class="comment-info">
<span class="comment-age">(12 Mar '14, 20:46)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="31505"></span>
<div id="comment-31505" class="comment">
<div id="post-31505-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>please write your tags, as usual, in this form: <code>key = value</code>. Do not use a ":" as separator.</p>
</div>
<div id="comment-31505-info" class="comment-info">
<span class="comment-age">(12 Mar '14, 20:50)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="31506"></span>
<div id="comment-31506" class="comment">
<div id="post-31506-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Since you are asking re. search: According to <span>its FAQ</span> Nominatim (the engine which is the main power of www.osm.org's search) understands the relation tagging and addr:street directly. Maybe you did it wrong (although <span>the object in question</span> looks good to me). Compare with working results.</p>
</div>
<div id="comment-31506-info" class="comment-info">
<span class="comment-age">(12 Mar '14, 20:52)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31502" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31502-form-container" class="comment-form-container">
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

<span id="31509"></span>

<div id="answer-container-31509" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31509-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-31509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This seems to be caused by a Nominatim bug with the <code>associatedStreet</code> relation. Bug <a href="https://trac.openstreetmap.org/ticket/4877">4877</a> is about the building being attached to a street without a name, which prevents Nominatim to determine the correct address. This is true in your case, because the building is located near <a href="https://www.openstreetmap.org/way/35883781">way 35883781</a> which is also part of the <code>associatedStreet</code> relation, but doesn't have a name tag.</p>
<p>Also do note that there is another issue. Bug <a href="https://trac.openstreetmap.org/ticket/4619">4619</a> is about Nominatim being unable to update its index correctly even if you modify the relation or the street. As far as I understand the bug you have to modify the building, too, in order to trigger a reindexing of the building's address.</p>
<p>According to user lonvia, one of the top most <a href="https://github.com/twain47/Nominatim/graphs/contributors">Nominatim contributors</a>, the best would be to use <code>addr:street</code> tags on each object instead of the <code>associatedStreet</code> relation. One could argue that this is <em>tagging for the geocoder</em>, but the <code>associatedStreet</code> relation <a href="http://taginfo.openstreetmap.org/tags/type=associatedStreet">isn't used very widely</a> and consequently lacks proper support in many tools. And I don't think that this situation will improve.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '14, 21:09</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Mar '14, 21:13</strong> </span></p>
</div>
</div>
<div id="comments-container-31509" class="comments-container">
<span id="31510"></span>
<div id="comment-31510" class="comment">
<div id="post-31510-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting, but note that the building for "Chemin de l'Ochettaz 27B" does have the proper tag "addr:street", yet osm.org/nominatim can't find it. Is the mere existence of the associatedStreet relation the problem then?</p>
</div>
<div id="comment-31510-info" class="comment-info">
<span class="comment-age">(12 Mar '14, 21:21)</span> <span class="comment-user userinfo">ma1</span>
</div>
</div>
<span id="31520"></span>
<div id="comment-31520" class="comment">
<div id="post-31520-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know the Nominatim internals to answer that question. But the query for <a href="https://www.openstreetmap.org/search?query=Chemin%20de%20l%27Ochettaz%2027B%2C%20Saint-Sulpice%2C%20Switzerland#map=17/46.51205/6.55559">Chemin de l'Ochettaz 27B</a> succeeds now. Likewise your original query for house number 15.</p>
</div>
<div id="comment-31520-info" class="comment-info">
<span class="comment-age">(13 Mar '14, 07:47)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="31525"></span>
<div id="comment-31525" class="comment">
<div id="post-31525-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The "highway=residential" https://www.openstreetmap.org/way/26637405#map=16/46.5120/6.5556 needs a tag "name", not a tag "addr:street" (visible on version #17) !</p>
</div>
<div id="comment-31525-info" class="comment-info">
<span class="comment-age">(13 Mar '14, 09:57)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-31509" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31509-form-container" class="comment-form-container">
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

