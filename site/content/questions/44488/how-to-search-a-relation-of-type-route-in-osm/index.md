+++
type = "question"
title = "How to search a relation of type route in OSM?"
description = '''I created a relation (data below) route type and like to know how search it in OSM (Nominatim). Do not assign name to it. I can only find it by searching for the tag:ref their main route (MS-166). Data relation/route:  link relation: http://www.openstreetmap.org/relation/5391799  tags:  nome: no add...'''
date = "2015-07-28T23:11:00Z"
lastmod = "2015-07-30T18:50:00Z"
weight = 44488
keywords = [ "route", "relations" ]
aliases = [ "/questions/44488" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to search a relation of type route in OSM?](/questions/44488/how-to-search-a-relation-of-type-route-in-osm)

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
<span id="post-44488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44488-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I created a relation (data below) route type and like to know how search it in OSM (Nominatim).</p>
<p>Do not assign name to it. I can only find it by searching for the tag:ref their main route (MS-166).</p>
<p>Data relation/route:</p>
<ul>
<li>link relation: <a href="http://www.openstreetmap.org/relation/5391799">http://www.openstreetmap.org/relation/5391799</a></li>
</ul>
<p>tags:</p>
<ul>
<li>nome: no add;</li>
<li>Network: BR: MS;</li>
<li>Ref: MS-166;</li>
<li>Route: road;</li>
<li>Type: route.</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jul '15, 23:11</strong></p>
<img src="https://secure.gravatar.com/avatar/62b0db5708737186a53757d471a515ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seth&#39;s gravatar image" />
<p><span>seth</span><br />
<span class="score" title="201 reputation points">201</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seth has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jul '15, 23:12</strong> </span></p>
</div>
</div>
<div id="comments-container-44488" class="comments-container">
&#10;</div>
<div id="comment-tools-44488" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44488-form-container" class="comment-form-container">
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

<span id="44499"></span>

