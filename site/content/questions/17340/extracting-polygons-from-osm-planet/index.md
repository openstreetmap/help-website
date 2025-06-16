+++
type = "question"
title = "Extracting Polygons from OSM planet."
description = '''Hi! I&#x27;m brand new to OSM data, so please be patient with me :) I want to extract administrative (or for that sake all named) polygons from OSM data. I have read https://help.openstreetmap.org/questions/8273/how-do-i-extract-the-polygon-of-an-administrative-boundary, but it does not work for me. Here...'''
date = "2012-10-31T22:25:00Z"
lastmod = "2012-11-01T19:17:00Z"
weight = 17340
keywords = [ "extract", "polygon", "rel2poly" ]
aliases = [ "/questions/17340" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting Polygons from OSM planet.](/questions/17340/extracting-polygons-from-osm-planet)

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
<span id="post-17340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17340-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I'm brand new to OSM data, so please be patient with me :)</p>
<p>I want to extract administrative (or for that sake all named) polygons from OSM data. I have read <a href="/questions/8273/how-do-i-extract-the-polygon-of-an-administrative-boundary,">https://help.openstreetmap.org/questions/8273/how-do-i-extract-the-polygon-of-an-administrative-boundary,</a> but it does not work for me. Here's what happens on my machine:</p>
<pre><code>$ bzcat great_britain.osm.bz2 | perl rel2poly.pl 
Killed</code></pre>
<p>I assume that is due to the process running out of memory (It's a VM without swap space...). However, I am not entirely sure that script does what I want. I read somewhere that it translates full relations to polygons. And AFAI understand, there are no full relations in the OSM extracts? I also don't speak pearl to check. If I was to write a python (right choice?) script to derive named polygons from OSM extracts how would I process the data? Here's my understanding of the data. Pleas correct me where I'm wrong:</p>
<ol>
<li>Nodes are points on the map having lat/lons.</li>
<li>Ways are collections of nodes. There are closed ways (polygons) and opened ways (paths)</li>
<li>Relations connect ways and nodes. All ways of a relation form polygons too.</li>
<li>All of the above (nodes, ways and relations) have tags containing meta data as names, types, links, and so on.</li>
<li>In the extract I downloaded the relations contain references to nodes and ways, but not the nodes and ways themselves.</li>
</ol>
<p>So my script would have to</p>
<ol>
<li>load all nodes</li>
<li>load all ways</li>
<li>expand all ways with the referenced nodes</li>
<li>load all relations</li>
<li>expand all relations with the referenced ways</li>
<li>for every relation that has a name tag, list the latlons of the nodes on the ways.</li>
</ol>
<p>Is that right? Is that what the perl script does anyways? Is it easier/faster to load the data into postgres using one of the available tools instead of processing the data in a script?</p>
<p>All suggestions are appreciated! K</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-rel2poly" rel="tag" title="see questions tagged &#39;rel2poly&#39;">rel2poly</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '12, 22:25</strong></p>
<img src="https://secure.gravatar.com/avatar/680bc1d9127776b4acb2e6af485a6869?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="konstantin&#39;s gravatar image" />
<p><span>konstantin</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="konstantin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17340" class="comments-container">
<span id="17344"></span>
<div id="comment-17344" class="comment">
<div id="post-17344-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to get around the memory issue (and to see if it actually does what you want) maybe try a smaller input file, like perhaps one of the English counties from <a href="http://download.geofabrik.de/openstreetmap/europe/great_britain/england/">here</a>?</p>
</div>
<div id="comment-17344-info" class="comment-info">
<span class="comment-age">(31 Oct '12, 23:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-17340" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17340-form-container" class="comment-form-container">
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

<span id="17370"></span>

<div id="answer-container-17370" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17370-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use the administrative boundary data only as input. This reduces the amount of data by orders of magnitude.</p>
<p>For example</p>
<p><a href="http://overpass-api.de/api/interpreter?data=(rel%5Bname=%22United+Kingdom%22%5D;%3E;);out;">http://overpass-api.de/api/interpreter?data=(rel[name="United Kingdom"];&gt;;);out;</a></p>
<p>will return exactly the boundary data of the nation "United Kingdom".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '12, 19:17</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-17370" class="comments-container">
&#10;</div>
<div id="comment-tools-17370" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17370-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17347"></span>

<div id="answer-container-17347" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17347-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Extracting multipolygon data from OSM is hard. Don't try to write the code yourself, there are already several implementations out there that do that. I always recommend <a href="http://wiki.osm.org/wiki/Osmium">Osmium/osmjs</a>, but I am biased. :-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '12, 08:36</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-17347" class="comments-container">
<span id="17351"></span>
<div id="comment-17351" class="comment">
<div id="post-17351-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ha, Jochen, now I understand how you're biased! Osmium seems like a tool that could do what I need. I will give it a shot. However, you mention several implementations, the most popular probably being Osmosis. Are there more? Could you point me there?</p>
<p>Thanks!</p>
</div>
<div id="comment-17351-info" class="comment-info">
<span class="comment-age">(01 Nov '12, 10:10)</span> <span class="comment-user userinfo">konstantin</span>
</div>
</div>
</div>
<div id="comment-tools-17347" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17347-form-container" class="comment-form-container">
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

