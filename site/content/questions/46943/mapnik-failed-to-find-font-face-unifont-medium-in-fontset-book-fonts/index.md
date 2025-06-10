+++
type = "question"
title = "Mapnik: Failed to find font face &#x27;unifont Medium&#x27; in FontSet &#x27;book-fonts&#x27;"
description = '''Hello, I get the following error when I try to render tiles using Mapnik with standard style.  RuntimeError: Failed to find font face &#x27;unifont Medium&#x27; in FontSet &#x27;book-fonts&#x27; in FontSet at line 5 of &#x27;/home/mapnik/osm.xml&#x27; I use fedora 22 and I have installed &quot;unifont&quot; package, I tested it using the ...'''
date = "2015-12-03T10:17:00Z"
lastmod = "2015-12-03T11:36:00Z"
weight = 46943
keywords = [ "rendering", "font", "mapnik" ]
aliases = [ "/questions/46943" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapnik: Failed to find font face 'unifont Medium' in FontSet 'book-fonts'](/questions/46943/mapnik-failed-to-find-font-face-unifont-medium-in-fontset-book-fonts)

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
<span id="post-46943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46943-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I get the following error when I try to render tiles using Mapnik with standard style.</p>
<p><code>RuntimeError: Failed to find font face 'unifont Medium' in FontSet 'book-fonts' in FontSet at line 5 of '/home/mapnik/osm.xml'</code></p>
<p>I use fedora 22 and I have installed "unifont" package, I tested it using the following command:</p>
<p><code> [root@...]$ ls </code><code>python -c "import mapnik;print mapnik.fontscollectionpath"</code><code> default dejavu unifont </code></p>
<p>any help appreciated!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-font" rel="tag" title="see questions tagged &#39;font&#39;">font</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Dec '15, 10:17</strong></p>
<img src="https://secure.gravatar.com/avatar/ca009706fa6df2b33eb931f781ff57f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="khamooshi&#39;s gravatar image" />
<p><span>khamooshi</span><br />
<span class="score" title="146 reputation points">146</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="khamooshi has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-46943" class="comments-container">
&#10;</div>
<div id="comment-tools-46943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46943-form-container" class="comment-form-container">
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

<span id="46944"></span>

<div id="answer-container-46944" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46944-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="scai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Found it!<br />
In <em>inc/fontset-settings.xml.inc.template</em> replace "<strong>u</strong>nifont Medium" with "<strong>U</strong>nifont Medium"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '15, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/ca009706fa6df2b33eb931f781ff57f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="khamooshi&#39;s gravatar image" />
<p><span>khamooshi</span><br />
<span class="score" title="146 reputation points">146</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="khamooshi has one accepted answer">50%</span> </br></p>
</div>
</div>
<div id="comments-container-46944" class="comments-container">
<span id="46946"></span>
<div id="comment-46946" class="comment">
<div id="post-46946-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You appear to be using some very old stylesheets, that's not the "Standard" style any more. The current stylesheet is found at <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a></p>
</div>
<div id="comment-46946-info" class="comment-info">
<span class="comment-age">(03 Dec '15, 11:36)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
</div>
<div id="comment-tools-46944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46944-form-container" class="comment-form-container">
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

