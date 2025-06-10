+++
type = "question"
title = "[UMAP] Linking public data to custom markers or surfaces hosted in private UMAP instance"
description = '''Hello dear mappers, I&#x27;m currently working for a public administration (30K citizen City) that is considering using OSM as a open-data backend for all publicly available content that we would also heavily enriched with our own data. Nevertheless, we&#x27;d prefer to keep technical informations or sensitiv...'''
date = "2017-04-04T15:30:00Z"
lastmod = "2017-04-11T07:51:00Z"
weight = 55473
keywords = [ "umap", "osm", "overpass" ]
aliases = [ "/questions/55473" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[UMAP\] Linking public data to custom markers or surfaces hosted in private UMAP instance](/questions/55473/umap-linking-public-data-to-custom-markers-or-surfaces-hosted-in-private-umap-instance)

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
<span id="post-55473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55473-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello dear mappers,</p>
<p>I'm currently working for a public administration (30K citizen City) that is considering using OSM as a open-data backend for all publicly available content that we would also heavily enriched with our own data. Nevertheless, we'd prefer to keep technical informations or sensitive content in a private instance of UMAP.</p>
<p>Therefore, I'm looking for a convenient way to link custom and "private" information (that would be kept in our own UMAP instance) to POI or buildings that are publicly available on the OSM map.</p>
<p>For example, we'd first contribute the location and details of the trash bins that are missing on the public map. Afterwards, we'd like to link them to our own pick-up circuit, designed and updated in UMAP, that is of little interest for the public community.</p>
<p>We'd also like to highlight some paths / road to trace the location of our optical fibers.</p>
<p>The following § have been answered below.</p>
<pre><code>In the same approach, we&#39;d like to be able to rapidly highlight all the buildings owned by the city (the Town Hall, the Swimming Pool) **without** having to create new polygons on top of the existing buildings.
&#10;A possible solution that I thought of would be to add specific tags to these building in the public map (Owner=&quot;City of ###&quot;) before being able to highlight these building in a custom rendering of tiles or using OverpassTurbo.
&#10;I&#39;m not sure whether it is possible or compliant with the good practices.</code></pre>
<p>Thanks a lot for your feedback and explanations. I'm still pretty new to OSM but quite knowledgeable regarding community-driven libre projects.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Apr '17, 15:30</strong></p>
<img src="https://secure.gravatar.com/avatar/b52f1d8d4aacb4cd8b0baddba952f6f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Le_PAH&#39;s gravatar image" />
<p><span>Le_PAH</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Le_PAH has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '17, 07:52</strong> </span></p>
</div>
</div>
<div id="comments-container-55473" class="comments-container">
&#10;</div>
<div id="comment-tools-55473" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55473-form-container" class="comment-form-container">
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

<span id="55547"></span>

<div id="answer-container-55547" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55547-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>I've found a partial solution to my question.</p>
<p>Contributors could add the <a href="https://wiki.openstreetmap.org/wiki/Key:ownership">ownership</a> key in order to specify that a building or marker belongs to a city. Along with the<a href="https://wiki.openstreetmap.org/wiki/Key:operator">operator</a> key, contributors may specify if buildings are operated by the city or a third party.</p>
<p>Nevertheless, I'm still struggling to find a proper way to link a marker in uMap to a building or a public marker other than by putting it at the same place on the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '17, 07:51</strong></p>
<img src="https://secure.gravatar.com/avatar/b52f1d8d4aacb4cd8b0baddba952f6f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Le_PAH&#39;s gravatar image" />
<p><span>Le_PAH</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Le_PAH has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55547" class="comments-container">
&#10;</div>
<div id="comment-tools-55547" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55547-form-container" class="comment-form-container">
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

