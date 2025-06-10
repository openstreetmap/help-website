+++
type = "question"
title = "Data incoherencce between overpass-turbo and umap/my map"
description = '''I&#x27;m looking for restaurants - and obviously also cafés - in Paris with french or regional cooking - (restaurant OR cafe) AND (cuisine=french OR cuisine=regional) - what shows hundreds of places in overpass-turbo.eu. Copying the URL-umap-link into umap:external data source (my site works in German th...'''
date = "2021-11-05T10:42:00Z"
lastmod = "2021-11-08T14:15:00Z"
weight = 82479
keywords = [ "umap", "overpass-turbo", "incomplete" ]
aliases = [ "/questions/82479" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Data incoherencce between overpass-turbo and umap/my map](/questions/82479/data-incoherencce-between-overpass-turbo-and-umapmy-map)

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
<span id="post-82479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82479-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking for restaurants - and obviously also cafés - in Paris with french or regional cooking - (restaurant OR cafe) AND (cuisine=french OR cuisine=regional) - what shows hundreds of places in overpass-turbo.eu. Copying the URL-umap-link into umap:external data source (my site works in German though the wording might be incorrect) I get also many places but not all I see in the overpass-map. I verify that with the restaurants around the corner I usually stay in a hotel. How can I asure that in umap all interesting places - the same as in overpass - are shown? Thanks for advice (and patience with a beginner).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-incomplete" rel="tag" title="see questions tagged &#39;incomplete&#39;">incomplete</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Nov '21, 10:42</strong></p>
<img src="https://secure.gravatar.com/avatar/60926ce04476f20c517c429981c94109?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ak54&#39;s gravatar image" />
<p><span>ak54</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ak54 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Nov '21, 10:43</strong> </span></p>
</div>
</div>
<div id="comments-container-82479" class="comments-container">
&#10;</div>
<div id="comment-tools-82479" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82479-form-container" class="comment-form-container">
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

<span id="82481"></span>

<div id="answer-container-82481" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82481-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>A common with umap, is that it doesn't display POI mapped as ways (polygons).</p>
<p>My solution was to add <code>center</code> to the <code>out</code> directive, so that the output is only nodes.</p>
<p>Please share your overpass query is your need more specific assistance.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Nov '21, 12:22</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-82481" class="comments-container">
&#10;</div>
<div id="comment-tools-82481" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82481-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82492"></span>

