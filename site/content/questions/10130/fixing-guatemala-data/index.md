+++
type = "question"
title = "Fixing Guatemala Data"
description = '''Hi, I have worked with maps mainly with google maps, but since change in terms after taking all our mapmaker data, I have decided to move my mapping projects with OSM.  I made some contributions on OSM but I now I have seen some contradictions in OSM for my country, so before starting to change data...'''
date = "2012-01-22T17:17:00Z"
lastmod = "2012-01-23T04:07:00Z"
weight = 10130
keywords = [ "guatemala", "nominatim", "editor" ]
aliases = [ "/questions/10130" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Fixing Guatemala Data](/questions/10130/fixing-guatemala-data)

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
<span id="post-10130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10130-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have worked with maps mainly with google maps, but since change in terms after taking all our mapmaker data, I have decided to move my mapping projects with OSM.</p>
<p>I made some contributions on OSM but I now I have seen some contradictions in OSM for my country, so before starting to change data will like some advice.</p>
<p>Level 1 Our country is divided in departments (like states) but there no see to be a polygon with that data only a point with place:state. Is this the correct way to set or a boundary polygon should be added?</p>
<p>Level 2 are municipalities same as level 1.</p>
<p>Level 3 cities, in this case city limit is not well defined since can take all its municipality, the thing with cities is that are divided in Zones (Well delimited) (like suburbs or zipcodes areas) I see our cities, suburbs are points like cities so if you make a nominatim search some places can return other zona (suburn) or other Colonia (like districts inside a zona, but not administrative)</p>
<p>Right now Colonia are tagged as Hamlets, but again as points. reverse geocoding some Colonia (hamlets) seems to have more precedence that others even suburbs.</p>
<p>I want to understand how is the best way to do it in order to start working.</p>
<p>Example.. <a href="http://open.mapquestapi.com/nominatim/v1/search.php?q=12+calle+zona+9+guatemala&amp;viewbox=-254.54%2C82.93%2C254.54%2C-75.63">http://open.mapquestapi.com/nominatim/v1/search.php?q=12+calle+zona+9+guatemala&amp;viewbox=-254.54%2C82.93%2C254.54%2C-75.63</a></p>
<p>returns Montufar, Zona 9, Colonia Lomas de Pamplona, El Progreso, 01011</p>
<p>Zona 9 is the correct suburb, but Colonia Lomas de Pamplona is not and is tagged as hamlet and should be out of Zona 9 suburb, is in other suburn (zona 13), El progreso is a state name but like 60kms away, and 01011 I dont know what it is.. maybe a zipcode but is incorrect.</p>
<p>So what you suggest to start the fix ?</p>
<p>regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-guatemala" rel="tag" title="see questions tagged &#39;guatemala&#39;">guatemala</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-editor" rel="tag" title="see questions tagged &#39;editor&#39;">editor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jan '12, 17:17</strong></p>
<img src="https://secure.gravatar.com/avatar/f33b256927bada8157d5158dd0f6e710?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neavilag&#39;s gravatar image" />
<p><span>neavilag</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neavilag has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-10130" class="comments-container">
&#10;</div>
<div id="comment-tools-10130" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10130-form-container" class="comment-form-container">
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

<span id="10140"></span>

<div id="answer-container-10140" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10140-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Polygons work better when searching in the nominatim as streets get linked to nearest place node otherwise, so often that gives an incorrect result. The problem is knowing the boundary of the polygon you wish to map without infringing copyright I have only been able to use local knowledge or very old out of copyright maps. If you can create a polygon and comply with copyright it is best to delete the place node afterwards.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '12, 22:16</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span> </br></p>
</div>
</div>
<div id="comments-container-10140" class="comments-container">
<span id="10145"></span>
<div id="comment-10145" class="comment">
<div id="post-10145-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>See also the country list on boundary=administrative <a href="http://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative">http://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative</a> for sub-national boundaries. (The values for Guatemala suggest that they are only proposed.)</p>
</div>
<div id="comment-10145-info" class="comment-info">
<span class="comment-age">(23 Jan '12, 02:10)</span> <span class="comment-user userinfo">Ebenezer</span>
</div>
</div>
<span id="10146"></span>
<div id="comment-10146" class="comment">
<div id="post-10146-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Suburb limits are available since are official, but is odd to get a name of a "colonia"=Neighborhood of a place that is officially other suburb, neighborhoods are now tagged as hamlets, do you think could help to tag it as is_in:suburb = XXXXX to force to stay in that suburb ?</p>
</div>
<div id="comment-10146-info" class="comment-info">
<span class="comment-age">(23 Jan '12, 04:07)</span> <span class="comment-user userinfo">neavilag</span>
</div>
</div>
</div>
<div id="comment-tools-10140" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10140-form-container" class="comment-form-container">
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

