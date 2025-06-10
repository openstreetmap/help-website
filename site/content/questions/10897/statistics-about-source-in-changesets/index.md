+++
type = "question"
title = "statistics about source=* in changesets"
description = '''Does anyone know if we can find anywhere some statistics on the tag source=* used on the changeset? I mean, for example:  percentage of changesets having this tag amount of primitives in the database that have at least one changeset tagged with a given source=* value  It can be usefull for measuring...'''
date = "2012-03-01T08:26:00Z"
lastmod = "2012-03-05T08:42:00Z"
weight = 10897
keywords = [ "source", "stastistics" ]
aliases = [ "/questions/10897" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [statistics about source=\* in changesets](/questions/10897/statistics-about-source-in-changesets)

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
<span id="post-10897-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10897-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-10897-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Does anyone know if we can find anywhere some statistics on the tag source=* used on the changeset? I mean, for example:</p>
<ul>
<li>percentage of changesets having this tag</li>
<li>amount of primitives in the database that have at least one changeset tagged with a given source=* value</li>
</ul>
<p>It can be usefull for measuring the use of a datasource, in a more precise way that only use <a href="http://taginfo.openstreetmap.org">taginfo</a> (that is great btw).</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span> <span class="post-tag tag-link-stastistics" rel="tag" title="see questions tagged &#39;stastistics&#39;">stastistics</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Mar '12, 08:26</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-10897" class="comments-container">
<span id="10969"></span>
<div id="comment-10969" class="comment">
<div id="post-10969-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'd be very interested in this as well. ChangesetMD might help out with this, but it still requires some database know-how: <a href="https://github.com/ToeBee/ChangesetMD">https://github.com/ToeBee/ChangesetMD</a></p>
</div>
<div id="comment-10969-info" class="comment-info">
<span class="comment-age">(05 Mar '12, 03:23)</span> <span class="comment-user userinfo">JoshD</span>
</div>
</div>
</div>
<div id="comment-tools-10897" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10897-form-container" class="comment-form-container">
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

<span id="10972"></span>

<div id="answer-container-10972" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10972-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The source tag is very seldomly used, about 0.5% of all changesets uses the source tag. But 2% of all changed/created/deleted objects have a source tag on the changeset, according to num_changes in the changeset header.</p>
<p>This is based on a <a href="https://gist.github.com/1977484">small perl script</a> (feel free to use it, it will be buggy).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '12, 08:42</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Mar '12, 09:09</strong> </span></p>
</div>
</div>
<div id="comments-container-10972" class="comments-container">
&#10;</div>
<div id="comment-tools-10972" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10972-form-container" class="comment-form-container">
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

