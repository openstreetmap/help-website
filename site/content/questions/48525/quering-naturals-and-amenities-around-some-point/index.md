+++
type = "question"
title = "Quering naturals and amenities around some point"
description = '''Hi, I am new to overpass api. This is my query: (node(around:2000,57.179,24.709)[&quot;amenity&quot;];way(around:2000,57.179,24.709)[&quot;amenity&quot;];way(around:2000,57.179,24.709)[&quot;natural&quot;];way(around:2000,57.179,24.709)[&quot;landuse&quot;~&quot;forest|grass&quot;];);(._;&amp;gt;;);out body; What I am wandering is that I need 4 times t...'''
date = "2016-03-06T17:53:00Z"
lastmod = "2016-03-08T13:15:00Z"
weight = 48525
keywords = [ "overpass", "amenity", "natural" ]
aliases = [ "/questions/48525" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Quering naturals and amenities around some point](/questions/48525/quering-naturals-and-amenities-around-some-point)

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
<span id="post-48525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48525-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am new to overpass api.</p>
<p>This is my query:</p>
<p>(node(around:2000,57.179,24.709)["amenity"];way(around:2000,57.179,24.709)["amenity"];way(around:2000,57.179,24.709)["natural"];way(around:2000,57.179,24.709)["landuse"~"forest|grass"];);(._;&gt;;);out body;</p>
<p>What I am wandering is that I need 4 times to repeat around command.</p>
<p>What I want is to have my location, and have all naturals and amenities (landuse=forest or grass) as well around my location.</p>
<p>Isn't there more effective way to make the same query... Also I would prefer buildings, but when I add buildings, then the query runs long time...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-natural" rel="tag" title="see questions tagged &#39;natural&#39;">natural</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '16, 17:53</strong></p>
<img src="https://secure.gravatar.com/avatar/31e2ccd391313fb8f357d1432a24d426?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shazard&#39;s gravatar image" />
<p><span>Shazard</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shazard has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '16, 17:55</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-48525" class="comments-container">
<span id="48534"></span>
<div id="comment-48534" class="comment">
<div id="post-48534-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You need to repeat your location as you make the union of 4 different queries. I guess you speed it up a bit by dropping the parts where you look for landuse points (or building points), as most of them will be mapped as areas. OTOH, you should include relations in your query, in order to obtain the multi-polygons</p>
</div>
<div id="comment-48534-info" class="comment-info">
<span class="comment-age">(07 Mar '16, 06:46)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-48525" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48525-form-container" class="comment-form-container">
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

<span id="48569"></span>

<div id="answer-container-48569" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48569-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not possible in Overpass API, but it is possible in Overpass Turbo (which is just some sort of IDE written around Overpass API).</p>
<p>Overpass Turbo allows you to define "shortcuts" that you can use to refer to a common query part. See the example here: <a href="http://overpass-turbo.eu/s/eQU">http://overpass-turbo.eu/s/eQU</a> (it creates a new shortcut names "area" that uses the definition of that "around" command).</p>
<p>However, if you want to execute the query on a regular Overpass API server (f.e. via a http request on a webpage), you must get rid of these shortcuts again. You can get a valid Overpass API query by using one of the export options in Overpass Turbo.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '16, 13:15</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-48569" class="comments-container">
&#10;</div>
<div id="comment-tools-48569" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48569-form-container" class="comment-form-container">
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

