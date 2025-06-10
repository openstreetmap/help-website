+++
type = "question"
title = "Show building names only for specific group"
description = '''I try to customize my own carto style. I try to reduce building names in my city only to the most important ones. I&#x27;ve found in style/addressing.mss part:  #building-text {  [zoom &amp;gt;= 14][way_pixels &amp;gt; 3000],  [zoom &amp;gt;= 17] {  text-name: &quot;[name]&quot;;  text-face-name: @book-fonts;  text-fill: #444...'''
date = "2021-03-24T12:48:00Z"
lastmod = "2021-03-24T13:10:00Z"
weight = 79370
keywords = [ "style", "carto", "mapnik" ]
aliases = [ "/questions/79370" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Show building names only for specific group](/questions/79370/show-building-names-only-for-specific-group)

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
<span id="post-79370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79370-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I try to customize my own <code>carto</code> style. I try to reduce building names in my city only to the most important ones. I've found in <code>style/addressing.mss</code> part:</p>
<pre><code>    #building-text {</code></pre>
<p>[zoom &gt;= 14][way_pixels &gt; 3000],<br />
[zoom &gt;= 17] {<br />
text-name: "[name]";<br />
text-face-name: <a href="https://help.openstreetmap.org/users/6424/booklounge">@book</a>-fonts;<br />
text-fill: #444;<br />
text-halo-radius: @standard-halo-radius;<br />
text-halo-fill: @standard-halo-fill;<br />
text-size: 11;<br />
text-wrap-width: 22; // 2.0 em<br />
text-line-spacing: -1.65; // -0.15 em<br />
}<br />
}<br />
(I cannot format that properly)</p>
<p>And by manipulating that values I can see that building names change and it's fine. What I'm wondering can I use that styling only to some groups/tags? In example to use that style only for <code>building: train_station</code> and not use in example for <code>building: commercial</code>. Or Can I use that attribute for <code>building: train_station</code> or <code>building: yes</code> (I don't have another examples, just wondering if the OR is possible).</p>
<p>I tried to find this in <code>carto documentation</code> pdf, but I couldn't find anything which at least aimed me to the solution.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-carto" rel="tag" title="see questions tagged &#39;carto&#39;">carto</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '21, 12:48</strong></p>
<img src="https://secure.gravatar.com/avatar/735ed8c1abf1a1f7b907b78d9594303c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="engopy&#39;s gravatar image" />
<p><span>engopy</span><br />
<span class="score" title="126 reputation points">126</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="engopy has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-79370" class="comments-container">
<span id="79371"></span>
<div id="comment-79371" class="comment">
<div id="post-79371-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tested to add [building = 'train_station'] inside curly braces, but from Kosmtik I received some SQL exception with some SELECT query. Looked at that query I figured out that maybe <code>building</code> attribute is not selecting from DB, so I tried to use <code>name</code> like: <code>[name = 'Dworzec PKP Gliwice']</code> and indeed only that building is labeled. But I'm looking for some more general solution, not selecting them by <code>name</code> which is very specific for concrete building.</p>
</div>
<div id="comment-79371-info" class="comment-info">
<span class="comment-age">(24 Mar '21, 13:10)</span> <span class="comment-user userinfo">engopy</span>
</div>
</div>
</div>
<div id="comment-tools-79370" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79370-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

