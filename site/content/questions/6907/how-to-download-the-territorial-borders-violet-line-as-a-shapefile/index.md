+++
type = "question"
title = "how to download the territorial borders (violet line) as a shapefile"
description = '''Where can I download the violet line representing the territorial borders (under water) in a shapefile format? I know about the download section of the Geofabrik server (http://download.geofabrik.de/osm/), the problem is that I can&#x27;t find the violet line in any of the country zip files. I want to im...'''
date = "2011-08-05T12:12:00Z"
lastmod = "2011-08-05T15:21:00Z"
weight = 6907
keywords = [ "shapefile", "download", "gis" ]
aliases = [ "/questions/6907" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to download the territorial borders (violet line) as a shapefile](/questions/6907/how-to-download-the-territorial-borders-violet-line-as-a-shapefile)

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
<span id="post-6907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6907-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Where can I download the violet line representing the territorial borders (under water) in a shapefile format? I know about the download section of the Geofabrik server (<a href="http://download.geofabrik.de/osm/),">http://download.geofabrik.de/osm/),</a> the problem is that I can't find the violet line in any of the country zip files. I want to import it in a GIS program (manifold gis) and reproject it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-gis" rel="tag" title="see questions tagged &#39;gis&#39;">gis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Aug '11, 12:12</strong></p>
<img src="https://secure.gravatar.com/avatar/56d900f4ad4bf88841920c43bca7a5ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="polyconic&#39;s gravatar image" />
<p><span>polyconic</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="polyconic has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Aug '11, 12:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-6907" class="comments-container">
&#10;</div>
<div id="comment-tools-6907" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6907-form-container" class="comment-form-container">
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

<span id="6908"></span>

<div id="answer-container-6908" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6908-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-6908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can download the normaly offered raw OSM data by <a href="http://geofabrik.de">geofabrik.de</a> or <a href="http://cloudmade.com">cloudmade.com</a> and do some filtering with osmosis or <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a>. You can define that you keep only elements like <em>boundary=administrative</em> or whatever you need.</p>
<p>After that, you can convert your filtered data into shapefiles with the tools listed at <a href="https://wiki.openstreetmap.org/wiki/Shapefiles">shapefile</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Aug '11, 12:31</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Aug '11, 13:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span></p>
</div>
</div>
<div id="comments-container-6908" class="comments-container">
<span id="6910"></span>
<div id="comment-6910" class="comment">
<div id="post-6910-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes, but i dont know in which of the raw osm data package that line is... it is not in eiter of the country packages and the does not be a "world" package of some kind...</p>
</div>
<div id="comment-6910-info" class="comment-info">
<span class="comment-age">(05 Aug '11, 13:47)</span> <span class="comment-user userinfo">polyconic</span>
</div>
</div>
</div>
<div id="comment-tools-6908" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6908-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6911"></span>

<div id="answer-container-6911" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6911-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6911-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-6911-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Firstly, a bit of info about how the data at Geofabrik is split is contained <a href="http://download.geofabrik.de/clipbounds/">here</a>. It's worth reading that to understand what will and won't be in individual Geofabik extracts.</p>
<p>If for whatever reason what you want isn't available from Geofabrik (presumably you want ways such as <a href="https://www.openstreetmap.org/browse/way/28421653">this</a> and the relations that they are part of) then perhaps an <a href="https://wiki.openstreetmap.org/wiki/Xapi">Xapi</a> query would help? The Overpass and Jxapi servers (either OSM's or Mapquest's) would be the ones to start with, although you need to experiment a bit to check that you're getting the data that you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Aug '11, 15:21</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-6911" class="comments-container">
&#10;</div>
<div id="comment-tools-6911" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6911-form-container" class="comment-form-container">
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

