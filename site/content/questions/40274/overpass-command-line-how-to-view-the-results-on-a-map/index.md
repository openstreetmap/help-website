+++
type = "question"
title = "Overpass (command line): how to view the results on a map?"
description = '''Hi all! I&#x27;ve tried to play with Overpass from command line because I&#x27;ve to do a query quite &quot;expensive&quot; that Overpass Turbo can&#x27;t to do My issue is about to download all the addresses in Italy Here you are my query (it comes from Overpass Turbo ...) &amp;lt;osm-script output=&quot;json&quot;&amp;gt;  &amp;lt;union into=&quot;...'''
date = "2015-01-13T09:10:00Z"
lastmod = "2018-11-11T03:22:00Z"
weight = 40274
keywords = [ "overpassapi", "overpass", "overpass-turbo" ]
aliases = [ "/questions/40274" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass (command line): how to view the results on a map?](/questions/40274/overpass-command-line-how-to-view-the-results-on-a-map)

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
<span id="post-40274-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40274-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40274-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all!</p>
<p>I've tried to play with Overpass from command line because I've to do a query quite "expensive" that Overpass Turbo can't to do</p>
<p>My issue is about to download all the addresses in Italy</p>
<p>Here you are my query (it comes from Overpass Turbo ...)</p>
<p>&lt;osm-script output="json"&gt; &lt;union into="<em>"&gt; &lt;query into="</em>" type="node"&gt; &lt;has-kv k="addr:housenumber" modv="" v=""/&gt; &lt;bbox-query e="20.01708984375" into="<em>" n="47.15984001304432" s="36.27970720524017" w="5.9765625"/&gt; &lt;/query&gt; &lt;/union&gt; &lt;print e="" from="</em>" geometry="skeleton" limit="" mode="body" n="" order="id" s="" w=""/&gt; &lt;recurse from="<em>" into="</em>" type="down"/&gt; &lt;print e="" from="_" geometry="skeleton" limit="" mode="skeleton" n="" order="quadtile" s="" w=""/&gt; &lt;/osm-script&gt;</p>
<p>I've saved it in a file "CiviciItalia.txt", and then I've used the following command</p>
<pre><code>wget --post-file=CiviciItalia.txt http://overpass-api.de/api/interpreter --output-document=CiviciItalia.json</code></pre>
<p>All works fine and I've obtained a .json file but ...... how may I visualize it on some GIS desktop tools (es. QGIS)?</p>
<p>Any suggestion is appreciated</p>
<p>Cesare</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jan '15, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a838d0000c6deb320a76f046b59f842c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cesaregerbino&#39;s gravatar image" />
<p><span>cesaregerbino</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cesaregerbino has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40274" class="comments-container">
&#10;</div>
<div id="comment-tools-40274" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40274-form-container" class="comment-form-container">
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

<span id="40286"></span>

