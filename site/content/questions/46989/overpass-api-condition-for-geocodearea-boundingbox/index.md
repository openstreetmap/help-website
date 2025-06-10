+++
type = "question"
title = "Overpass API Condition for GeocodeArea &amp; BoundingBox"
description = '''I could able to retrieve data using BoundingBoxes or GeocodeArea using over-pass API. While i want to get specific information from particular GeocodeArea i use  {{geocodeArea:India}}-&amp;gt;.searchArea;  For BoundingBoxes I use like  node[&quot;leisure&quot;=&quot;park&quot;](50.6,7.0,50.8,7.3);  How Can i prepare Overpa...'''
date = "2015-12-05T11:00:00Z"
lastmod = "2016-05-27T12:11:00Z"
weight = 46989
keywords = [ "query", "overpass-turbo" ]
aliases = [ "/questions/46989" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass API Condition for GeocodeArea & BoundingBox](/questions/46989/overpass-api-condition-for-geocodearea-boundingbox)

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
<span id="post-46989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46989-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I could able to retrieve data using BoundingBoxes or GeocodeArea using over-pass API. While i want to get specific information from particular GeocodeArea i use</p>
<pre><code> {{geocodeArea:India}}-&gt;.searchArea;</code></pre>
<p>For BoundingBoxes I use like</p>
<pre><code>  node[&quot;leisure&quot;=&quot;park&quot;](50.6,7.0,50.8,7.3);</code></pre>
<p>How Can i prepare Overpass query condition that satisfies both BBox &amp; GeocodeArea. Any Examples? Any Help would be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Dec '15, 11:00</strong></p>
<img src="https://secure.gravatar.com/avatar/ed7461b0364a7e373ebc6ed74a477108?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="suri1983&#39;s gravatar image" />
<p><span>suri1983</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="suri1983 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Dec '15, 11:01</strong> </span></p>
</div>
</div>
<div id="comments-container-46989" class="comments-container">
<span id="47037"></span>
<div id="comment-47037" class="comment">
<div id="post-47037-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As far as I know you can only limit one query by either bbox or area parameter ... there is no combination feature in overpass-api documentation.</p>
<p>But maybe you can do a difference between one result from the other and get a result you want. See <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Difference">http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Difference</a></p>
</div>
<div id="comment-47037-info" class="comment-info">
<span class="comment-age">(07 Dec '15, 17:11)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-46989" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46989-form-container" class="comment-form-container">
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

<span id="47107"></span>

<div id="answer-container-47107" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47107-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-47107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="suri1983 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can simply combine multiple filters in one query statement. In the following example we're looking for all pubs in Cologne (inside relation 62578), which in addition are inside a given bounding box. The resulting query should look like this:</p>
<pre><code>area(3600062578)-&gt;.searchArea;
node
  [&quot;amenity&quot;=&quot;pub&quot;]
  (area.searchArea)
  (50.91928498040378,6.7814483642578125,51.03858753963086,6.8932342529296875);
out body;</code></pre>
<p>Overpass Turbo Link: <a href="http://overpass-turbo.eu/s/ddV">http://overpass-turbo.eu/s/ddV</a></p>
<p>If you leave out the <code>(area.searchArea)</code> line in overpass turbo, you'll notice some additional pubs, whcih are inside the bounding box, but not in the Cologne area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Dec '15, 17:32</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Dec '15, 17:36</strong> </span></p>
</div>
</div>
<div id="comments-container-47107" class="comments-container">
<span id="47121"></span>
<div id="comment-47121" class="comment">
<div id="post-47121-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you all. Its kind of fun with OSM.</p>
</div>
<div id="comment-47121-info" class="comment-info">
<span class="comment-age">(12 Dec '15, 18:14)</span> <span class="comment-user userinfo">suri1983</span>
</div>
</div>
<span id="49859"></span>
<div id="comment-49859" class="comment">
<div id="post-49859-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/8708/mmd">@mmd</a>, may i know why is the 36000 number is prefixed with relation id?</p>
</div>
<div id="comment-49859-info" class="comment-info">
<span class="comment-age">(27 May '16, 10:12)</span> <span class="comment-user userinfo">yogi_ks</span>
</div>
</div>
<span id="49861"></span>
<div id="comment-49861" class="comment">
<div id="post-49861-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10906/yogi_ks"></a><a href="http://help.openstreetmap.org/users/10906/yogi_ks">@yogi_ks</a>: it's simply a convention which is only used for Overpass API: read more about it <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29">on the wiki page</a>.</p>
<p><em>By convention the area id can be calculated from an existing OSM way by adding 2400000000 to its OSM id, or in case of a relation by adding 3600000000 respectively</em></p>
</div>
<div id="comment-49861-info" class="comment-info">
<span class="comment-age">(27 May '16, 11:43)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="49862"></span>
<div id="comment-49862" class="comment">
<div id="post-49862-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/8708/mmd">@mmd</a>: thank you for the explanation.</p>
</div>
<div id="comment-49862-info" class="comment-info">
<span class="comment-age">(27 May '16, 12:11)</span> <span class="comment-user userinfo">yogi_ks</span>
</div>
</div>
</div>
<div id="comment-tools-47107" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47107-form-container" class="comment-form-container">
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

