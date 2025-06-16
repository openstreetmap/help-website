+++
type = "question"
title = "Is it possible to add the history of the shop owners and usages?"
description = '''Question exactly as in title.'''
date = "2013-04-12T17:14:00Z"
lastmod = "2013-04-12T17:51:00Z"
weight = 21478
keywords = [ "shop", "usage", "history" ]
aliases = [ "/questions/21478" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to add the history of the shop owners and usages?](/questions/21478/is-it-possible-to-add-the-history-of-the-shop-owners-and-usages)

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
<span id="post-21478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21478-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Question exactly as in title.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shop" rel="tag" title="see questions tagged &#39;shop&#39;">shop</span> <span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '13, 17:14</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '13, 17:15</strong> </span></p>
</div>
</div>
<div id="comments-container-21478" class="comments-container">
<span id="21479"></span>
<div id="comment-21479" class="comment">
<div id="post-21479-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This question was asked by a new contributor <a href="https://www.openstreetmap.org/user/andrewj74">andrewj74</a> as a comment in changeset <a href="https://www.openstreetmap.org/browse/changeset/15693142">15693142</a>. As this seemed interesting and pertinent I thought I'd add it to OSM Help.</p>
</div>
<div id="comment-21479-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 17:15)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-21478" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21478-form-container" class="comment-form-container">
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

<span id="21485"></span>

<div id="answer-container-21485" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21485-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-21485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Although OSM was not designed for mapping history of objects there is considerable interest in doing so for a number of reasons:</p>
<ul>
<li><strong>Intrinsic interest.</strong> It is difficult to spend time surveying an area without wondering about quirks of it's geography which often have historical explanations.</li>
<li><strong>Defensive mapping.</strong> POIs which have recently changed may be prone to being reverted if other editors are not aware of the change. Keeping the old values associated with the POI therefore provides an additional means of showing that something genuinely has changed.</li>
<li><strong>Conflation with other sources.</strong> Many other sources of (open) data are not updated as frequently or rapidly as OSM. Being able to access recently used names or usages of POIs makes it much easier to make combined use of these disparate data sources.</li>
</ul>
<p>This being said there is no firm consensus about how to tag this kind of information. For the immediate prior usage the most usual method is to prepend <code>old_</code> to the relevant tags, such as <code>old_amenity</code> (161), <code>old_shop</code> (58), <code>old_name</code> (65 077), the numbers in brackets indicate number of times the tag has been used from <a href="http://taginfo.openstreetmap.org/search?q=old">taginfo</a>. Much less widely used is <code>old:</code> as a namespace for the original tag, as in <code>old:amenity</code> or prepending <code>dead_</code> to the value of key as in <code>['dead_pub'][2]</code>. A very useful tag to associate with the change of use is <code>[start_date][3]</code>, but this may need to be name-spaced to disambiguate between, say, a building, and its current use.</p>
<p>All of these work for one previous usage. I am not aware of anyone trying to tag multiple previous usages, but one can envisage a range of approaches, such as:</p>
<ul>
<li>Just adding a numerical suffix to the <code>old_xxx</code> tags. So <code>old_shop</code> would be previous usage, <code>old_shop2</code> the one before etc. This is a simple but maintenance gets complicated if usages are added out of sequence. Ideally this would be combined with start_date:old_shop and end_date:old_shop which would reduce this problem (although from personal experience it's extremely hard to find accurate values for these dates).</li>
<li>Using the suffix after old, so that shop=general, with old_shop=convenience and old2_amenity=pub would better represent a broader range of multiple uses. Again date range tags make it easier to interpret the data.</li>
<li>Date range namespaces to the key value, such as amenity:18970304:20121212=pub (roughly appropriate for the <a href="https://www.openstreetmap.org/browse/node/264961019">Golden Harp</a>). This is more complicated, requires that we know the date ranges and is much less obvious for people editing and inspecting the data.</li>
</ul>
<p>All these options really <strong>apply only</strong> to POIs with no changes in geography over time, but are widely applicable to shops, bars, pubs, restaurants etc.</p>
<p>There are a number of people interested in problems such as this one with a mailing list at <a href="https://wiki.openstreetmap.org/wiki/Historical_OSM">Historical OSM</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '13, 17:51</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-21485" class="comments-container">
&#10;</div>
<div id="comment-tools-21485" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21485-form-container" class="comment-form-container">
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

