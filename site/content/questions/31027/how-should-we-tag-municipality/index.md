+++
type = "question"
title = "How should we tag Municipality?"
description = '''If we want to add additional information to roads and restaurants should we tag the municipality or the village? Example: http://en.wikipedia.org/wiki/La_P%C3%AAche,_Quebec La Pêche is a merger of multiple small villages, but locally no one calls &quot;Wakefield&quot; La pêche, they call it Wakefield. Should ...'''
date = "2014-02-25T17:56:00Z"
lastmod = "2014-02-26T16:09:00Z"
weight = 31027
keywords = [ "osm", "standards", "municipality", "tagging", "convention" ]
aliases = [ "/questions/31027" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How should we tag Municipality?](/questions/31027/how-should-we-tag-municipality)

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
<span id="post-31027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31027-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If we want to add additional information to roads and restaurants should we tag the municipality or the village?</p>
<p>Example: <a href="http://en.wikipedia.org/wiki/La_P%C3%AAche,_Quebec">http://en.wikipedia.org/wiki/La_P%C3%AAche,_Quebec</a></p>
<p>La Pêche is a merger of multiple small villages, but locally no one calls "Wakefield" La pêche, they call it Wakefield.</p>
<p>Should the roads and restaurants be tagged under Wakefield or La Pêche?</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-standards" rel="tag" title="see questions tagged &#39;standards&#39;">standards</span> <span class="post-tag tag-link-municipality" rel="tag" title="see questions tagged &#39;municipality&#39;">municipality</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-convention" rel="tag" title="see questions tagged &#39;convention&#39;">convention</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Feb '14, 17:56</strong></p>
<img src="https://secure.gravatar.com/avatar/55b745b283e8f1a78cd942c72b6021f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LogicalViolinist&#39;s gravatar image" />
<p><span>LogicalVioli...</span><br />
<span class="score" title="246 reputation points">246</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LogicalViolinist has one accepted answer">16%</span></p>
</div>
</div>
<div id="comments-container-31027" class="comments-container">
&#10;</div>
<div id="comment-tools-31027" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31027-form-container" class="comment-form-container">
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

<span id="31054"></span>

<div id="answer-container-31054" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31054-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-31054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your question is a bit confusing. But I can try to explain how the municipality and places can be mapped in OSM.</p>
<p>First, the "municipality" which is more an administrative entity. Create a polygone (a closed way) or better a multipolygon of the admin borders, create a relation of "type=boundary", "boundary=administrative", "admin_level=8" and "name=La Pêche" (<a href="http://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative">see the wiki</a>). You also tag the way(s) with the tag "boundary=administrative" + "admin_level=x" where x is the highest admin level (the lowest number) used to define a boundary with this way (a way can define more than one admin_level, it can also define the boundary of a county, a region, a province or the country). This <a href="http://wiki.openstreetmap.org/wiki/WikiProject_France/Limites_administratives/Tracer_les_limites_administratives">wiki page</a> in French is also providing some hints, especially when the <a href="http://wiki.openstreetmap.org/wiki/WikiProject_France/Limites_administratives/Tracer_les_limites_administratives#Limites_administratives_utilisant_des_.C3.A9l.C3.A9ments_physiques">boundary is defined by natural features (rivers) or human constructions (roads)</a>.</p>
<p>Second, the "places" which are the towns and villages. This is the populated places within the municipality polygon. Each is identified with the "place=*" tag, e.g. "place=village" + "name=Duclos". Populated places in OSM can be <a href="http://wiki.openstreetmap.org/wiki/Key:place">"city", "town", "village" or "hamlet"</a>. The limit between the values is usually based on the population but you have to check with your local OSM community or in the wiki how it is done in Canada (it has to be consistent within the country).</p>
<p>Last, you can link the municipality entity (the "boundary" + "admin_level=8" relation) to the town/village where the townhall or administration is by adding the "place" node or way in the relation with the role "admin_centre".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '14, 14:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Feb '14, 23:57</strong> </span></p>
</div>
</div>
<div id="comments-container-31054" class="comments-container">
<span id="31057"></span>
<div id="comment-31057" class="comment">
<div id="post-31057-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>in general you do not have to add addr:city to a node representing e,g, a restaurant, When all the administrative boundaries are set-up as Pieren describes, the software should be able to deduce the city from the position of the node. e.g. Nominatim (used for search on osm.org) can do this. On the other hand it is possible that some data consumers (other maps) do not properly handle all those administrative boundaries.</p>
</div>
<div id="comment-31057-info" class="comment-info">
<span class="comment-age">(26 Feb '14, 16:09)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-31054" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31054-form-container" class="comment-form-container">
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

