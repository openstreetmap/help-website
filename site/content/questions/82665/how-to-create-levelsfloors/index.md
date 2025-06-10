+++
type = "question"
title = "How to create levels/floors ?"
description = '''I am a newbie to java openstreetmap. How can i create different levels of an indoor building? For ex. by adding new layers or something else? I&#x27;ve tried indoorHelper, and i guess i handled the creating different levels but don&#x27;t know how to access these different levels. I see some indoor mapping ap...'''
date = "2021-11-23T20:10:00Z"
lastmod = "2021-11-25T10:16:00Z"
weight = 82665
keywords = [ "indoor", "leaflet", "levels", "mapsforge", "level" ]
aliases = [ "/questions/82665" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to create levels/floors ?](/questions/82665/how-to-create-levelsfloors)

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
<span id="post-82665-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82665-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82665-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am a newbie to java openstreetmap. How can i create different levels of an indoor building? For ex. by adding new layers or something else? I've tried indoorHelper, and i guess i handled the creating different levels but don't know how to access these different levels. I see some indoor mapping apps, there are buttons for switching levels like -1,0,1, how buttons know these levels and switch between them. Are there any functions like getLevel()?</p>
<p>To sum up what is your way to create levels and access them ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span> <span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-levels" rel="tag" title="see questions tagged &#39;levels&#39;">levels</span> <span class="post-tag tag-link-mapsforge" rel="tag" title="see questions tagged &#39;mapsforge&#39;">mapsforge</span> <span class="post-tag tag-link-level" rel="tag" title="see questions tagged &#39;level&#39;">level</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Nov '21, 20:10</strong></p>
<img src="https://secure.gravatar.com/avatar/7f1c260e99dffff55f895757e570cf43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baranacikgoz&#39;s gravatar image" />
<p><span>baranacikgoz</span><br />
<span class="score" title="76 reputation points">76</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baranacikgoz has 2 accepted answers">100%</span></p>
</div>
</div>
<div id="comments-container-82665" class="comments-container">
<span id="82683"></span>
<div id="comment-82683" class="comment">
<div id="post-82683-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've left an answer at the corresponding StackOverflow question: <a href="https://stackoverflow.com/a/70109278/1391631">https://stackoverflow.com/a/70109278/1391631</a></p>
</div>
<div id="comment-82683-info" class="comment-info">
<span class="comment-age">(25 Nov '21, 10:16)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-82665" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82665-form-container" class="comment-form-container">
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

<span id="82668"></span>

<div id="answer-container-82668" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82668-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-82668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap is a database of geospatial information. Levels/floors are modeled with attributes of geometry primitives in the data (the level tag to be concrete). How attributes are made available to applications depends completely on what framework you are using so can't be answered without further context.</p>
<p>But very roughly you can determine from attributes on the building outline the min and max level and then simply only display objects with the correct level tag, for more information see</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging">https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Nov '21, 09:07</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Nov '21, 09:08</strong> </span></p>
</div>
</div>
<div id="comments-container-82668" class="comments-container">
<span id="82671"></span>
<div id="comment-82671" class="comment">
<div id="post-82671-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a> thans for answer. Assume that i am using mapsforge or leaflet as frameworks, any advice ?</p>
</div>
<div id="comment-82671-info" class="comment-info">
<span class="comment-age">(24 Nov '21, 10:00)</span> <span class="comment-user userinfo">baranacikgoz</span>
</div>
</div>
<span id="82672"></span>
<div id="comment-82672" class="comment">
<div id="post-82672-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No advice really, in the case of leaflet you will need to use an API like Overpass or use a database to retrieve the level relevant data. This is what I believe for example <a href="https://openlevelup.net/?l=0#20/47.45100/8.55930">https://openlevelup.net/?l=0#20/47.45100/8.55930</a> does.</p>
</div>
<div id="comment-82672-info" class="comment-info">
<span class="comment-age">(24 Nov '21, 10:17)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82668" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82668-form-container" class="comment-form-container">
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

