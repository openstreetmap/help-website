+++
type = "question"
title = "OSM doesn&#x27;t search for an organization by its name in English and Russian"
description = '''Hello! I recently added the organization called Eco Magia (Эко Магия in russian) to OSM. I filled its fields very thoroughly including its name and description in 3 languages, fixed the shape of the building. I see it on the map but I can&#x27;t find it through the search. It says Nominatim and Geoname f...'''
date = "2022-04-19T10:33:00Z"
lastmod = "2022-04-19T16:43:00Z"
weight = 84214
keywords = [ "search", "nominatim", "geonames" ]
aliases = [ "/questions/84214" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OSM doesn't search for an organization by its name in English and Russian](/questions/84214/osm-doesnt-search-for-an-organization-by-its-name-in-english-and-russian)

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
<span id="post-84214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84214-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello!</p>
<p>I recently added the organization called <a href="https://www.openstreetmap.org/node/9670171394">Eco Magia (Эко Магия in russian)</a> to OSM. I filled its fields very thoroughly including its name and description in 3 languages, fixed the shape of the building. I see it on the map but I can't find it through the search. It says Nominatim and Geoname found nothing.</p>
<p>I tried to Google such problem but haven't found any solution.</p>
<p>How can I fix it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geonames" rel="tag" title="see questions tagged &#39;geonames&#39;">geonames</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Apr '22, 10:33</strong></p>
<img src="https://secure.gravatar.com/avatar/674b9d152fc865a1772be658df5abea3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="catoshock&#39;s gravatar image" />
<p><span>catoshock</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="catoshock has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84214" class="comments-container">
&#10;</div>
<div id="comment-tools-84214" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84214-form-container" class="comment-form-container">
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

<span id="84216"></span>

<div id="answer-container-84216" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84216-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-84216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="catoshock has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The name would be "Eco Magia" and not "Eco Magia | All day healthy breakfasts cafe and healthy food shop", that's a mix of a name and a description.</p>
<p>So right now Nominatim only finds the cafe if you search for the exact name the way you entered it in the name fields, e.g.: <a href="https://nominatim.osm.org/ui/search.html?q=Eco+Magia+%7C+All+day+healthy+breakfasts+cafe+and+healthy+food+shop">https://nominatim.osm.org/ui/search.html?q=Eco+Magia+%7C+All+day+healthy+breakfasts+cafe+and+healthy+food+shop</a></p>
<p>So you'll have to change the name into "Eco Magia" for e.g. name:en (and resp. for name:ru "Эко Магия" etc.) and put the rest in the resp. description tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '22, 11:35</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Apr '22, 11:36</strong> </span></p>
</div>
</div>
<div id="comments-container-84216" class="comments-container">
<span id="84219"></span>
<div id="comment-84219" class="comment">
<div id="post-84219-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you! That works for Nominatim. How to make GeoNames work too?</p>
</div>
<div id="comment-84219-info" class="comment-info">
<span class="comment-age">(19 Apr '22, 16:01)</span> <span class="comment-user userinfo">catoshock</span>
</div>
</div>
<span id="84220"></span>
<div id="comment-84220" class="comment">
<div id="post-84220-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Geonames is not related to OSM. So OSM cannot help you with any data questions in regard to Geonames. You'll have to look at geonames.org and maybe the forum there for any information about their database.</p>
</div>
<div id="comment-84220-info" class="comment-info">
<span class="comment-age">(19 Apr '22, 16:43)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-84216" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84216-form-container" class="comment-form-container">
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

