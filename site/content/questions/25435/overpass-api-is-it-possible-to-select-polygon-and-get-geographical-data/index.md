+++
type = "question"
title = "Overpass API: Is it possible to select polygon and get geographical data?"
description = '''Overpass API: Is it possible to select polygon and get geographical data? Thanks in advance! I want to select polygon and get geographical data of polygon&#x27;s edges, like polyline.'''
date = "2013-08-15T14:59:00Z"
lastmod = "2013-08-19T16:49:00Z"
weight = 25435
keywords = [ "overpassapi" ]
aliases = [ "/questions/25435" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass API: Is it possible to select polygon and get geographical data?](/questions/25435/overpass-api-is-it-possible-to-select-polygon-and-get-geographical-data)

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
<span id="post-25435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25435-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Overpass API: Is it possible to select polygon and get geographical data?</p>
<p>Thanks in advance!</p>
<p>I want to select polygon and get geographical data of polygon's edges, like polyline.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Aug '13, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/6b7cf3bcdadfb73ea2f5f36e8d9d0f13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AnkaAnica&#39;s gravatar image" />
<p><span>AnkaAnica</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AnkaAnica has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Aug '13, 15:44</strong> </span></p>
</div>
</div>
<div id="comments-container-25435" class="comments-container">
&#10;</div>
<div id="comment-tools-25435" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25435-form-container" class="comment-form-container">
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

<span id="25437"></span>

<div id="answer-container-25437" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25437-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-25437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AnkaAnica has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do you mean you want to download all data inside a non-rectangular polygon? That is explained on <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Select_Region_by_Polygon">http://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Select_Region_by_Polygon</a> .</p>
<pre><code>(
  node(poly:&quot;50.7 7.1 50.7 7.12 50.71 7.11&quot;);
  &lt;;
);
out meta;</code></pre>
<p>Note that you need some kind of recurse magic to also get ways and relations.</p>
<p>To get bounding box coordinates by selecting from a map use <a href="http://osm.duschmarke.de/bbox.html">http://osm.duschmarke.de/bbox.html</a> (german; you need to hold down ctrl and then click and drag the bbox, the coordinates will be displayed in the bottom text fields).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '13, 15:08</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Aug '13, 15:53</strong> </span></p>
</div>
</div>
<div id="comments-container-25437" class="comments-container">
<span id="25468"></span>
<div id="comment-25468" class="comment">
<div id="post-25468-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>To download by country, use <strong>area[name="Belgium"];( node(area); &lt;;);out meta;</strong>. The precise name can be tricky, but you can open [the popup UI][1], click somewhere in your country and search on the last pages of the popup for an entry with "Country Boundary". That gives you the OSM name of your country to use in the above query.</p>
<p>[1] <a href="http://overpass.apis.dev.openstreetmap.org">http://overpass.apis.dev.openstreetmap.org</a></p>
</div>
<div id="comment-25468-info" class="comment-info">
<span class="comment-age">(16 Aug '13, 07:13)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
<span id="25479"></span>
<div id="comment-25479" class="comment">
<div id="post-25479-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much! Just one question more...can I select or entry name of provice?</p>
</div>
<div id="comment-25479-info" class="comment-info">
<span class="comment-age">(16 Aug '13, 12:34)</span> <span class="comment-user userinfo">AnkaAnica</span>
</div>
</div>
</div>
<div id="comment-tools-25437" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25437-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25449"></span>

<div id="answer-container-25449" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25449-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-25449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>see <a href="https://help.openstreetmap.org/questions/20841/how-to-query-all-elements-within-an-outline-way-from-overpass-api">how-to-query-all-elements-within-an-outline-way-from-overpass-api</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '13, 17:15</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-25449" class="comments-container">
<span id="25453"></span>
<div id="comment-25453" class="comment">
<div id="post-25453-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can I do it by selecting name of country and how?</p>
</div>
<div id="comment-25453-info" class="comment-info">
<span class="comment-age">(15 Aug '13, 17:24)</span> <span class="comment-user userinfo">AnkaAnica</span>
</div>
</div>
<span id="25457"></span>
<div id="comment-25457" class="comment">
<div id="post-25457-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>If you are looking for country outlines, go to www.naturalearthdata.com and download their "admin0" data set.</p>
</div>
<div id="comment-25457-info" class="comment-info">
<span class="comment-age">(15 Aug '13, 18:25)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="25581"></span>
<div id="comment-25581" class="comment">
<div id="post-25581-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you want to do the mentioned query via overpassapi limited by the outline of a country, go to <a href="http://nominatim.openstreetmap.org">http://nominatim.openstreetmap.org</a> and enter the countries name ... examine the results carefully and find the right relation within the raw OSM data.</p>
<p>Then you can decide to use the relation ID number that you can use by adding the mentioned offset, or type the name of the "area" that you have found.</p>
<p>But be sure to use the right name, and that the name is unique in the OSM database.</p>
</div>
<div id="comment-25581-info" class="comment-info">
<span class="comment-age">(19 Aug '13, 16:49)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-25449" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25449-form-container" class="comment-form-container">
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

