+++
type = "question"
title = "Road data for routing"
description = '''I am trying to extract road data to use to implement a shortest path routing algorithm like A* or Dijksktras, I have been using QGis to try and extract the road data from map but I am really not sure what data to extract as there is huge amounts of data. Can anyone help me out ?'''
date = "2015-02-06T10:30:00Z"
lastmod = "2015-02-13T13:36:00Z"
weight = 40815
keywords = [ "data", "road", "for", "routing" ]
aliases = [ "/questions/40815" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Road data for routing](/questions/40815/road-data-for-routing)

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
<span id="post-40815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40815-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to extract road data to use to implement a shortest path routing algorithm like A* or Dijksktras, I have been using QGis to try and extract the road data from map but I am really not sure what data to extract as there is huge amounts of data. Can anyone help me out ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-for" rel="tag" title="see questions tagged &#39;for&#39;">for</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Feb '15, 10:30</strong></p>
<img src="https://secure.gravatar.com/avatar/b0714352f343c4076d9ae1794c258c68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pmcgrath_1&#39;s gravatar image" />
<p><span>pmcgrath_1</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pmcgrath_1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Feb '15, 10:30</strong> </span></p>
</div>
</div>
<div id="comments-container-40815" class="comments-container">
<span id="40982"></span>
<div id="comment-40982" class="comment">
<div id="post-40982-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Would it be possible for me to add my own roads to my own osm MAP ? I have added my area of Ireland to a postgres database and I plan on using pgrouting for routing, but would it be possible for me to add any new roads I find to the data and for them to considered when calculating the shortest path ?</p>
</div>
<div id="comment-40982-info" class="comment-info">
<span class="comment-age">(12 Feb '15, 19:39)</span> <span class="comment-user userinfo">pmcgrath_1</span>
</div>
</div>
<span id="40990"></span>
<div id="comment-40990" class="comment">
<div id="post-40990-score" class="comment-score">
2
</div>
<div class="comment-text">
<ol>
<li><p>When your "own" roads are based on a free data source, at least no licence breaking when using them for OSM purposes, why not adding them directly to the main OSM database?</p></li>
<li><p>by using an internet search engine I found the following hints:</p></li>
</ol>
<p><a href="/questions/10817/how-to-use-my-private-data-with-osm">https://help.openstreetmap.org/questions/10817/how-to-use-my-private-data-with-osm</a></p>
<p><a href="http://inasafe.org/en/training/intermediate/osm/305-using-private-data-store.html">http://inasafe.org/en/training/intermediate/osm/305-using-private-data-store.html</a></p>
<p><a href="http://gis.stackexchange.com/questions/28898/conflate-merge-private-shapefile-data-with-osm-data">http://gis.stackexchange.com/questions/28898/conflate-merge-private-shapefile-data-with-osm-data</a></p>
</div>
<div id="comment-40990-info" class="comment-info">
<span class="comment-age">(13 Feb '15, 12:23)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="40992"></span>
<div id="comment-40992" class="comment">
<div id="post-40992-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The purpose of the app is to allow the user to update the map and not have to wait on official updates from Osm, so they basically have their own version a map. Thanks for those links</p>
</div>
<div id="comment-40992-info" class="comment-info">
<span class="comment-age">(13 Feb '15, 12:34)</span> <span class="comment-user userinfo">pmcgrath_1</span>
</div>
</div>
<span id="40994"></span>
<div id="comment-40994" class="comment">
<div id="post-40994-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If you add roads to your own copy of the OpenStreetMap database, and you host this on a publicly accessible website (or similar), note that the OSM database requires you to make these additional roads available to OSM on request.</p>
</div>
<div id="comment-40994-info" class="comment-info">
<span class="comment-age">(13 Feb '15, 13:05)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="40995"></span>
<div id="comment-40995" class="comment">
<div id="post-40995-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would have no problem making the data available for the OSM database, its just the primary function of this app is too allow the user to update their own map</p>
</div>
<div id="comment-40995-info" class="comment-info">
<span class="comment-age">(13 Feb '15, 13:36)</span> <span class="comment-user userinfo">pmcgrath_1</span>
</div>
</div>
</div>
<div id="comment-tools-40815" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40815-form-container" class="comment-form-container">
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

<span id="40817"></span>

<div id="answer-container-40817" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40817-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-40817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want smaller amounts of data, you can download country (or region) specific extracts from <a href="http://download.geofabrik.de/">Geofabrik download service</a>. The <a href="https://wiki.openstreetmap.org/wiki/API_v0.6">OSM API</a> can provide (much) smaller boxes of data.</p>
<p>It really depends what you want to do. Do you want to write a routing algorithm from scratch? In which case you should look at the <a href="https://wiki.openstreetmap.org/wiki/OSM_XML">OSM XML schema</a> (sometimes you will get <a href="https://wiki.openstreetmap.org/wiki/PBF_Format">PBF files</a>) and learn about the <a href="https://wiki.openstreetmap.org/wiki/Elements">OSM Data model</a>.</p>
<p>However, there are numerous <a href="https://wiki.openstreetmap.org/wiki/Routing">existing routing software libraries</a> that can be used with OSM data (e.g <a href="https://wiki.openstreetmap.org/wiki/Open_Source_Routing_Machine">OSRM</a> or <a href="https://wiki.openstreetmap.org/wiki/GraphHopper">GraphHopper</a>)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '15, 11:20</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-40817" class="comments-container">
<span id="40820"></span>
<div id="comment-40820" class="comment">
<div id="post-40820-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want to write an algorithm from scratch if possible, but I am struggling to extract the data that I will need to do this.</p>
</div>
<div id="comment-40820-info" class="comment-info">
<span class="comment-age">(06 Feb '15, 11:55)</span> <span class="comment-user userinfo">pmcgrath_1</span>
</div>
</div>
<span id="40821"></span>
<div id="comment-40821" class="comment">
<div id="post-40821-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Take a look at <a href="https://wiki.openstreetmap.org/wiki/Tags">tags</a> and <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing">tags for routing</a>. It will also be helpful to look at other existing routing engines that are based on OSM data.</p>
</div>
<div id="comment-40821-info" class="comment-info">
<span class="comment-age">(06 Feb '15, 12:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="40822"></span>
<div id="comment-40822" class="comment">
<div id="post-40822-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Once you've decided how large an area you want, have a read of this previous question: <a href="/questions/19213/">osm-xml-into-graph</a>.</p>
</div>
<div id="comment-40822-info" class="comment-info">
<span class="comment-age">(06 Feb '15, 12:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40817" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40817-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40823"></span>

<div id="answer-container-40823" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40823-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(regarding: "extract the road data from map but I am really not sure what data to extract" and "extract the data that I will need")</p>
<p><a href="#40817">rorym already</a> linked the OSM data model. If you want roads only, you will want to <span>filter</span> the data to only have objects with specific <span><code>highway</code></span> <span>tags</span>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '15, 12:06</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-40823" class="comments-container">
&#10;</div>
<div id="comment-tools-40823" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40823-form-container" class="comment-form-container">
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

