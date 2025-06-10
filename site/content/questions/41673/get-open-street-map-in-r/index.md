+++
type = "question"
title = "get open street map in R"
description = '''Hello,  I am trying to load up a norway map using &#x27;osm&#x27; within R,  myLocation &amp;lt;- c(lon = 17.468946, lat = 66.87202) myMap &amp;lt;- get_map(location=myLocation,source=&quot;osm&quot;, color=&#x27;bw&#x27;) ggmap(myMap)  I am getting error saying service unavailable-  Map from URL : http://maps.googleapis.com/maps/api/st...'''
date = "2015-03-13T10:13:00Z"
lastmod = "2015-03-13T11:55:00Z"
weight = 41673
keywords = [ "r" ]
aliases = [ "/questions/41673" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [get open street map in R](/questions/41673/get-open-street-map-in-r)

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
<span id="post-41673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41673-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am trying to load up a norway map using 'osm' within R,</p>
<pre><code>myLocation &lt;- c(lon = 17.468946, lat = 66.87202)
myMap &lt;- get_map(location=myLocation,source=&quot;osm&quot;, color=&#39;bw&#39;)
ggmap(myMap)</code></pre>
<p>I am getting error saying service unavailable-</p>
<blockquote>
<p>Map from URL : <a href="http://maps.googleapis.com/maps/api/staticmap?center=66.87202,17.468946&amp;zoom=10&amp;size=640x640&amp;maptype=terrain&amp;sensor=false">http://maps.googleapis.com/maps/api/staticmap?center=66.87202,17.468946&amp;zoom=10&amp;size=640x640&amp;maptype=terrain&amp;sensor=false</a> Error: map grabbing failed - see details in ?get_openstreetmap. In addition: Warning message: In download.file(url, destfile = destfile, quiet = !messaging, mode = "wb") : cannot open: HTTP status was '503 Service Unavailable'</p>
</blockquote>
<p>Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-r" rel="tag" title="see questions tagged &#39;r&#39;">r</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Mar '15, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/afaad1371bb76e489977e9e490099c37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aborg88&#39;s gravatar image" />
<p><span>aborg88</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aborg88 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Mar '15, 11:35</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-41673" class="comments-container">
<span id="41679"></span>
<div id="comment-41679" class="comment">
<div id="post-41679-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I very much doubt that a maptype=terrain through the google map api would give you OSM data, or is this just an example of the area?</p>
</div>
<div id="comment-41679-info" class="comment-info">
<span class="comment-age">(13 Mar '15, 11:51)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41673" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41673-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="41680"></span>

<div id="answer-container-41680" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41680-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-41680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You don't say but this looks like the ggmap package (<a href="http://cran.r-project.org/web/packages/ggmap/ggmap.pdf">http://cran.r-project.org/web/packages/ggmap/ggmap.pdf</a>) which appears to use the Export function of the OSM API to provide a raster image . The latter hardly ever works because it is very resource intensive and it rarely gets cycles because of the standard load on tile servers.</p>
<p>Additionally if this ever became heavily used it might be seen as a tile scraping application (see the get_cloudmade and get_stamen function documentation) which is contarary to OSM's Terms of Service.</p>
<p>In summary this is probably not working because it is using part of the OSM API which rarely functions for performance/load balancing reasons.</p>
<p>For vector data in R, the <a href="http://osmar.r-forge.r-project.org/">osmar</a> package is probably the best choice.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '15, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-41680" class="comments-container">
&#10;</div>
<div id="comment-tools-41680" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41680-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41677"></span>

<div id="answer-container-41677" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41677-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>ggmap package seems buggy. Why ask to google API for retrieving osm tiles? Maybe you may try the package 'OpenStreetMap': <a href="http://blog.fellstat.com/?cat=15">http://blog.fellstat.com/?cat=15</a> I've tested it, and it works fine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '15, 11:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-41677" class="comments-container">
&#10;</div>
<div id="comment-tools-41677" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41677-form-container" class="comment-form-container">
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

