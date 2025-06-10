+++
type = "question"
title = "Should the way-based polygon for a city be tagged with both place=city and boundary=administrative+admin_level=8?"
description = '''Summary Some objects, such as cities, are tagged with both place=* and boundary=administrative+admin_level=*. Should it be one or the other, and if so, which one, or is there a conceivable benefit for having both sets of tags? Detailed problem description This is a Nominatim related question. I don&#x27;...'''
date = "2011-04-14T00:46:00Z"
lastmod = "2014-05-31T04:42:00Z"
weight = 4460
keywords = [ "nominatim", "administrative", "places", "tagging" ]
aliases = [ "/questions/4460" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Should the way-based polygon for a city be tagged with both place=city and boundary=administrative+admin_level=8?](/questions/4460/should-the-way-based-polygon-for-a-city-be-tagged-with-both-placecity-and-boundaryadministrativeadmin_level8)

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
<span id="post-4460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4460-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Summary</strong></p>
<p>Some objects, such as cities, are tagged with both place=* and boundary=administrative+admin_level=*. Should it be one or the other, and if so, which one, or is there a conceivable benefit for having both sets of tags?</p>
<p><strong>Detailed problem description</strong></p>
<p>This is a Nominatim related question. I don't think I will ever run out of those.</p>
<p>Here's the outline polygon for my favorite city: <a href="http://www.openstreetmap.org/browse/way/33261354">http://www.openstreetmap.org/browse/way/33261354</a></p>
<p>It's tagged with every possible key and it may be a case of TMI (too much information):</p>
<p>boundary = administrative<br />
admin_level = 8<br />
border_type = city<br />
name = Irvine<br />
place = city<br />
place_name = Irvine</p>
<p>plus a full complement of is_in tags (which may or may not be needed depending on who you ask) and the usual tiger: schema tags.</p>
<p>I don't know if place_name and border_type tags are of any consequence. However, I believe that because it is tagged as both a place=city and boundary=administrative + admin_level=8, Nominatim ends up importing it twice as two separate places, and it bothers me. Check it out:</p>
<p><a href="http://open.mapquestapi.com/nominatim/v1/details.php?place_id=36822949">Irvine as admin boundary polygon</a><br />
<a href="http://open.mapquestapi.com/nominatim/v1/details.php?place_id=36822841">Irvine as place polygon</a></p>
<p>Both point to the same OSM polygon.</p>
<p>I assume Nominatim has its reason for importing OSM places and admin boundaries separately. I am guessing it does <em>not</em> expect the same object to be tagged as both. What ends up happening, if you look at the children, is that, as far as Nominatim is concerned, one "Irvine" is a parent of the zip codes, most neighborhoods, streets, parks, etc., while the "other Irvine" is a parent of small, but not insignificant number of neighborhoods, shopping plazas, streets, etc.</p>
<p>In practical terms, when Nominatim returns a search result set or does reverse geocoding, it is going to list any street or park as being in "Irvine". Whether its one "Irvine" or the "other Irvine" is not that important to the end user, but you have to agree that the situation is pretty clumsy and is rife with potential for data integrity problems (in Nominatim, that is).</p>
<p>The fact that there is also a "third Irvine"</p>
<p><a href="http://open.mapquestapi.com/nominatim/v1/details.php?place_id=215314">Irvine as node</a></p>
<p>represented by a node tagged with place=city, with its own subset of children that are missing from either of the other two Irvines, is a whole other story.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-administrative" rel="tag" title="see questions tagged &#39;administrative&#39;">administrative</span> <span class="post-tag tag-link-places" rel="tag" title="see questions tagged &#39;places&#39;">places</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Apr '11, 00:46</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Apr '11, 01:20</strong> </span></p>
</div>
</div>
<div id="comments-container-4460" class="comments-container">
<span id="4472"></span>
<div id="comment-4472" class="comment">
<div id="post-4472-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey, this sounds quite similar to my recent question: <a href="http://help.openstreetmap.org/questions/4068/when-does-it-make-sense-to-use-place-on-an-area">http://help.openstreetmap.org/questions/4068/when-does-it-make-sense-to-use-place-on-an-area</a> Good that there's some more discussion on where the <code>place</code> tag is appropriate.</p>
</div>
<div id="comment-4472-info" class="comment-info">
<span class="comment-age">(14 Apr '11, 11:07)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="4494"></span>
<div id="comment-4494" class="comment">
<div id="post-4494-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Similar, yet different. You ask when to use one set of tags vs. the other. I ask if it;s ever a good idea to use both. I am slowly arriving at a conclusion that there isn't, albeit without any input from the gurus.</p>
</div>
<div id="comment-4494-info" class="comment-info">
<span class="comment-age">(14 Apr '11, 19:22)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="4510"></span>
<div id="comment-4510" class="comment">
<div id="post-4510-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why didn't you guys tell me that my links don't work (because of the escaped underscore?) Let me update them and see if the question gets an actual answer.</p>
</div>
<div id="comment-4510-info" class="comment-info">
<span class="comment-age">(14 Apr '11, 23:28)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-4460" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4460-form-container" class="comment-form-container">
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

<span id="4461"></span>

<div id="answer-container-4461" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4461-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Check out the "As Areas" section in the wiki page for <a href="http://wiki.openstreetmap.org/wiki/Key:place">place</a>. One suggestion there is to mark a node as the "centre" of the city (where the name will go) with place=city. Create a boundary=administrative relation for the perimeter (with the appropriate admin level), and make the node a member of the relation with role=admin_centre. See also the <a href="http://wiki.openstreetmap.org/wiki/Relation:boundary">Relation:boundary</a> page.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '11, 02:43</strong></p>
<img src="https://secure.gravatar.com/avatar/f075add936ab95d2d368f2e48f5ddc22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ebenezer&#39;s gravatar image" />
<p><span>Ebenezer</span><br />
<span class="score" title="948 reputation points">948</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ebenezer has 2 accepted answers">9%</span> </br></br></p>
</div>
</div>
<div id="comments-container-4461" class="comments-container">
<span id="4462"></span>
<div id="comment-4462" class="comment">
<div id="post-4462-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, I have seen those. The "As areas" best practice is actually a pretty poor piece of advice written without any thought of what having a place node and an admin boundary for the same city, county, etc. object will do to Nominatim searches. I have researched and talked about this issue extensively over the past two days. The consensus today is to <em>delete</em> the place node when a polygon is available, not <em>add</em> one. Adding a node to a relation with a "label" role is a swell idea, but it is not currently supported by renderers.</p>
</div>
<div id="comment-4462-info" class="comment-info">
<span class="comment-age">(14 Apr '11, 03:39)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="33568"></span>
<div id="comment-33568" class="comment">
<div id="post-33568-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><em>Adding a node to a relation with a "label" role is a swell idea, but it is not currently supported by renderers.</em></p>
<p>True, but doesn't that mean the correct course would be 'add nodes with no tags but with role=label', and lean on render developers to support that?</p>
<p>Particularly since "delete the place node when a polygon is available, not add one" seems to be the best/accepted practice, and in that case, most renderers show <em>nothing at all</em> on a map for a border relation without a place node -- right?</p>
</div>
<div id="comment-33568-info" class="comment-info">
<span class="comment-age">(30 May '14, 22:03)</span> <span class="comment-user userinfo">Skybunny</span>
</div>
</div>
<span id="33572"></span>
<div id="comment-33572" class="comment">
<div id="post-33572-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that this is a pretty old discussion. One of the Nominatim maintainers recently wrote (here? talk@?) that it is <strong>not</strong> a good idea to remove the place node if there is a boundary.</p>
</div>
<div id="comment-33572-info" class="comment-info">
<span class="comment-age">(31 May '14, 04:42)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-4461" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4461-form-container" class="comment-form-container">
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

