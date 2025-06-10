+++
type = "question"
title = "Do I include bus stops in a route relation?"
description = '''The case I&#x27;m interested in is here: https://www.openstreetmap.org/way/625808720 It is the only bus stop on that route that is included in the route relation (&quot;Bus 4&quot; is the one I&#x27;m currently interested in). The wiki seems to say that the stop should not have a route=* tag, and should be part of the ...'''
date = "2019-11-15T11:08:00Z"
lastmod = "2019-11-15T14:55:00Z"
weight = 71646
keywords = [ "routes", "busstops", "relations", "busroutes" ]
aliases = [ "/questions/71646" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Do I include bus stops in a route relation?](/questions/71646/do-i-include-bus-stops-in-a-route-relation)

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
<span id="post-71646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71646-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The case I'm interested in is here: <a href="https://www.openstreetmap.org/way/625808720">https://www.openstreetmap.org/way/625808720</a></p>
<p>It is the only bus stop on that route that is included in the route relation ("Bus 4" is the one I'm currently interested in).</p>
<p>The wiki <em>seems</em> to say that the stop should <em>not</em> have a <code>route=*</code> tag, and <em>should</em> be part of the route relation.</p>
<p>But when I use the <a href="http://ra.osmsurround.org/analyzeMap?relationId=2580522">relations analyser</a> I get a problem flag for this bus stop: the analyser doesn't like that this it's part of the route relation</p>
<p>Which is correct, please?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routes" rel="tag" title="see questions tagged &#39;routes&#39;">routes</span> <span class="post-tag tag-link-busstops" rel="tag" title="see questions tagged &#39;busstops&#39;">busstops</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-busroutes" rel="tag" title="see questions tagged &#39;busroutes&#39;">busroutes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Nov '19, 11:08</strong></p>
<img src="https://secure.gravatar.com/avatar/4f273f48fd8756729fc15f4fcf4aae2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eteb3&#39;s gravatar image" />
<p><span>eteb3</span><br />
<span class="score" title="295 reputation points">295</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eteb3 has one accepted answer">6%</span></p>
</div>
</div>
<div id="comments-container-71646" class="comments-container">
<span id="71647"></span>
<div id="comment-71647" class="comment">
<div id="post-71647-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wiki says (<a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dbus_stop#Bus_stop):">https://wiki.openstreetmap.org/wiki/Tag:highway%3Dbus_stop#Bus_stop):</a></p>
<p><em>Use of the tags route_ref=</em>, 'location' and 'towards' is no longer recommended in conjunction with highway=bus_stop. This information should instead be associated with the corresponding route= <em>relation.</em></p>
</div>
<div id="comment-71647-info" class="comment-info">
<span class="comment-age">(15 Nov '19, 11:09)</span> <span class="comment-user userinfo">eteb3</span>
</div>
</div>
<span id="71648"></span>
<div id="comment-71648" class="comment">
<div id="post-71648-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><code>route_ref=</code> is an acceptable, crude first step. Only that you have to make the relation to consider it done.</p>
</div>
<div id="comment-71648-info" class="comment-info">
<span class="comment-age">(15 Nov '19, 12:17)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-71646" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71646-form-container" class="comment-form-container">
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

<span id="71649"></span>

<div id="answer-container-71649" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71649-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Which is correct, please?</p>
</blockquote>
<p>Both. They are two different questions.</p>
<blockquote>
<p>The wiki seems to say that the stop should not have a route=* tag, and should be part of the route relation.</p>
</blockquote>
<p>Of course stops shouldn't have <code>route=</code>. It is for identifying route type in relation objects. You are looking for <code>route_ref=</code>, see my previous comment below.</p>
<blockquote>
<p>But when I use the relations analyser I get a problem flag for this bus stop: the analyser doesn't like that this it's part of the troute relation</p>
</blockquote>
<p>The problem is you forgot to add the role <code>platform</code> for the bus platform area. OSM area are ways, that must be identified with a non-empty role for ways not part of the traveled route. Look at how it is added to other bus route relations with "(as platform)".</p>
<p>An additional suggestion:</p>
<p>The <code>name=Rivergate Stop A</code> can be tagged as <code>ref=A</code> instead.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '19, 12:31</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Nov '19, 12:35</strong> </span></p>
</div>
</div>
<div id="comments-container-71649" class="comments-container">
<span id="71651"></span>
<div id="comment-71651" class="comment">
<div id="post-71651-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks: I've made the role 'platform'.</p>
<p>So to be clear, all the other bus stops should be added to that route relation? Eg, <a href="https://www.openstreetmap.org/node/6936897416">this one</a> where currently only the road is part of the route relation.</p>
</div>
<div id="comment-71651-info" class="comment-info">
<span class="comment-age">(15 Nov '19, 14:54)</span> <span class="comment-user userinfo">eteb3</span>
</div>
</div>
<span id="71652"></span>
<div id="comment-71652" class="comment">
<div id="post-71652-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>The name=Rivergate Stop A can be tagged as ref=A instead.</p>
</blockquote>
<p>Why is this?</p>
</div>
<div id="comment-71652-info" class="comment-info">
<span class="comment-age">(15 Nov '19, 14:55)</span> <span class="comment-user userinfo">eteb3</span>
</div>
</div>
</div>
<div id="comment-tools-71649" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71649-form-container" class="comment-form-container">
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

