+++
type = "question"
title = "Can the maps for a region be shown differently when accessed from different countries?"
description = '''Due to political reasons, geographic maps of different countries show up differently in different countries. For example the map of India that shows up would not be accepted in India , esp govt organizations. Google has a technique of showing this. So the Google map identifies the source country and...'''
date = "2018-08-27T09:22:00Z"
lastmod = "2018-08-27T10:47:00Z"
weight = 65574
keywords = [ "access", "country", "boundary", "different" ]
aliases = [ "/questions/65574" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can the maps for a region be shown differently when accessed from different countries?](/questions/65574/can-the-maps-for-a-region-be-shown-differently-when-accessed-from-different-countries)

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
<span id="post-65574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65574-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Due to political reasons, geographic maps of different countries show up differently in different countries. For example the map of India that shows up would not be accepted in India , esp govt organizations. Google has a technique of showing this. So the Google map identifies the source country and accordingly displays a map. Does OSM have similar capability?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-different" rel="tag" title="see questions tagged &#39;different&#39;">different</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Aug '18, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/c76b6ebf26ce4cfb5f39ab24c55e20da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steven%20zhao&#39;s gravatar image" />
<p><span>steven zhao</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steven zhao has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65574" class="comments-container">
&#10;</div>
<div id="comment-tools-65574" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65574-form-container" class="comment-form-container">
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

<span id="65575"></span>

<div id="answer-container-65575" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65575-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This requires two parts:</p>
<ul>
<li>first, OSM would have to have a way to record what needs to be shown - e.g. "government of India requires this boundary to be shown, government of China requires this other boundary to be shown". There is currently no established way in OSM to tag this.</li>
<li>second, the OSM tile server would have to detect where you come from (this is already done to some degree) and then generate a map that matches your local requirements. This is currently not possible because there is only one set of world-wide tiles that is generated for everyone.</li>
</ul>
<p>For the time being, people who want a different-looking map for political reasons (or any other reasons) have to create their own, replacing the OSM data source with something else where needed, like for example the map on <a href="https://openstreetmap.in">www.openstreetmap.in</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '18, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Aug '18, 10:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-65575" class="comments-container">
&#10;</div>
<div id="comment-tools-65575" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65575-form-container" class="comment-form-container">
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

