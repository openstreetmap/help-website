+++
type = "question"
title = "JOSM: automagically download data or draw path following a GPS receiver data?"
description = '''Hello, there. I&#x27;m interested in mapping data along the road when my wife drives, but that would require downloading data along the road as she crosses it. Is there a possibility to configure JOSM to read data from a receiver to  continuously download OSM and imagery data along the road; use this dat...'''
date = "2016-07-16T09:14:00Z"
lastmod = "2016-07-16T12:14:00Z"
weight = 50939
keywords = [ "ways", "josm", "on-the-road", "automatically", "gps" ]
aliases = [ "/questions/50939" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM: automagically download data or draw path following a GPS receiver data?](/questions/50939/josm-automagically-download-data-or-draw-path-following-a-gps-receiver-data)

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
<span id="post-50939-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50939-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50939-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, there.</p>
<p>I'm interested in mapping data along the road when my wife drives, but that would require downloading data along the road as she crosses it. Is there a possibility to configure JOSM to read data from a receiver to</p>
<ol>
<li>continuously download OSM and imagery data along the road;</li>
<li>use this data to draw a way on-demand — when the GPS accuracy is adequate —, way which will be tagged on the fly using what I see through the windscreen.</li>
</ol>
<p>I assume I could program these functionalities in a custom plugin that I would open-source in the end, but I currently don't have the required knowledge of its internals and my Java is really rusted, so having these functionalities already coded, even partly, would be greatly time-saving.</p>
<p>Awaiting your answers,</p>
<p>Regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-on-the-road" rel="tag" title="see questions tagged &#39;on-the-road&#39;">on-the-road</span> <span class="post-tag tag-link-automatically" rel="tag" title="see questions tagged &#39;automatically&#39;">automatically</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '16, 09:14</strong></p>
<img src="https://secure.gravatar.com/avatar/03b6014ac927da400a55374bbbe5152a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Penegal&#39;s gravatar image" />
<p><span>Penegal</span><br />
<span class="score" title="631 reputation points">631</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Penegal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50939" class="comments-container">
&#10;</div>
<div id="comment-tools-50939" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50939-form-container" class="comment-form-container">
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

<span id="50940"></span>

<div id="answer-container-50940" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50940-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-50940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Penegal has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins">https://wiki.openstreetmap.org/wiki/JOSM/Plugins</a> lists</p>
<ul>
<li><a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/LiveGPS">LiveGPS</a> (displays your current position, a trace of your past positions and centres the map on the current positon)</li>
<li><a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Surveyor">Surveyor</a> (allows to enter text notes and tag presets directly on new OSM node objects)</li>
<li><a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/continuosDownload">continuosDownload</a> ("download OSM data for you current viewing area when you are zooming and paning around")</li>
</ul>
<p>I think you would rather not want to have a way's geometry to be based on raw GPS data. Manual way creation based on a trace is not that much work and eliminates zig zags due to bad GPS reception. But I guess those plugins could a good start for programming such functionality. Maybe some bits are possible with the <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Scripting">scripting plugin</a>.</p>
<p>I would make notes and/or photos or videos and record a gps trace and do the editing afterwards at home (possibly with aerial imagery support).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '16, 09:58</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jul '16, 09:59</strong> </span></p>
</div>
</div>
<div id="comments-container-50940" class="comments-container">
<span id="50941"></span>
<div id="comment-50941" class="comment">
<div id="post-50941-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Seems a good start to me, thanks.</p>
<p>Regarding drawing the way, I would use it to do a first try, and then refine it with imagery at home; besides, here in France, not much roads are missing in OSM.</p>
<p>This question is to help me about an idea I had: having a screen showing me the different signs I can encounter, and apply them on the current way if not already tagged accordingly. I'll have to code something to allow JOSM to guess which way I'm following in order to select it to apply the tag updates, or to ask me to select the way if my code is unable to guess it. Then, it would check if the data I want to add is already present and, if not, cut and tag the way accordingly. When in doubt, or if according tags are already present around the current position, the program would ask what to do, and I would manually check the data once at home. In addition, I could permanently compare the GPS receiver data with the one integrated in my car, the imagery and my vision, and correct offset much better combining these 4 sources than mapping later at home.</p>
</div>
<div id="comment-50941-info" class="comment-info">
<span class="comment-age">(16 Jul '16, 11:01)</span> <span class="comment-user userinfo">Penegal</span>
</div>
</div>
<span id="50943"></span>
<div id="comment-50943" class="comment">
<div id="post-50943-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Most of this will not work automagically. For cutting the way you will have to choose a proper position, e.g. an intersection, a crossing, a narrow part. Determining this position automatically is a challenge. Also correcting the offset shouldn't be automated. You never know whether your signal is really better than previously uploaded traces or imagery. This can only be done manually to be really useful. This applies to lots of things in OSM (at least as of today).</p>
</div>
<div id="comment-50943-info" class="comment-info">
<span class="comment-age">(16 Jul '16, 12:14)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50940" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50940-form-container" class="comment-form-container">
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

