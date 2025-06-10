+++
type = "question"
title = "Fixing a subway stop"
description = '''I&#x27;m trying to use an iPhone app for transit planning. The app uses OpenStreetMap, (surprise,) at the moment, the app/OSM does not seem to recognize an existing subway (railway) stop. Specifically, in Chicago, IL USA, the Blue Line subway has a stop at Irving Park. The map shows a &quot;platform&quot; at that ...'''
date = "2010-10-05T18:47:00Z"
lastmod = "2010-10-06T08:46:00Z"
weight = 1012
keywords = [ "railway", "editing", "newbie" ]
aliases = [ "/questions/1012" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Fixing a subway stop](/questions/1012/fixing-a-subway-stop)

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
<span id="post-1012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1012-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to use an iPhone app for transit planning. The app uses OpenStreetMap, (surprise,) at the moment, the app/OSM does not seem to recognize an existing subway (railway) stop.</p>
<p>Specifically, in Chicago, IL USA, the Blue Line subway has a stop at Irving Park. The map shows a "platform" at that location rather than a station for a subway line.</p>
<p>I haven't done any editing before, and I am not understanding how I would go about either, eliminating the "platform" and replacing it with a station/stop, or adding a station/stop on top of the existing platform.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Oct '10, 18:47</strong></p>
<img src="https://secure.gravatar.com/avatar/1be712c25171a2eaa51daa8cead7a7d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wes%20M&#39;s gravatar image" />
<p><span>Wes M</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wes M has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1012" class="comments-container">
&#10;</div>
<div id="comment-tools-1012" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1012-form-container" class="comment-form-container">
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

<span id="1014"></span>

<div id="answer-container-1014" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1014-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-1014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you haven't done so already, create an OpenStreetMap account using the link at the top right of <a href="http://www.openstreetmap.org"></a><a href="http://www.openstreetmap.org"></a><a href="http://www.openstreetmap.org">www.openstreetmap.org</a>, then log in.</p>
<p>Navigate to Irving Park on the map, then zoom right in, so that you can see the relevant bit of subway and not much else. Then hit 'Edit'.</p>
<p>The online editor, Potlatch, will load. When the splash screen appears, hit 'Edit with save'.</p>
<p>You'll see a wireframe-ish view of the map. You'll probably find that the subway is a black line. At Irving Park, you should find a black node (point). The black indicates that the node is 'tagged' - in other words, that it has some attributes to say what it is.</p>
<p>Click the node, and the tags will appear in the panel at the bottom. You want to change it from the tags for 'platform' to the tags for 'station'. In this case you can probably just replace the word 'platform' with 'station', but if you want to know exactly what tags are commonly used for this and a million other things, see the <a href="http://wiki.openstreetmap.org/wiki/Map_Features">Map Features</a> page on OSM's wiki.</p>
<p>Finally, deselect the point (by clicking elsewhere on the map), then click 'Save' at the bottom right. Enter a brief comment explaining what you've done.</p>
<p>Your change will be saved, and should be visible on the map in an hour or so (subject to caching).</p>
<p>Enjoy!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Oct '10, 08:46</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-1014" class="comments-container">
&#10;</div>
<div id="comment-tools-1014" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1014-form-container" class="comment-form-container">
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