<div id="answer-container-82492" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82492-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi and thanks. My query looks like:</p>
<p>{{OverpassTurboExample|loc=48.85825;2.35775;18|query=</p>
<p>[out:json][timeout:25];</p>
<p>// fetch area “Paris” to search in {{((}}geocodeArea:Paris{{))}}-&gt;.searchArea; // gather results</p>
<p>( // query part for: “restaurant and cuisine=french”</p>
<p>nwr["amenity"="restaurant"]<a href="area.searchArea">"cuisine"="french"</a>; nwr["amenity"="restaurant"]<a href="area.searchArea">"cuisine"="regional"</a>; nwr["amenity"="cafe"]<a href="area.searchArea">"cuisine"="french"</a>; nwr["amenity"="cafe"]<a href="area.searchArea">"cuisine"="regional"</a>;<br />
);</p>
<p>// print results</p>
<p>out center;</p>
<p>}}</p>
<p>Exporting the result as geojson and importing it to umap/mymap ends in a correct map. However, exporting just the umap-link</p>
<p>[out:json][timeout:25];area(3600007444)-&gt;.searchArea;(nwr["amenity"="restaurant"]<a href="area.searchArea">"cuisine"="french"</a>;nwr["amenity"="restaurant"]<a href="area.searchArea">"cuisine"="regional"</a>;nwr["amenity"="cafe"]<a href="area.searchArea">"cuisine"="french"</a>;nwr["amenity"="cafe"]<a href="area.searchArea">"cuisine"="regional"</a>; );out center;</p>
<p>results in nothing useful, even - that's new - in empty maps.</p>
<p>There must be a linking / coordinating effect I do not understand. Therefore, if you have some more advice it will be highly appreciated.</p>
<p>Andreas</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '21, 14:09</strong></p>
<img src="https://secure.gravatar.com/avatar/60926ce04476f20c517c429981c94109?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ak54&#39;s gravatar image" />
<p><span>ak54</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ak54 has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Nov '21, 14:21</strong> </span></p>
</div>
</div>
<div id="comments-container-82492" class="comments-container">
<span id="82493"></span>
<div id="comment-82493" class="comment">
<div id="post-82493-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Your cuisine filters in the 2nd e.g., lack "[]"</p>
</div>
<div id="comment-82493-info" class="comment-info">
<span class="comment-age">(06 Nov '21, 14:38)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="82494"></span>
<div id="comment-82494" class="comment">
<div id="post-82494-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I'd also think a timeout of 25 seconds may be a bit small for a big place like Paris.</p>
</div>
<div id="comment-82494-info" class="comment-info">
<span class="comment-age">(06 Nov '21, 14:38)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="82500"></span>
<div id="comment-82500" class="comment">
<div id="post-82500-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The missing brackets are just a copy/paste-error, themquery looks like</p>
<p>[out:json] [timeout:125] ; area(3600007444)-&gt;.searchArea; ( nwr ["amenity"="restaurant"] ["cuisine"="regional"] (area.searchArea); nwr ["amenity"="restaurant"] ["cuisine"="french"] (area.searchArea); nwr ["amenity"="cafe"] ["cuisine"="french"] (area.searchArea); nwr ["amenity"="cafe"] ["cuisine"="regional"] (area.searchArea); ); out center;</p>
<p>A longer timeout produces a useful geojson-file but still no working link for umap</p>
</div>
<div id="comment-82500-info" class="comment-info">
<span class="comment-age">(06 Nov '21, 23:43)</span> <span class="comment-user userinfo">ak54</span>
</div>
</div>
</div>
<div id="comment-tools-82492" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82492-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82503"></span>

<div id="answer-container-82503" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82503-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sorry, the missing brackets are a copy/paste error, the query looks like</p>
<p><img src="https://help.openstreetmap.org/upfiles/7E74E290-4A0C-43B9-9D07-847A64F16020.jpeg" alt="alt text" /></p>
<p>However, even with a higher timeout rate the umap link does not work correctly, but the import with geojson works. I prefer the link solution because that would permit an automatic update in a vivid restaurant scene.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '21, 06:35</strong></p>
<img src="https://secure.gravatar.com/avatar/60926ce04476f20c517c429981c94109?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ak54&#39;s gravatar image" />
<p><span>ak54</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ak54 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-82503" class="comments-container">
<span id="82516"></span>
<div id="comment-82516" class="comment">
<div id="post-82516-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can use the "Share" functionality of overpass-turbo, instead of copy-pasting, it's faster and less prone to errors. For example : <a href="http://overpass-turbo.eu/s/1cOo">http://overpass-turbo.eu/s/1cOo</a></p>
</div>
<div id="comment-82516-info" class="comment-info">
<span class="comment-age">(08 Nov '21, 13:46)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-82503" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82503-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82522"></span>

<div id="answer-container-82522" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82522-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How did you build the query for umap ? Here is the doc : <a href="https://wiki.openstreetmap.org/wiki/UMap/Guide/Import_data_with_Overpass">https://wiki.openstreetmap.org/wiki/UMap/Guide/Import_data_with_Overpass</a></p>
<p>Did you urlencode it ? I found that usually it helps.</p>
<p>Did you use the same overpass server as in overpass-turbo ? IIRC the area ids might not be consistent from one server to another.</p>
<p>I created a <a href="https://umap.openstreetmap.fr/en/map/overpass-test_677911">test umap</a>. You will find the layer settings in a screenshot below.</p>
<p>It seems all right to me. With clustering and unzooming, it seems that all 1069 elements are displayed !</p>
<p>You can check in the <a href="https://developer.mozilla.org/en-US/docs/Tools/Network_Monitor">network console</a> of your browser what the response of the server is (timeout, empty request, etc).</p>
<p>Also, you should uncheck "Dynamic", and check "proxy" and "one day" because this kind of query is not easy on the server, and might get you blacklisted. You can change the language of umap in the url of the map, put en where you should find de.</p>
<p>Hope this helps.</p>
<p><img src="https://help.openstreetmap.org/upfiles/test_overpass.png" alt="test settings" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '21, 14:15</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</img>
</div>
</div>
<div id="comments-container-82522" class="comments-container">
&#10;</div>
<div id="comment-tools-82522" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82522-form-container" class="comment-form-container">
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

