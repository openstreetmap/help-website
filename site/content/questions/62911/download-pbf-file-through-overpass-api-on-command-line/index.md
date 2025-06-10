+++
type = "question"
title = "Download .pbf file through Overpass API on command line"
description = '''I would like to be able to download .pbf files of OSM data extracts directly through the Overpass API (or suitable alternative) using wget, cURL or something similar from the command line. My goal is to be able to specify a country name (using a country boundary for the extract) to be used in the Ov...'''
date = "2018-04-04T21:31:00Z"
lastmod = "2018-04-04T22:40:00Z"
weight = 62911
keywords = [ "overpassapi", "wget", "pbf", "overpass" ]
aliases = [ "/questions/62911" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Download .pbf file through Overpass API on command line](/questions/62911/download-pbf-file-through-overpass-api-on-command-line)

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
<span id="post-62911-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62911-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62911-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to be able to download .pbf files of OSM data extracts directly through the Overpass API (or suitable alternative) using wget, cURL or something similar from the command line. My goal is to be able to specify a country name (using a country boundary for the extract) to be used in the Overpass API request, like this:</p>
<pre><code>wget &quot;http://overpass-api.de/api/interpreter?data=node[name=\&quot;Singapore\&quot;];out;&quot;</code></pre>
<p>I've been working with the documentation for this <a href="https://wiki.openstreetmap.org/wiki/User:Tagtheworld/overpass-api_commandline">here</a>, but can't figure out how to download a .pbf formatted file directly. So far I can only get a download of .osm format file to work, with this:</p>
<pre><code>wget -O target.osm &quot;http://overpass-api.de/api/interpreter?data=node[name=\&quot;Singapore\&quot;];out;&quot;</code></pre>
<p>I tried several methods of converting the .osm to a .pbf using osmconvert, osmosis, ogr2ogr, etc after downloading, but ran into problems or documentation that I couldn't follow to set the options properly in all cases.</p>
<p>It seems like downloading directly to .pbf format is the simplest method, maybe I am missing something basic to specify this.</p>
<p>To summarize my key asks, I would like: * to download directly from the command line * data in .pbf format * to use country boundaries (such as offered with name=&lt;countryname&gt;) in the Overpass API for the extract specification</p>
<p>My environment is a Mac.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-wget" rel="tag" title="see questions tagged &#39;wget&#39;">wget</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Apr '18, 21:31</strong></p>
<img src="https://secure.gravatar.com/avatar/12cd3da9d1a0d975766591dc679e01c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neutronbarn&#39;s gravatar image" />
<p><span>neutronbarn</span><br />
<span class="score" title="14 reputation points">14</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neutronbarn has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Apr '18, 22:13</strong> </span></p>
</div>
</div>
<div id="comments-container-62911" class="comments-container">
&#10;</div>
<div id="comment-tools-62911" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62911-form-container" class="comment-form-container">
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

<span id="62913"></span>

<div id="answer-container-62913" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62913-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="neutronbarn has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you're asking will put a high burden on the Overpass server since it has to collect all the data for the whole country. Overpass will refuse to do this for all but the smallest countries, and rightly so - a few people downloading a whole country like that could easily make the server unusable for everybody else.</p>
<p>So: don't do it.</p>
<p>Instead, download the nightly updated country files from download.geofabrik.de; if the fact that these are slightly larger than the exact country boundary is a problem, run an "osmium" or "osmosis" step afterwards to cut out the precise country extent. If what you're looking for is not found on download.geofabrik.de, head over to extracts.bbbike.org where you can request custom extracts for arbitrary polygonal areas; they, too, have a size limit but they will allow larger files than Overpass.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '18, 22:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-62913" class="comments-container">
<span id="62914"></span>
<div id="comment-62914" class="comment">
<div id="post-62914-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It sounds like cutting at the country boundary after download from geofabrik is what I want. I'll give this a try with osmium and osmosis. Thanks for the description of why not to do this on the Overpass server.</p>
</div>
<div id="comment-62914-info" class="comment-info">
<span class="comment-age">(04 Apr '18, 22:40)</span> <span class="comment-user userinfo">neutronbarn</span>
</div>
</div>
</div>
<div id="comment-tools-62913" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62913-form-container" class="comment-form-container">
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

