+++
type = "question"
title = "Problem importing data from external source and possibly need for revert of changesets."
description = '''Hello, I tried to make some modification to some forest in france (Changeset: 124566485, Changeset: 124566904, #Changeset: 124571114). The goal was to add some data from a json I got from the ONF, french national forest organization but I messed things up I think. I think I overwrote the changes of ...'''
date = "2022-08-06T18:26:00Z"
lastmod = "2022-08-07T08:49:00Z"
weight = 85280
keywords = [ "import", "forest", "france" ]
aliases = [ "/questions/85280" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Problem importing data from external source and possibly need for revert of changesets.](/questions/85280/problem-importing-data-from-external-source-and-possibly-need-for-revert-of-changesets)

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
<span id="post-85280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85280-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I tried to make some modification to some forest in france (Changeset: 124566485, Changeset: 124566904, #Changeset: 124571114). The goal was to add some data from a json I got from the ONF, french national forest organization but I messed things up I think. I think I overwrote the changes of some previous contributor which is a problem because I think the new changes don't fit osm formatting. What is the best way to do the merge ? Should I try to revert my changesets and do everything by hand ? Is there a canonical way to import data from external (geojson) source that I did not see (for now I tried using geojson plugin for josm).</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-forest" rel="tag" title="see questions tagged &#39;forest&#39;">forest</span> <span class="post-tag tag-link-france" rel="tag" title="see questions tagged &#39;france&#39;">france</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Aug '22, 18:26</strong></p>
<img src="https://secure.gravatar.com/avatar/0302449a11ab3bf751c067cc20ec7a87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TMat42&#39;s gravatar image" />
<p><span>TMat42</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TMat42 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85280" class="comments-container">
&#10;</div>
<div id="comment-tools-85280" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85280-form-container" class="comment-form-container">
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

<span id="85281"></span>

<div id="answer-container-85281" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85281-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-85281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TMat42 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, It does look like quite a mess around that area with a lot of strangely tagged areas. I would say revert everything and start again. Do you want me to revert for you?</p>
<p>Please be aware that there are guidelines for importing data into OSM, please see here:- <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">https://wiki.openstreetmap.org/wiki/Import/Guidelines</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '22, 07:21</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-85281" class="comments-container">
<span id="85282"></span>
<div id="comment-85282" class="comment">
<div id="post-85282-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes if you could revert for me it would be great. I am still learning how to use josm.</p>
<p>Thanks.</p>
</div>
<div id="comment-85282-info" class="comment-info">
<span class="comment-age">(07 Aug '22, 08:17)</span> <span class="comment-user userinfo">TMat42</span>
</div>
</div>
<span id="85283"></span>
<div id="comment-85283" class="comment">
<div id="post-85283-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I reviewed the import guideline and I will send email to the mailing list talk-fr. I did not think I had to do it because the wiki says that the source is OK and the job was already half done (half the forest was already imported).</p>
</div>
<div id="comment-85283-info" class="comment-info">
<span class="comment-age">(07 Aug '22, 08:26)</span> <span class="comment-user userinfo">TMat42</span>
</div>
</div>
<span id="85284"></span>
<div id="comment-85284" class="comment">
<div id="post-85284-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>OK, all three changesets are now reverted. The database is now back to its prior state. Stick with JOSM, there's a lot to learn but it's worth it. Importing, all I know is there's often a lot of debate about how it's done.</p>
</div>
<div id="comment-85284-info" class="comment-info">
<span class="comment-age">(07 Aug '22, 08:49)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
</div>
<div id="comment-tools-85281" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85281-form-container" class="comment-form-container">
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

