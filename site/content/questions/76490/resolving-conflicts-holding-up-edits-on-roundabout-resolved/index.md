+++
type = "question"
title = "Resolving conflicts holding up edits on roundabout [RESOLVED]"
description = '''Noticed a series of edits never got through, but when opening the standard browser based editor they&#x27;re all there. Today I happened on a highway-highway conflict while parsing through the multiple edits and fixed it to include adding an obligatory stop for the bus lane feed (put a sign, though it&#x27;s ...'''
date = "2020-09-07T15:03:00Z"
lastmod = "2020-09-07T20:46:00Z"
weight = 76490
keywords = [ "roundabouts" ]
aliases = [ "/questions/76490" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Resolving conflicts holding up edits on roundabout \[RESOLVED\]](/questions/76490/resolving-conflicts-holding-up-edits-on-roundabout-resolved)

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
<span id="post-76490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76490-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Noticed a series of edits never got through, but when opening the standard browser based editor they're all there. Today I happened on a highway-highway conflict while parsing through the multiple edits and fixed it to include adding an obligatory stop for the bus lane feed (put a sign, though it's painted big on the bus lane exit that feeds into a new roundabout. The warning disappeared, but still the series of edits and any other subsequent edit that feeds into the same roundabout object dont show through. Question is, is there an easy way to find problems/conflicts. The last edit on the roundabout in hopes of resolving the set is <a href="https://www.openstreetmap.org/edit#map=20/42.51682/14.15172">https://www.openstreetmap.org/edit#map=20/42.51682/14.15172</a></p>
<p>Thanks.</p>
<p>PS noticed on other edits that there are 'ignore issue' of other's cases standing. Will these cause edits not to appear when routing gets broken? I presume yes, but again, how to find those.</p>
<p>Edit: It looks like browser cache is not clearing in full, turning up stale pages in OSM.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roundabouts" rel="tag" title="see questions tagged &#39;roundabouts&#39;">roundabouts</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Sep '20, 15:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ed39ace8cbefe3b5c45da98f60f5e34c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SekeRob&#39;s gravatar image" />
<p><span>SekeRob</span><br />
<span class="score" title="211 reputation points">211</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SekeRob has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Sep '20, 16:23</strong> </span></p>
</div>
</div>
<div id="comments-container-76490" class="comments-container">
&#10;</div>
<div id="comment-tools-76490" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76490-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="76491"></span>

<div id="answer-container-76491" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76491-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM does not have a concept of an edit pipeline. Any edit you upload "gets through" into the central database. There's no such thing as a pending or conflicting edit that could keep another edit from "getting through". (Only thing that can happen is you get a conflict message during upload because someone else has edited the same thing at the same time.)</p>
<p>Can you re-phrase: "noticed on other edits that there are 'ignore issue' of other's cases standing"? What exactly did you notice?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '20, 15:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-76491" class="comments-container">
<span id="76492"></span>
<div id="comment-76492" class="comment">
<div id="post-76492-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8468/sekerob">@SekeRob</a>, could you also explain which "warning disappeared"? Where (which tool/site/process step) did you see a warning?</p>
</div>
<div id="comment-76492-info" class="comment-info">
<span class="comment-age">(07 Sep '20, 16:00)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="76493"></span>
<div id="comment-76493" class="comment">
<div id="post-76493-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Weird, as many edits get through within minutes or hours, just this one isn't. And yes, when switching to edit mode the edits appear exactly as I entered them for that location. Moreover, I clear the browser cache daily, automated, when exiting the browser, so there should not be any local copies mucking up what I get to see, so I know they are stored server side. Puzzling.</p>
<p>"ignore issue" e.g. a building object is not aligned anymore, overlaying a street or other building objects. When updating the street it gives the 'ignore issue' as an option, when it was already overlaying before the edit which then results in a warning when saving the current edit. The option is there so one would imaging it has a purpose.</p>
<p>The warning that disappeared was the noyed highway-highway crossing when revisiting the edit-set and after. It showed near the very bottom below the nodes list. in the left edit bar.</p>
</div>
<div id="comment-76493-info" class="comment-info">
<span class="comment-age">(07 Sep '20, 16:04)</span> <span class="comment-user userinfo">SekeRob</span>
</div>
</div>
</div>
<div id="comment-tools-76491" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76491-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76494"></span>

<div id="answer-container-76494" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76494-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OK, closed Vivaldi (Chrome based), after clearing cache and cookies. Opened, and not showing. Closed it again. Opened Chrome (vers. 85) and pasted the copied address from Vivaldi into Chrome and all edits are showing through. Either the bus lane edit resolved this or it's just bad cache clearing behavior by Vivaldi.</p>
<p>For now, consider case closed. If I can edit the OP title i'll add [RESOLVED] to the title. Apologies for the interruption.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '20, 16:14</strong></p>
<img src="https://secure.gravatar.com/avatar/ed39ace8cbefe3b5c45da98f60f5e34c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SekeRob&#39;s gravatar image" />
<p><span>SekeRob</span><br />
<span class="score" title="211 reputation points">211</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SekeRob has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Sep '20, 16:14</strong> </span></p>
</div>
</div>
<div id="comments-container-76494" class="comments-container">
&#10;</div>
<div id="comment-tools-76494" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76494-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76503"></span>

<div id="answer-container-76503" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76503-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As far as I know this is what happens when the map is edited. The database is modified immediately. The map tiles will then be redrawn, one at a time,( there are millions of them) but this will take a while and often you will see old data on some zoom levels and new data on others because different zoom levels are redrawn in some sort of rota. You may also see old data because your browser has stored it, Ctrl F5, on a Win PC may refresh the data. If you want to test routing through a junction with Graphopper or OSRM that won't work for maybe a few days until the routers have downloaded the data for the Junction or area you wish to test. I hope this helps :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '20, 20:46</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-76503" class="comments-container">
&#10;</div>
<div id="comment-tools-76503" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76503-form-container" class="comment-form-container">
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

