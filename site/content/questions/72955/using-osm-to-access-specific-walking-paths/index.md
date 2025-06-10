+++
type = "question"
title = "Using OSM to access specific walking paths"
description = '''Hi, I&#x27;m pretty new to Python and extremely new to OSM, but I&#x27;m hoping to use OSM&#x27;s data to calculate shortest walking paths on my college campus. Do you guys have any suggestions on how to start doing this? I&#x27;m having trouble understanding how to access and identify specific walking paths. Thanks.'''
date = "2020-02-09T05:58:00Z"
lastmod = "2020-02-10T14:55:00Z"
weight = 72955
keywords = [ "newbie" ]
aliases = [ "/questions/72955" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Using OSM to access specific walking paths](/questions/72955/using-osm-to-access-specific-walking-paths)

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
<span id="post-72955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72955-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm pretty new to Python and extremely new to OSM, but I'm hoping to use OSM's data to calculate shortest walking paths on my college campus. Do you guys have any suggestions on how to start doing this? I'm having trouble understanding how to access and identify specific walking paths. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '20, 05:58</strong></p>
<img src="https://secure.gravatar.com/avatar/8e422604ecc0be0c8bc419b488bea42b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jklod&#39;s gravatar image" />
<p><span>Jklod</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jklod has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72955" class="comments-container">
<span id="72961"></span>
<div id="comment-72961" class="comment">
<div id="post-72961-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Are you looking for an API that will do all the work for you; or some ready-made library code that you can host locally; or do you want to write the whole thing from scratch?</p>
</div>
<div id="comment-72961-info" class="comment-info">
<span class="comment-age">(09 Feb '20, 11:28)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="72963"></span>
<div id="comment-72963" class="comment">
<div id="post-72963-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd like to find a way to access the data, but do the work of computing shortest paths and displaying them manually. Though if there are resources that would help me do this manually that'd be useful.</p>
</div>
<div id="comment-72963-info" class="comment-info">
<span class="comment-age">(09 Feb '20, 20:40)</span> <span class="comment-user userinfo">Jklod</span>
</div>
</div>
<span id="72982"></span>
<div id="comment-72982" class="comment">
<div id="post-72982-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Especially for walking, you need to be aware of data quality and usage as it's more complicated than driving.</p>
</div>
<div id="comment-72982-info" class="comment-info">
<span class="comment-age">(10 Feb '20, 13:44)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-72955" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72955-form-container" class="comment-form-container">
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

<span id="72984"></span>

<div id="answer-container-72984" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72984-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-72984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jklod has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your first task is to get OpenStreetMap data and transform it into a routable graph. I wouldn't recommend reinventing the wheel for this: you can use osm4routing (Python) or osm4routing2 (Rust) for this. Both are available on github. In osm4routing2's output data, it'll signify whether a particular way is routable for pedestrians or not.</p>
<p>You can then build your shortest-path algorithm on this data. I'd suggest you start with the (unidirectional) Dijkstra algorithm, which is simple and understandable. There are lots of resources online explaining how to implement Dijkstra in Python. Once you've got the hang of that, you can move on to slightly more advanced algorithms such as bidirectional Dijkstra, A*, etc. etc.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '20, 14:55</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-72984" class="comments-container">
&#10;</div>
<div id="comment-tools-72984" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72984-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72975"></span>

<div id="answer-container-72975" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72975-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jklod has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please have a look at the <a href="https://wiki.openstreetmap.org/wiki/Routing">Routing</a> page on the OSM wiki. It has a lot of information, also for developpers.</p>
<p>Most types of highway are accessible to pedestrian, but you have to consider several tags to be sure ( access,foot...).</p>
<p>I'm not sure you can start from scratch, unless you have a lot of free time, this is a really complex problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '20, 11:58</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-72975" class="comments-container">
&#10;</div>
<div id="comment-tools-72975" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72975-form-container" class="comment-form-container">
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

