+++
type = "question"
title = "How to get the user id for a certain user?"
description = '''Is there a way to query the user id given a certain user display name? What about the other way around? The display name can be changed any time, so the id seem to be the better solution to identify an account. Is it possible to link to the user page by id? (Something like http://www.openstreetmap.o...'''
date = "2011-11-22T15:22:00Z"
lastmod = "2020-05-08T23:59:00Z"
weight = 9181
keywords = [ "uid", "id", "user", "name" ]
aliases = [ "/questions/9181" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [How to get the user id for a certain user?](/questions/9181/how-to-get-the-user-id-for-a-certain-user)

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
<span id="post-9181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9181-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-9181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to query the user id given a certain user display name? What about the other way around?</p>
<p>The display name can be changed any time, so the id seem to be the better solution to identify an account. Is it possible to link to the user page by id? (Something like <a href="https://www.openstreetmap.org/user?id=xxxx)">https://www.openstreetmap.org/user?id=xxxx)</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-uid" rel="tag" title="see questions tagged &#39;uid&#39;">uid</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-user" rel="tag" title="see questions tagged &#39;user&#39;">user</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Nov '11, 15:22</strong></p>
<img src="https://secure.gravatar.com/avatar/766400faa78a96dce84422cdb20779d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bastik&#39;s gravatar image" />
<p><span>bastik</span><br />
<span class="score" title="651 reputation points">651</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bastik has 5 accepted answers">41%</span></p>
</div>
</div>
<div id="comments-container-9181" class="comments-container">
<span id="33645"></span>
<div id="comment-33645" class="comment">
<div id="post-33645-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there anything new on that topic. Is it still impossible to get a user name from its uid?</p>
</div>
<div id="comment-33645-info" class="comment-info">
<span class="comment-age">(03 Jun '14, 14:03)</span> <span class="comment-user userinfo">pgiraud</span>
</div>
</div>
<span id="33648"></span>
<div id="comment-33648" class="comment">
<div id="post-33648-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>See new answer from me below.</p>
</div>
<div id="comment-33648-info" class="comment-info">
<span class="comment-age">(03 Jun '14, 14:47)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-9181" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9181-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="9184"></span>

<div id="answer-container-9184" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9184-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-9184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can't link by id (as Gnonthgol says), but if you want to find an id from a given display name, go to that user's edits page, select a changeset from the list, then view the Changeset XML to find the uid.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Nov '11, 16:10</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-9184" class="comments-container">
&#10;</div>
<div id="comment-tools-9184" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9184-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33650"></span>

<div id="answer-container-33650" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33650-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-33650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do bear in mind that user names can change. If you want to do a search (by current or by historical name or by ID) you can use <a href="http://whosthat.osmz.ru"></a><a href="http://whosthat.osmz.ru">http://whosthat.osmz.ru</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '14, 19:00</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-33650" class="comments-container">
&#10;</div>
<div id="comment-tools-33650" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33650-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33647"></span>

<div id="answer-container-33647" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33647-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-33647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The API has supported a call with the UID as argument for quite a while now. The call returns user information including the user name:</p>
<p><a href="https://www.openstreetmap.org/api/0.6/user/">https://www.openstreetmap.org/api/0.6/user/</a><em>the_uid</em></p>
<p>This will naturally only give you the current mapping uid-&gt;user name and not historic ones.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '14, 14:47</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jun '14, 15:17</strong> </span></p>
</div>
</div>
<div id="comments-container-33647" class="comments-container">
<span id="43819"></span>
<div id="comment-43819" class="comment">
<div id="post-43819-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can't open the link?</p>
</div>
<div id="comment-43819-info" class="comment-info">
<span class="comment-age">(27 Jun '15, 01:37)</span> <span class="comment-user userinfo">marla729</span>
</div>
</div>
<span id="43821"></span>
<div id="comment-43821" class="comment">
<div id="post-43821-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Marla729 Try this :- <a href="https://www.openstreetmap.org/user/marla729">https://www.openstreetmap.org/user/marla729</a></p>
</div>
<div id="comment-43821-info" class="comment-info">
<span class="comment-age">(27 Jun '15, 07:05)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
<span id="74667"></span>
<div id="comment-74667" class="comment">
<div id="post-74667-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Link Simon gave returns "Couldn't find a file/directory/API operation by that name". Link BCNorwich gave is just the normal profile link.</p>
</div>
<div id="comment-74667-info" class="comment-info">
<span class="comment-age">(08 May '20, 21:06)</span> <span class="comment-user userinfo">Richlv</span>
</div>
</div>
<span id="74669"></span>
<div id="comment-74669" class="comment">
<div id="post-74669-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are slightly, that is 5 years, late :-)</p>
</div>
<div id="comment-74669-info" class="comment-info">
<span class="comment-age">(08 May '20, 21:27)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33647" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33647-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74673"></span>

<div id="answer-container-74673" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74673-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-74673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Since this has been nudged to the top of the list again, I might as well explain how I've always done it :)</p>
<ul>
<li>From a user page, click "edits".</li>
<li>Click the first changset in the list</li>
<li>Scroll down and click "changeset XML"</li>
<li>Read the "uid" from that XML - there will be a line with <code>uid="somethingorother"</code> near the top.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 May '20, 23:59</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-74673" class="comments-container">
&#10;</div>
<div id="comment-tools-74673" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74673-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16112"></span>

<div id="answer-container-16112" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16112-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes an UID is better. On <a href="http://odbl.de/belgium.html.gz">Odbl here</a>, they might as well have cumulated the merits for the same UID !!!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Sep '12, 20:45</strong></p>
<img src="https://secure.gravatar.com/avatar/22d0547d929d81aa90014a6f0aef484a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GentilPapou&#39;s gravatar image" />
<p><span>GentilPapou</span><br />
<span class="score" title="160 reputation points">160</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GentilPapou has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16112" class="comments-container">
<span id="74668"></span>
<div id="comment-74668" class="comment">
<div id="post-74668-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This doesn't seem to answer the question, though (and the website is gone by now).</p>
</div>
<div id="comment-74668-info" class="comment-info">
<span class="comment-age">(08 May '20, 21:07)</span> <span class="comment-user userinfo">Richlv</span>
</div>
</div>
</div>
<div id="comment-tools-16112" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16112-form-container" class="comment-form-container">
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

