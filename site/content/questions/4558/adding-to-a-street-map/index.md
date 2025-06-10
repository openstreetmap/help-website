+++
type = "question"
title = "Adding to a street map"
description = '''Hello. I am confused. I want to add borders of my local councilmanic district to a map of Los Angeles and post it to Wikipedia for use in an article. How do I do this? How do I get the map, and how do I draw the borders. I will copy the borders from a City of Los Angeles Web page and, I guess, draw ...'''
date = "2011-04-16T21:44:00Z"
lastmod = "2015-01-15T21:10:00Z"
weight = 4558
keywords = [ "borders" ]
aliases = [ "/questions/4558" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Adding to a street map](/questions/4558/adding-to-a-street-map)

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
<span id="post-4558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4558-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello. I am confused. I want to add borders of my local councilmanic district to a map of Los Angeles and post it to Wikipedia for use in an article. How do I do this? How do I get the map, and how do I draw the borders. I will copy the borders from a City of Los Angeles Web page and, I guess, draw them freehand on the map. Sincerely, your friend.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-borders" rel="tag" title="see questions tagged &#39;borders&#39;">borders</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Apr '11, 21:44</strong></p>
<img src="https://secure.gravatar.com/avatar/d169c917f1ab4e89362adc14bdf0e3b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeorgeLouis&#39;s gravatar image" />
<p><span>GeorgeLouis</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeorgeLouis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4558" class="comments-container">
<span id="4560"></span>
<div id="comment-4560" class="comment">
<div id="post-4560-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You are not allowed to copy from another map/web page/whatever if it doesn't have a license that says the data if free to reproduce.</p>
</div>
<div id="comment-4560-info" class="comment-info">
<span class="comment-age">(16 Apr '11, 21:54)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
</div>
<div id="comment-tools-4558" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4558-form-container" class="comment-form-container">
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

<span id="40421"></span>

<div id="answer-container-40421" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40421-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, You can search for existing administrative borders in Los Angeles in OSM with</p>
<ul>
<li><p><a href="http://overpass-turbo.eu">http://overpass-turbo.eu</a> with following request : <code>boundary=* in 'Los Angeles'</code></p></li>
<li><p>Export these borders in GeoJSON format.</p>
<p>Now you got the borders,</p></li>
<li><p>Launch : <a href="http://umap.openstreetmap.fr/en/">http://umap.openstreetmap.fr/en/</a></p></li>
<li>Create a map and import your GeoJson File.</li>
</ul>
<p>You can than edit the color, width of the borders.</p>
<p>And don't forget to add the copyright !!!</p>
<p>Mappa Mercia blog includes some detailed examples of the workflow, this is the first: <a href="http://www.mappa-mercia.org/2014/08/openstreetmap-alternatives-to-googles-maps-engine-and-fusion-tables.html">http://www.mappa-mercia.org/2014/08/openstreetmap-alternatives-to-googles-maps-engine-and-fusion-tables.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '15, 21:10</strong></p>
<img src="https://secure.gravatar.com/avatar/669afc5a0f42b94aec8450a16a53696a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DF45&#39;s gravatar image" />
<p><span>DF45</span><br />
<span class="score" title="196 reputation points">196</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DF45 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jan '15, 22:11</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-40421" class="comments-container">
&#10;</div>
<div id="comment-tools-40421" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40421-form-container" class="comment-form-container">
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

