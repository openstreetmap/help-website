+++
type = "question"
title = "How to tag the school academic calendar"
description = '''In Colombia, schools (ISCED 1, 2, or 3) has two calendars:  Calendario A: One starting at end of January, pausing in mid-June, restarting in mid-July, and finishing at the end of November (beginning December). Calendario B: The same as in northern hemisphere countries - Starting at the end of August...'''
date = "2022-01-15T17:08:00Z"
lastmod = "2022-01-16T08:23:00Z"
weight = 83081
keywords = [ "calendar", "holidays", "school", "year" ]
aliases = [ "/questions/83081" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag the school academic calendar](/questions/83081/how-to-tag-the-school-academic-calendar)

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
<span id="post-83081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83081-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In Colombia, schools (ISCED 1, 2, or 3) has two calendars:</p>
<ul>
<li>Calendario A: One starting at end of January, pausing in mid-June, restarting in mid-July, and finishing at the end of November (beginning December).</li>
<li>Calendario B: The same as in northern hemisphere countries - Starting at the end of August, pausing in December, restarting in January, and finishing in June.</li>
</ul>
<p>I would like to know how can I tag this on a school, to differentiate them between Calendar A or Calendar B.</p>
<p>For more information:</p>
<ul>
<li><a href="https://es.wikipedia.org/wiki/A%C3%B1o_escolar">https://es.wikipedia.org/wiki/A%C3%B1o_escolar</a></li>
<li><a href="https://en.wikipedia.org/wiki/Academic_year">https://en.wikipedia.org/wiki/Academic_year</a></li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-calendar" rel="tag" title="see questions tagged &#39;calendar&#39;">calendar</span> <span class="post-tag tag-link-holidays" rel="tag" title="see questions tagged &#39;holidays&#39;">holidays</span> <span class="post-tag tag-link-school" rel="tag" title="see questions tagged &#39;school&#39;">school</span> <span class="post-tag tag-link-year" rel="tag" title="see questions tagged &#39;year&#39;">year</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jan '22, 17:08</strong></p>
<img src="https://secure.gravatar.com/avatar/6998587ec6de0bab814c70777bcdd2ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AngocA&#39;s gravatar image" />
<p><span>AngocA</span><br />
<span class="score" title="281 reputation points">281</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AngocA has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83081" class="comments-container">
&#10;</div>
<div id="comment-tools-83081" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83081-form-container" class="comment-form-container">
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

<span id="83082"></span>

<div id="answer-container-83082" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83082-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AngocA has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This should be acceptable like other time data as you are not trying to add the exact schedule.</p>
<p>The simplest is to come up with something specific with your country. There are a lot of <code>school:*=</code> the most being <code>school:FR=</code> from France, however this is for school categories.</p>
<p><code>opening_hours=</code> should not be used. The school can still be "open" during after school and semester breaks. <code>service_times=</code> should be more suitable. So a possible hierarchy is something like <code>service_times:ref:CO=</code> for your <code>=A</code> and <code>=B</code>.</p>
<p>The more general option is to try to list out the school term.<br />
A: <code>service_times=Jan-Jun,Jul-Nov; SH closed</code><br />
B: <code>service_times=Sep-Dec,Jan-Jun; SH closed</code></p>
<p>If you have more precise ranges, you may try ISO year-week. Eg:<br />
A: <code>service_times=Week 4-24,28-48; SH closed</code><br />
B: <code>service_times=Week 31-50,3-26; SH closed</code></p>
<p>You can add both your country's community-decided tag and <code>service_times=</code> to show both the actual periods and the national designation for the system.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jan '22, 08:23</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jan '22, 08:24</strong> </span></p>
</div>
</div>
<div id="comments-container-83082" class="comments-container">
&#10;</div>
<div id="comment-tools-83082" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83082-form-container" class="comment-form-container">
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

