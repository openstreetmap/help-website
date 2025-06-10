+++
type = "question"
title = "missing names related to pedestrian/steps/service/living_s highways ?"
description = '''It seems happening 3 days now in different areas. For example the entire city of Venice has almost no more names rendered: https://www.openstreetmap.org/#map=17/45.43810/12.33042'''
date = "2014-02-24T19:22:00Z"
lastmod = "2014-02-28T15:27:00Z"
weight = 30978
keywords = [ "bug", "labels", "names", "mapnik", "missing" ]
aliases = [ "/questions/30978" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [missing names related to pedestrian/steps/service/living_s highways ?](/questions/30978/missing-names-related-to-pedestrianstepsserviceliving_s-highways)

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
<span id="post-30978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30978-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>It seems happening 3 days now in different areas. For example the entire city of Venice has almost no more names rendered: <a href="https://www.openstreetmap.org/#map=17/45.43810/12.33042">https://www.openstreetmap.org/#map=17/45.43810/12.33042</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span> <span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Feb '14, 19:22</strong></p>
<img src="https://secure.gravatar.com/avatar/68384505c1fe85ebf302402ff7bbbcb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ualios&#39;s gravatar image" />
<p><span>ualios</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ualios has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '14, 19:57</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-30978" class="comments-container">
&#10;</div>
<div id="comment-tools-30978" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30978-form-container" class="comment-form-container">
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

<span id="30980"></span>

<div id="answer-container-30980" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30980-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-30980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That is a known issue with a recent style update. It is mentioned in <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/355">355</a>. Also see <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/351">351</a>.</p>
<p>The likely "cause" (problems were expected) was this change to our rendering style: <a href="https://github.com/gravitystorm/openstreetmap-carto/commit/286d0981675b9dcf795c2ceef9524fbed73f75ac">Remove the catchall on road-text</a>. It was needed to remove name renderings where the should be none and for general cleanliness.</p>
<p>Over there is a previous <a href="http://forum.openstreetmap.org/viewtopic.php?pid=401441#p401441">bug report/discussion (in German)</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '14, 19:45</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Feb '14, 10:59</strong> </span></p>
</div>
</div>
<div id="comments-container-30980" class="comments-container">
<span id="31005"></span>
<div id="comment-31005" class="comment">
<div id="post-31005-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for response. So waiting for reistated features...?</p>
</div>
<div id="comment-31005-info" class="comment-info">
<span class="comment-age">(25 Feb '14, 11:49)</span> <span class="comment-user userinfo">ualios</span>
</div>
</div>
<span id="31006"></span>
<div id="comment-31006" class="comment">
<div id="post-31006-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span>@ualios</span>: yes, just wait. It is mentioned in the bug report ("issue"), so it will not be forgotten (hopefully). If you like you could comment there (it requires a new account registration at the company "github", not your osm.org login).</p>
</div>
<div id="comment-31006-info" class="comment-info">
<span class="comment-age">(25 Feb '14, 12:09)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="31091"></span>
<div id="comment-31091" class="comment">
<div id="post-31091-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Seems to be fixed now and already live on the tile servers (clear/refresh your browser cache).</p>
</div>
<div id="comment-31091-info" class="comment-info">
<span class="comment-age">(27 Feb '14, 15:23)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="31122"></span>
<div id="comment-31122" class="comment">
<div id="post-31122-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes that's ok... still some problem with area/square label.</p>
</div>
<div id="comment-31122-info" class="comment-info">
<span class="comment-age">(28 Feb '14, 15:27)</span> <span class="comment-user userinfo">ualios</span>
</div>
</div>
</div>
<div id="comment-tools-30980" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30980-form-container" class="comment-form-container">
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

