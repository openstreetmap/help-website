+++
type = "question"
title = "Overpass: export data as simplified list in CSV with lat and long?"
description = '''I&#x27;m trying to create a liste with overpass so i can create my own map with http://printmaps-osm.de/de/beispiele.html  One example is using csv containing  id|name|wkt 1|Open Air Museum|POINT(7.59918 51.95005) 2|Zoo|POINT(7.59074 51.94666)  Is it possible to get this output instantly(or, something li...'''
date = "2021-12-19T22:03:00Z"
lastmod = "2021-12-20T03:31:00Z"
weight = 82876
keywords = [ "overpass", "export", "list", "printmaps" ]
aliases = [ "/questions/82876" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass: export data as simplified list in CSV with lat and long?](/questions/82876/overpass-export-data-as-simplified-list-in-csv-with-lat-and-long)

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
<span id="post-82876-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82876-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82876-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to create a liste with overpass so i can create my own map with <a href="http://printmaps-osm.de/de/beispiele.html">http://printmaps-osm.de/de/beispiele.html</a></p>
<p>One example is using csv containing</p>
<pre><code>id|name|wkt
1|Open Air Museum|POINT(7.59918 51.95005)
2|Zoo|POINT(7.59074 51.94666)</code></pre>
<p>Is it possible to get this output instantly(or, something like that)? It feels like an simple request but i could not find it on <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Exporting_Data">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Exporting_Data</a> there or in the docs itself.</p>
<pre><code>[out:csv(&quot;id&quot;,&quot;name&quot;,&quot;website&quot;,&quot;long&quot;)][timeout:25];
//[out:json][timeout:25];
// gather results
(
  // query part for: “amenity=hospital”
  node[&quot;amenity&quot;=&quot;hospital&quot;]({{bbox}});
  way[&quot;amenity&quot;=&quot;hospital&quot;]({{bbox}});
  relation[&quot;amenity&quot;=&quot;hospital&quot;]({{bbox}});
);
&#10;// print results
out body center; // just get center of values
&gt;;</code></pre>
<p>I added "website" for testing purposes. So i can access tags, but i cannot access lat and long to write in the csv?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-list" rel="tag" title="see questions tagged &#39;list&#39;">list</span> <span class="post-tag tag-link-printmaps" rel="tag" title="see questions tagged &#39;printmaps&#39;">printmaps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Dec '21, 22:03</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1a4ff035eecbaa52273ed663b19f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Negreheb&#39;s gravatar image" />
<p><span>Negreheb</span><br />
<span class="score" title="129 reputation points">129</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Negreheb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82876" class="comments-container">
&#10;</div>
<div id="comment-tools-82876" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82876-form-container" class="comment-form-container">
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

<span id="82877"></span>

<div id="answer-container-82877" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82877-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Negreheb has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#CSV_output_mode">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#CSV_output_mode</a></p>
<pre><code>[out:csv(::id,name,website,::lat,::lon; false; &quot;,&quot;)]
[bbox:{{bbox}}];
nwr[amenity=hospital];
out center;</code></pre>
<p><a href="https://overpass-turbo.eu/s/1ej9">https://overpass-turbo.eu/s/1ej9</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '21, 03:31</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-82877" class="comments-container">
&#10;</div>
<div id="comment-tools-82877" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82877-form-container" class="comment-form-container">
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

