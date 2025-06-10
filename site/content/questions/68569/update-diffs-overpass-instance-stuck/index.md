+++
type = "question"
title = "update (diffs) overpass instance - stuck"
description = '''Hi, I have an overpass instance on a ubuntu server. I download a few geographic zones from geofabrik, and merged them in my database. The I run this 2 lines in order to keep my database updated: sudo nohup bin/fetch_osc.sh 2 http://planet.openstreetmap.org/replication/minute/ diffs/  nohup bin/apply...'''
date = "2019-04-01T08:17:00Z"
lastmod = "2019-04-01T08:17:00Z"
weight = 68569
keywords = [ "overpass", "diffs", "minutes", "updates", "stuck" ]
aliases = [ "/questions/68569" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [update (diffs) overpass instance - stuck](/questions/68569/update-diffs-overpass-instance-stuck)

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
<span id="post-68569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68569-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have an overpass instance on a ubuntu server.</p>
<p>I download a few geographic zones from geofabrik, and merged them in my database.</p>
<p>The I run this 2 lines in order to keep my database updated:</p>
<pre><code>sudo nohup bin/fetch_osc.sh 2 http://planet.openstreetmap.org/replication/minute/ diffs/
&#10;nohup bin/apply_osc_to_db.sh &quot;db/&quot; &quot;diffs/&quot; 2 --meta=yes &amp;</code></pre>
<p>later, I realized that the id=2 (the 2 in the cmd lines), is really really old, and I want to update from a newer id, so I killed both processes..</p>
<p>tried to run this 2 lines with a new id, but now I see in apply_osc_to_db.log:</p>
<pre><code>2019-04-01 07:07:12: updating from 174163
2019-04-01 07:07:17: updating from 174163
2019-04-01 07:07:22: updating from 174163
2019-04-01 07:07:27: updating from 174163
2019-04-01 07:07:32: updating from 174163
2019-04-01 07:07:37: updating from 174163
2019-04-01 07:07:42: updating from 174163
2019-04-01 07:07:47: updating from 174163
2019-04-01 07:07:52: updating from 174163
...</code></pre>
<p>I need help.</p>
<p>I tried to delete the diffs folder and start again.. but nothing</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-diffs" rel="tag" title="see questions tagged &#39;diffs&#39;">diffs</span> <span class="post-tag tag-link-minutes" rel="tag" title="see questions tagged &#39;minutes&#39;">minutes</span> <span class="post-tag tag-link-updates" rel="tag" title="see questions tagged &#39;updates&#39;">updates</span> <span class="post-tag tag-link-stuck" rel="tag" title="see questions tagged &#39;stuck&#39;">stuck</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '19, 08:17</strong></p>
<img src="https://secure.gravatar.com/avatar/db301418af6836e8e2aa894ba975cb9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BrianG13&#39;s gravatar image" />
<p><span>BrianG13</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BrianG13 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Apr '19, 08:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-68569" class="comments-container">
&#10;</div>
<div id="comment-tools-68569" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68569-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

