+++
type = "question"
title = "[closed] osmosis --buffer - is this correct usage?"
description = '''Hello - I have the following osmosis command and am wondering if I am using --buffer correctly: osmosis -v &#92; --read-pbf-fast .../{var}D.osm.pbf workers=7 &#92; --buffer bufferCapacity=12000 &#92; --bounding-polygon file=&quot;.../$var.poly&quot; &#92; --buffer bufferCapacity=12000 &#92; --write-pbf .../${var}D.osm.pbf omitme...'''
date = "2015-01-19T20:52:00Z"
lastmod = "2015-01-22T17:08:00Z"
weight = 40484
keywords = [ "osmosis" ]
aliases = [ "/questions/40484" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] osmosis --buffer - is this correct usage?](/questions/40484/osmosis-buffer-is-this-correct-usage)

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
<span id="post-40484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40484-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello -</p>
<p>I have the following osmosis command and am wondering if I am using --buffer correctly:</p>
<p>osmosis -v \</p>
<pre><code>--read-pbf-fast .../{var}D.osm.pbf workers=7 \
--buffer bufferCapacity=12000 \
--bounding-polygon file=&quot;.../$var.poly&quot; \
--buffer bufferCapacity=12000 \
--write-pbf .../${var}D.osm.pbf omitmetadata=true granularity=10000</code></pre>
<p>I think I am buffering twice -</p>
<p>once from read-pbf to the bounding polygon and second from the bounding polygon to write-pbf.</p>
<p>(IMHO a few examples in osmosis detailed usage would be helpful rather than just a description)</p>
<p>Thanks, pitney</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jan '15, 20:52</strong></p>
<img src="https://secure.gravatar.com/avatar/92443a39a30b5e613ce00de446845b9e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pitney&#39;s gravatar image" />
<p><span>pitney</span><br />
<span class="score" title="44 reputation points">44</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pitney has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>22 Jan '15, 17:09</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-40484" class="comments-container">
<span id="40510"></span>
<div id="comment-40510" class="comment">
<div id="post-40510-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>if no answer here, try to ask at the osmosis-dev mailinglist:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Mailing_lists">http://wiki.openstreetmap.org/wiki/Mailing_lists</a></p>
</div>
<div id="comment-40510-info" class="comment-info">
<span class="comment-age">(21 Jan '15, 17:31)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="40535"></span>
<div id="comment-40535" class="comment">
<div id="post-40535-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks, <em>think</em> I posted there, what a horrible interface!</p>
</div>
<div id="comment-40535-info" class="comment-info">
<span class="comment-age">(22 Jan '15, 17:00)</span> <span class="comment-user userinfo">pitney</span>
</div>
</div>
<span id="40536"></span>
<div id="comment-40536" class="comment">
<div id="post-40536-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>looks like you did. The new location: <a href="https://lists.openstreetmap.org/pipermail/osmosis-dev/2015-January/001667.html">https://lists.openstreetmap.org/pipermail/osmosis-dev/2015-January/001667.html</a> (<a href="https://lists.openstreetmap.org/pipermail/osmosis-dev/2015-January/thread.html#1667">thread view</a>)</p>
</div>
<div id="comment-40536-info" class="comment-info">
<span class="comment-age">(22 Jan '15, 17:08)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40484-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "New location, closing here to avoid duplicate answers/work." by aseerel4c26 22 Jan '15, 17:09

</div>

</div>

</div>

