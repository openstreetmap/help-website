+++
type = "question"
title = "osm2pgsql - expired tiles with tag name change"
description = '''While inserting the *.osc file with osm2pgsql, I am using --expire-tiles option to output the expired tiles with --append mode.  What I have observed if only tag name is changed or added then that tile is not in the expired tile list. Is it the correct observation or am I doing something wrong? Here...'''
date = "2016-08-16T08:04:00Z"
lastmod = "2016-08-18T08:35:00Z"
weight = 51430
keywords = [ "osm2pgsql", "expiry" ]
aliases = [ "/questions/51430" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql - expired tiles with tag name change](/questions/51430/osm2pgsql-expired-tiles-with-tag-name-change)

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
<span id="post-51430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51430-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>While inserting the *.osc file with osm2pgsql, I am using --expire-tiles option to output the expired tiles with --append mode. What I have observed if only tag name is changed or added then that tile is not in the expired tile list. Is it the correct observation or am I doing something wrong? Here is the command that I am using:</p>
<pre><code>osm2pgsql --append --slim --cache 3000 --number-processes 3 --hstore --style ~/openstreetmap-carto/openstreetmap-carto.style update-within-india.osc --expire-tiles 8-17 --expire-output today_update_tiles.txt</code></pre>
<p>How to overcome this issue, I want all the tiles where labels have changed or added.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-expiry" rel="tag" title="see questions tagged &#39;expiry&#39;">expiry</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '16, 08:04</strong></p>
<img src="https://secure.gravatar.com/avatar/39d75f04e1a21ba653b41ac75ec1b026?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gagan&#39;s gravatar image" />
<p><span>Gagan</span><br />
<span class="score" title="305 reputation points">305</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gagan has 2 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Aug '16, 15:25</strong> </span></p>
</div>
</div>
<div id="comments-container-51430" class="comments-container">
<span id="51436"></span>
<div id="comment-51436" class="comment">
<div id="post-51436-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you supply us with the complete command line you are using?</p>
</div>
<div id="comment-51436-info" class="comment-info">
<span class="comment-age">(16 Aug '16, 10:43)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="51437"></span>
<div id="comment-51437" class="comment">
<div id="post-51437-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No idea if it's related, but I did have to make a minor change to openstreetmap-tiles-update-expire to get tile expiry to work properly for me. See <a href="https://github.com/SomeoneElseOSM/mod_tile/commit/0e74c67a75f042faf99ac81a14f4a665f467f3d5#diff-c4481b5ad3192fd03c13bffec4a8c368">https://github.com/SomeoneElseOSM/mod_tile/commit/0e74c67a75f042faf99ac81a14f4a665f467f3d5#diff-c4481b5ad3192fd03c13bffec4a8c368</a> and search for "Previously openstreetmap-tiles-update-expire tried to dirty". Other changes in that commit (make it cronable, use Zverik's trim_osc.py) shouldn't be relevant.</p>
</div>
<div id="comment-51437-info" class="comment-info">
<span class="comment-age">(16 Aug '16, 10:49)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="51447"></span>
<div id="comment-51447" class="comment">
<div id="post-51447-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I added the full command, I am not using the mod_tiles.</p>
</div>
<div id="comment-51447-info" class="comment-info">
<span class="comment-age">(16 Aug '16, 15:28)</span> <span class="comment-user userinfo">Gagan</span>
</div>
</div>
<span id="51512"></span>
<div id="comment-51512" class="comment">
<div id="post-51512-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Is there any other tool to find out the expired tiles with respect to *.osc file?</p>
</div>
<div id="comment-51512-info" class="comment-info">
<span class="comment-age">(18 Aug '16, 08:35)</span> <span class="comment-user userinfo">Gagan</span>
</div>
</div>
</div>
<div id="comment-tools-51430" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51430-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

