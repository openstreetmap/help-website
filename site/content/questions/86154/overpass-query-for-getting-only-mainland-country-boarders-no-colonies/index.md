+++
type = "question"
title = "Overpass query for getting only mainland country boarders (No colonies)"
description = '''Dear all, I am trying to get the Country borders of France from open street map using overpass turbo as follows: [out:json]; rel[admin_level=2][&quot;ISO3166-1&quot;=&quot;FR&quot;]; out geom; is there a way to only get the country border on the European continent (Main Country borders), excluding all the hundreds of f...'''
date = "2022-11-15T17:41:00Z"
lastmod = "2022-11-16T09:49:00Z"
weight = 86154
keywords = [ "openstreetmap", "overpass-turbo" ]
aliases = [ "/questions/86154" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass query for getting only mainland country boarders (No colonies)](/questions/86154/overpass-query-for-getting-only-mainland-country-boarders-no-colonies)

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
<span id="post-86154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86154-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear all, I am trying to get the Country borders of France from open street map using overpass turbo as follows:</p>
<p>[out:json]; rel[admin_level=2]["ISO3166-1"="FR"]; out geom;</p>
<p>is there a way to only get the country border on the European continent (Main Country borders), excluding all the hundreds of french colonial islands around the world? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Nov '22, 17:41</strong></p>
<img src="https://secure.gravatar.com/avatar/bd39fa8901794d6ac20ba4faa765d461?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jojojatt&#39;s gravatar image" />
<p><span>jojojatt</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jojojatt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86154" class="comments-container">
&#10;</div>
<div id="comment-tools-86154" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86154-form-container" class="comment-form-container">
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

<span id="86156"></span>

<div id="answer-container-86156" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86156-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jojojatt has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Area of France in Europe (including Corse) is called France métropolitaine.</p>
<p>So your overpass query would look like:</p>
<pre><code>[out:json]; rel[admin_level=3][name=&quot;France métropolitaine&quot;]; out geom;</code></pre>
<p>See: <a href="http://overpass-turbo.eu/s/1nOq">http://overpass-turbo.eu/s/1nOq</a></p>
<p>(here is the corresponding nominatim query: <a href="https://nominatim.osm.org/ui/search.html?q=France+m%C3%A9tropolitaine">https://nominatim.osm.org/ui/search.html?q=France+m%C3%A9tropolitaine</a> that will get you the same relation <a href="https://www.openstreetmap.org/relation/1403916#map=5/42.488/15.403">https://www.openstreetmap.org/relation/1403916#map=5/42.488/15.403</a> )</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '22, 09:49</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '22, 10:12</strong> </span></p>
</div>
</div>
<div id="comments-container-86156" class="comments-container">
&#10;</div>
<div id="comment-tools-86156" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86156-form-container" class="comment-form-container">
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