<div id="answer-container-44499" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44499-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-44499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="seth has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unfortunately, you didn't tell us why you want to use Nominatim for this purpose. I would recommend to use Overpass API for such exactly defined tags:</p>
<p>Query:</p>
<pre><code>rel[network=&quot;BR:MS&quot;][ref=&quot;MS-166&quot;][route=road][type=route];
out geom;</code></pre>
<p>Try it in overpass turbo: <a href="http://overpass-turbo.eu/s/aE2">http://overpass-turbo.eu/s/aE2</a></p>
<p>Adjust the ref tag as needed</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jul '15, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-44499" class="comments-container">
<span id="44521"></span>
<div id="comment-44521" class="comment">
<div id="post-44521-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I do not, but other people who do not know the road.</p>
<p>If the route exists is because for a purpose. What would it be? To join the "thousands" of parts of a highway or determine a destination / origin more easily.</p>
<p>For example, the relation limits neighborhoods. If the neighborhood is delimited, when your name is entered in researching the OSM (Nominatim), the district boundary is shown in the result (orange line).</p>
<p>That's what I want to happen in the case of road routes, you understand now?</p>
</div>
<div id="comment-44521-info" class="comment-info">
<span class="comment-age">(29 Jul '15, 18:36)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
<span id="44524"></span>
<div id="comment-44524" class="comment">
<div id="post-44524-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you want something to happen that isn't currently happening, that's a feature request and should be entered in the issue tracker for that particular software. This site is just for finding out "how do I...?".</p>
</div>
<div id="comment-44524-info" class="comment-info">
<span class="comment-age">(29 Jul '15, 22:40)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="44540"></span>
<div id="comment-44540" class="comment">
<div id="post-44540-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Richard,</p>
<p>I know the purpose dessse forum, but thought something might be wrong in the relationship that I created.</p>
<p>Okay, tell me how to make this appeal request, please.</p>
</div>
<div id="comment-44540-info" class="comment-info">
<span class="comment-age">(30 Jul '15, 12:36)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
<span id="44541"></span>
<div id="comment-44541" class="comment">
<div id="post-44541-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://trac.openstreetmap.org">http://trac.openstreetmap.org</a>, select Nominatim component.</p>
</div>
<div id="comment-44541-info" class="comment-info">
<span class="comment-age">(30 Jul '15, 12:37)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="44542"></span>
<div id="comment-44542" class="comment not_top_scorer">
<div id="post-44542-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just guessing but it is quite possible that Nominatim ignores relations without names. In the end it is mainly a service for searching named features. If you know more specific information about the object you are searching for (like ref and network) then Overpass API might be a better choice.</p>
</div>
<div id="comment-44542-info" class="comment-info">
<span class="comment-age">(30 Jul '15, 13:33)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44546"></span>
<div id="comment-44546" class="comment not_top_scorer">
<div id="post-44546-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>scai,</p>
<p>I tested before with name like that; * Route name: MS-166 (official name of the main Highway Route).</p>
<p>But one OSM user informed me that it is not correct to name the route (relationship) with the name of any member of it (route).</p>
<p>Although not condorde it, as this can be done (and I do) in the relations of the limits of neighborhoods, I removed the name. He told me that if the route has no official name, the route is best to stay unnamed.</p>
<p>What do you think?</p>
</div>
<div id="comment-44546-info" class="comment-info">
<span class="comment-age">(30 Jul '15, 14:28)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
<span id="44547"></span>
<div id="comment-44547" class="comment not_top_scorer">
<div id="post-44547-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's correct, don't make up your own names. Also see <a href="https://wiki.openstreetmap.org/wiki/Names#Name_is_the_name_only">name is the name only</a>.</p>
</div>
<div id="comment-44547-info" class="comment-info">
<span class="comment-age">(30 Jul '15, 14:57)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44548"></span>
<div id="comment-44548" class="comment not_top_scorer">
<div id="post-44548-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, but with no name will be ignored in the OSM search, as was said before.</p>
<p>In fact, road routes (in theory) have no names. For example, if it goal is to group the "thousands" of stretches of highway.</p>
<p>But it should be possible to locate them (identify them) in the search.</p>
</div>
<div id="comment-44548-info" class="comment-info">
<span class="comment-age">(30 Jul '15, 16:39)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
<span id="44549"></span>
<div id="comment-44549" class="comment">
<div id="post-44549-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Nominatim is a geocoder and not made for finding <em>all</em> kinds of objects in the OSM database. Is there any particular reason why Overpass API doesn't work for you?</p>
</div>
<div id="comment-44549-info" class="comment-info">
<span class="comment-age">(30 Jul '15, 17:09)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44550"></span>
<div id="comment-44550" class="comment not_top_scorer">
<div id="post-44550-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For me there is no problem because I created the route and know find it (even by nominatim) but for the common OSM users.</p>
<p>As they find this route? When I create something in OSM, I think the end user and the difficulties he may have.</p>
</div>
<div id="comment-44550-info" class="comment-info">
<span class="comment-age">(30 Jul '15, 18:01)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
<span id="44551"></span>
<div id="comment-44551" class="comment not_top_scorer">
<div id="post-44551-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>openstreetmap.org isn't intended to be an end-user service with all the features of a commercial mapping service.</p>
</div>
<div id="comment-44551-info" class="comment-info">
<span class="comment-age">(30 Jul '15, 18:10)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="44552"></span>
<div id="comment-44552" class="comment not_top_scorer">
<div id="post-44552-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, but small increments, as this (search routes made relations), can be done.</p>
</div>
<div id="comment-44552-info" class="comment-info">
<span class="comment-age">(30 Jul '15, 18:50)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
</div>
<div id="comment-tools-44499" class="comment-tools">
<span class="comments-showing"> showing 5 of 12 </span> <a href="#" class="show-all-comments-link">show 7 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-44499-form-container" class="comment-form-container">
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

