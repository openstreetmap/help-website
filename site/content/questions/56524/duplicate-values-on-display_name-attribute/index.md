+++
type = "question"
title = "Duplicate values on display_name attribute."
description = '''Hi. I&#x27;m trying to apply with osmosis the day diff #1726 to my osm apidb, but I got this error: &#x27;duplicate key value violates unique constraint &quot;users_display_name_idx&quot;&#x27;.  This happens because, apparently, two users (whose ids are 6115593 and 4518891) have the same display_name (&quot;Андрей Б&quot;), but this...'''
date = "2017-06-08T11:15:00Z"
lastmod = "2017-06-11T22:19:00Z"
weight = 56524
keywords = [ "violation", "duplicate", "apidb", "display_name", "constraint" ]
aliases = [ "/questions/56524" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Duplicate values on display_name attribute.](/questions/56524/duplicate-values-on-display_name-attribute)

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
<span id="post-56524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56524-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. I'm trying to apply with osmosis the day diff <a href="http://planet.openstreetmap.org/replication/day/000/001/726.osc.gz">#1726</a> to my osm apidb, but I got this error: 'duplicate key value violates unique constraint "users_display_name_idx"'. This happens because, apparently, two users (whose ids are <a href="https://www.openstreetmap.org/api/0.6/user/6115593">6115593</a> and <a href="https://www.openstreetmap.org/api/0.6/user/4518891">4518891</a>) have the same display_name ("Андрей Б"), but this should not be possible, according to the current osm apidb <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/db/structure.sql">schema</a>. How could this happen on OSM? What should I do in order to address this issue?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-violation" rel="tag" title="see questions tagged &#39;violation&#39;">violation</span> <span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-apidb" rel="tag" title="see questions tagged &#39;apidb&#39;">apidb</span> <span class="post-tag tag-link-display_name" rel="tag" title="see questions tagged &#39;display_name&#39;">display_name</span> <span class="post-tag tag-link-constraint" rel="tag" title="see questions tagged &#39;constraint&#39;">constraint</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '17, 11:15</strong></p>
<img src="https://secure.gravatar.com/avatar/63b4bcbffe5b058a2b6384af2e613f61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ardean80&#39;s gravatar image" />
<p><span>ardean80</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ardean80 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jun '17, 13:25</strong> </span></p>
</div>
</div>
<div id="comments-container-56524" class="comments-container">
<span id="56583"></span>
<div id="comment-56583" class="comment">
<div id="post-56583-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The display_names are not identical: 6115593 is <code>"Андрей Б"</code> and 4518891 is <code>"Андрей Б "</code>. The latter has a trailing space.</p>
</div>
<div id="comment-56583-info" class="comment-info">
<span class="comment-age">(11 Jun '17, 20:12)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
<span id="56585"></span>
<div id="comment-56585" class="comment">
<div id="post-56585-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No, they were identical. The older one has been changed with a trailing space, as a fix, after I opened the same issue on github ( <a href="https://github.com/openstreetmap/openstreetmap-website/issues/1560">https://github.com/openstreetmap/openstreetmap-website/issues/1560</a> ).</p>
</div>
<div id="comment-56585-info" class="comment-info">
<span class="comment-age">(11 Jun '17, 22:19)</span> <span class="comment-user userinfo">ardean80</span>
</div>
</div>
</div>
<div id="comment-tools-56524" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56524-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

