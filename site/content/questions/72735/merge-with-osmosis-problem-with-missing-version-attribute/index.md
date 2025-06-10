+++
type = "question"
title = "Merge with Osmosis: problem with missing version attribute"
description = '''I want to merge two osm files (a certain area and the corresponding contour lines). The purpose is to create a combined osm file to be further processed with mkgmap. Situation The first file is a regular osm file coming from Overpass Turbo (with Meta attributes). The second was originally an shp fil...'''
date = "2020-01-28T11:47:00Z"
lastmod = "2020-01-28T21:06:00Z"
weight = 72735
keywords = [ "merge", "version", "osmosis", "attribute" ]
aliases = [ "/questions/72735" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Merge with Osmosis: problem with missing version attribute](/questions/72735/merge-with-osmosis-problem-with-missing-version-attribute)

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
<span id="post-72735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72735-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to merge two osm files (a certain area and the corresponding contour lines). The purpose is to create a combined osm file to be further processed with mkgmap.</p>
<p>Situation The first file is a regular osm file coming from Overpass Turbo (with Meta attributes). The second was originally an shp file with contour lines of the same area, coming from a cartographic server of my region. I opened it in JOSM with the plugin OpenData and saved it as osm. Correctly, JOSM creates id's for each object, but not a "Version" attribute.</p>
<p>Problem I want to merge both files using a command line program under Windows. I tried with Osmosis, but it fails because of the missing Version attributes in the second file. Any suggestion on how to force JOSM to produce Version attributes or to convince Osmosis to ignore the missing attributes?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-attribute" rel="tag" title="see questions tagged &#39;attribute&#39;">attribute</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jan '20, 11:47</strong></p>
<img src="https://secure.gravatar.com/avatar/5caa28ca253794e166c1ad85f15bdb45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stenan&#39;s gravatar image" />
<p><span>stenan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stenan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72735" class="comments-container">
&#10;</div>
<div id="comment-tools-72735" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72735-form-container" class="comment-form-container">
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

<span id="72737"></span>

<div id="answer-container-72737" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72737-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would try to open both files in JOSM and merge the layers with it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '20, 13:34</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-72737" class="comments-container">
<span id="72741"></span>
<div id="comment-72741" class="comment">
<div id="post-72741-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, but this is not the idea. Maybe I should add a bit of context. I'm a hiking guide. Every time I explore a new hike, I want to have a fresh Garmin map for the area. Of course, paths change frequently, but contour lines don't. Thus, the process should look like this:</p>
<ul>
<li>I prepare just one time a big osm file with contour lines for the whole mountain area.</li>
<li>I prepare some scripts to run on the command line (on Windows), where the only parameter I have to change every time is the bounding box related to the small area which includes my new hike. Before every hike, I just want to run the scripts and produce quickly and with a semi-automated process a fresh Garmin map, ready to install. The scripts should do the following, in sequence:</li>
</ul>
<p>A. launch wget to download an up-to-date osm file related to the small area of my interest B. launch osmconvert to cut the big osm file with the contour lines along the same bounding box C. launch osmosis (or similar) to merge the two osm files D. launch mkgmap to produce the map using a proper style sheet</p>
<p>Point C is where I'm stuck because of the missing Version attributes. All the rest works well.</p>
<p>Thanks</p>
</div>
<div id="comment-72741-info" class="comment-info">
<span class="comment-age">(28 Jan '20, 16:04)</span> <span class="comment-user userinfo">stenan</span>
</div>
</div>
<span id="72743"></span>
<div id="comment-72743" class="comment">
<div id="post-72743-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think you can fake version ids with osmconvert, see --fake-version here <a href="http://manpages.ubuntu.com/manpages/trusty/man1/osmconvert.1.html">http://manpages.ubuntu.com/manpages/trusty/man1/osmconvert.1.html</a></p>
</div>
<div id="comment-72743-info" class="comment-info">
<span class="comment-age">(28 Jan '20, 20:32)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="72744"></span>
<div id="comment-72744" class="comment">
<div id="post-72744-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Right, sorry I did not pay enough attention to the stance "command line program under Windows."</p>
<p>I was going to suggest osmium, as I've read it's much more flexible than osmosis, but I don't see any windows version.</p>
<p>As .osm is just xml, I think it should be quite easy to add a dummy Version attribute (put "1" everywhere). I would use sed, but if don't already have cygwin, it will be complicated. But search and replace tools must exists for windows.</p>
<p>You might also find an xml tool for windows commandline.</p>
<p>Regards.</p>
</div>
<div id="comment-72744-info" class="comment-info">
<span class="comment-age">(28 Jan '20, 21:06)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-72737" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72737-form-container" class="comment-form-container">
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

