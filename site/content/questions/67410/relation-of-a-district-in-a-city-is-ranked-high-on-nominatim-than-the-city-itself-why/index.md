+++
type = "question"
title = "Relation of a district in a city is ranked high on nominatim than the city itself - why?"
description = '''This relation (https://nominatim.openstreetmap.org/details.php?place_id=198913696) is one of 8 smaller districts of the German city of Essen (https://nominatim.openstreetmap.org/details.php?place_id=197694959). Nevertheless: Nominatim gives you this small subset as the first result when searching fo...'''
date = "2019-01-01T13:38:00Z"
lastmod = "2019-01-02T14:56:00Z"
weight = 67410
keywords = [ "nominatim" ]
aliases = [ "/questions/67410" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Relation of a district in a city is ranked high on nominatim than the city itself - why?](/questions/67410/relation-of-a-district-in-a-city-is-ranked-high-on-nominatim-than-the-city-itself-why)

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
<span id="post-67410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67410-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This relation (<a href="https://nominatim.openstreetmap.org/details.php?place_id=198913696)">https://nominatim.openstreetmap.org/details.php?place_id=198913696)</a> is one of 8 smaller districts of the German city of Essen (<a href="https://nominatim.openstreetmap.org/details.php?place_id=197694959).">https://nominatim.openstreetmap.org/details.php?place_id=197694959).</a></p>
<p>Nevertheless: Nominatim gives you this small subset as the first result when searching for "Essen". This leads to some unexpected behaviour. For example when using overpass turbo to search in the area {{geocodeArea:Essen}}-&gt;.searchArea; you only get results from this small district when you would expect results from the city.</p>
<p>How can I change that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jan '19, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/eb29a07f49b3256adf8cb2fdee6ad160?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="klischka&#39;s gravatar image" />
<p><span>klischka</span><br />
<span class="score" title="71 reputation points">71</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="klischka has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67410" class="comments-container">
<span id="67423"></span>
<div id="comment-67423" class="comment">
<div id="post-67423-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Meanwhile Nominatim returns the city as first result when <a href="https://nominatim.openstreetmap.org/search.php?q=Essen">searching for Essen</a>.</p>
</div>
<div id="comment-67423-info" class="comment-info">
<span class="comment-age">(02 Jan '19, 13:01)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="67425"></span>
<div id="comment-67425" class="comment">
<div id="post-67425-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I added a different wikipedia reference to the smaller relation of the district - that changed this behaviour</p>
</div>
<div id="comment-67425-info" class="comment-info">
<span class="comment-age">(02 Jan '19, 14:56)</span> <span class="comment-user userinfo">klischka</span>
</div>
</div>
</div>
<div id="comment-tools-67410" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67410-form-container" class="comment-form-container">
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

<span id="67411"></span>

<div id="answer-container-67411" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67411-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-67411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I see your removed <code>alt_name=Essen</code> from the Stadtbezirk (admin_level=9) already, that's good <a href="https://www.openstreetmap.org/relation/5928878/history">https://www.openstreetmap.org/relation/5928878/history</a></p>
<p>Nominatim merges boundaries (relations) and center points (nodes) if they represent the same. So <a href="https://nominatim.openstreetmap.org/details.php?osmtype=R&amp;osmid=5928878">https://nominatim.openstreetmap.org/details.php?osmtype=R&amp;osmid=5928878</a> is still showing names like 'Essen' and 'place=city' (in the extratags section). That's because this node <a href="https://www.openstreetmap.org/node/27350363">https://www.openstreetmap.org/node/27350363</a> is linked to multiple relations, one (well, two links even) of them the Stadtbezirk. Scroll down below to the end of the page to see "Relation Stadtmitte (5928917) (as admin_centre), Relation Stadtmitte (5928917) (as label)".</p>
<p>You'd change that in the relations, see <a href="https://wiki.openstreetmap.org/wiki/Relation:boundary#Relation_members">https://wiki.openstreetmap.org/wiki/Relation:boundary#Relation_members</a> I'm not sure if the ID editor can do that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jan '19, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-67411" class="comments-container">
<span id="67414"></span>
<div id="comment-67414" class="comment">
<div id="post-67414-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the idea and the help. So I have to add the node 27350363 as admin_centre to the boundary of Essen 62713. I tried to find out how to do that with josm for the last hours without success. Do you know any good tutorials on that?</p>
</div>
<div id="comment-67414-info" class="comment-info">
<span class="comment-age">(01 Jan '19, 18:12)</span> <span class="comment-user userinfo">klischka</span>
</div>
</div>
<span id="67418"></span>
<div id="comment-67418" class="comment">
<div id="post-67418-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I use the <a href="http://level0.osmz.ru/">http://level0.osmz.ru/</a> editor for those usually, e.g. removing a tag, renaming a tag or such. It's powerful, certainly for experienced OSM mappers.</p>
</div>
<div id="comment-67418-info" class="comment-info">
<span class="comment-age">(02 Jan '19, 00:12)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-67411" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67411-form-container" class="comment-form-container">
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

