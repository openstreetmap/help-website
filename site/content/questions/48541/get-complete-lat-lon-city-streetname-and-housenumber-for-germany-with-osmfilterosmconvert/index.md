+++
type = "question"
title = "Get complete lat, lon, city, streetname and housenumber for germany with osmfilter/osmconvert"
description = '''Hello, I would like to have lat, lon and adress for every adress in germany.  The problem with my codesnippet is, that it seems that I get every street as a result, but with large gaps between housenumbers. When I visit osm in my browser, I can see housenumbers on the map which are surprisingly not ...'''
date = "2016-03-07T13:10:00Z"
lastmod = "2016-03-07T18:34:00Z"
weight = 48541
keywords = [ "lat", "germany", "adresses", "lon" ]
aliases = [ "/questions/48541" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Get complete lat, lon, city, streetname and housenumber for germany with osmfilter/osmconvert](/questions/48541/get-complete-lat-lon-city-streetname-and-housenumber-for-germany-with-osmfilterosmconvert)

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
<span id="post-48541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48541-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I would like to have lat, lon and adress for every adress in germany. The problem with my codesnippet is, that it seems that I get every street as a result, but with large gaps between housenumbers. When I visit osm in my browser, I can see housenumbers on the map which are surprisingly not contained in my csv. But I want all adresses with coordinates, and when I can see adresses in the browser, I know its possible to extract the whole set into a csv. file.</p>
<p>This is my code snippet: osmfilter deutschland.osm --keep="addr:country= and addr:city= and addr:postcode= and addr:street= addr:housenumber=" --ignore-dependencies | osmconvert - --csv="@oname <a href="http://help.openstreetmap.org/users/260/idoneus">@id</a> <a href="http://help.openstreetmap.org/users/1350/longestaugust">@lon</a> <a href="http://help.openstreetmap.org/users/5110/latroc">@lat</a> addr:country addr:city addr:postcode addr:street addr:housenumber" -o=deutschland.csv</p>
<p>I want complete adresses, or to be more precise: lat, lon, city, street, housenumber. For every housenumber in germany.</p>
<p>Thank you for your professional help.</p>
<p>Greetz</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lat" rel="tag" title="see questions tagged &#39;lat&#39;">lat</span> <span class="post-tag tag-link-germany" rel="tag" title="see questions tagged &#39;germany&#39;">germany</span> <span class="post-tag tag-link-adresses" rel="tag" title="see questions tagged &#39;adresses&#39;">adresses</span> <span class="post-tag tag-link-lon" rel="tag" title="see questions tagged &#39;lon&#39;">lon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Mar '16, 13:10</strong></p>
<img src="https://secure.gravatar.com/avatar/4aeaae6ed1cbb7581b9338affb59e4d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stephano007&#39;s gravatar image" />
<p><span>Stephano007</span><br />
<span class="score" title="61 reputation points">61</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stephano007 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48541" class="comments-container">
&#10;</div>
<div id="comment-tools-48541" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48541-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="48542"></span>

<div id="answer-container-48542" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48542-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It would seem as if osmconvert is doing exactly what you asked it to, just not what you actually wanted.</p>
<p>There are a number of obvious misconceptions present in the arguments</p>
<ul>
<li>that every object with a tagged address has addr:country, addr:city and addr:postcode values. That is not the case and while there are some discussions around if it best to add redundant information or not, in practice the information will very very often be missing because it can be derived from administrative and postcode boundaries enclosing the object in question.</li>
<li>every address has a addr:street tag: on the one hand addr:place is just as valid when there is no associated street for the address and historically not tagging the street was a legimate option (the nearest street was then considered to be part of the address). Further the street information can be contained in a "associatedStreet" relation which the object with a housenumber is a member of.</li>
<li>and naturally there are address interpolations too.</li>
</ul>
<p>As you can see there is some work and heuristics involved in producing a complete addess hierarchy from OSM data. It could be very well be that a local nominatim installation containing the data for Germany would be an easier and better solution than trying to build it yourself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '16, 14:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Mar '16, 08:15</strong> </span></p>
</div>
</div>
<div id="comments-container-48542" class="comments-container">
<span id="48544"></span>
<div id="comment-48544" class="comment">
<div id="post-48544-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank your for your answer.</p>
<p>Ok, I see the point, looks like a lot of programming. Work, that already seemed to be done by nominatim.</p>
<p>When I have a database, with lets say 100.000 adresses, could Nominatim api provide me with the fitting lat / lon? Automatically, so I dont have to do it manually for every adress? Can Nominatim also write back to DB?</p>
<p>Thank you for your expertise,</p>
<p>Greetz, Stephano</p>
</div>
<div id="comment-48544-info" class="comment-info">
<span class="comment-age">(07 Mar '16, 14:47)</span> <span class="comment-user userinfo">Stephano007</span>
</div>
</div>
<span id="48553"></span>
<div id="comment-48553" class="comment">
<div id="post-48553-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello SimonPoole, you seem to have a good kind of overview, please answer my questions ^^). I have certain adresses, can I enrich for example 1000 of those adresses with lat/lon by using a local nominatim installation?</p>
<p>Is it possible to automatize this process? So could I connect nominatim to my db or generate a .csv file with it? Because I would like to give adress as input, and get lat/lon as result.</p>
</div>
<div id="comment-48553-info" class="comment-info">
<span class="comment-age">(07 Mar '16, 18:08)</span> <span class="comment-user userinfo">Stephano007</span>
</div>
</div>
<span id="48554"></span>
<div id="comment-48554" class="comment">
<div id="post-48554-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, this is possible. Nominatim has a simple HTTP API which you can use for geocoding your addresses.</p>
</div>
<div id="comment-48554-info" class="comment-info">
<span class="comment-age">(07 Mar '16, 18:34)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48542" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48542-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48551"></span>

<div id="answer-container-48551" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48551-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should also pay attention that there are at least two other options to tag a complete address, at least in Germany:</p>
<p>addr:housenumber=* AND addr:place=xxxx ... for villages and hamlets which are so small that there are no extra street names,</p>
<p>and</p>
<p>OSM relations of type=associatedStreet ... see <a href="http://wiki.openstreetmap.org/wiki/Relation:associatedStreet">Relation:associatedStreet</a> in the OSM wiki.</p>
<p>If you are able to read in German, also have a look at this <a href="http://blog.openstreetmap.de/blog/2016/02/wochenaufgabe-strassennamen-neuauflage/">article</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '16, 16:56</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-48551" class="comments-container">
<span id="48552"></span>
<div id="comment-48552" class="comment">
<div id="post-48552-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>ahemmm didn't I already point that out? :-)</p>
</div>
<div id="comment-48552-info" class="comment-info">
<span class="comment-age">(07 Mar '16, 16:59)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48551" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48551-form-container" class="comment-form-container">
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

