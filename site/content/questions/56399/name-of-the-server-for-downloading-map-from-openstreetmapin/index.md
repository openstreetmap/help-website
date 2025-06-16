+++
type = "question"
title = "Name of the Server for downloading map from openstreetmap.in"
description = '''which server should I use for downloading map from openstreetmap.in . I am using this map in COSMCtrl in VC++2010 MFC application.'''
date = "2017-06-01T08:24:00Z"
lastmod = "2017-06-01T09:30:00Z"
weight = 56399
keywords = [ "openstreetmap.in", "of", "use" ]
aliases = [ "/questions/56399" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Name of the Server for downloading map from openstreetmap.in](/questions/56399/name-of-the-server-for-downloading-map-from-openstreetmapin)

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
<span id="post-56399-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56399-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56399-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>which server should I use for downloading map from openstreetmap.in . I am using this map in COSMCtrl in VC++2010 MFC application.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap.in" rel="tag" title="see questions tagged &#39;openstreetmap.in&#39;">openstreetmap.in</span> <span class="post-tag tag-link-of" rel="tag" title="see questions tagged &#39;of&#39;">of</span> <span class="post-tag tag-link-use" rel="tag" title="see questions tagged &#39;use&#39;">use</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '17, 08:24</strong></p>
<img src="https://secure.gravatar.com/avatar/fc05c2c5fc342294a293b43c15dd299b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vaibhaw&#39;s gravatar image" />
<p><span>Vaibhaw</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vaibhaw has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56399" class="comments-container">
&#10;</div>
<div id="comment-tools-56399" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56399-form-container" class="comment-form-container">
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

<span id="56402"></span>

<div id="answer-container-56402" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56402-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd not heard of COSMCtrl before, but a <a href="https://duckduckgo.com/html?q=COSMCtrl">quick web search</a> suggests it just displays OSM map tiles.</p>
<p>Most servers don't like people bulk downloading from them, because it prevents server resources from being used by people who just want to browse 1 or 2 tiles.</p>
<p>In the case of <a href="http://openstreetmap.in">openstreetmap.in</a>, you'll need to check with them whether your tile downloading would be a problem, though the "using this map" <a href="https://github.com/osm-in/openstreetmap.in#using-this-map">link</a> suggests that your use might be acceptable.</p>
<p>Another option would be to create map tiles yourself. There are a few ways to do this - <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> describes how to set up your own server that isn't dependent on any external map data servers; and openstreetmap.in is created using <a href="http://mapbox.com">Mapbox</a> tools.</p>
<p>If you want your map to include the "claimed" rather than the "actual" boundaries of India, read <a href="https://www.openstreetmap.org/user/PlaneMad/diary/38176">this diary entry</a> by <a href="https://www.openstreetmap.org/user/PlaneMad">PlaneMad</a>, the same person behind openstreetmap.in, for some information about how to do that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '17, 09:30</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-56402" class="comments-container">
&#10;</div>
<div id="comment-tools-56402" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56402-form-container" class="comment-form-container">
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

