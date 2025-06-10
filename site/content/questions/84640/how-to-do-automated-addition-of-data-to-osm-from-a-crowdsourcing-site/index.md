+++
type = "question"
title = "How to do automated addition of data to OSM from a crowdsourcing site"
description = '''I have been using a crowdsourcing site called openbenches that catalogs the memorial plaques often found on benches. When someone adds a bench to their site, how can they then push their uniqueid for it into OSM? They have the geographic co-ordinates and already have a tag in osm called Key:openbenc...'''
date = "2022-05-31T16:05:00Z"
lastmod = "2022-06-06T11:14:00Z"
weight = 84640
keywords = [ "openbenches", "api" ]
aliases = [ "/questions/84640" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to do automated addition of data to OSM from a crowdsourcing site](/questions/84640/how-to-do-automated-addition-of-data-to-osm-from-a-crowdsourcing-site)

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
<span id="post-84640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84640-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been using a crowdsourcing site called openbenches that catalogs the memorial plaques often found on benches.</p>
<p>When someone adds a bench to their site, how can they then push their uniqueid for it into OSM? They have the geographic co-ordinates and already have a tag in osm called Key:openbenches:id</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openbenches" rel="tag" title="see questions tagged &#39;openbenches&#39;">openbenches</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '22, 16:05</strong></p>
<img src="https://secure.gravatar.com/avatar/8ba525a4b7ec932bac394623ab38391d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="back_ache&#39;s gravatar image" />
<p><span>back_ache</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="back_ache has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84640" class="comments-container">
&#10;</div>
<div id="comment-tools-84640" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84640-form-container" class="comment-form-container">
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

<span id="84642"></span>

<div id="answer-container-84642" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84642-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-84642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It would be necessary to first check if the bench in question is already in OSM; if yes, maybe the "openbenches:id" tag needs to be added to the existing bench. (I am not convinced that openbenches:id is a good tag, typically such IDs would be recorded as ref:openbenches or something similar.) Therefore it is not a simple matter of "pushing" something to OSM. Also, OSM contributors must sign up with OSM and would have to authenticate with OSM before uploading data. All in all, a significant amount of programming would be required on the side of the openbenches project to integrate properly with OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '22, 19:45</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-84642" class="comments-container">
<span id="84658"></span>
<div id="comment-84658" class="comment">
<div id="post-84658-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>AFAIK openbenches is very aware of OSM, probably the best thing to do would be to talk to openbenches, particularly given that they could simply add their information to OSM to start with.</p>
</div>
<div id="comment-84658-info" class="comment-info">
<span class="comment-age">(01 Jun '22, 17:40)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="84712"></span>
<div id="comment-84712" class="comment">
<div id="post-84712-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi,</p>
<p>I have put it on their suggestion/dev board as I think as the benches inscription they store is in effect a "fingerprint" for the bench, and with that, they could help OSM up to date, for example, if the bench is moved.</p>
<p><a href="https://github.com/openbenches/openbenches.org/issues/262">https://github.com/openbenches/openbenches.org/issues/262</a></p>
</div>
<div id="comment-84712-info" class="comment-info">
<span class="comment-age">(06 Jun '22, 11:14)</span> <span class="comment-user userinfo">back_ache</span>
</div>
</div>
</div>
<div id="comment-tools-84642" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84642-form-container" class="comment-form-container">
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

