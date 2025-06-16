+++
type = "question"
title = "Why does only one of the &quot;Antelope Buttes&quot; show up in Nominatim?"
description = '''There are two peaks (one, two) called Antelope Buttes near each other, and added in the same changeset. Why does only one show up in Nominatim? It seems like a possible bug.'''
date = "2014-11-27T18:23:00Z"
lastmod = "2014-11-30T00:39:00Z"
weight = 38886
keywords = [ "mountain", "nominatim" ]
aliases = [ "/questions/38886" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why does only one of the "Antelope Buttes" show up in Nominatim?](/questions/38886/why-does-only-one-of-the-antelope-buttes-show-up-in-nominatim)

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
<span id="post-38886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38886-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-38886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There are two peaks (<a href="https://www.openstreetmap.org/node/358804247">one</a>, <a href="https://www.openstreetmap.org/node/358807763">two</a>) called Antelope Buttes near each other, and added in the same changeset.</p>
<p>Why does only one show up <a href="https://www.openstreetmap.org/search?query=Antelope%20Buttes">in Nominatim</a>? It seems like a possible bug.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mountain" rel="tag" title="see questions tagged &#39;mountain&#39;">mountain</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Nov '14, 18:23</strong></p>
<img src="https://secure.gravatar.com/avatar/e72946d7c81ee170b322f6e6abae3442?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mattflaschen&#39;s gravatar image" />
<p><span>mattflaschen</span><br />
<span class="score" title="226 reputation points">226</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mattflaschen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38886" class="comments-container">
<span id="38895"></span>
<div id="comment-38895" class="comment">
<div id="post-38895-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are these two peaks really named exactly equally in reality?</p>
</div>
<div id="comment-38895-info" class="comment-info">
<span class="comment-age">(28 Nov '14, 13:09)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="38947"></span>
<div id="comment-38947" class="comment">
<div id="post-38947-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a> I don't know (I didn't add them).</p>
</div>
<div id="comment-38947-info" class="comment-info">
<span class="comment-age">(30 Nov '14, 00:36)</span> <span class="comment-user userinfo">mattflaschen</span>
</div>
</div>
</div>
<div id="comment-tools-38886" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38886-form-container" class="comment-form-container">
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

<span id="38890"></span>

<div id="answer-container-38890" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38890-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think that this is caused by "During the indexing process an address is also calculated using the first feature found for each level. Where an is_in value is provided it is used to filter the address." This text is taken from the <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Development_overview">Nominatim Development page</a>.</p>
<p>Since a peak is considered a place (see <a href="http://nominatim.openstreetmap.org/details.php?place_id=3281978),">http://nominatim.openstreetmap.org/details.php?place_id=3281978),</a> it only takes the first feature with that name.</p>
<p>Disclaimer: I'm not a Nominatim developer, so I just made this conclusion from reading the documentation</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '14, 10:38</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-38890" class="comments-container">
<span id="38948"></span>
<div id="comment-38948" class="comment">
<div id="post-38948-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think this means the first feature of each level found in the hierarchy (see the part with "using the following algorithm" at that page for how this hierarchy is calculated), rather than the first of the changeset, but I'm not sure.</p>
</div>
<div id="comment-38948-info" class="comment-info">
<span class="comment-age">(30 Nov '14, 00:39)</span> <span class="comment-user userinfo">mattflaschen</span>
</div>
</div>
</div>
<div id="comment-tools-38890" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38890-form-container" class="comment-form-container">
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

