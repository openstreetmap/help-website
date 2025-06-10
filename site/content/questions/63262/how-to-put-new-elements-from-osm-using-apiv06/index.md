+++
type = "question"
title = "How to PUT new elements from .osm using APIv0.6?"
description = '''Hello all, I have an Android app which helps users to map some features at runtime using Deep Learning. The features (roundabouts, football fields, ...) are converted to xml/osm format file with their lat, lon attributes and negative ID&#x27;s. I want to call to the API (i had read all the guidelines abo...'''
date = "2018-05-02T00:14:00Z"
lastmod = "2018-05-03T12:04:00Z"
weight = 63262
keywords = [ "put", "android", "api", "elements" ]
aliases = [ "/questions/63262" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to PUT new elements from .osm using APIv0.6?](/questions/63262/how-to-put-new-elements-from-osm-using-apiv06)

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
<span id="post-63262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63262-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all,</p>
<p>I have an Android app which helps users to map some features at runtime using Deep Learning. The features (roundabouts, football fields, ...) are converted to xml/osm format file with their lat, lon attributes and negative ID's.</p>
<p>I want to call to the API (i had read all the guidelines about the topic and i want to try it first with the dev's api) to make a PUT call but i am not sure about how to do this... Which is the simplest way to make a Java PUT request passing a xml/osm file?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-put" rel="tag" title="see questions tagged &#39;put&#39;">put</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-elements" rel="tag" title="see questions tagged &#39;elements&#39;">elements</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 May '18, 00:14</strong></p>
<img src="https://secure.gravatar.com/avatar/d62b2a4724372f0c7873679f978c66f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andresCC12&#39;s gravatar image" />
<p><span>andresCC12</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andresCC12 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63262" class="comments-container">
<span id="63280"></span>
<div id="comment-63280" class="comment">
<div id="post-63280-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Before uploading data, have you actually downloaded data from the API? You do know that you will have to do that (and merge the edits from your users in to the existing downloaded data)?</p>
</div>
<div id="comment-63280-info" class="comment-info">
<span class="comment-age">(02 May '18, 23:16)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="63282"></span>
<div id="comment-63282" class="comment">
<div id="post-63282-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I show a OSM map in the interface (with the osmdroid library) to let users check what is actually in the OSM and I only let them import new content to the map (in unmapping places).</p>
</div>
<div id="comment-63282-info" class="comment-info">
<span class="comment-age">(03 May '18, 10:30)</span> <span class="comment-user userinfo">andresCC12</span>
</div>
</div>
<span id="63286"></span>
<div id="comment-63286" class="comment">
<div id="post-63286-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A roundabout not connected existing data is not going to be very helpful</p>
</div>
<div id="comment-63286-info" class="comment-info">
<span class="comment-age">(03 May '18, 12:04)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63262" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63262-form-container" class="comment-form-container">
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

<span id="63268"></span>

<div id="answer-container-63268" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63268-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-63268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="andresCC12 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Does this <a href="https://help.openstreetmap.org/questions/17694/create-a-changeset-using-api">previous question</a> help?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 May '18, 11:00</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-63268" class="comments-container">
<span id="63283"></span>
<div id="comment-63283" class="comment">
<div id="post-63283-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do I have to create first my own changeset in order to import new elements (for example a way)?</p>
</div>
<div id="comment-63283-info" class="comment-info">
<span class="comment-age">(03 May '18, 10:35)</span> <span class="comment-user userinfo">andresCC12</span>
</div>
</div>
<span id="63284"></span>
<div id="comment-63284" class="comment">
<div id="post-63284-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, changes can only happen inside a changeset.</p>
</div>
<div id="comment-63284-info" class="comment-info">
<span class="comment-age">(03 May '18, 10:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63268" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63268-form-container" class="comment-form-container">
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

