+++
type = "question"
title = "How to use output of overpass api"
description = '''Dear All, I have extracted way data for Railways over one country with [out:json], now how can i use this data to get all ways on google earth or QGIS? I am very new to this , just ignore for any stupidity. ( area[&quot;ISO3166-1:alpha2&quot;=&quot;PK&quot;];) -&amp;gt;.a;  way[&quot;railway&quot;]  (area.a);  (._;&amp;gt;;);  out body;...'''
date = "2020-04-13T18:23:00Z"
lastmod = "2020-04-14T11:16:00Z"
weight = 74136
keywords = [ "overpass", "json" ]
aliases = [ "/questions/74136" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to use output of overpass api](/questions/74136/how-to-use-output-of-overpass-api)

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
<span id="post-74136-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74136-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74136-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear All, I have extracted way data for Railways over one country with [out:json], now how can i use this data to get all ways on google earth or QGIS? I am very new to this , just ignore for any stupidity.</p>
<pre><code>( area[&quot;ISO3166-1:alpha2&quot;=&quot;PK&quot;];) -&gt;.a;
        way[&quot;railway&quot;]
          (area.a);
         (._;&gt;;);
 out body;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Apr '20, 18:23</strong></p>
<img src="https://secure.gravatar.com/avatar/df472021d41cc45f21580b8991a3d1d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PRailway&#39;s gravatar image" />
<p><span>PRailway</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PRailway has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Apr '20, 18:25</strong> </span></p>
</div>
</div>
<div id="comments-container-74136" class="comments-container">
<span id="74140"></span>
<div id="comment-74140" class="comment">
<div id="post-74140-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>if by "get all ways on google earth" you mean display them on GE then converting to KML or GPX would be best. You don't say if you're using Overpass turbo but there's an export tab which provides the options. PS if your after just the rail tracks it better to do a more specific search.</p>
<p><a href="https://overpass-turbo.eu/s/SN5">https://overpass-turbo.eu/s/SN5</a></p>
</div>
<div id="comment-74140-info" class="comment-info">
<span class="comment-age">(13 Apr '20, 21:14)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="74150"></span>
<div id="comment-74150" class="comment">
<div id="post-74150-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you sir, does your query give me the whole railway network? and what is the difference between both?</p>
</div>
<div id="comment-74150-info" class="comment-info">
<span class="comment-age">(14 Apr '20, 07:48)</span> <span class="comment-user userinfo">PRailway</span>
</div>
</div>
<span id="74153"></span>
<div id="comment-74153" class="comment">
<div id="post-74153-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>cross-post: <a href="https://gis.stackexchange.com/questions/358153/how-to-use-output-of-overpass-api">https://gis.stackexchange.com/questions/358153/how-to-use-output-of-overpass-api</a></p>
</div>
<div id="comment-74153-info" class="comment-info">
<span class="comment-age">(14 Apr '20, 08:35)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="74169"></span>
<div id="comment-74169" class="comment">
<div id="post-74169-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/18204/prailway">@PRailway</a> it returns all ways within PK which are tagged as railway=rail. Whether it's the 'whole network', you're probably better placed to tell. Your original routine probably won't find all 'railway' objects as you were only searching for ways types, omitting nodes &amp; relations. Please read the wiki to understand the differences.</p>
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a> It's not a cross post as it's a forum independent of OSM. Answers from one do not appear in the other.</p>
</div>
<div id="comment-74169-info" class="comment-info">
<span class="comment-age">(14 Apr '20, 11:16)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-74136" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74136-form-container" class="comment-form-container">
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

<span id="74155"></span>

<div id="answer-container-74155" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74155-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="PRailway has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>i mean best way in this case - export result as geojson (menu: "export" - "as geojson") and open this file.geojson in QGIS - in this way you save all geometries and attribute data. For add, you can use plugin "QuickMapServices" in QGIS to see imagery covers as WMS\TMS, for example, bing imagery, Google satellite imagery, Openstreetmap Mapnik cover and more.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '20, 08:44</strong></p>
<img src="https://secure.gravatar.com/avatar/cef3009cbb97c14c9ea084c6872f03f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ForstEK&#39;s gravatar image" />
<p><span>ForstEK</span><br />
<span class="score" title="81 reputation points">81</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ForstEK has one accepted answer">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Apr '20, 08:47</strong> </span></p>
</div>
</div>
<div id="comments-container-74155" class="comments-container">
&#10;</div>
<div id="comment-tools-74155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74155-form-container" class="comment-form-container">
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

