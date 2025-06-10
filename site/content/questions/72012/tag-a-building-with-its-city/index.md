+++
type = "question"
title = "tag a building with its city"
description = '''I am trying to tag a building but cannot get the city right. I have provided values for addr:housenumber, addr:street, addr:postcode and addr:city but when I right-click on the building in openstreetmap.org and ask for the address it gets everything right except for the city. We seem to be inheritin...'''
date = "2019-12-05T19:26:00Z"
lastmod = "2019-12-07T07:03:00Z"
weight = 72012
keywords = [ "city", "nominatim" ]
aliases = [ "/questions/72012" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [tag a building with its city](/questions/72012/tag-a-building-with-its-city)

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
<span id="post-72012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72012-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to tag a building but cannot get the city right. I have provided values for addr:housenumber, addr:street, addr:postcode and addr:city but when I right-click on the building in openstreetmap.org and ask for the address it gets everything right except for the city. We seem to be inheriting the name of an entity nearby that is characterized as follows:</p>
<ul>
<li>place hamlet</li>
<li>gnis:Class Populated Place</li>
</ul>
<p>I have tried using the tags addr:hamlet, addr:district, addr:province, addr:subdistrict, and addr:suburb but none of them work.</p>
<p>Is there a way to override this default?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Dec '19, 19:26</strong></p>
<img src="https://secure.gravatar.com/avatar/89d05342bbe4395e1bd01bdf0202269d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edkademan&#39;s gravatar image" />
<p><span>edkademan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edkademan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72012" class="comments-container">
<span id="72013"></span>
<div id="comment-72013" class="comment">
<div id="post-72013-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Ed, can you link to the building in question?</p>
</div>
<div id="comment-72013-info" class="comment-info">
<span class="comment-age">(05 Dec '19, 20:40)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="72017"></span>
<div id="comment-72017" class="comment">
<div id="post-72017-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, Thanks for responding. I'm not sure of the best way to supply a link but the following gets you in the neighborhood:</p>
<p><a href="https://www.openstreetmap.org/#map=19/42.99725/-78.12668">https://www.openstreetmap.org/#map=19/42.99725/-78.12668</a></p>
<p>I'm trying to get the address for the building labelled "Farm House" for example to include the city of Batavia but it gives "Five Corners" instead.</p>
</div>
<div id="comment-72017-info" class="comment-info">
<span class="comment-age">(06 Dec '19, 09:50)</span> <span class="comment-user userinfo">edkademan</span>
</div>
</div>
<span id="72019"></span>
<div id="comment-72019" class="comment">
<div id="post-72019-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here's the details page for the street: <a href="https://nominatim.openstreetmap.org/details.php?place_id=78244064">https://nominatim.openstreetmap.org/details.php?place_id=78244064</a></p>
<p>Do note that adding tags to manipulate the behavior of one service is frowned upon. I understand you are trying to find something that works at the moment, but the extra tags on the buildings should be cleaned up and so on.</p>
</div>
<div id="comment-72019-info" class="comment-info">
<span class="comment-age">(06 Dec '19, 11:02)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="72021"></span>
<div id="comment-72021" class="comment">
<div id="post-72021-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Nominatim looks at the city boundaries (<a href="https://www.openstreetmap.org/relation/176203)">https://www.openstreetmap.org/relation/176203)</a> and the street is outside. I know people on the ground often say a place belongs to a city when it's outside the boundaries, but it's harder for computers to know when to ignore information.</p>
</div>
<div id="comment-72021-info" class="comment-info">
<span class="comment-age">(06 Dec '19, 11:29)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="72022"></span>
<div id="comment-72022" class="comment">
<div id="post-72022-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>place_id changes whenever the database gets reimported. This is the same URL <a href="https://nominatim.openstreetmap.org/details.php?osmtype=W&amp;osmid=20644760">https://nominatim.openstreetmap.org/details.php?osmtype=W&amp;osmid=20644760</a></p>
</div>
<div id="comment-72022-info" class="comment-info">
<span class="comment-age">(06 Dec '19, 11:31)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="72027"></span>
<div id="comment-72027" class="comment not_top_scorer">
<div id="post-72027-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>furthermore, are "Barn" and "Garden Shed" really the names of the buildings? Or should that be tagged as building=barn and building=shed instead?</p>
</div>
<div id="comment-72027-info" class="comment-info">
<span class="comment-age">(07 Dec '19, 07:03)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-72012" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-72012-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="72014"></span>

<div id="answer-container-72014" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72014-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-72014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The geocoder that powers that feature, <a href="https://nominatim.openstreetmap.org/">https://nominatim.openstreetmap.org/</a>, does not index those address tags.</p>
<p>(it associates a <code>highway</code> with a given city and then links addresses to that <code>highway</code>)</p>
<p>The <code>place=hamlet</code> tag might be sensibly changed to something else, if the thing really is something else. The <code>gnis:Class</code> tag is from the import of the data and not really used by anything.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Dec '19, 22:12</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-72014" class="comments-container">
&#10;</div>
<div id="comment-tools-72014" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72014-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72024"></span>

<div id="answer-container-72024" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72024-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's best to think of the map at openstreetmap.org as a demo, of the OSM database and of some of the mapping technologies that have arisen along with it -- map rendering, map search, routing.</p>
<p>In this case, the right-click "Show Address" feature demonstrates the reverse geocoding capabilities of the search tool Nominatim.</p>
<p>"Reverse geocoding" means taking map coordinates and attempting to deduce the address. In its simplest form, it does <em>not</em> look at any of the data tags of the building, but instead just tries to make a best guess based on the coordinates. In this implementation it <em>does</em> try to pull some data from the building (the building name and housenumber) but takes the city name strictly from the coordinates, which, as Maxerikson mentioned, are outside the city limits of Batavia.</p>
<p>My guess is that it assigns the city name Five Corners since it's the nearest placename that does not have distinct boundaries -- it's just indicated by a node. Nominatim "knows" the building isn't in Batavia so it's looking for the nearest place it <em>might</em> be in.</p>
<p>I can see how this might not look like ideal behavior. Nominatim, like everything else in the OSM world, is under constant development, and you could open a issue at the <a href="https://github.com/openstreetmap/Nominatim">Nominatim Github page</a> to suggest different behavior. Don't hold your breath, though, because there may well be a very good reason for this design choice.</p>
<p>The good news is that the city is tagged correctly on the building, so if you want to see the house with the correct address just use the link <a href="https://www.openstreetmap.org/way/182393593">https://www.openstreetmap.org/way/182393593</a>.</p>
<p>Btw, it looks like as of now there's still one incorrect address tag, <code>addr:province=Batavia</code>. Best to delete that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '19, 17:34</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Dec '19, 17:44</strong> </span></p>
</div>
</div>
<div id="comments-container-72024" class="comments-container">
&#10;</div>
<div id="comment-tools-72024" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72024-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72026"></span>

<div id="answer-container-72026" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72026-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks to all those who took the time to answer my question. I have a better appreciation for how openstreetmap and the geocoding applications relate now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '19, 23:20</strong></p>
<img src="https://secure.gravatar.com/avatar/89d05342bbe4395e1bd01bdf0202269d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edkademan&#39;s gravatar image" />
<p><span>edkademan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edkademan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72026" class="comments-container">
&#10;</div>
<div id="comment-tools-72026" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72026-form-container" class="comment-form-container">
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

