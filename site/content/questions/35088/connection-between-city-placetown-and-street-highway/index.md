+++
type = "question"
title = "Connection between city (place=town) and street (highway=*)"
description = '''Hello, I have problem with extract datas, which I need. I need data like: &quot;city;street&quot; (but i have country file, with all streets and cities in selected country) I know that some of information i can get from &quot;addr:street&quot; but much more streets we can find in tag k=&quot;highway&quot;. With osmfilter I can f...'''
date = "2014-07-22T22:38:00Z"
lastmod = "2014-07-23T12:53:00Z"
weight = 35088
keywords = [ "city", "street" ]
aliases = [ "/questions/35088" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Connection between city (place=town) and street (highway=\*)](/questions/35088/connection-between-city-placetown-and-street-highway)

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
<span id="post-35088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35088-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have problem with extract datas, which I need. I need data like: "city;street" (but i have country file, with all streets and cities in selected country)</p>
<p>I know that some of information i can get from "addr:street" but much more streets we can find in tag k="highway". With osmfilter I can filter that datas, but there is no connection with city name?</p>
<p>Is it possible to filter/convert streets (highway=*) from osm file and connected it to specify city (place=town)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '14, 22:38</strong></p>
<img src="https://secure.gravatar.com/avatar/c44250c8ac6a5ab1985e327cb9a28a84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miklosz_deki&#39;s gravatar image" />
<p><span>miklosz_deki</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miklosz_deki has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35088" class="comments-container">
&#10;</div>
<div id="comment-tools-35088" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35088-form-container" class="comment-form-container">
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

<span id="35091"></span>

<div id="answer-container-35091" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35091-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Does the country in question have aministrative boundary polygons for the cities? If yes you probably can use the overpass api to get all streets in a city.</p>
<p>See <a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a></p>
<p>A further method to get the information is to use nominatim ( <a href="http://nominatim.openstreetmap.org/">http://nominatim.openstreetmap.org/</a> ) which will build hierarchies with the required information (this will even work approximately with place nodes if the polygons are missing).</p>
<p>Note that in both cases you should respect the corresponding acceptable use policies and protentially run your own servers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '14, 23:30</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jul '14, 09:45</strong> </span></p>
</div>
</div>
<div id="comments-container-35091" class="comments-container">
<span id="35100"></span>
<div id="comment-35100" class="comment">
<div id="post-35100-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In addition, you have to know that "addr:street" is not a tag you find normally on the "street" itself but on an "address" item (a node or a small building polygon along the street road). Also the "highway=*" key is used for all roads, not only the ones in cities. They can be combined with a "name" tag but not necessarily (OSM is not strict in attributes like in classic GIS datasets)</p>
</div>
<div id="comment-35100-info" class="comment-info">
<span class="comment-age">(23 Jul '14, 12:53)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-35091" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35091-form-container" class="comment-form-container">
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

