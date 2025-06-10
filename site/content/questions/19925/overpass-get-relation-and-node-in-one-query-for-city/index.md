+++
type = "question"
title = "Overpass: Get relation and node in one query for city?"
description = '''Hello, I use the Overpass-API to get cities from some area. As an example I use this simple query: node [&quot;place&quot;~&quot;village|city|town|metropolis&quot;] [&quot;name&quot;~&quot;^A&quot;] (area:3602145268); out body;  So I get a lot of villages/cities/towns/metropolises which starts with &quot;A&quot; which is fine so far. What I need no...'''
date = "2013-02-14T12:49:00Z"
lastmod = "2013-02-15T18:31:00Z"
weight = 19925
keywords = [ "overpass", "nodes", "relations" ]
aliases = [ "/questions/19925" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass: Get relation and node in one query for city?](/questions/19925/overpass-get-relation-and-node-in-one-query-for-city)

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
<span id="post-19925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19925-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I use the Overpass-API to get cities from some area. As an example I use this simple query:</p>
<pre><code>node
[&quot;place&quot;~&quot;village|city|town|metropolis&quot;]
[&quot;name&quot;~&quot;^A&quot;]
(area:3602145268);
out body;</code></pre>
<p>So I get a lot of villages/cities/towns/metropolises which starts with "A" which is fine so far.</p>
<p>What I need now are - besides the information the query above delivers in the node - all relation-ids to that found cities. How can it be done? Can the query above be modified to deliever all relation-ids as well? It would avoid sending a query for every city I got.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Feb '13, 12:49</strong></p>
<img src="https://secure.gravatar.com/avatar/12f399704c1d69150128133157881125?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wuschba&#39;s gravatar image" />
<p><span>wuschba</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wuschba has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Feb '13, 12:49</strong> </span></p>
</div>
</div>
<div id="comments-container-19925" class="comments-container">
&#10;</div>
<div id="comment-tools-19925" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19925-form-container" class="comment-form-container">
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

<span id="19943"></span>

<div id="answer-container-19943" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19943-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wuschba has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In principle, it is possible to get with <a href="http://overpass-turbo.eu/?Q=area(3602145268)%3B%0Arel%0A%20%20%5Badmin_level~%226%7C7%7C8%22%5D%0A%20%20(area)%3B%0Aout%20ids%3B%0A&amp;C=50.84858;7.10726;16">this request</a> all city boundaries in bavaria.</p>
<p>In detail, there are two things to consider: First, it also returns cities that have a common boundary with bavaria, although they are actually outside bavaria. This is a side effect of the query semantics I have not thought about: Ways are considered inside an area if they are completely on the border (which makes sense), and relations are considered inside if one or more of its elements are inside (which also makes sense on its own), but both together is a little bit odd.</p>
<p>Second, there is no connection between the place nodes and the boundary relations. In some cases, they may be contained as members in the boundary relations, but not always.</p>
<p>edit:</p>
<p>Ahh, now I understand your question better. <a href="http://overpass-turbo.eu/?Q=%5Btimeout%3A900%5D%3B%0Aarea%5Bname%3D%22Bayern%22%5D%3B%0Anode(area)%5Bplace~%22%5E(town%7Ccity)%24%22%5D%5Bname~%22%5EA%22%5D%3B%0Aforeach(%0A%20%20out%3B%0A%20%20is_in%3B%0A%20%20area._%5Badmin_level~%226%7C8%22%5D%5B%22de%3Aplace%22!%3D%22county%22%5D%3B%0A%20%20out%3B%0A)%3B%0A&amp;C=48.77067;11.02478;8">This query</a> finds all place nodes (I added those of type town to cover more places) and for each the area it belongs to. To simplify testing, I have restricted these again to "A..". Feel free to remove that condition, but the query then runs for several minutes.</p>
<p>You can in principle deduce the relation ids from the area ids: just substract 3.6 billion. However, if you want to query for postcodes and so on afterwards, it is likely that you anyway still need the area and not the relation. I've written about the issue in <a href="http://forum.openstreetmap.org/viewtopic.php?id=20090">this forum thread</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Feb '13, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Feb '13, 18:45</strong> </span></p>
</div>
</div>
<div id="comments-container-19943" class="comments-container">
<span id="19961"></span>
<div id="comment-19961" class="comment">
<div id="post-19961-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for your reply. When looking at:</p>
<p><a href="http://nominatim.openstreetmap.org/details.php?place_id=97345357">http://nominatim.openstreetmap.org/details.php?place_id=97345357</a></p>
<p>or</p>
<p><a href="http://nominatim.openstreetmap.org/details.php?place_id=3676853724">http://nominatim.openstreetmap.org/details.php?place_id=3676853724</a> it seems I always get somewhere an "relation" for a city:</p>
<p>Munich: 62428</p>
<p>Ingolstadt: 62381</p>
<p>I need that to query all postcodes or streets for example via overpass to be used in the area-part of the request.</p>
<p>So I have nodes (cities) and need the relations like shown in nominatim - how would you do that with overpass?</p>
</div>
<div id="comment-19961-info" class="comment-info">
<span class="comment-age">(15 Feb '13, 14:45)</span> <span class="comment-user userinfo">wuschba</span>
</div>
</div>
<span id="19963"></span>
<div id="comment-19963" class="comment">
<div id="post-19963-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello wuschba, your aims seem to be a bit more than an FAQ for this site .. come to forum.openstreetmap.org, there is even a very active German sub forum if my assumption is right and you are from there.</p>
<p>If you get a solution for your aims, you can add it as an overpassAPI example in the collection in the OSM wiki, so others can benefit, too.</p>
</div>
<div id="comment-19963-info" class="comment-info">
<span class="comment-age">(15 Feb '13, 15:31)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="19969"></span>
<div id="comment-19969" class="comment">
<div id="post-19969-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Stephan, thanks for your reply. So you suggest discussing this in "users:Germany" on forum.openstreetmal.org?! Or is it more something for "Developers"?</p>
</div>
<div id="comment-19969-info" class="comment-info">
<span class="comment-age">(15 Feb '13, 17:01)</span> <span class="comment-user userinfo">wuschba</span>
</div>
</div>
<span id="19971"></span>
<div id="comment-19971" class="comment">
<div id="post-19971-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I suggest "users:Germany".</p>
</div>
<div id="comment-19971-info" class="comment-info">
<span class="comment-age">(15 Feb '13, 18:31)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-19943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19943-form-container" class="comment-form-container">
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

