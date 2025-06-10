+++
type = "question"
title = "Nominatim - Why is a small nearby village included in a location description?"
description = '''Looking at http://nominatim.openstreetmap.org/details.php?place_id=35602344, http://nominatim.openstreetmap.org/details.php?place_id=39331659 and a good number of the roads around the area, they all seem to incorrectly include &#x27;Wick&#x27; using the place node of a small nearby village - http://www.openst...'''
date = "2014-06-05T15:54:00Z"
lastmod = "2014-06-12T06:03:00Z"
weight = 33731
keywords = [ "node", "wrongname", "place", "name", "nominatim" ]
aliases = [ "/questions/33731" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim - Why is a small nearby village included in a location description?](/questions/33731/nominatim-why-is-a-small-nearby-village-included-in-a-location-description)

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
<span id="post-33731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33731-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Looking at <a href="http://nominatim.openstreetmap.org/details.php?place_id=35602344">http://nominatim.openstreetmap.org/details.php?place_id=35602344</a>, <a href="http://nominatim.openstreetmap.org/details.php?place_id=39331659">http://nominatim.openstreetmap.org/details.php?place_id=39331659</a> and a good number of the roads around the area, they all seem to incorrectly include 'Wick' using the place node of a small nearby village - <a href="http://www.openstreetmap.org/node/30133595">http://www.openstreetmap.org/node/30133595</a></p>
<p>I haven't been able to work out why Nominatim includes the 'Wick' place node in this case, can anyone help explain it for me? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-wrongname" rel="tag" title="see questions tagged &#39;wrongname&#39;">wrongname</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jun '14, 15:54</strong></p>
<img src="https://secure.gravatar.com/avatar/68791600aba005984a3eddbd82f6c0ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Elliveny&#39;s gravatar image" />
<p><span>Elliveny</span><br />
<span class="score" title="66 reputation points">66</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Elliveny has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jun '14, 16:00</strong> </span></p>
</div>
</div>
<div id="comments-container-33731" class="comments-container">
&#10;</div>
<div id="comment-tools-33731" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33731-form-container" class="comment-form-container">
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

<span id="33734"></span>

<div id="answer-container-33734" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33734-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That's because <em>Wick</em> is just a node and therefore hasn't an exact boundary. As a consequence, Nominatim has to guess it's boundary and obviously it can't be 100% right about it.</p>
<p>But I wonder whether <em>Whick</em> is really a village and not just a suburb?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '14, 18:02</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-33734" class="comments-container">
<span id="33751"></span>
<div id="comment-33751" class="comment">
<div id="post-33751-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Suburb or city doesn't really matter for Nominatim. I had to draw a administrative boundary around a neigborhood node in order to prevent Nominatim to add it to each street in the village.</p>
</div>
<div id="comment-33751-info" class="comment-info">
<span class="comment-age">(06 Jun '14, 12:49)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="33754"></span>
<div id="comment-33754" class="comment">
<div id="post-33754-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sure, Nominatim can't know whether the streets are located inside the neighborhood if there is no exact boundary either. But in this case the mentioned places are already part of another suburb. So if Wick really is a suburb and gets tagged as a suburb, then Nominatim would no longer assign these places to Whick. Of course this is only half the solution, because the suburbs don't have an exact boundary either.</p>
</div>
<div id="comment-33754-info" class="comment-info">
<span class="comment-age">(06 Jun '14, 13:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33842"></span>
<div id="comment-33842" class="comment">
<div id="post-33842-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@escada</span> - Can you provide an example? I'm keen to dig into this a bit more and could do with something to compare to please.</p>
</div>
<div id="comment-33842-info" class="comment-info">
<span class="comment-age">(10 Jun '14, 14:11)</span> <span class="comment-user userinfo">Elliveny</span>
</div>
</div>
<span id="33843"></span>
<div id="comment-33843" class="comment">
<div id="post-33843-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've added the relation Bosstraat <a href="http://www.openstreetmap.org/relation/3777416">http://www.openstreetmap.org/relation/3777416</a> Unfortunately, I now notice that it does not work. e.g. Oude Reetse Baan 89, Boom is still linked to this neighborhood. It is certainly not part of it. I though I edited some address at that time and I got rid of the pesky "Bosstraat"</p>
</div>
<div id="comment-33843-info" class="comment-info">
<span class="comment-age">(10 Jun '14, 14:27)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="33844"></span>
<div id="comment-33844" class="comment">
<div id="post-33844-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><em>Oude Reetse Baan 89, Boom</em> is linked to the <a href="http://www.openstreetmap.org/node/2886010337">neighborhood node</a> and not the relation you created, according to <a href="http://nominatim.openstreetmap.org/details.php?place_id=3676767676">Nominatim's detail page</a> (funny place ID, btw.). I'm not quite sure how to prevent that and it seems appropriate to ask a new question about this issue.</p>
</div>
<div id="comment-33844-info" class="comment-info">
<span class="comment-age">(10 Jun '14, 15:25)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33845"></span>
<div id="comment-33845" class="comment not_top_scorer">
<div id="post-33845-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know if it would work at all. But I do know that if it works, then you need to use matching importance for the admin level and the place node. Relation Bosstraat is at admin level 10 (calculated importance=20). The node for Bosstraat is tagged as neighbourhood (calculated importance=22).</p>
<p>See: <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Development_overview#Country_to_street_level">Nominatim Development Overview</a></p>
</div>
<div id="comment-33845-info" class="comment-info">
<span class="comment-age">(10 Jun '14, 15:35)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="33897"></span>
<div id="comment-33897" class="comment not_top_scorer">
<div id="post-33897-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yesterday I removed the place node and now it seems that everything is OK. The neighborhood is only added to those streets that are actually in the neighborhood, due to the administrative boundary. I'll now try to add the admin centre again and see what happens.</p>
</div>
<div id="comment-33897-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 06:03)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-33734" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-33734-form-container" class="comment-form-container">
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

