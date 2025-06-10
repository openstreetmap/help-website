+++
type = "question"
title = "JOSM - is it possible to copy data from the &quot;Suspicious data found&quot; dialog?"
description = '''On a JOSM upload, if a potential problem such as a single-node way is found, a dialog box appears:  Is it possible to copy details of the errors from this? It seems not to be.'''
date = "2013-09-14T10:48:00Z"
lastmod = "2013-09-16T12:44:00Z"
weight = 26336
keywords = [ "josm" ]
aliases = [ "/questions/26336" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM - is it possible to copy data from the "Suspicious data found" dialog?](/questions/26336/josm-is-it-possible-to-copy-data-from-the-suspicious-data-found-dialog)

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
<span id="post-26336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26336-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>On a JOSM upload, if a potential problem such as a single-node way is found, a dialog box appears:</p>
<p><img src="http://help.openstreetmap.org/upfiles/josm_01007_1.png" alt="JOSM validator box" /></p>
<p>Is it possible to copy details of the errors from this? It seems not to be.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '13, 10:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</img>
</div>
</div>
<div id="comments-container-26336" class="comments-container">
&#10;</div>
<div id="comment-tools-26336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26336-form-container" class="comment-form-container">
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

<span id="26372"></span>

<div id="answer-container-26372" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26372-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-26372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If by "copying" you mean "put in the copy-paste buffer", then it seems to be possible at a basic level:</p>
<ul>
<li>Get the dialog to appear or even use the validatior tool in the sidebar</li>
<li>Open all branches of the tree using the mouse</li>
<li>Type Ctrl-A to select all and Ctrl-C to copy</li>
<li>Open your favorite text editor and type Ctrl-V to paste</li>
</ul>
<p>It returns something like</p>
<pre><code>Warnings
Crossing buildings (1)
TestError [tester=org.openstreetmap.josm.data.validation.tests.CrossingWays@7a48772, code=601]
Building inside building (2)
TestError [tester=org.openstreetmap.josm.data.validation.tests.BuildingInBuilding@2f6d8855, code=2001]
TestError [tester=org.openstreetmap.josm.data.validation.tests.BuildingInBuilding@2f6d8855, code=2001]
Unnamed ways (1)
TestError [tester=org.openstreetmap.josm.data.validation.tests.UntaggedWay@2636111d, code=303]
Way end node near other way (1)
TestError [tester=org.openstreetmap.josm.data.validation.tests.UnconnectedWays@5c0b646d, code=1301]
Crossing ways (4)
TestError [tester=org.openstreetmap.josm.data.validation.tests.CrossingWays@7a48772, code=601]
TestError [tester=org.openstreetmap.josm.data.validation.tests.CrossingWays@7a48772, code=601]
TestError [tester=org.openstreetmap.josm.data.validation.tests.CrossingWays@7a48772, code=601]
TestError [tester=org.openstreetmap.josm.data.validation.tests.CrossingWays@7a48772, code=601]
Other
A name:* translation is missing. (1)
TestError [tester=org.openstreetmap.josm.data.validation.tests.NameMismatch@30de03a5, code=1502]
...etc</code></pre>
<p>Which is only mildly useful. This works for me, JOSM 6232 on Linux.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '13, 23:58</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-26372" class="comments-container">
<span id="26379"></span>
<div id="comment-26379" class="comment">
<div id="post-26379-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That works for me too now. Must have been user error at my end previously.</p>
</div>
<div id="comment-26379-info" class="comment-info">
<span class="comment-age">(16 Sep '13, 12:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-26372" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26372-form-container" class="comment-form-container">
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

