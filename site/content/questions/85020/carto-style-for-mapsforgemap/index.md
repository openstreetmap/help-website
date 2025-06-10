+++
type = "question"
title = "Carto-style for Mapsforge/.map?!"
description = '''I feel like I am asking a very stupid question, because what I am searching for seems so obvious. But I have not been able to find it so far. Is there some form of the Carto-style that is applicable on (standard) Mapsforge-maps? I would prefer that because I am most used to that, besides some partic...'''
date = "2022-07-09T20:05:00Z"
lastmod = "2022-07-11T17:05:00Z"
weight = 85020
keywords = [ "style", "mapsforge", "carto", "theme" ]
aliases = [ "/questions/85020" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Carto-style for Mapsforge/.map?!](/questions/85020/carto-style-for-mapsforgemap)

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
<span id="post-85020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85020-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I feel like I am asking a very stupid question, because what I am searching for seems so obvious. But I have not been able to find it so far.</p>
<p>Is there some form of the Carto-style that is applicable on (standard) Mapsforge-maps?</p>
<p>I would prefer that because I am most used to that, besides some particular details in various other styles that I don't like, or that just lack. And I think that's exactly what I have seen in ViewRanger. Unless that worked differently.</p>
<p>Currently I use maps from Freizeitkarte and BBBike in Locus.</p>
<ul>
<li>Freizeitkarte has its own nomenclature, surprisingly.</li>
<li>For BBBike I was able to apply the <a href="https://github.com/mapsforge/mapsforge/blob/master/docs/Rendertheme.md">MapsForge RenderTheme</a>. But only after hacking it, and downgrading the nominal version from 5 to 3. I don't know if there is an 'official' way in this case. The result isn't great.</li>
</ul>
<p>I have been looking into the <a href="https://github.com/gravitystorm/openstreetmap-carto">Carto-project</a> itself. That did not seem appropriate to me. Or just with a lot of other tools for generation or conversion. That went beyond me.</p>
<p>So again. Isn't there just the plain and simple xml-file that I am looking for somewhere?! Preferably going along with new versions of Carto.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-mapsforge" rel="tag" title="see questions tagged &#39;mapsforge&#39;">mapsforge</span> <span class="post-tag tag-link-carto" rel="tag" title="see questions tagged &#39;carto&#39;">carto</span> <span class="post-tag tag-link-theme" rel="tag" title="see questions tagged &#39;theme&#39;">theme</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '22, 20:05</strong></p>
<img src="https://secure.gravatar.com/avatar/858d6bd0ad7e1eb00776cceae44a7253?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BertMule&#39;s gravatar image" />
<p><span>BertMule</span><br />
<span class="score" title="7 reputation points">7</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BertMule has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jul '22, 20:06</strong> </span></p>
</div>
</div>
<div id="comments-container-85020" class="comments-container">
&#10;</div>
<div id="comment-tools-85020" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85020-form-container" class="comment-form-container">
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

<span id="85030"></span>

<div id="answer-container-85030" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85030-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the main issue is that the MapsForge rendering rules are basically similar to those of OSMarender which used XLST transforms to convert OSM XML to SVG using another XML document as the style sheet. Indeed the main style sheet on the MapsForge repo is even called <a href="https://github.com/mapsforge/mapsforge/blob/master/mapsforge-themes/src/main/resources/assets/mapsforge/osmarender.xml"><code>osmarender.xml</code></a>!</p>
<p>This is technology which has not been maintained for 10 years, so the number of people familiar with the principles, and particularly, limitations of the approach is now small.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '22, 17:05</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jul '22, 17:06</strong> </span></p>
</div>
</div>
<div id="comments-container-85030" class="comments-container">
&#10;</div>
<div id="comment-tools-85030" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85030-form-container" class="comment-form-container">
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

