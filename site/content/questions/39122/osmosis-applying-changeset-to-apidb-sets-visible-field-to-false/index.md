+++
type = "question"
title = "Osmosis applying changeset to apiDB sets visible field to false"
description = '''I am following the blog post here to maintain an up to date region of OSM data. I had trouble filtering my API db in Postgres by a bounding polygon after applying changesets. I eventually discovered that this was because the visible field of all entities I imported with: osmosis --rri --simc --wdc h...'''
date = "2014-12-07T19:54:00Z"
lastmod = "2014-12-07T19:54:00Z"
weight = 39122
keywords = [ "visible", "apidb", "osmosis" ]
aliases = [ "/questions/39122" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis applying changeset to apiDB sets visible field to false](/questions/39122/osmosis-applying-changeset-to-apidb-sets-visible-field-to-false)

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
<span id="post-39122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39122-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am following the blog post <a href="http://openparceldata.wordpress.com/2013/02/26/up-to-date-region-of-openstreetmap-data/">here</a> to maintain an up to date region of OSM data. I had trouble filtering my API db in Postgres by a bounding polygon after applying changesets. I eventually discovered that this was because the visible field of all entities I imported with:</p>
<p><code>osmosis --rri --simc --wdc host=localhost database=test user=xx password=yy validateSchemaVersion=no</code></p>
<p>was set to <strong>false</strong>. If I manually set the visible field to true I can filter out the new points successfully, otherwise the new points are not filtered out with a bounding polygon query.</p>
<p>Is there a reason that osmosis sets visible to false or that visible=f nodes are not included in polygon queries? I had a look through the source code and did some searches but couldn't see anything obvious there.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-visible" rel="tag" title="see questions tagged &#39;visible&#39;">visible</span> <span class="post-tag tag-link-apidb" rel="tag" title="see questions tagged &#39;apidb&#39;">apidb</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Dec '14, 19:54</strong></p>
<img src="https://secure.gravatar.com/avatar/201c52faa380da64ae76e493d12c0f1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stev&#39;s gravatar image" />
<p><span>stev</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stev has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jan '15, 14:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-39122" class="comments-container">
&#10;</div>
<div id="comment-tools-39122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39122-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

