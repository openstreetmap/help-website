+++
type = "question"
title = "Postal Code &quot;Clustering&quot; from OSM Data"
description = '''Hey there people, I was curious if anyone can help me or guide me on how to create a map with the Postal Code Boundaries of Greece.  Roaming around the web, I found the initiative Free the post code where some creative people tried to create postal code boundaries from data, with an example here. Wh...'''
date = "2020-11-30T12:15:00Z"
lastmod = "2020-12-01T14:42:00Z"
weight = 77790
keywords = [ "postalcode", "osmfilter", "osm", "postcode", "help" ]
aliases = [ "/questions/77790" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Postal Code "Clustering" from OSM Data](/questions/77790/postal-code-clustering-from-osm-data)

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
<span id="post-77790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77790-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey there people,</p>
<p>I was curious if anyone can help me or guide me on how to create a map with the Postal Code Boundaries of Greece.</p>
<p>Roaming around the web, I found the initiative <a href="http://www.freethepostcode.org/">Free the post code</a> where some creative people tried to create postal code boundaries from data, with an example <a href="https://random.dev.openstreetmap.org/postcodes/">here</a>.</p>
<p>When I saw the Source code, I noticed that the authors approach and solve this problem with a Voronoi diagram, where as an input they give coordinates followed by postal code.</p>
<p>Can anyone help me to create the same input file for the Greece, from the Greek OSM data so I can test if the results are good enough?</p>
<p>The input should be <code>latitude longitude post code</code> but I am not sure how to extract them from the OSM file of Greece.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postalcode" rel="tag" title="see questions tagged &#39;postalcode&#39;">postalcode</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '20, 12:15</strong></p>
<img src="https://secure.gravatar.com/avatar/68cc0e804e9205bfc011ddbe896c2916?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="konsalex&#39;s gravatar image" />
<p><span>konsalex</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="konsalex has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77790" class="comments-container">
&#10;</div>
<div id="comment-tools-77790" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77790-form-container" class="comment-form-container">
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

<span id="77793"></span>

<div id="answer-container-77793" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77793-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77793-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77793-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One way to approach it is to use osmium to filter the objects and translate them into a <a href="https://osmcode.org/opl-file-format/">text oriented format</a>:</p>
<pre><code>osmium tags-filter -o codes.opl &lt;Greece&gt; &#39;addr:postcode&#39;</code></pre>
<p>You'd then want to process the ways in the file to have locations: <a href="https://docs.osmcode.org/osmium/latest/osmium-add-locations-to-ways.html">https://docs.osmcode.org/osmium/latest/osmium-add-locations-to-ways.html</a></p>
<p>Then from there you would extract the information of interest from each line. I had recently done something similar to the first step, but have not done the other steps, but I think it's a reasonable approach. There's other tools that can do similar things.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '20, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-77793" class="comments-container">
<span id="77805"></span>
<div id="comment-77805" class="comment">
<div id="post-77805-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey <a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> thanks for the reply.</p>
<p>I downloaded some data from overpass turbo with this query</p>
<p>` This has been generated by the overpass-turbo wizard. The original search was: “"addr:postcode"= <em>in Greece”</em> / [out:json][timeout:25]; // fetch area “Ελλάς” to search in {{geocodeArea:Ελλάς}}-&gt;.searchArea; // gather results ( // query part for: “"addr:postcode"=*” node<a href="area.searchArea">"addr:postcode"</a>;</p>
<p>); // print results out body;</p>
<blockquote>
<p>; `</p>
</blockquote>
<p>Then I imported them to QGIS and performed a Voronoi clustering and then Dissolved with the Postal Code property.</p>
<p>Although the results are pretty nice and accurate, some areas seem to have not enough representative data to cluster them properly.</p>
<p>Any clue how to extract more data rather than using only nodes?</p>
<p>P.S.: As I can see Nominatim is computing the postal codes correctly so I am guessing behind the scenes they are not using only nodes.</p>
</div>
<div id="comment-77805-info" class="comment-info">
<span class="comment-age">(30 Nov '20, 15:10)</span> <span class="comment-user userinfo">konsalex</span>
</div>
</div>
<span id="77822"></span>
<div id="comment-77822" class="comment">
<div id="post-77822-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Max! I managed to do this as you said. The resulted ways although they include a postcode attribute it is empty when I load it to QGIS. Any clue why?</p>
</div>
<div id="comment-77822-info" class="comment-info">
<span class="comment-age">(01 Dec '20, 12:56)</span> <span class="comment-user userinfo">konsalex</span>
</div>
</div>
<span id="77823"></span>
<div id="comment-77823" class="comment">
<div id="post-77823-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Use nwr instead of node, and use out center for centroids (or you can just take polygons &amp; compute centroids in QGIS &amp; merge with node layer before doing the Voronoi.</p>
</div>
<div id="comment-77823-info" class="comment-info">
<span class="comment-age">(01 Dec '20, 13:19)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="77824"></span>
<div id="comment-77824" class="comment">
<div id="post-77824-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey <a href="https://help.openstreetmap.org/users/647/sk53">@sk53</a> . I executed the query with nwr instead of only nodes, but the are no ways displayed see here: <a href="https://prnt.sc/vtnmd7">https://prnt.sc/vtnmd7</a> (with addr:postcode I suppose).</p>
</div>
<div id="comment-77824-info" class="comment-info">
<span class="comment-age">(01 Dec '20, 14:42)</span> <span class="comment-user userinfo">konsalex</span>
</div>
</div>
</div>
<div id="comment-tools-77793" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77793-form-container" class="comment-form-container">
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