<div id="answer-container-40286" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40286-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-40286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try QuickOSM (a QGIS plugin). It can run Overpass queries, does all the conversion 'under the hood' and presents the result as new layer in QGIS. You can also save that result as shape file, etc. And it should also run on Windows.</p>
<p>BTW: I wonder why you didn't specify a timeout value in your query. Quite likely you're getting incomplete results after hitting the timeout.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '15, 11:52</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jan '15, 11:58</strong> </span></p>
</div>
</div>
<div id="comments-container-40286" class="comments-container">
<span id="40287"></span>
<div id="comment-40287" class="comment">
<div id="post-40287-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've also tried to use QuickOSM using QGIS 2.6.1 but can't obtain the result, something goes wrong.</p>
<p>About timeout .... By default Overpass Turbo put timeout:25 but my query is much longer ..... So I've decided to drop timeout ... I'm a newbie about overpass: have I to specify in any case a timeout to avoid incomplete result?</p>
</div>
<div id="comment-40287-info" class="comment-info">
<span class="comment-age">(13 Jan '15, 12:24)</span> <span class="comment-user userinfo">cesaregerbino</span>
</div>
</div>
<span id="40314"></span>
<div id="comment-40314" class="comment">
<div id="post-40314-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Regarding the timeout: Overpass API immediately starts sending some data rather than buffering the whole result. If you happen to see a respective error message at the end of your json file, your timeout was too low. (see <a href="https://github.com/drolbr/Overpass-API/issues/94#issuecomment-44868471">timeout</a> for more details).</p>
<p>In any case, I would recommend to set at least a timeout of 300 seconds. The query took about 2-3 minutes when I executed it.</p>
</div>
<div id="comment-40314-info" class="comment-info">
<span class="comment-age">(13 Jan '15, 20:45)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="40317"></span>
<div id="comment-40317" class="comment">
<div id="post-40317-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your query result gives QGIS a really hard time. Crunching numbers for 20 minutes now, still not finished, GeoJSON temporary file is now at about 3.5GB, still counting...</p>
<p>Maybe you need to think about some other approach, like feeding the result into a PostGIS database instead.</p>
</div>
<div id="comment-40317-info" class="comment-info">
<span class="comment-age">(13 Jan '15, 21:53)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-40286" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40286-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40275"></span>

<div id="answer-container-40275" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40275-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40275-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40275-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have done something similar to that for my <a href="http://www.technomancy.org/osm-hackerspaces/">hackerspace map</a> <em>(ignore the old link for 'how it's made')</em>. I used <a href="http://tyrasd.github.io/osmtogeojson/">osmtogeojson</a>, a command line programme that converts the JSON from Overpass into a GeoJSON file, that you can then display with <a href="http://leafletjs.com/">Leaflet</a>, like I do with that map. QGis should be able to open GeoJSON files as well. osmtogeojson is the programme that overpass turbo uses to convert to geojson to display on the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '15, 09:48</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-40275" class="comments-container">
<span id="40277"></span>
<div id="comment-40277" class="comment">
<div id="post-40277-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've seen ... Unfortunately I'm on Windows 7 now ..... I'll try to do using a Linux VM ....</p>
</div>
<div id="comment-40277-info" class="comment-info">
<span class="comment-age">(13 Jan '15, 09:59)</span> <span class="comment-user userinfo">cesaregerbino</span>
</div>
</div>
<span id="40278"></span>
<div id="comment-40278" class="comment">
<div id="post-40278-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's a javascript programme, and installable with node package manager (npm). Maybe it might work on windows? Javascript /is/ cross platform (ish)...</p>
</div>
<div id="comment-40278-info" class="comment-info">
<span class="comment-age">(13 Jan '15, 10:03)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
<span id="40279"></span>
<div id="comment-40279" class="comment">
<div id="post-40279-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'll try ....</p>
</div>
<div id="comment-40279-info" class="comment-info">
<span class="comment-age">(13 Jan '15, 10:05)</span> <span class="comment-user userinfo">cesaregerbino</span>
</div>
</div>
<span id="66745"></span>
<div id="comment-66745" class="comment">
<div id="post-66745-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>geojson.io can also open and display the geojson files from the osmtogeojson script (I presume). To make it all happen from the command line, you should be able to pipe the output of osmtogeojson into <code>geoq map</code> after installing geoq from <a href="https://github.com/worace/geoq">https://github.com/worace/geoq</a></p>
</div>
<div id="comment-66745-info" class="comment-info">
<span class="comment-age">(11 Nov '18, 03:22)</span> <span class="comment-user userinfo">b-jazz</span>
</div>
</div>
</div>
<div id="comment-tools-40275" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40275-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40343"></span>

<div id="answer-container-40343" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40343-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Another option is to use the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Output_Format_.28out.29">CSV output format</a>, with the <code>::lat</code> and <code>::lon</code> columns, which gives you the lat/lon of the 'centre' of a polygon or the location of the point. You can add extra tags as columns. This will only give you points, not polygons.</p>
<p>QGis can support <a href="http://www.qgistutorials.com/en/docs/importing_spreadsheets_csv.html">Deliminted Text (like CSV)</a>, so you should be able to open the file in it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '15, 11:46</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-40343" class="comments-container">
&#10;</div>
<div id="comment-tools-40343" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40343-form-container" class="comment-form-container">
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

