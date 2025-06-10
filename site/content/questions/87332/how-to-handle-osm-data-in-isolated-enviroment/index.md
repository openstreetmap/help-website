+++
type = "question"
title = "How to handle OSM data in isolated enviroment"
description = '''Hi, My question is fairly simple but unable to get the answer. So thanks in advance. I am working on the software in which I will be making edits to maps based on my operations needs and dont want my changes to impact globally. So would like to know, how we can achieve it? Like we can use JOSM and i...'''
date = "2023-06-01T19:39:00Z"
lastmod = "2023-06-02T09:49:00Z"
weight = 87332
keywords = [ "openstreetmap", "ways", "way_barrier", "barriers", "mappings" ]
aliases = [ "/questions/87332" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to handle OSM data in isolated enviroment](/questions/87332/how-to-handle-osm-data-in-isolated-enviroment)

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
<span id="post-87332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87332-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, My question is fairly simple but unable to get the answer. So thanks in advance.</p>
<p>I am working on the software in which I will be making edits to maps based on my operations needs and dont want my changes to impact globally. So would like to know, how we can achieve it? Like we can use JOSM and instead of updating the data back to OSM, can do OSRM processing on that but will it really work.</p>
<p>The other question is for barrier. Adding the point on the way and making it of type barrier work but what if I want to make a line as type barrier and if that line is intersecting with any other way, then it should be non accessible. Is it possible somehow.</p>
<p>Your help will be highly appreciated and will save me from lot of troubles. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-way_barrier" rel="tag" title="see questions tagged &#39;way_barrier&#39;">way_barrier</span> <span class="post-tag tag-link-barriers" rel="tag" title="see questions tagged &#39;barriers&#39;">barriers</span> <span class="post-tag tag-link-mappings" rel="tag" title="see questions tagged &#39;mappings&#39;">mappings</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '23, 19:39</strong></p>
<img src="https://secure.gravatar.com/avatar/48f927a70cdc8e9d47d4a6b463894acb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajay007in&#39;s gravatar image" />
<p><span>ajay007in</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajay007in has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jun '23, 11:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-87332" class="comments-container">
&#10;</div>
<div id="comment-tools-87332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87332-form-container" class="comment-form-container">
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

<span id="87333"></span>

<div id="answer-container-87333" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87333-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The answer to the first part of your question is:</p>
<p>What you want is possible as long as you understand that from the point on where you start making your own local changes, you will never be able to update from OSM again - i.e. you're stuck at that point in time and the full responsibility for making changes now lies with you.</p>
<p>If the area you are working with is small enough to be loaded wholly into JOSM then you can work with a local OSM file, edit that in JOSM, and load it into OSRM. JOSM's way of saving an OSM file is slightly different from standard OSM, e.g. newly created objects will receive negative IDs, and it might be necessary to reformat or renumber the file for processing but that's not a big hurdle.</p>
<p>If the area you are working with is too large to load into JOSM at once, then you will need to set up a complete OSM server (the "openstreetmap-website" code from GitHub) to hold your local data. You can then use that much like you would use the standard OSM database but be warned, it's a lot of components (you'll need to set up the data export for consumption by OSRM as well, and so on).</p>
<p>The answer to your second question is, it is probably possible to make OSRM query a secondary data set while building the routing graph so that you can feed linear barriers into it but it will require some coding. Maybe check out routing engines that already support "avoid areas", like e.g. OpenRouteService.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '23, 22:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-87333" class="comments-container">
<span id="87338"></span>
<div id="comment-87338" class="comment">
<div id="post-87338-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I know that people are using OSRM with altitude data to change the costing of steep segments - I don't know how it's done exactly but I figure that linear barriers are very similar to that. See <a href="https://github.com/Project-OSRM/osrm-backend/issues/546">https://github.com/Project-OSRM/osrm-backend/issues/546</a> for a discussion of using altitude data - it's a bit dated though so I cannot say how it relates to the current code base.</p>
</div>
<div id="comment-87338-info" class="comment-info">
<span class="comment-age">(02 Jun '23, 09:46)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="87339"></span>
<div id="comment-87339" class="comment">
<div id="post-87339-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>osm-website is free software and you can use it any way you want. Data-wise, if you start with OSM data and your users make changes to that, the resulting data set is still ODbL licensed and must, when publicly used, be offered under ODbL as well. This means you can make "private" changes as long as only you and people in your organisation use it, but if you then build a public-facing service ("come to my web site for better routing with all the improvements I made") then you need to release your data under ODbL, at least to those who use your web site.</p>
</div>
<div id="comment-87339-info" class="comment-info">
<span class="comment-age">(02 Jun '23, 09:49)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-87333" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87333-form-container" class="comment-form-container">
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

