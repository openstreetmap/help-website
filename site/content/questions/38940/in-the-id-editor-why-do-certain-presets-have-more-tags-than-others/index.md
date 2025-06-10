+++
type = "question"
title = "In the iD editor, why do certain presets have more tags than others"
description = '''I&#x27;ve noticed that the &quot;McDonald&#x27;s&quot; preset has cuisine=burger, but &quot;Pizza Hut&quot; has no cuisine. It appears the presets are compiled as part of the iD build, but it&#x27;s not clear why some presets have more tags than others. '''
date = "2014-11-29T15:55:00Z"
lastmod = "2014-11-29T21:07:00Z"
weight = 38940
keywords = [ "ideditor", "cuisine" ]
aliases = [ "/questions/38940" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [In the iD editor, why do certain presets have more tags than others](/questions/38940/in-the-id-editor-why-do-certain-presets-have-more-tags-than-others)

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
<span id="post-38940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38940-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've noticed that the "McDonald's" preset has cuisine=burger, but "Pizza Hut" has no cuisine. It appears the presets are compiled as part of the iD build, but it's not clear why some presets have more tags than others.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-cuisine" rel="tag" title="see questions tagged &#39;cuisine&#39;">cuisine</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Nov '14, 15:55</strong></p>
<img src="https://secure.gravatar.com/avatar/f221969d01bf7d2a0707c85897d84ec5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brianegge&#39;s gravatar image" />
<p><span>brianegge</span><br />
<span class="score" title="126 reputation points">126</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brianegge has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Nov '14, 00:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-38940" class="comments-container">
&#10;</div>
<div id="comment-tools-38940" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38940-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="38944"></span>

<div id="answer-container-38944" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38944-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-38944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="brianegge has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>AFAIK this issue has nothing to do with presets. Name based tag suggestions for iD and vespucci are generated from <a href="https://github.com/osmlab/name-suggestion-index">https://github.com/osmlab/name-suggestion-index</a> which in turn is generated from an OSM planet dump.</p>
<p>That naturally doesn't explain the difference except that perhaps Pizza Huts may simply not have a cuisine tag very often and that it doesn't turn up in the index for that reason. In any case you should probably create an issue in the name-suggestion-index repository.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Nov '14, 21:07</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Dec '14, 15:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span></p>
</div>
</div>
<div id="comments-container-38944" class="comments-container">
&#10;</div>
<div id="comment-tools-38944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38944-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38941"></span>

<div id="answer-container-38941" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38941-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-38941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi. read these pages about the development of the OSM Id editor, <a href="https://www.mapbox.com/osmdev/">https://www.mapbox.com/osmdev/</a> <a href="http://comments.gmane.org/gmane.comp.gis.openstreetmap.devel/27337">http://comments.gmane.org/gmane.comp.gis.openstreetmap.devel/27337</a> or ask your question there. You might get a good and sturdy answer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Nov '14, 16:09</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-38941" class="comments-container">
&#10;</div>
<div id="comment-tools-38941" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38941-form-container" class="comment-form-container">
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

