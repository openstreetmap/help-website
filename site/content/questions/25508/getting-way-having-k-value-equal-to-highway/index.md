+++
type = "question"
title = "Getting Way having k value equal to highway"
description = '''I want to filter the osm data such that k value under &amp;lt;tag&amp;gt; equals to highway, right now i am downloading whole data using bbox(GET /api/0.6/map?bbox=left,bottom,right,top) API checking whether value of k equals to &quot;highway&quot; or not, Is there any short method such that i can fetch the data wher...'''
date = "2013-08-17T11:25:00Z"
lastmod = "2013-08-19T06:47:00Z"
weight = 25508
keywords = [ "xml", "filter", "way", "highway" ]
aliases = [ "/questions/25508" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting Way having k value equal to highway](/questions/25508/getting-way-having-k-value-equal-to-highway)

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
<span id="post-25508-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25508-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25508-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to filter the osm data such that k value under &lt;tag&gt; equals to highway, right now i am downloading whole data using bbox(GET /api/0.6/map?bbox=left,bottom,right,top) API checking whether value of k equals to "highway" or not, Is there any short method such that i can fetch the data where k value equals to "highway" . Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Aug '13, 11:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a2cf8d184bda62f6b2c7af42e787300d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mawa&#39;s gravatar image" />
<p><span>Mawa</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mawa has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Aug '13, 11:26</strong> </span></p>
</div>
</div>
<div id="comments-container-25508" class="comments-container">
&#10;</div>
<div id="comment-tools-25508" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25508-form-container" class="comment-form-container">
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

<span id="25512"></span>

<div id="answer-container-25512" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25512-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-25512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's much better to use <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide">Overpass</a> for this type of query. It offloads a big <code>bbox GET</code> request from the API and you can filter by tags. See the wiki page for details, or use the xapi syntax as follows (example is for mapquest version, there are others, for instance on <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/XAPI_Compatibility_Layer">Overpass Turbo</a>):</p>
<pre><code>http://open.mapquestapi.com/xapi/api/0.6/way[highway=*][bbox=lon_low,lat_low,lon_hi,lat_hi]</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '13, 13:35</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-25512" class="comments-container">
<span id="25562"></span>
<div id="comment-25562" class="comment">
<div id="post-25562-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please note that the MapQuest XAPI endpoint is not associated to the Overpass API, and that MapQuest currently uses an outdated data base. For this reason I strongly recommend to use one of the other instances instead.</p>
<p>I, as maintainer of the Overpass XAPI instances, get from time to time bug reports that the MapQuest instance is out of date, but I cannot do more than anybody else on that problem.</p>
</div>
<div id="comment-25562-info" class="comment-info">
<span class="comment-age">(19 Aug '13, 06:47)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-25512" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25512-form-container" class="comment-form-container">
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

