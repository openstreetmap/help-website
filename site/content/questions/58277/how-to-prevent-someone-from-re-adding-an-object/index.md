+++
type = "question"
title = "How to prevent someone from re-adding an object?"
description = '''Recently I deleted some buildings, that have been torn down, though the buildings are still visible on the aerial imagery. If someone sees the houses on the background map, but not in the OSM database, he will probably just re-add the building, not knowing that it doesn&#x27;t exist anymore. How can I pr...'''
date = "2017-08-13T11:42:00Z"
lastmod = "2022-10-31T08:01:00Z"
weight = 58277
keywords = [ "deleted", "satellite", "re-add", "aerial", "delete" ]
aliases = [ "/questions/58277" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to prevent someone from re-adding an object?](/questions/58277/how-to-prevent-someone-from-re-adding-an-object)

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
<span id="post-58277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58277-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Recently I deleted some buildings, that have been torn down, though the buildings are still visible on the aerial imagery. If someone sees the houses on the background map, but not in the OSM database, he will probably just re-add the building, not knowing that it doesn't exist anymore. How can I prevent someone from adding the object to OSM again? Or are there always edit wars going on, until a newer satellite imagery is available?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-deleted" rel="tag" title="see questions tagged &#39;deleted&#39;">deleted</span> <span class="post-tag tag-link-satellite" rel="tag" title="see questions tagged &#39;satellite&#39;">satellite</span> <span class="post-tag tag-link-re-add" rel="tag" title="see questions tagged &#39;re-add&#39;">re-add</span> <span class="post-tag tag-link-aerial" rel="tag" title="see questions tagged &#39;aerial&#39;">aerial</span> <span class="post-tag tag-link-delete" rel="tag" title="see questions tagged &#39;delete&#39;">delete</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Aug '17, 11:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ad3e998af874e04adfb3a569d8125995?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wanderw%C3%BCtiger&#39;s gravatar image" />
<p><span>wanderwütiger</span><br />
<span class="score" title="375 reputation points">375</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wanderwütiger has one accepted answer">16%</span></p>
</div>
</div>
<div id="comments-container-58277" class="comments-container">
&#10;</div>
<div id="comment-tools-58277" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58277-form-container" class="comment-form-container">
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

<span id="58281"></span>

<div id="answer-container-58281" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58281-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-58281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wanderwütiger has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If buildings are torn down, but still visible in current aerial imagery, it's recommended that rather than just delete them, you tag them with a <a href="https://wiki.openstreetmap.org/wiki/Lifecycle_prefix">lifecycle</a> prefix. In your case you would probably want to use "demolished:". Note that you'll end up with buildings tagged "demolished:building=yes" rather than just "building=yes". This way they will no longer be rendered, but just act as a notification to other mappers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '17, 13:30</strong></p>
<img src="https://secure.gravatar.com/avatar/6edf3a421a450237beae62ba93582637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hjart&#39;s gravatar image" />
<p><span>Hjart</span><br />
<span class="score" title="2961 reputation points"><span>3.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hjart has 14 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Aug '17, 18:08</strong> </span></p>
</div>
</div>
<div id="comments-container-58281" class="comments-container">
<span id="86028"></span>
<div id="comment-86028" class="comment">
<div id="post-86028-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Seems like Trash icon/delete button could be smarter and give user the option to a) really delete mistake vs. b) hide object with lifecycle tag (or whatever) to prevent someone from wasting time, effort re-creating from scratch. #trash #delete #UI #UX #FeatureRequest</p>
</div>
<div id="comment-86028-info" class="comment-info">
<span class="comment-age">(31 Oct '22, 08:01)</span> <span class="comment-user userinfo">DougGrinbergs</span>
</div>
</div>
</div>
<div id="comment-tools-58281" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58281-form-container" class="comment-form-container">
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

