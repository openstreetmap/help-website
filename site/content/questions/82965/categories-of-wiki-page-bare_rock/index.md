+++
type = "question"
title = "categories of wiki page bare_rock"
description = '''Hi, in the wiki, on the page bare_rock in deutsch, english, français and polski, at the bottom of the page, we have in red &quot;Mismatched osmcarto-rendering&quot; (red because the page doesn&#x27;t exist). In other languages (italiano for example), there isn&#x27;t this link. I wanted to delete it but I can&#x27;t, if I s...'''
date = "2022-01-06T00:40:00Z"
lastmod = "2022-01-06T16:17:00Z"
weight = 82965
keywords = [ "wiki", "bare_rock" ]
aliases = [ "/questions/82965" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [categories of wiki page bare_rock](/questions/82965/categories-of-wiki-page-bare_rock)

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
<span id="post-82965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82965-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>in the wiki, on the page bare_rock in <a href="https://wiki.openstreetmap.org/wiki/DE:Tag:natural%3Dbare_rock">deutsch</a>, <a href="https://wiki.openstreetmap.org/wiki/Tag:natural%3Dbare_rock">english</a>, <a href="https://wiki.openstreetmap.org/wiki/FR:Tag:natural%3Dbare_rock">français</a> and <a href="https://wiki.openstreetmap.org/wiki/Pl:Tag:natural%3Dbare_rock">polski</a>, at the bottom of the page, we have in red "Mismatched osmcarto-rendering" (red because the page doesn't exist). In other languages (<a href="https://wiki.openstreetmap.org/wiki/IT:Tag:natural%3Dbare_rock">italiano</a> for example), there isn't this link.</p>
<p>I wanted to delete it but I can't, if I select "modify" or "modify the wikicode", I don't find the link. Do you know how I can improve these 4 pages ?</p>
<p>Other problem of this "Categories", for the french translation, the link next to this bad link is "FR:Natural". It is not in french, the good link should be "FR:Naturel" (it is what we have on the page <a href="https://wiki.openstreetmap.org/wiki/FR:Tag:wetland%3Dmarsh">marsh</a> for example).</p>
<p>Same thing that above, I don't find where I could fix that.</p>
<p>Best regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wiki" rel="tag" title="see questions tagged &#39;wiki&#39;">wiki</span> <span class="post-tag tag-link-bare_rock" rel="tag" title="see questions tagged &#39;bare_rock&#39;">bare_rock</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jan '22, 00:40</strong></p>
<img src="https://secure.gravatar.com/avatar/33b586336c1978cc33b67e8b3cff9cb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fred73000&#39;s gravatar image" />
<p><span>Fred73000</span><br />
<span class="score" title="54 reputation points">54</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fred73000 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82965" class="comments-container">
&#10;</div>
<div id="comment-tools-82965" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82965-form-container" class="comment-form-container">
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

<span id="82975"></span>

<div id="answer-container-82975" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82975-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I solved both problems :</p>
<p>1) in the ValueDescription, for the rendering, we need to use</p>
<ul>
<li>osmcarto-rendering-area</li>
<li>osmcarto-rendering-area-size</li>
</ul>
<p>instead of</p>
<ul>
<li>osmcarto-rendering</li>
<li>osmcarto-rendering-size</li>
</ul>
<p>but <strong>only</strong> if we need something :</p>
<ul>
<li>for the <a href="https://wiki.openstreetmap.org/wiki/Tag:wetland%3Dmarsh">marsh</a> it is necessary to have these 2 lignes,</li>
<li>for the bare_rock, we don't need these 2 lines otherwise the rendering appears twice</li>
</ul>
<p>(I don't know why these differences).</p>
<p>2) in the ValueDescription, we don't need 'group=natural' otherwise the text stays in english. I don't try 'group=naturel' because with nothing it works so it is useless to add these parameters</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jan '22, 16:17</strong></p>
<img src="https://secure.gravatar.com/avatar/33b586336c1978cc33b67e8b3cff9cb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fred73000&#39;s gravatar image" />
<p><span>Fred73000</span><br />
<span class="score" title="54 reputation points">54</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fred73000 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jan '22, 16:34</strong> </span></p>
</div>
</div>
<div id="comments-container-82975" class="comments-container">
&#10;</div>
<div id="comment-tools-82975" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82975-form-container" class="comment-form-container">
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

