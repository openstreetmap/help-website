+++
type = "question"
title = "How to tag &quot;approximately positioned&quot; in a machine-parseable way?"
description = '''In my area, a bunch of highway=bus_stop nodes were added from an inaccurate data source. The nodes are positioned inaccurately, sometimes on the wrong side of the street. That affects users of foot routers: they are navigated to the wrong side of the street. One solution we&#x27;re considering is to tag ...'''
date = "2017-08-03T15:22:00Z"
lastmod = "2017-08-03T20:17:00Z"
weight = 57436
keywords = [ "inaccuracy", "tagging", "accuracy" ]
aliases = [ "/questions/57436" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag "approximately positioned" in a machine-parseable way?](/questions/57436/how-to-tag-approximately-positioned-in-a-machine-parseable-way)

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
<span id="post-57436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57436-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-57436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In my area, a bunch of highway=bus_stop nodes were added from an inaccurate data source. The nodes are positioned inaccurately, sometimes on the wrong side of the street. That affects users of foot routers: they are navigated to the wrong side of the street.</p>
<p>One solution we're considering is to tag the imported nodes with something like a <code>accuracy=10m</code> tag, which foot routers would consume and alert the user accordingly. ("Destination reached; you are now within 10 metres of the bus stop")</p>
<p>Would this make sense? Is there already a standard tag for this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-inaccuracy" rel="tag" title="see questions tagged &#39;inaccuracy&#39;">inaccuracy</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-accuracy" rel="tag" title="see questions tagged &#39;accuracy&#39;">accuracy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Aug '17, 15:22</strong></p>
<img src="https://secure.gravatar.com/avatar/8440750fd002fd989ab2e6b613ca3ccb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsh4&#39;s gravatar image" />
<p><span>dsh4</span><br />
<span class="score" title="867 reputation points">867</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsh4 has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-57436" class="comments-container">
<span id="57439"></span>
<div id="comment-57439" class="comment">
<div id="post-57439-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>One question here - do you know how inaccurate the data is?</p>
<p>The NaPTAN data in the UK has an accuracy that varies greatly by area - in some places you can bet it's with a couple of meters (at least of where the stop was at import time), but elsewhere could be significantly out. If you only know "it may not be accurate everywhere" then adding an "accuracy" tag may be misleading.</p>
</div>
<div id="comment-57439-info" class="comment-info">
<span class="comment-age">(03 Aug '17, 16:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="57445"></span>
<div id="comment-57445" class="comment">
<div id="post-57445-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unluckily you haven't told us where this is and how many stops we are taking about. Depending on a number of aspects it may make sense to run a maproulette challenge and adjust the stop positions from imagery.</p>
</div>
<div id="comment-57445-info" class="comment-info">
<span class="comment-age">(03 Aug '17, 18:50)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="57448"></span>
<div id="comment-57448" class="comment">
<div id="post-57448-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've asked my local community to join this thread and answer your questions.</p>
</div>
<div id="comment-57448-info" class="comment-info">
<span class="comment-age">(03 Aug '17, 18:57)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
</div>
<div id="comment-tools-57436" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57436-form-container" class="comment-form-container">
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

<span id="57437"></span>

<div id="answer-container-57437" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57437-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do not waste time on trying to find ways to describe just how faulty the data is. Either delete it, or fix it.</p>
<p>The data shouldn't have been imported like that in the first place (if what you say is true, you'll also have bus stops in the middle of the road or inside buildings), but now that the deed is done, I'd say you (and very much so the original importer) should concentrate on fixing it, by moving the bus stops to the correct ground-surveyed positions. Isn't that a great challenge for a rainy day: Get a GPS and a day pass for the bus, and see who manages to stop at more stops.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '17, 16:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-57437" class="comments-container">
<span id="57438"></span>
<div id="comment-57438" class="comment">
<div id="post-57438-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Whilst it makes sense to ensure that the accuracy of imported data is as good as it can be, "delete it or fix it" isn't really the best option - OSM has always grown on the basis of step-by-step improvement (initial data, whether traced from old maps or GPS traces was often some distance out and later, more accurate sources of all kinds has helped to imrpove it.</p>
<p>The way that the NaPTAN bus stop data import was handled in the UK was to have a "naptan:verified" tag, initially set to "no". Other imports have had similar schemes.</p>
</div>
<div id="comment-57438-info" class="comment-info">
<span class="comment-age">(03 Aug '17, 16:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="57444"></span>
<div id="comment-57444" class="comment">
<div id="post-57444-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The data contains correct bus stop names and ref=* numbers. The latter could be used to easily import bus route relations later, which would enable planning bus trips using OSM data, even if the stops are inaccurate.</p>
</div>
<div id="comment-57444-info" class="comment-info">
<span class="comment-age">(03 Aug '17, 18:34)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
<span id="57450"></span>
<div id="comment-57450" class="comment">
<div id="post-57450-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would have thought Fix-me tags could encourage bus users to check them.</p>
</div>
<div id="comment-57450-info" class="comment-info">
<span class="comment-age">(03 Aug '17, 20:17)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-57437" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57437-form-container" class="comment-form-container">
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

