+++
type = "question"
title = "Where is the postcode information of the Netherlands stored?"
description = '''I&#x27;ve noticed that the postcode information of many streets in the Netherlands are known by nominatim. For instance, this place is very correctly reported by nominatim as &quot;Buitenboogerd, 2611 KA, Nederland&quot; (as can be seen here). In the Netherlands, each street has a different postcode (or more). But...'''
date = "2011-06-14T10:22:00Z"
lastmod = "2011-06-15T12:54:00Z"
weight = 5754
keywords = [ "netherlands", "postcode", "nominatim" ]
aliases = [ "/questions/5754" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Where is the postcode information of the Netherlands stored?](/questions/5754/where-is-the-postcode-information-of-the-netherlands-stored)

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
<span id="post-5754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5754-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-5754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've noticed that the postcode information of many streets in the Netherlands are known by nominatim. For instance, <a href="http://www.openstreetmap.org/?lat=52.016512&amp;lon=4.354438&amp;zoom=18">this place</a> is very correctly reported by nominatim as "Buitenboogerd, 2611 KA, Nederland" (as can be seen <a href="http://nominatim.openstreetmap.org/reverse?lat=52.016512&amp;lon=4.354438">here</a>).</p>
<p>In the Netherlands, each street has a different postcode (or more). But on the "Buitenboogerd" way, I cannot see any information about the postcode, nor anywhere around! So I wonder, where is this information stored? How can I edit/update it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-netherlands" rel="tag" title="see questions tagged &#39;netherlands&#39;">netherlands</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jun '11, 10:22</strong></p>
<img src="https://secure.gravatar.com/avatar/eea25ff6647bea6fd95feb3afdcac3b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="%C3%89ric%20Piel&#39;s gravatar image" />
<p><span>Éric Piel</span><br />
<span class="score" title="116 reputation points">116</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Éric Piel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jun '11, 10:25</strong> </span></p>
</div>
</div>
<div id="comments-container-5754" class="comments-container">
&#10;</div>
<div id="comment-tools-5754" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5754-form-container" class="comment-form-container">
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

<span id="5784"></span>

<div id="answer-container-5784" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5784-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-5784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Éric Piel has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can check how Nominatim got its data by going to <a href="http://nominatim.openstreetmap.org/">Nominatim's page</a>, and entering the query there.</p>
<p>For "Buitenboogerd", you'll get (after clicking on "details"):</p>
<p><a href="http://open.mapquestapi.com/nominatim/v1/details.php?place_id=15365374">http://open.mapquestapi.com/nominatim/v1/details.php?place_id=15365374</a></p>
<p>There you can see that Nominatim used a node located next to "Molenstraat" (two blocks to the south). That node belongs to a shop, but it also has complete address information, including postcode, and Nominatim just guesses that streets close to it have the same postcode.</p>
<p>The node in Nominatim: <a href="http://open.mapquestapi.com/nominatim/v1/details.php?place_id=79652437">http://open.mapquestapi.com/nominatim/v1/details.php?place_id=79652437</a></p>
<p>The same node in OSM: <a href="http://www.openstreetmap.org/browse/node/553511622">http://www.openstreetmap.org/browse/node/553511622</a></p>
<p>In general, Nominatim seems to use a variety of heuristics to find out where areas of cities, postcodes etc. are. This sometimes works... and sometimes not.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jun '11, 12:03</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-5784" class="comments-container">
<span id="5787"></span>
<div id="comment-5787" class="comment">
<div id="post-5787-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks! I didn't know that nominatim was using the info from POI around. That's pretty clever :-) Actually I now realize on this example that the real postcode of Buitenboogerd is 2611 WS. So the explanation also explain why it's the wrong postcode.</p>
</div>
<div id="comment-5787-info" class="comment-info">
<span class="comment-age">(15 Jun '11, 12:54)</span> <span class="comment-user userinfo">Éric Piel</span>
</div>
</div>
</div>
<div id="comment-tools-5784" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5784-form-container" class="comment-form-container">
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

