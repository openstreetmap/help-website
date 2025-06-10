+++
type = "question"
title = "osmfilter all speed cameras with related way"
description = '''I&#x27;m successfully managed to filter all nodes of a specific type by using osmfilter: osmfilter austria.o5m --keep=&quot;highway=speed_camera&quot;  Now I have got a lot of nodes like this: &amp;lt;node id=&quot;3906966442&quot; lat=&quot;48.2975844&quot; lon=&quot;14.2988663&quot; version=&quot;1&quot; timestamp=&quot;2015-12-23T18:18:11Z&quot; changeset=&quot;3613158...'''
date = "2016-04-25T09:07:00Z"
lastmod = "2016-04-26T16:48:00Z"
weight = 49400
keywords = [ "overpass", "osmfilter" ]
aliases = [ "/questions/49400" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [osmfilter all speed cameras with related way](/questions/49400/osmfilter-all-speed-cameras-with-related-way)

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
<span id="post-49400-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49400-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49400-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm successfully managed to filter all nodes of a specific type by using osmfilter:</p>
<pre><code>osmfilter austria.o5m --keep=&quot;highway=speed_camera&quot;</code></pre>
<p>Now I have got a lot of nodes like this:</p>
<pre><code>&lt;node id=&quot;3906966442&quot; lat=&quot;48.2975844&quot; lon=&quot;14.2988663&quot; version=&quot;1&quot; timestamp=&quot;2015-12-23T18:18:11Z&quot; changeset=&quot;36131585&quot; uid=&quot;180830&quot; user=&quot;flaimo&quot;&gt;
    &lt;tag k=&quot;highway&quot; v=&quot;speed_camera&quot;/&gt;
    &lt;tag k=&quot;maxspeed&quot; v=&quot;50&quot;/&gt;
&lt;/node&gt;</code></pre>
<p>However in addition to the <code>maxspeed</code> value I'd also be interested in the name of the street where this node is attached too. Is there any way (except manual reverse lookup for every node) to fetch all the related street names? Using alternative tools or APIs (like Overpass) would be fine too.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '16, 09:07</strong></p>
<img src="https://secure.gravatar.com/avatar/e3a6d6b45fdb0f5d8e79e0db82a75804?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hohl&#39;s gravatar image" />
<p><span>hohl</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hohl has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49400" class="comments-container">
<span id="49439"></span>
<div id="comment-49439" class="comment">
<div id="post-49439-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>CROSSPOSTING</p>
<p>from <a href="http://gis.stackexchange.com/questions/190153/osmfilter-filter-for-nodes-and-find-the-related-nearest-street-to-every-node">http://gis.stackexchange.com/questions/190153/osmfilter-filter-for-nodes-and-find-the-related-nearest-street-to-every-node</a></p>
</div>
<div id="comment-49439-info" class="comment-info">
<span class="comment-age">(26 Apr '16, 16:48)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-49400" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49400-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

