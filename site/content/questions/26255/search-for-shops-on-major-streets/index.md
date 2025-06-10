+++
type = "question"
title = "Search for shops on major streets"
description = '''Hello, WE have a nominatim database setup on AWS with all the streets in the planet. We are trying to find all shops, museums etc on major streets, for example Oxford Street (London). Does anyone know how this is possible using sql? Which tables i.e placex and others we should run a query on and how...'''
date = "2013-09-10T16:08:00Z"
lastmod = "2013-09-13T09:16:00Z"
weight = 26255
keywords = [ "shop", "museum", "nominatim" ]
aliases = [ "/questions/26255" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Search for shops on major streets](/questions/26255/search-for-shops-on-major-streets)

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
<span id="post-26255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26255-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>WE have a <strong>nominatim</strong> database setup on AWS with all the streets in the planet. We are trying to find all shops, museums etc on <em>major streets</em>, for example Oxford Street (London). Does anyone know how this is possible using sql? Which tables i.e <em>placex</em> and others we should run a query on and how we can run joins?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shop" rel="tag" title="see questions tagged &#39;shop&#39;">shop</span> <span class="post-tag tag-link-museum" rel="tag" title="see questions tagged &#39;museum&#39;">museum</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Sep '13, 16:08</strong></p>
<img src="https://secure.gravatar.com/avatar/e567ac886de3df68c63f58ce75365a2c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mezbaur&#39;s gravatar image" />
<p><span>mezbaur</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mezbaur has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Sep '13, 16:19</strong> </span></p>
</div>
</div>
<div id="comments-container-26255" class="comments-container">
<span id="26270"></span>
<div id="comment-26270" class="comment">
<div id="post-26270-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hi, then tell us first how a computer or a database should know what street is a major street, and which is not. The general classification on street types are defined at <a href="http://wiki.openstreetmap.org/wiki/Key:highway">http://wiki.openstreetmap.org/wiki/Key:highway</a> ... but does this help?</p>
<p>Or do you have a manual selection of streets that are in your focus?</p>
</div>
<div id="comment-26270-info" class="comment-info">
<span class="comment-age">(11 Sep '13, 08:26)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="26278"></span>
<div id="comment-26278" class="comment">
<div id="post-26278-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We want to search on primary streets <a href="http://wiki.openstreetmap.org/wiki/Tag:highway%3Dprimary">http://wiki.openstreetmap.org/wiki/Tag:highway%3Dprimary</a> for example Oxford Street and bring back all shops on that street.</p>
</div>
<div id="comment-26278-info" class="comment-info">
<span class="comment-age">(11 Sep '13, 11:02)</span> <span class="comment-user userinfo">mezbaur</span>
</div>
</div>
<span id="26289"></span>
<div id="comment-26289" class="comment">
<div id="post-26289-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>next question:</p>
<p>How do you define whether a POI belongs to a primary street or not? Is it enough do determine them via addr-tags? in many aread addr-tags are not complete in OSM data.</p>
<p>Or do you aim at a certain distance? is it then 30 meters or 50 meters or 100 meters from the center of the street line?</p>
<p>So before thinking about a concrete SQL query, be aware how you will find your objects in a logical way. Are you really familiar with the OSM data elements, and how they interact to each other and how not?</p>
</div>
<div id="comment-26289-info" class="comment-info">
<span class="comment-age">(11 Sep '13, 15:34)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="26292"></span>
<div id="comment-26292" class="comment">
<div id="post-26292-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for making asking some valid questions. I am a newbie on OSM and Nominatim.</p>
</div>
<div id="comment-26292-info" class="comment-info">
<span class="comment-age">(11 Sep '13, 17:52)</span> <span class="comment-user userinfo">mezbaur</span>
</div>
</div>
</div>
<div id="comment-tools-26255" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26255-form-container" class="comment-form-container">
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

<span id="26312"></span>

<div id="answer-container-26312" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26312-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-26312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mezbaur has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The main problem is indeed to define what is a major road and what is the POI you are looking for. If you can define that in terms of an OSM tag then you can do a simple self-join on <code>placex</code> using distance between geometries and filtering by class and type.</p>
<p>For example, lets say you want all shops close to a <code>highway=primary</code> in Great Britain, you'd do something like:</p>
<pre><code>select shop.place_id, road.name-&gt;&#39;name&#39;
  from placex as road, placex as shop
 where road.class = &#39;highway&#39; and road.type = &#39;primary&#39; and road.calculated_country_code = &#39;gb&#39;
   and shop.class = &#39;shop&#39;
   and ST_DWithin(road.geometry, shop.geometry, 0.01);</code></pre>
<p>If you want to search for all major roads as defined in Nominatim's details view you can also search by rank:</p>
<pre><code>select shop.place_id, road.name-&gt;&#39;name&#39;
  from placex as road, placex as shop
 where road.class = &#39;highway&#39; and road.rank_search = 26 and road.calculated_country_code = &#39;gb&#39;
   and shop.class = &#39;shop&#39;
   and ST_DWithin(road.geometry, shop.geometry, 0.01);</code></pre>
<p>This will even be faster because there is an index over rank_search. (The highway constraint is still necessary so you don't end up with things like airports which are also in this rank.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Sep '13, 19:17</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-26312" class="comments-container">
<span id="26319"></span>
<div id="comment-26319" class="comment">
<div id="post-26319-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@lonvia</span>, many thanks! I will try it and check the results.</p>
</div>
<div id="comment-26319-info" class="comment-info">
<span class="comment-age">(13 Sep '13, 09:16)</span> <span class="comment-user userinfo">mezbaur</span>
</div>
</div>
</div>
<div id="comment-tools-26312" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26312-form-container" class="comment-form-container">
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

