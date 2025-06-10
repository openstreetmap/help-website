+++
type = "question"
title = "Typical data sizes of raw OSM data for map-based WEB GIS applications"
description = '''Hi, I&#x27;m currently doing my undergraduate thesis where I compare Protocol Buffers and Flatbuffers as serialization formats for raw OSM data in map-based Web GIS applications. The client makes a request to the server who respond with OSM data. My question is, what are the typical data sizes (KB or MB)...'''
date = "2018-03-07T15:46:00Z"
lastmod = "2018-03-10T08:03:00Z"
weight = 62550
keywords = [ "planet", "comparison", "research", "data", "size" ]
aliases = [ "/questions/62550" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Typical data sizes of raw OSM data for map-based WEB GIS applications](/questions/62550/typical-data-sizes-of-raw-osm-data-for-map-based-web-gis-applications)

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
<span id="post-62550-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62550-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62550-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm currently doing my undergraduate thesis where I compare Protocol Buffers and Flatbuffers as serialization formats for raw OSM data in map-based Web GIS applications. The client makes a request to the server who respond with OSM data. My question is, what are the typical data sizes (KB or MB) for this kind of architecture? Is there any max/min size of what is typically sent? I imagine you wouldnt send the whole Planet.osm to the client. Is there a way for me to generate these test files given a max and min size? Any answers who point me in the right direction is very appreciated. I feel like im overwhelmed with information and cant seem to find an article discussing this.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-comparison" rel="tag" title="see questions tagged &#39;comparison&#39;">comparison</span> <span class="post-tag tag-link-research" rel="tag" title="see questions tagged &#39;research&#39;">research</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Mar '18, 15:46</strong></p>
<img src="https://secure.gravatar.com/avatar/f444e3649822b1bf9a43e0bef867cba1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Johan%20R%C3%B6nkk%C3%B6&#39;s gravatar image" />
<p><span>Johan Rönkkö</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Johan Rönkkö has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Mar '18, 22:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-62550" class="comments-container">
&#10;</div>
<div id="comment-tools-62550" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62550-form-container" class="comment-form-container">
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

<span id="62610"></span>

<div id="answer-container-62610" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62610-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-62610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The OSM (editing) API currently returns data in the standard OSM XML representation and limits responses both in geographic extent and size, see <a href="https://wiki.openstreetmap.org/wiki/API_v0.6">https://wiki.openstreetmap.org/wiki/API_v0.6</a> capabilities and map endpoint.</p>
<p>If you simply want to retrieve the same area in multiple formats <a href="https://extract.bbbike.org/">https://extract.bbbike.org/</a> is something you should look at. <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a> has downloads in pbf format for individual countries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Mar '18, 08:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Mar '18, 07:52</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-62610" class="comments-container">
&#10;</div>
<div id="comment-tools-62610" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62610-form-container" class="comment-form-container">
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

