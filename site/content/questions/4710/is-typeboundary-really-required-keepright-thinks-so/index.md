+++
type = "question"
title = "Is type=boundary really required? (Keepright thinks so)"
description = '''Keepright wants me to add tag type=boundary to all the boundary relations I have created for city areas (admin_level=9). It says type=* is mandatory for a relation. I read somewhere that if a relation is tagged boundary=administrative, then type=boundary is implied and this was good enough for me. T...'''
date = "2011-04-21T18:30:00Z"
lastmod = "2011-04-21T22:11:00Z"
weight = 4710
keywords = [ "boundary", "type", "keepright", "relations" ]
aliases = [ "/questions/4710" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is type=boundary really required? (Keepright thinks so)](/questions/4710/is-typeboundary-really-required-keepright-thinks-so)

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
<span id="post-4710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4710-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Keepright wants me to add tag type=boundary to all the boundary relations I have created for city areas (admin_level=9). It says type=* is mandatory for a relation. I read somewhere that if a relation is tagged boundary=administrative, then type=boundary is implied and this was good enough for me.</p>
<p>The practical upshot of trying to please Keepright is that once a if a relation is tagged with type=boundary, it shows up in in the bottom left pane of Potlatch2 (where it shows which relations a way belongs to) as "boundary administrative [ref] [relation name]", with only "boundary admin" visible unless the pane is severely expanded. If a way belongs to several of these, then obviously this is not very handy.</p>
<p>If there is no type=boundary tag, then it shows up as simply "[ref] [relation name]" in the pane, which is helpful when there are multiple lines.</p>
<p>I would prefer to continue omitting type=boundary if that's okay.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-type" rel="tag" title="see questions tagged &#39;type&#39;">type</span> <span class="post-tag tag-link-keepright" rel="tag" title="see questions tagged &#39;keepright&#39;">keepright</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Apr '11, 18:30</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4710" class="comments-container">
&#10;</div>
<div id="comment-tools-4710" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4710-form-container" class="comment-form-container">
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

<span id="4711"></span>

<div id="answer-container-4711" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4711-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ponzu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I usually tag boundaries as type=multipolygon because that's what they essentially are. (OSM Inspector will display a warning if a boundary is tagged type=boundary instead of type=multipolygon, and there are IMHO valid reasons for not using type=boundary).</p>
<p>Keepright is correct though in saying that we don't usually like relations without any type=* tag. While theoretically the type could be inferred from your setting of boundary=administrative, we don't usually rely on that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '11, 18:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-4711" class="comments-container">
<span id="4719"></span>
<div id="comment-4719" class="comment">
<div id="post-4719-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oops. The wiki page on boundary relations says to tag type=multipolygon ''or'' type=boundary and gives some background on why we have both and why software has to support both. At the same time, other sources explicitly recommend using type=boundary. Yours is the first recommendation, and I know you qualified it as YHO, not to use type=boundary. I guess the important part is that a type has to be assigned, so that's what I am going to keep in mind. As far as the UI, multipolygons show up as "multipolygon [ref] [name]" in the Potlatch2 pane, which is slightly less bulky than the alternative.</p>
</div>
<div id="comment-4719-info" class="comment-info">
<span class="comment-age">(21 Apr '11, 22:11)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-4711" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4711-form-container" class="comment-form-container">
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

