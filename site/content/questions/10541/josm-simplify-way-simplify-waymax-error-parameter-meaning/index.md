+++
type = "question"
title = "JOSM: Simplify way - simplify-way.max-error parameter meaning"
description = '''What does exactly simplify-way.max-error parameter mean? I found in a discussion from 2009 it was supposed to be mean an error counted in meters (m). But the function seems to run pretty high even with a parameter smaller than 1. I used 0.25 and it seemed to me the error was still counted in several...'''
date = "2012-02-11T15:31:00Z"
lastmod = "2012-02-26T13:05:00Z"
weight = 10541
keywords = [ "josm", "way", "simplify" ]
aliases = [ "/questions/10541" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM: Simplify way - simplify-way.max-error parameter meaning](/questions/10541/josm-simplify-way-simplify-waymax-error-parameter-meaning)

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
<span id="post-10541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10541-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-10541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What does exactly simplify-way.max-error parameter mean? I found in a discussion from 2009 it was supposed to be mean an error counted in meters (m). But the function seems to run pretty high even with a parameter smaller than 1. I used 0.25 and it seemed to me the error was still counted in several meters... cound not find a real clue here myself.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-simplify" rel="tag" title="see questions tagged &#39;simplify&#39;">simplify</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '12, 15:31</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-10541" class="comments-container">
&#10;</div>
<div id="comment-tools-10541" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10541-form-container" class="comment-form-container">
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

<span id="10562"></span>

<div id="answer-container-10562" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10562-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-10562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kozuch has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is the maximum deviation of old and new way in meters. I've extended the <a href="http://josm.openstreetmap.de/wiki/Help/Action/SimplifyWay">help page</a>, hope this answers your questions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '12, 15:46</strong></p>
<img src="https://secure.gravatar.com/avatar/766400faa78a96dce84422cdb20779d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bastik&#39;s gravatar image" />
<p><span>bastik</span><br />
<span class="score" title="651 reputation points">651</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bastik has 5 accepted answers">41%</span></p>
</div>
</div>
<div id="comments-container-10562" class="comments-container">
<span id="10809"></span>
<div id="comment-10809" class="comment">
<div id="post-10809-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes, it is worth noting that you <strong>should generally NOT APPLY this function to geometry other then what you entered yourself!</strong> This algorithm is <strong>harming the geometry seriously</strong> in some cases (narrow curves), because it is not aware of angles but only of differences in position in metres.</p>
<p>Application of this function has to be considered a <strong>kind of automated edit</strong> and is therefor subject to the special rules we have for this kind of edits.</p>
<p>Look at this for more info: <a href="http://wiki.openstreetmap.org/wiki/Automated_Edits">http://wiki.openstreetmap.org/wiki/Automated_Edits</a></p>
</div>
<div id="comment-10809-info" class="comment-info">
<span class="comment-age">(26 Feb '12, 12:27)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
<span id="10811"></span>
<div id="comment-10811" class="comment">
<div id="post-10811-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please stay calm, I am not touching data of others. I used this tool to simplify my import of CDDA by EEA (source=EEA:CDDA2009).</p>
</div>
<div id="comment-10811-info" class="comment-info">
<span class="comment-age">(26 Feb '12, 13:05)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
</div>
<div id="comment-tools-10562" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10562-form-container" class="comment-form-container">
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

