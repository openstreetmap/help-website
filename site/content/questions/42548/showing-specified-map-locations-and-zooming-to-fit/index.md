+++
type = "question"
title = "Showing specified map locations and zooming to fit"
description = '''I need to quickly determine if OpenStreetMap will allow me to show a map with locations marked (e.g. pin drops) based on a list of supplied addresses and then zoom the map so all marked locations are visible. Are there any examples that show how to do this?'''
date = "2015-04-22T00:05:00Z"
lastmod = "2015-04-22T17:15:00Z"
weight = 42548
keywords = [ "marker", "geocoding", "zoom" ]
aliases = [ "/questions/42548" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Showing specified map locations and zooming to fit](/questions/42548/showing-specified-map-locations-and-zooming-to-fit)

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
<span id="post-42548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42548-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to quickly determine if OpenStreetMap will allow me to show a map with locations marked (e.g. pin drops) based on a list of supplied addresses and then zoom the map so all marked locations are visible.</p>
<p>Are there any examples that show how to do this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '15, 00:05</strong></p>
<img src="https://secure.gravatar.com/avatar/5197b67c68e02821c0b3ae09a15bbe55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DesertFoxAZ&#39;s gravatar image" />
<p><span>DesertFoxAZ</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DesertFoxAZ has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Apr '15, 00:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42548" class="comments-container">
&#10;</div>
<div id="comment-tools-42548" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42548-form-container" class="comment-form-container">
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

<span id="42549"></span>

<div id="answer-container-42549" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42549-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-42549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>are you speaking of a <span>web map</span>? Sure, that is possible (with some JS coding by you), <a href="https://wiki.openstreetmap.org/wiki/Nominatim">geocode</a> the addresses and then display the resulting coordinates as markers with your <a href="https://wiki.openstreetmap.org/wiki/Deploying_your_own_Slippy_Map">map display software</a>. Telling the map display software to display a specific area should be possible too.</p>
<p>You can find examples e.g. here: <a href="http://leafletjs.com/examples.html">http://leafletjs.com/examples.html</a> . Also see <a href="/questions/1778/">how-can-i-display-a-map-with-multiple-markers</a>. Maybe somebody else knows glued-together working examples …</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '15, 00:49</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Apr '15, 00:55</strong> </span></p>
</div>
</div>
<div id="comments-container-42549" class="comments-container">
<span id="42552"></span>
<div id="comment-42552" class="comment">
<div id="post-42552-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, I'll research it. I need to have a solution by Friday.</p>
</div>
<div id="comment-42552-info" class="comment-info">
<span class="comment-age">(22 Apr '15, 17:15)</span> <span class="comment-user userinfo">DesertFoxAZ</span>
</div>
</div>
</div>
<div id="comment-tools-42549" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42549-form-container" class="comment-form-container">
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

