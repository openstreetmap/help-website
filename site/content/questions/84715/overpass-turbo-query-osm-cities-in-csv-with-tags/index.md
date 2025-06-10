+++
type = "question"
title = "Overpass turbo query - OSM Cities in CSV with tags"
description = '''I&#x27;m trying to run an Overpass turbo query of OpenStreetMaps Cities that will return the cities as CSV data with several fields (columns). I&#x27;m currently able to get these fields: Latitude, Longitude, Name, Population (plus any other simple tags of the nodes) By running this query: [out:csv(::lat,::lo...'''
date = "2022-06-06T22:35:00Z"
lastmod = "2022-06-06T22:35:00Z"
weight = 84715
keywords = [ "csv", "overpass-turbo" ]
aliases = [ "/questions/84715" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass turbo query - OSM Cities in CSV with tags](/questions/84715/overpass-turbo-query-osm-cities-in-csv-with-tags)

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
<span id="post-84715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84715-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to run an Overpass turbo query of OpenStreetMaps Cities that will return the cities as CSV data with several fields (columns).</p>
<p>I'm currently able to get these fields:</p>
<p>Latitude, Longitude, Name, Population (plus any other simple tags of the nodes)</p>
<p>By running this query:</p>
<pre><code>[out:csv(::lat,::lon,name,population)][timeout:300];
// fetch area to search in
{{geocodeArea:united states}}-&gt;.searchArea;
// gather results
(
  node[place=&quot;city&quot;](area.searchArea)(if:count_tags() &gt; 0);
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>But, I would like to also get these fields, and I have been unable to do so:</p>
<ol>
<li>Total number of tags associated with the node</li>
<li>Name of the Country in which the node is located</li>
<li>Name of the State in which the node is located</li>
</ol>
<p>I know that data is there, because I can use both the country and tag count to filter the data, but I can't seem to get those as data in my CSV output.</p>
<p>Any help would be greatly appreciated!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jun '22, 22:35</strong></p>
<img src="https://secure.gravatar.com/avatar/cb35d3ef69463d088e0a8f9328db41dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="salb1845&#39;s gravatar image" />
<p><span>salb1845</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="salb1845 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84715" class="comments-container">
&#10;</div>
<div id="comment-tools-84715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84715-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

