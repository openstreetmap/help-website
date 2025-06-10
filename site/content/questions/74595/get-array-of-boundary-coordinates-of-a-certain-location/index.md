+++
type = "question"
title = "Get Array of boundary coordinates of a certain location."
description = '''Hello, Can anyone please help me get the array of boundary coordinates (lat and lng) of a certain location? Attached with this post is an example showing a screenshot that shows the boundary of the district, &quot;Munshiganj&quot; of Dhaka City in Bangladesh. I want to extract the boundary coordinates of this...'''
date = "2020-05-04T09:16:00Z"
lastmod = "2020-05-05T17:48:00Z"
weight = 74595
keywords = [ "boundaries", "json", "bangladesh", "coordinates" ]
aliases = [ "/questions/74595" ]
osqa_answers = 7
osqa_accepted = true
+++

<div class="headNormal">

# [Get Array of boundary coordinates of a certain location.](/questions/74595/get-array-of-boundary-coordinates-of-a-certain-location)

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
<span id="post-74595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74595-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, Can anyone please help me get the array of boundary coordinates (lat and lng) of a certain location?</p>
<p>Attached with this post is an example showing a screenshot that shows the boundary of the district, "Munshiganj" of Dhaka City in Bangladesh. I want to extract the boundary coordinates of this location and other locations as well in a JSON file.</p>
<p><a href="https://ibb.co/q5yPwv0"><img src="https://i.ibb.co/m8DM73v/image.png" data-border="0" alt="image" /></a><br />
<a href="https://imgbb.com/">img photo hosting</a><br />
</p>
<p>My main goal is to get boundary coordinates of all locations of Bangladesh in a JSON file.</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-bangladesh" rel="tag" title="see questions tagged &#39;bangladesh&#39;">bangladesh</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 May '20, 09:16</strong></p>
<img src="https://secure.gravatar.com/avatar/d14fcae6ba396f4830f9b10eb507c849?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hotmailbelike&#39;s gravatar image" />
<p><span>hotmailbelike</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hotmailbelike has no accepted answers">0%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 May '20, 07:43</strong> </span></p>
</div>
</div>
<div id="comments-container-74595" class="comments-container">
&#10;</div>
<div id="comment-tools-74595" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74595-form-container" class="comment-form-container">
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

7 Answers:

</div>

</div>

<span id="74627"></span>

<div id="answer-container-74627" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74627-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hotmailbelike has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>These queries use the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide">Overpass QL</a> language. Please read about.</p>
<p>I think that you should run the query once, store the GeoJSON, and extracts the array of coordinates from there. It will be way more efficient that calling the crowded overpass API each time, to get exactly the same data. This becomes a JS (or whatever language you're using) problem, just look at the structure of the GeoJSON file.</p>
<p>Otherwise, here is a <a href="https://overpass-turbo.eu/s/TF6">query</a> that will return you only the coordinates of the nodes of the border of a specific district.</p>
<p>Really close, this <a href="https://overpass-turbo.eu/s/TF7">one</a> returns the geometry of the relation, as an array of coordinates ! The <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Geometry">geom</a> keyword is the key here.</p>
<p>To combine the first and last approach, you can download all the bangladesh's borders with this <a href="https://overpass-turbo.eu/s/TF8">query</a>. The result should be easier to use that the first proposition, as the geometry is included is each object.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '20, 17:34</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-74627" class="comments-container">
&#10;</div>
<div id="comment-tools-74627" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74627-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74602"></span>

<div id="answer-container-74602" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74602-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use Overpass turbo, with this <a href="https://overpass-turbo.eu/s/TC7">query</a> for example. You can then export in JSON. It's quite hard on the browser, you might want to filter a bit.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '20, 14:18</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-74602" class="comments-container">
<span id="74618"></span>
<div id="comment-74618" class="comment">
<div id="post-74618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, but this query does not return boundary coordinates</p>
</div>
<div id="comment-74618-info" class="comment-info">
<span class="comment-age">(05 May '20, 07:42)</span> <span class="comment-user userinfo">hotmailbelike</span>
</div>
</div>
</div>
<div id="comment-tools-74602" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74602-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74622"></span>

<div id="answer-container-74622" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74622-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sorry, it seems that comments are unusable...</p>
<p>So, to answer your comment, what do you mean by "boundary coordinates" ?</p>
<p>The query I gave you display the boundary, so it returns all the necessary coordinates. In OSM boundaries are usually relations, composed of ways, in turn composed of nodes. Only the nodes have coordinates.</p>
<p>When you export as GeoJSON, this hierarchy gets flattened. Depending on your needs this can be a good thing or not.</p>
<p>Please read some doc about <a href="https://wiki.openstreetmap.org/wiki/Beginners_Guide_1.3">OSM data model</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '20, 16:25</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-74622" class="comments-container">
&#10;</div>
<div id="comment-tools-74622" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74622-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74624"></span>

<div id="answer-container-74624" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74624-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, but is there a way to get the coordinates of the boundaries instead of the ways and nodes? Or, is there a way to extract the coordinates from the nodes and ways?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '20, 16:37</strong></p>
<img src="https://secure.gravatar.com/avatar/d14fcae6ba396f4830f9b10eb507c849?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hotmailbelike&#39;s gravatar image" />
<p><span>hotmailbelike</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hotmailbelike has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74624" class="comments-container">
&#10;</div>
<div id="comment-tools-74624" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74624-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74625"></span>

<div id="answer-container-74625" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74625-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Of course, just recurse on the members (ways) of the relations, and then the members (nodes) of the ways, and then get lat and lon from nodes.</p>
<p>Or as I said, the GeoJSON (and other formats) exports flatten this, so the coordinates of the nodes are duplicated in every relation.</p>
<p>Without more context about your application, there's no way to give you a more precise answer to your question.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '20, 16:45</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-74625" class="comments-container">
&#10;</div>
<div id="comment-tools-74625" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74625-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74626"></span>

<div id="answer-container-74626" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74626-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am sorry I don't know very well about how to use the OSM queries. Can you tell me how to recurse the members of the relations and then the members of the ways, and then get lat and lon from nodes?</p>
<p>About the application I am working on; I need to get the border as an array of coordinates when user searches for an area</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '20, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/d14fcae6ba396f4830f9b10eb507c849?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hotmailbelike&#39;s gravatar image" />
<p><span>hotmailbelike</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hotmailbelike has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74626" class="comments-container">
&#10;</div>
<div id="comment-tools-74626" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74626-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74628"></span>

<div id="answer-container-74628" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74628-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you so much <a href="https://help.openstreetmap.org/users/13231/h_mlet">@H_mlet</a> ! I have been stuck with this problem for weeks and finally you gave me a lead!</p>
<p>Truly, Thank you so much!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '20, 17:48</strong></p>
<img src="https://secure.gravatar.com/avatar/d14fcae6ba396f4830f9b10eb507c849?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hotmailbelike&#39;s gravatar image" />
<p><span>hotmailbelike</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hotmailbelike has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74628" class="comments-container">
&#10;</div>
<div id="comment-tools-74628" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74628-form-container" class="comment-form-container">
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

