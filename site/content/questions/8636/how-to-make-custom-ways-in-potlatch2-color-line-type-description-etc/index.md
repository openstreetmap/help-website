+++
type = "question"
title = "How to make custom ways in potlatch2? (color, line type, description etc)"
description = '''I&#x27;m trying to draw a line that will represent data transport cables. I want to make them of a specific colour, thickness, line type etc. I also want to be able to give it some properties, as how many cables exist per line, how many are used etc. And i can&#x27;t seem to find how to make my custom ways/ma...'''
date = "2011-10-25T09:34:00Z"
lastmod = "2011-10-25T12:56:00Z"
weight = 8636
keywords = [ "potlatch2", "ways", "editing" ]
aliases = [ "/questions/8636" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to make custom ways in potlatch2? (color, line type, description etc)](/questions/8636/how-to-make-custom-ways-in-potlatch2-color-line-type-description-etc)

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
<span id="post-8636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8636-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to draw a line that will represent data transport cables. I want to make them of a specific colour, thickness, line type etc. I also want to be able to give it some properties, as how many cables exist per line, how many are used etc. And i can't seem to find how to make my custom ways/markers.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '11, 09:34</strong></p>
<img src="https://secure.gravatar.com/avatar/dc9b01669c0702f230fa57c384b947a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexz&#39;s gravatar image" />
<p><span>alexz</span><br />
<span class="score" title="225 reputation points">225</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8636" class="comments-container">
&#10;</div>
<div id="comment-tools-8636" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8636-form-container" class="comment-form-container">
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

<span id="8639"></span>

<div id="answer-container-8639" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8639-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="alexz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM is not about making a map rendering but about making a vector map that is easy for others to use. You should find or make a descriptive tag set to mark data cables.</p>
<p>For Potlatch2 you can create your own <a href="http://www.mapcss.org/">mapCSS</a> and add it to <em>stylesheets.xml</em> on a local potlatch2 installation (i assume from your previous posts that you have one). This style sheet can also be used in JOSM.</p>
<p>If you want to customize Potlatch's tagging presets you can edit <a href="https://wiki.openstreetmap.org/wiki/Potlatch_2/Developer_Documentation/Map_Features"><em>map_features.xml</em></a>, but this in itself doesn't alter how anything appears in the editor.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '11, 10:49</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Oct '11, 15:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-8639" class="comments-container">
<span id="8640"></span>
<div id="comment-8640" class="comment">
<div id="post-8640-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hm, i don't think i want to make a totally new map style. All i want is to be able to make custom notations, like misc devices and data cables. It looks like editing map_features.xml is all i need. Unless you can advise me differently? Are there some map making principles i should follow to increase its flexibility? Thx a lot for you answer,btw!</p>
</div>
<div id="comment-8640-info" class="comment-info">
<span class="comment-age">(25 Oct '11, 12:56)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
</div>
<div id="comment-tools-8639" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8639-form-container" class="comment-form-container">
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

