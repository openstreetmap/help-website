+++
type = "question"
title = "Print screen attribution using JOSM"
description = '''I am currently documenting some editing procedures in the wiki. As suggested, I tried to upload the images I need to Wikimedia Commons. The problem is that I don&#x27;t know under which license to assign these images. Images are subsets of &quot;print screens&quot; I made when I was editing OSM data with JOSM with...'''
date = "2020-01-17T21:24:00Z"
lastmod = "2020-01-19T13:46:00Z"
weight = 72562
keywords = [ "josm", "imagery", "attribution", "wikimedia" ]
aliases = [ "/questions/72562" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Print screen attribution using JOSM](/questions/72562/print-screen-attribution-using-josm)

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
<span id="post-72562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72562-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently documenting some editing procedures in the wiki. As suggested, I tried to upload the images I need to Wikimedia Commons. The problem is that I don't know under which license to assign these images.</p>
<p>Images are subsets of "print screens" I made when I was editing OSM data with JOSM with Bing or ESRI images in the background. Any idea?</p>
<p>Daniel</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span> <span class="post-tag tag-link-attribution" rel="tag" title="see questions tagged &#39;attribution&#39;">attribution</span> <span class="post-tag tag-link-wikimedia" rel="tag" title="see questions tagged &#39;wikimedia&#39;">wikimedia</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jan '20, 21:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a504353df13461ace2c733906a99ce16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfd553&#39;s gravatar image" />
<p><span>jfd553</span><br />
<span class="score" title="389 reputation points">389</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfd553 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72562" class="comments-container">
&#10;</div>
<div id="comment-tools-72562" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72562-form-container" class="comment-form-container">
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

<span id="72566"></span>

<div id="answer-container-72566" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72566-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72566-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72566-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jfd553 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Besides your own copyright as the creator of the image, there are at least three sources of copyrightable content involved:</p>
<ul>
<li>OSM data</li>
<li>JOSM itself</li>
<li>Bing/ESRI imagery</li>
</ul>
<p>OSM is relatively easy to attribute on Commons, as they have a pre-made <a href="https://commons.wikimedia.org/wiki/Template:OpenStreetMap">template</a> that you can stick on the image description page.</p>
<p>JOSM is trickier. You should be on the safe side by adding another template to the image description page, namely <code>{{Free screenshot|template=GPL}}</code>, which indicates that this is a screenshot of software under the GPL license. (It would be interesting to hear the JOSM developers' position on the license of JOSM screenshots.)</p>
<p>Unfortunately, that issue won't really matter because the dealbreaker here is likely going to be the imagery in the background. Bing and ESRI imagery is not actually available under an open license, they merely permit us to use it for mapping. Commons does not permit content under non-open licenses (not even <a href="https://commons.wikimedia.org/wiki/Commons:Fair_use">"fair use"</a>).</p>
<p>So while the advice to upload to Commons instead of the OSM wiki is usually a good one, this is not going to be an option here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '20, 19:08</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-72566" class="comments-container">
<span id="72571"></span>
<div id="comment-72571" class="comment">
<div id="post-72571-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Clear answer in a three components complex topic : +3 Tordanik</p>
</div>
<div id="comment-72571-info" class="comment-info">
<span class="comment-age">(19 Jan '20, 13:46)</span> <span class="comment-user userinfo">jfd553</span>
</div>
</div>
</div>
<div id="comment-tools-72566" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72566-form-container" class="comment-form-container">
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

