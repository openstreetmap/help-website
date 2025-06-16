+++
type = "question"
title = "export boundaries"
description = '''I am trying to get the longitude/latitude points for the admin boundary for the entire US coast. Can I get this data from your site? If so, how?'''
date = "2011-09-22T17:11:00Z"
lastmod = "2011-09-22T20:04:00Z"
weight = 8082
keywords = [ "export", "admin_boundary" ]
aliases = [ "/questions/8082" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [export boundaries](/questions/8082/export-boundaries)

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
<span id="post-8082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8082-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to get the longitude/latitude points for the admin boundary for the entire US coast. Can I get this data from your site? If so, how?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Sep '11, 17:11</strong></p>
<img src="https://secure.gravatar.com/avatar/3c3e863f5f89ed1d4ea2831ab84c2032?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ljd&#39;s gravatar image" />
<p><span>ljd</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ljd has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8082" class="comments-container">
&#10;</div>
<div id="comment-tools-8082" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8082-form-container" class="comment-form-container">
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

<span id="8085"></span>

<div id="answer-container-8085" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8085-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My answer is valid for all countries:</p>
<p>First, you have to find the entity representing the admin boundary. Usually, country borders are identified by an <a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative">OSM relation of type boundary=administrative</a> with admin_level=2. One method to find it is to use an OSM editor and download an area where you know that the boundary is present and seek the relation id.<br />
But you can also use the 'search' tool from the main page (called <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a>). If you enter e.g "Washington", you get a list of place entities containing this word. But more interesting, you also find a link to the nominatim home page : <a href="http://nominatim.openstreetmap.org/">http://nominatim.openstreetmap.org/</a>. If you type "Washington" again there, you will find the same list of results and one of them is "Washington, Fairfax, District of Columbia, United States of America, North America (City) (details)". If you click on the "details" link, you will find the node id <a href="https://www.openstreetmap.org/browse/node/424317935">424317935 and its URL in OSM site</a>. Here, you can see that the node is part of the relation "United States of America (<a href="https://www.openstreetmap.org/browse/relation/148838">148838</a>) (as label)" (at the bottom).</p>
<p>Next, you have different ways to retrieve the relation <a href="https://www.openstreetmap.org/browse/relation/148838">148838</a> and all its members, the collection of ways and nodes representing the admin boundary. The problem is the size of this relation. It is normally possible to retrieve all information in <a href="http://api.openstreetmap.org/api/0.6/relation/148838/full">one request to the OSM server</a> but this will fail for such big relations. I know a python script which downloads all relation members one by one. But you can also use the editor <a href="https://wiki.openstreetmap.org/wiki/JOSM">JOSM</a> and the command "Download object..." where you specify the Object type "node" and Object ID "424317935" with the option "Download referrers". Then, save the content with the menu "File" -&gt; "Save As...". You have now an XML file containing all ways and nodes with their lat/lon coordinates. If you need a shapefile, you will have to use <a href="https://wiki.openstreetmap.org/wiki/Shapefiles">a script converting OSM data to this format</a>.</p>
<p>Be aware that many countries have more than one relation identifying the boundary (e.g. with and without the territorial waters).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '11, 20:04</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></p>
</div>
</div>
<div id="comments-container-8085" class="comments-container">
&#10;</div>
<div id="comment-tools-8085" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8085-form-container" class="comment-form-container">
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

