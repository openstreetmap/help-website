+++
type = "question"
title = "How to get missing city and state from a node that represents an address point?"
description = '''I&#x27;m new to OSM and I&#x27;m particularly interested in address point data. Currently I&#x27;m hoping to extract address point data using osmosis: osmosis --rx washington-latest.osm --tf accept-nodes &#x27;addr:housenumber=&#x27;, &#x27;addr:street=&#x27; --tf reject-ways --tf reject-relations --wx ap_hn_st_nd_only.osm I found th...'''
date = "2017-03-05T18:59:00Z"
lastmod = "2017-03-06T04:45:00Z"
weight = 54926
keywords = [ "point", "address" ]
aliases = [ "/questions/54926" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get missing city and state from a node that represents an address point?](/questions/54926/how-to-get-missing-city-and-state-from-a-node-that-represents-an-address-point)

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
<span id="post-54926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54926-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to OSM and I'm particularly interested in address point data. Currently I'm hoping to extract address point data using osmosis:</p>
<p>osmosis --rx washington-latest.osm --tf accept-nodes 'addr:housenumber=<em>', 'addr:street=</em>' --tf reject-ways --tf reject-relations --wx ap_hn_st_nd_only.osm</p>
<p>I found that many nodes that have housenumber and street information do not have a city or state tag. For instance:</p>
<p>&lt;node id="31368542" version="8" timestamp="2016-07-08T22:50:39Z" uid="137875" user="lukobe" changeset="40602379" lat="47.6611364" lon="-122.3140309"&gt; &lt;tag k="name" v="Neptune Theatre"/&gt; &lt;tag k="source" v="local knowledge"/&gt; &lt;tag k="amenity" v="theatre"/&gt; &lt;tag k="addr:street" v="Northeast 45th Street"/&gt; &lt;tag k="addr:housenumber" v="1303"/&gt; &lt;/node&gt;</p>
<p>Is there a way to find out and backfill the data? For my use case, housenumber, street, city, and state are indispensable.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-point" rel="tag" title="see questions tagged &#39;point&#39;">point</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Mar '17, 18:59</strong></p>
<img src="https://secure.gravatar.com/avatar/113f3247b68d1f21a2c594b2b87519c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zlzhao1104&#39;s gravatar image" />
<p><span>zlzhao1104</span><br />
<span class="score" title="61 reputation points">61</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zlzhao1104 has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-54926" class="comments-container">
&#10;</div>
<div id="comment-tools-54926" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54926-form-container" class="comment-form-container">
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

<span id="54929"></span>

<div id="answer-container-54929" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54929-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The safest way would be loading the whole Washington file into a database with osm2pgsql (use hstore!) and then copy interesting objects into a new table, filling in missing state (well all should be Washington, right?) and city info based on what polygons the points are in.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '17, 19:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-54929" class="comments-container">
<span id="54936"></span>
<div id="comment-54936" class="comment">
<div id="post-54936-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the suggestion. Actually, we are working on extracting address point data at different countries. As far as I understand, in many countries (other than US), I can download data in the country-level granularity.</p>
<p>Does OSM provide administrative boundary data as well (e.g., city, state)? If yes, I assume the type should be relation, right? If I understand you correctly, I probably can backfill missing city/state information in terms of the point-in-polygon relationship?</p>
</div>
<div id="comment-54936-info" class="comment-info">
<span class="comment-age">(06 Mar '17, 04:45)</span> <span class="comment-user userinfo">zlzhao1104</span>
</div>
</div>
</div>
<div id="comment-tools-54929" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54929-form-container" class="comment-form-container">
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

