+++
type = "question"
title = "Get all streetnames for a single country without using city/polygon parameters"
description = '''I want to get all streetnames, the neighborhood (suburb) of that street, zipcode, and all housenumbers of the street with their individual latitude/longitude for the COUNTRY of Germany. For example, the details from this node: https://www.openstreetmap.org/node/3081665937 I found this: https://help....'''
date = "2022-05-11T17:20:00Z"
lastmod = "2022-05-11T18:51:00Z"
weight = 84438
keywords = [ "download", "nodes", "streetnames", "metadata" ]
aliases = [ "/questions/84438" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get all streetnames for a single country without using city/polygon parameters](/questions/84438/get-all-streetnames-for-a-single-country-without-using-citypolygon-parameters)

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
<span id="post-84438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84438-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to get all streetnames, the neighborhood (suburb) of that street, zipcode, and all housenumbers of the street with their individual latitude/longitude for the COUNTRY of Germany.</p>
<p>For example, the details from this node: <a href="https://www.openstreetmap.org/node/3081665937">https://www.openstreetmap.org/node/3081665937</a></p>
<p>I found this: <a href="https://help.openstreetmap.org/questions/23488/export-streets-names">https://help.openstreetmap.org/questions/23488/export-streets-names</a> and <a href="https://help.openstreetmap.org/questions/9816/the-best-way-to-extract-street-list">https://help.openstreetmap.org/questions/9816/the-best-way-to-extract-street-list</a></p>
<p>I tried following what's here: <a href="https://wiki.openstreetmap.org/wiki/Osmconvert">https://wiki.openstreetmap.org/wiki/Osmconvert</a> I downloaded osmconvert.exe already.</p>
<p>But the existing answers don't seem to provide a clear cut solution for what I think is a common request. I see other people struggling too, but then they don't post what worked for them if it even did.</p>
<p>I don't want to download per city (takes a lot of work) or use polygons (lot of work and error prone) for a specific area. I just want the above details for street nodes in a specific country.</p>
<p>What would be the command(s) to do this? Also taking into account the <code>--max-refs</code> parameter as this might result in a lot of nodes.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-metadata" rel="tag" title="see questions tagged &#39;metadata&#39;">metadata</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 May '22, 17:20</strong></p>
<img src="https://secure.gravatar.com/avatar/af0ca0130c6bca861e7224bd3c7e076d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ItsPete1987&#39;s gravatar image" />
<p><span>ItsPete1987</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ItsPete1987 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84438" class="comments-container">
&#10;</div>
<div id="comment-tools-84438" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84438-form-container" class="comment-form-container">
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

<span id="84439"></span>

<div id="answer-container-84439" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84439-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is a common request but there is not an easy solution.</p>
<p>You can extract all objects - nodes and ways - that have a house number AND a street name AND a city AND a postcode. That is relatively easy. However, your result will not contain all street names, for example here's a street that will be missing (all examples are current as of May 11, 2022):</p>
<p><a href="https://www.openstreetmap.org/way/30761152">https://www.openstreetmap.org/way/30761152</a></p>
<p>because there are no house numbers mapped along that street. You will also be missing this street</p>
<p><a href="https://www.openstreetmap.org/way/632243700">https://www.openstreetmap.org/way/632243700</a></p>
<p>because while there are house numbers, the addresses are mapped without an addr:street or addr:postcode or addr:city tag. For the same reason you will be missing almost all streets in Haßbergen: <a href="https://www.openstreetmap.org/#map=16/52.7307/9.2317">https://www.openstreetmap.org/#map=16/52.7307/9.2317</a></p>
<p>And so on. And this is not even starting to discuss the corner case of address interpolation lines.</p>
<p>It is a complicated issue and no one solution exists that solves everything. The cheap and easy approach is to indeed look only for objects with addr:* tags - no polygons required. On the other hand, if you want to capture streets that do not have addresses on them as well, then you will have to choose one of the solutions that looks at highway=* objects too. Since these will never have city or postal code names tagged on them, you will then have to look at city and postal code polygons to determine the matching values.</p>
<p>The most flexible solution is probably importing everything into a PostGIS database with osm2pgsql, and then applying the necessary SQL to get what you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '22, 18:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 May '22, 18:53</strong> </span></p>
</div>
</div>
<div id="comments-container-84439" class="comments-container">
&#10;</div>
<div id="comment-tools-84439" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84439-form-container" class="comment-form-container">
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

