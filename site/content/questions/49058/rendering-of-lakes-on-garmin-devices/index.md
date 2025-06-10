+++
type = "question"
title = "Rendering of lakes on Garmin devices"
description = '''I recently downloaded a map of the United Kingdom from http://garmin.openstreetmap.nl/ and installed it on an Etrex 30. I found that lakes and ponds (e.g. https://www.openstreetmap.org/#map=17/50.80484/-1.18653) do not render in blue as they used to. I also noticed that when the cursor is left on a ...'''
date = "2016-04-05T22:28:00Z"
lastmod = "2016-08-21T09:11:00Z"
weight = 49058
keywords = [ "rendering", "garmin", "lake" ]
aliases = [ "/questions/49058" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering of lakes on Garmin devices](/questions/49058/rendering-of-lakes-on-garmin-devices)

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
<span id="post-49058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49058-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently downloaded a map of the United Kingdom from <a href="http://garmin.openstreetmap.nl/">http://garmin.openstreetmap.nl/</a> and installed it on an Etrex 30. I found that lakes and ponds (e.g. <a href="https://www.openstreetmap.org/#map=17/50.80484/-1.18653)">https://www.openstreetmap.org/#map=17/50.80484/-1.18653)</a> do not render in blue as they used to. I also noticed that when the cursor is left on a blank area of the map, it is identified as 'Great Britain', which is also new behaviour. The same problem occurs on a Garmin Colorado, and occurs with much larger lakes (e.g. Windermere). A map downloaded from the same site in January renders correctly on Garmin devices, and the map still renders correctly on the OSM website. I asked a similar question a long while ago (<a href="https://help.openstreetmap.org/questions/12148/rendering-of-lakes),">https://help.openstreetmap.org/questions/12148/rendering-of-lakes),</a> and some helpful people told me about multipolygon relations, which fixed the problem. Has an entity called 'Great Britain' recently been created, and is the Garmin rendering engine seeing it as a kind of land use? Sorry, I'm guessing, but I cannot see how to fix the problem.</p>
<p>Additional information: While trying to determine whether the problem is in the OSM data, the preparation of the downloaded Garmin 'img' file or the Garmin GPS software, I found that the 'img' file renders correctly in BaseCamp. Unfortunately I do not know enough about map rendering to determine where the fault lies. Can anyone help?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span> <span class="post-tag tag-link-lake" rel="tag" title="see questions tagged &#39;lake&#39;">lake</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Apr '16, 22:28</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Apr '16, 11:25</strong> </span></p>
</div>
</div>
<div id="comments-container-49058" class="comments-container">
&#10;</div>
<div id="comment-tools-49058" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49058-form-container" class="comment-form-container">
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

<span id="49074"></span>

<div id="answer-container-49074" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49074-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, a 4598-member multipolygon relation (6038068) was created on March 9th for the entire landmass of Great Britain. I haven't linked directly to it here because most tools seem to be unable to display it due to its size.</p>
<p>The relation has the <code>place=island</code> tag, which is probably causing the behaviour you see. You can report this to Lambertus <a href="http://forum.openstreetmap.org/viewtopic.php?id=2625">here</a> and he may be able to make changes to his style to better accommodate <code>place=island</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Apr '16, 19:27</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-49074" class="comments-container">
<span id="49075"></span>
<div id="comment-49075" class="comment">
<div id="post-49075-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You could argue that it's full of errors because it's been created as a multipolygon with no inners :)</p>
<p>The creating changeset, for info, is this one:</p>
<p><a href="https://www.openstreetmap.org/changeset/37713755">https://www.openstreetmap.org/changeset/37713755</a></p>
<p>(you can link to that without problems). Currently the latest version of it is 6 and you can use something like:</p>
<p>wget <a href="http://openstreetmap.org/api/0.6/relation/6038068/6">http://openstreetmap.org/api/0.6/relation/6038068/6</a></p>
<p>to retrieve the XML of it.</p>
<p><a href="http://osm.mapki.com/history/relation.php?id=6038068">http://osm.mapki.com/history/relation.php?id=6038068</a></p>
<p>currently also works, provided that your browser supports large tables.</p>
</div>
<div id="comment-49075-info" class="comment-info">
<span class="comment-age">(06 Apr '16, 20:20)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="51583"></span>
<div id="comment-51583" class="comment">
<div id="post-51583-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>See <a href="https://lists.openstreetmap.org/pipermail/talk-gb/2016-August/thread.html#19100">https://lists.openstreetmap.org/pipermail/talk-gb/2016-August/thread.html#19100</a> for discussion on talk-gb about the relation.</p>
</div>
<div id="comment-51583-info" class="comment-info">
<span class="comment-age">(21 Aug '16, 09:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-49074" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49074-form-container" class="comment-form-container">
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

