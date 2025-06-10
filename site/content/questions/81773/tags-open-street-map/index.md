+++
type = "question"
title = "Tags Open Street Map"
description = '''Greetings,  The tags is_in appear only in the first layer, how can I activate the tags for the secondary layer ? Picture of where the tags appear:   Picture of where the tags don&#x27;t appear:  '''
date = "2021-09-16T09:32:00Z"
lastmod = "2021-09-20T11:06:00Z"
weight = 81773
keywords = [ "umap", "layer", "openlayers", "tags" ]
aliases = [ "/questions/81773" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tags Open Street Map](/questions/81773/tags-open-street-map)

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
<span id="post-81773-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81773-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81773-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Greetings,</p>
<p>The tags is_in appear only in the first layer, how can I activate the tags for the secondary layer ?</p>
<p>Picture of where the tags appear: <img src="https://help.openstreetmap.org/upfiles/Screenshot_from_2021-09-16_11-26-27(1).png" alt="alt text" /></p>
<p>Picture of where the tags don't appear:</p>
<p><img src="https://help.openstreetmap.org/upfiles/Screenshot_from_2021-09-16_11-26-46(1).png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Sep '21, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/48668f97edcb8dfdc4eff793fb9683e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="calinj&#39;s gravatar image" />
<p><span>calinj</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="calinj has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Sep '21, 10:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</img>
</div>
</div>
<div id="comments-container-81773" class="comments-container">
<span id="81774"></span>
<div id="comment-81774" class="comment">
<div id="post-81774-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is a question on uMap I presume.</p>
<p>How do you populate your map with data? If you take the field "is_in" from the OSM database please be aware that it is not a mandatory key and may only be present on some features.</p>
</div>
<div id="comment-81774-info" class="comment-info">
<span class="comment-age">(16 Sep '21, 10:16)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="81775"></span>
<div id="comment-81775" class="comment">
<div id="post-81775-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>the map I populate with GEOJSON from <a href="https://osm-boundaries.com/">https://osm-boundaries.com/</a> -&gt; Bucharest -&gt; Sector 1, etc.</p>
<p>But if I put the polygon in the First Layer it shows the is_in tag on the polygon .</p>
</div>
<div id="comment-81775-info" class="comment-info">
<span class="comment-age">(16 Sep '21, 10:46)</span> <span class="comment-user userinfo">calinj</span>
</div>
</div>
<span id="81784"></span>
<div id="comment-81784" class="comment">
<div id="post-81784-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The second screenshot looks like imported data from OSM Boundaries. <a href="https://www.openstreetmap.org/relation/7960954">Sector 1</a> does not have any <code>is_in</code> tag in OSM.</p>
<p>The first screenshot does not appear to hold OSM Boundaries data. I don't even find an object named <em>Baneasa 4</em> in the OSM data. How did you obtain the data and how have you loaded it into uMap?</p>
</div>
<div id="comment-81784-info" class="comment-info">
<span class="comment-age">(16 Sep '21, 21:30)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-81773" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81773-form-container" class="comment-form-container">
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

<span id="81818"></span>

<div id="answer-container-81818" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81818-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The area Baneasa, was created manually, but the layer of the areas that were created manually have is_in, the imported ones from OSM only have is_in when the areas are moved to the first layer.</p>
<p>Anyway, the problem was solved through programming, adding in the properties array the is_in tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '21, 11:06</strong></p>
<img src="https://secure.gravatar.com/avatar/48668f97edcb8dfdc4eff793fb9683e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="calinj&#39;s gravatar image" />
<p><span>calinj</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="calinj has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Sep '21, 11:07</strong> </span></p>
</div>
</div>
<div id="comments-container-81818" class="comments-container">
&#10;</div>
<div id="comment-tools-81818" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81818-form-container" class="comment-form-container">
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

