+++
type = "question"
title = "How to do complex edit of tag data for many objects through text input ?"
description = '''I would like to fix broken URLs in the source tag of many objects and also include a &quot;GPS;&quot; prefix.  I will need to change the domain name and insert the prefix. This is not something that can be done with the simple UI editor of Id or JOSM.  Is there a way (JOSM?) to edit objects manually using tex...'''
date = "2021-09-26T08:27:00Z"
lastmod = "2021-11-28T12:53:00Z"
weight = 81961
keywords = [ "josm", "id" ]
aliases = [ "/questions/81961" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How to do complex edit of tag data for many objects through text input ?](/questions/81961/how-to-do-complex-edit-of-tag-data-for-many-objects-through-text-input)

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
<span id="post-81961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81961-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to fix broken URLs in the source tag of many objects and also include a "GPS;" prefix. I will need to change the domain name and insert the prefix. This is not something that can be done with the simple UI editor of Id or JOSM.</p>
<p>Is there a way (JOSM?) to edit objects manually using text manipulation (.osm extension?) before uploading them to OSM?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Sep '21, 08:27</strong></p>
<img src="https://secure.gravatar.com/avatar/e3f994b2488e2182c63a7c44a5028ff6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmoffroad&#39;s gravatar image" />
<p><span>cmoffroad</span><br />
<span class="score" title="205 reputation points">205</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmoffroad has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81961" class="comments-container">
<span id="81972"></span>
<div id="comment-81972" class="comment">
<div id="post-81972-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>curious: What is a "GPS" prefix in an URL?</p>
<p>And a thought: Does it make sense to update <code>source</code> tags at all, where we usually tag the sources to the changesets nowadays?</p>
</div>
<div id="comment-81972-info" class="comment-info">
<span class="comment-age">(26 Sep '21, 19:27)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="82708"></span>
<div id="comment-82708" class="comment">
<div id="post-82708-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hi. don't forget to accept an answer, otherwise your question will still figure as unanswered.</p>
</div>
<div id="comment-82708-info" class="comment-info">
<span class="comment-age">(28 Nov '21, 12:53)</span> <span class="comment-user userinfo">mariotomo</span>
</div>
</div>
</div>
<div id="comment-tools-81961" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81961-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="81964"></span>

<div id="answer-container-81964" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81964-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-81964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>what about you:</p>
<ul>
<li>download the data into JOSM,</li>
<li>save the data in an <code>.osm</code> file,</li>
<li>edit it with your favourite text editor (or even through <code>sed -i</code>),</li>
<li>reload into JOSM,</li>
<li>upload to OSM?</li>
</ul>
<p>(but I support the answer by <a href="https://help.openstreetmap.org/users/13231/h_mlet">h_mlet</a>, the OP's question is really a very good use case for <a href="http://level0.osmz.ru/">level0</a>)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Sep '21, 13:32</strong></p>
<img src="https://secure.gravatar.com/avatar/482a09a1d3540beaa18993d358753a34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mariotomo&#39;s gravatar image" />
<p><span>mariotomo</span><br />
<span class="score" title="300 reputation points">300</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mariotomo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '21, 13:48</strong> </span></p>
</div>
</div>
<div id="comments-container-81964" class="comments-container">
&#10;</div>
<div id="comment-tools-81964" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81964-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81967"></span>

<div id="answer-container-81967" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81967-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've never used it myself, but Level0 editor was made for that kind of operation I think.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Sep '21, 14:22</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-81967" class="comments-container">
<span id="81971"></span>
<div id="comment-81971" class="comment">
<div id="post-81971-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I also keep hearing about this "level0" and I still can't decide I should try it out. ;-)</p>
</div>
<div id="comment-81971-info" class="comment-info">
<span class="comment-age">(26 Sep '21, 18:52)</span> <span class="comment-user userinfo">mariotomo</span>
</div>
</div>
</div>
<div id="comment-tools-81967" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81967-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81987"></span>

<div id="answer-container-81987" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81987-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the objects you want to modify have some common tag, and others have not: - Download area of interest to JOSM. - Search all objects after the unique property. - Select all found objects. - Change the tag/tags. (Which mean all the found objects are changed simultaneously). - Upload</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '21, 08:00</strong></p>
<img src="https://secure.gravatar.com/avatar/7fbbe44e24bdb695025fddb0879817a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Msiipola&#39;s gravatar image" />
<p><span>Msiipola</span><br />
<span class="score" title="227 reputation points">227</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Msiipola has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81987" class="comments-container">
&#10;</div>
<div id="comment-tools-81987" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81987-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82707"></span>

<div id="answer-container-82707" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82707-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try Level0 (<a href="http://level0.osmz.ru/).">http://level0.osmz.ru/).</a> You can copy the text into an editor like VSCode or Sublime Text where you can do advanced string manipulations, using RegEx for example. When done, copy the text back to Level0.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '21, 05:17</strong></p>
<img src="https://secure.gravatar.com/avatar/15d45a99f101e06c9e79916af33f8336?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Privatemajory&#39;s gravatar image" />
<p><span>Privatemajory</span><br />
<span class="score" title="1125 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Privatemajory has 4 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-82707" class="comments-container">
&#10;</div>
<div id="comment-tools-82707" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82707-form-container" class="comment-form-container">
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

