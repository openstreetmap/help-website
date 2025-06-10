+++
type = "question"
title = "adding new column in osm database"
description = '''i am new to openstreetmap. Basically, I am working on a project where i am collecting dynamic road conditions from users. Once they submit, it will be rendered in the osm. Also, we will use it in our algorithms such as shortest path avoiding those nodes and edges. My question is how do i add these e...'''
date = "2013-12-27T06:03:00Z"
lastmod = "2013-12-27T10:37:00Z"
weight = 29351
keywords = [ "dynamic", "condition", "road" ]
aliases = [ "/questions/29351" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [adding new column in osm database](/questions/29351/adding-new-column-in-osm-database)

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
<span id="post-29351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29351-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i am new to openstreetmap. Basically, I am working on a project where i am collecting dynamic road conditions from users. Once they submit, it will be rendered in the osm. Also, we will use it in our algorithms such as shortest path avoiding those nodes and edges. My question is how do i add these extra dynamic road conditions coming from the user? If i want to add a new column such as number of lanes, or dynamic attributes such as an accident has happened in a certain node? I appreciate your kind response.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-dynamic" rel="tag" title="see questions tagged &#39;dynamic&#39;">dynamic</span> <span class="post-tag tag-link-condition" rel="tag" title="see questions tagged &#39;condition&#39;">condition</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Dec '13, 06:03</strong></p>
<img src="https://secure.gravatar.com/avatar/7ca5c1be3cfc90f13ed04f4c1a313ce5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdrahman&#39;s gravatar image" />
<p><span>mdrahman</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdrahman has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29351" class="comments-container">
&#10;</div>
<div id="comment-tools-29351" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29351-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="29366"></span>

<div id="answer-container-29366" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29366-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Static data like number of lanes etc. is fine to keep in OSM (it is very welcome, even); note that when letting your users edit OSM data through an app, those users will need to have personal accounts with OSM (you cannot create one single account in OSM and upload all your user edits under that one single account).</p>
<p>Dynamic data like traffic flow or accident information has no room in OSM and you will have to add that to a separate table in your local database, possibly keyed against OSM IDs so that you can merge OSM and your dynamic data with appropriate queries.</p>
<p>Note that there may be license implications - if your dynamic data is in any way "derived" from OSM, perhaps in that the user used an OSM map as a reference when they identified the traffic condition, then your dynamic data would have to be made available under the ODbL (see our <a href="http://wiki.openstreetmap.org/wiki/Legal%20FAQ">Legal FAQ).</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '13, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-29366" class="comments-container">
&#10;</div>
<div id="comment-tools-29366" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29366-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29352"></span>

<div id="answer-container-29352" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29352-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you collecting the information using OSM editors (Potlatch/JOSM/iD)? If so, you can add another attribute fields in the category type. For example when name of the road is being updated, similarly condition of the road, number of lanes etc also can be collected.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '13, 06:12</strong></p>
<img src="https://secure.gravatar.com/avatar/c59921537afd0b14f63f47aac9b4b600?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GoldenCompass&#39;s gravatar image" />
<p><span>GoldenCompass</span><br />
<span class="score" title="40 reputation points">40</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GoldenCompass has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29352" class="comments-container">
<span id="29353"></span>
<div id="comment-29353" class="comment">
<div id="post-29353-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wao. That is too fast. Thanks GoldenCompass. To clarify my question here is what i am planning to do:</p>
<blockquote>
<blockquote>
<p>OSM editors (Potlatch/JOSM/iD) I am using your beautiful openstreetmap web editor to add nodes, lines and areas.</p>
</blockquote>
</blockquote>
<ol>
<li>Imagine that i want users on the street to tell me that there is an accident/flood/lane closure...</li>
<li>A user on the spot will tap an app developed by us such as checkbox to give us feedback in real-time</li>
<li>we want to store this dynamic road conditions in OSM postGIS db so that</li>
<li>in our shortest path algorithm I can find which node(s) and edge this has happened and is it within my shortest route</li>
<li>I will recalculate the path from road network in OSM database using shortest path algorithm avoiding these routes</li>
</ol>
<p>I appreciate your kind reply.</p>
</div>
<div id="comment-29353-info" class="comment-info">
<span class="comment-age">(27 Dec '13, 06:22)</span> <span class="comment-user userinfo">mdrahman</span>
</div>
</div>
<span id="29358"></span>
<div id="comment-29358" class="comment">
<div id="post-29358-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you maintaining your own servers and editors like OSM to store the data with required attributes? If you are editing on OSM website, it may not be available to you and you may also not get the customized attribute information as per your requirement.</p>
<p>If you are using OSM editors to add the data and then downloading the data for your usage, you may have to think differently like take road network information from OSM data as a layer while accident points etc as another layer and display it in your application.</p>
</div>
<div id="comment-29358-info" class="comment-info">
<span class="comment-age">(27 Dec '13, 08:39)</span> <span class="comment-user userinfo">GoldenCompass</span>
</div>
</div>
<span id="29362"></span>
<div id="comment-29362" class="comment">
<div id="post-29362-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Actually, I am just starting to collect the OSM part. I already expressed my scenario. We will provide an app (desktop + smartphone) that will allow them to add POIs, road names, intersections, speed limit... so that these are added to the openstreetmap database and can be visible to your openstreemap website. However, we need to run algorithms to find shortest paths. Hence, we need to maintain a nightly build of the latest OSM database of our city. The only hurdle here is we have to add some dynamic constraints that will be used in our query language. I am not sure how to proceed. In summary, doing processing on local database but everything else in openstreetmap website/database. I hope I could express you. Thanks ahead</p>
</div>
<div id="comment-29362-info" class="comment-info">
<span class="comment-age">(27 Dec '13, 08:48)</span> <span class="comment-user userinfo">mdrahman</span>
</div>
</div>
</div>
<div id="comment-tools-29352" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29352-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29364"></span>

<div id="answer-container-29364" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29364-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is an agreement that on OSM we do not map temporary nor highly dynamic features like <a href="http://wiki.openstreetmap.org/wiki/Talk:Tag:amenity%3Dfuel#Prices">gasoline[1]</a> <a href="http://forum.openstreetmap.org/viewtopic.php?id=19327">prices[2]</a>, accidents, minor short lived construction sites, <a href="http://wiki.openstreetmap.org/wiki/Talk:Proposed_features/farmland#landuse.3Dagricultural_produce.3D.2A">produce on farmland</a> and such.<br />
But of course you are free to use the OSM map/data with an extra layer on it to display the data you collect - be it traffic jams, <a href="http://tom.acrewoods.net/2013/09/12/mapping-dirty-london/">air pollution</a>, flash mobs or a <a href="http://www.apps-bahn.de/bin/livemap/query-livemap.exe/dn?L=vs_livefahrplan&amp;livemap=yes">live railway map</a>.<br />
Other people luckily think straightforward about using an <a href="https://lists.openstreetmap.org/pipermail/dev/2009-April/014907.html">external service</a> for what you want to try.<br />
</p>
<p>Good luck! :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '13, 09:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Dec '13, 09:33</strong> </span></p>
</div>
</div>
<div id="comments-container-29364" class="comments-container">
&#10;</div>
<div id="comment-tools-29364" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29364-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29365"></span>

<div id="answer-container-29365" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29365-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As malenki has told that we don't map highly dynamic thing features on osm website but if you are having your own setup (like OSM) to collect data required for you, you are free to do so. However your requirement can be fulfilled as mashup application where you can use no. of layers from different sources visualising it at common platform.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '13, 09:34</strong></p>
<img src="https://secure.gravatar.com/avatar/c59921537afd0b14f63f47aac9b4b600?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GoldenCompass&#39;s gravatar image" />
<p><span>GoldenCompass</span><br />
<span class="score" title="40 reputation points">40</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GoldenCompass has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-29365" class="comments-container">
&#10;</div>
<div id="comment-tools-29365" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29365-form-container" class="comment-form-container">
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

