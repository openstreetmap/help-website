+++
type = "question"
title = "How do I display OSM boundaries in QGIS?"
description = '''OK I&#x27;m a bit stuck - the OSM boundaries seem fine to me, but how on earth do i get them to display in QGIS? converted to new question from answer in Using OS and OSM data on the same map - copyright question.'''
date = "2020-02-06T16:31:00Z"
lastmod = "2020-02-07T18:09:00Z"
weight = 72898
keywords = [ "boundaries", "qgis" ]
aliases = [ "/questions/72898" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I display OSM boundaries in QGIS?](/questions/72898/how-do-i-display-osm-boundaries-in-qgis)

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
<span id="post-72898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72898-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>OK I'm a bit stuck - the OSM boundaries seem fine to me, but how on earth do i get them to display in QGIS?</p>
<p><em>converted to new question from answer in <a href="/questions/72872/using-os-and-osm-data-on-the-same-map-copyright-question">Using OS and OSM data on the same map - copyright question</a>.</em></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Feb '20, 16:31</strong></p>
<img src="https://secure.gravatar.com/avatar/7baf5e478fe32061cfc2f3da6ddfd42c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CurrentLandscape&#39;s gravatar image" />
<p><span>CurrentLands...</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CurrentLandscape has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Feb '20, 17:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-72898" class="comments-container">
<span id="72899"></span>
<div id="comment-72899" class="comment">
<div id="post-72899-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/17854/currentlandscape">@CurrentLandscape</a>: I created a new question for this as it is completely different from your previous legal question. This way both questions can be found and answered more easily.</p>
</div>
<div id="comment-72899-info" class="comment-info">
<span class="comment-age">(06 Feb '20, 17:05)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-72898" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72898-form-container" class="comment-form-container">
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

<span id="72930"></span>

<div id="answer-container-72930" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72930-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems it depends heavily on the QGis version you're using.</p>
<p>Here is an example : <a href="https://www.qgistutorials.com/en/docs/3/downloading_osm_data.html">tutorial</a>. More info on the <a href="https://wiki.openstreetmap.org/wiki/QGIS">OSM wiki</a>.</p>
<p>For county boundaries in UK, you'll search for boundary=administrative and admin_level=10 (according the <a href="https://wiki.openstreetmap.org/wiki/Tag:boundary=administrative">boundary=administrative</a> wiki page).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '20, 18:09</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-72930" class="comments-container">
&#10;</div>
<div id="comment-tools-72930" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72930-form-container" class="comment-form-container">
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

