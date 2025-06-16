+++
type = "question"
title = "Osmosis: Filter for certain ways and nodes"
description = '''Hi I want to filter the map of Denmark downloaded from Geofabrik. What I would like are the following ways: highway.motorway,highway.motorway_link,highway.trunk,highway.trunk_link,highway.primary,highway.primary_link,highway.secondary,highway.unclassified,highway.tertiary  And also, I&#x27;d like the fol...'''
date = "2014-02-23T10:21:00Z"
lastmod = "2014-02-23T18:44:00Z"
weight = 30952
keywords = [ "filter", "pipeline", "osm", "osmosis" ]
aliases = [ "/questions/30952" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Osmosis: Filter for certain ways and nodes](/questions/30952/osmosis-filter-for-certain-ways-and-nodes)

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
<span id="post-30952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30952-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I want to filter the map of Denmark downloaded from Geofabrik.</p>
<p>What I would like are the following ways:</p>
<pre><code>highway.motorway,highway.motorway_link,highway.trunk,highway.trunk_link,highway.primary,highway.primary_link,highway.secondary,highway.unclassified,highway.tertiary</code></pre>
<p>And also, I'd like the following nodes:</p>
<pre><code>amenity.fuel</code></pre>
<p>I've been trying using the filter options in osmosis using the following setup created in OSMembrane:</p>
<pre><code>osmosis.bat ^
--read-pbf file=Dropbox/Documents/P6/Data/denmark-latest.osm.pbf outPipe.0=1 ^
--tee 2 inPipe.0=1 outPipe.0=2 outPipe.1=3 ^
--way-key-value keyValueList=highway.motorway,highway.motorway_link,highway.trunk,highway.trunk_link,highway.primary,highway.primary_link,highway.secondary,highway.unclassified,highway.tertiary inPipe.0=2 outPipe.0=4 ^
--node-key-value keyValueList=amenity.fuel inPipe.0=3 outPipe.0=5 ^
--merge inPipe.0=5 inPipe.1=4 outPipe.0=6 ^
--write-xml file=Dropbox/Documents/P6/Data/Output.osm.xml inPipe.0=6</code></pre>
<p>However, when I run this, osmosis start, but never finishes. When I look in my Windows Task Manager, it looks the the task is not even running at all. No CPU is being used. It just stays at the state "INFO: Pipeline executing, waiting for completion.".</p>
<p>Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-pipeline" rel="tag" title="see questions tagged &#39;pipeline&#39;">pipeline</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Feb '14, 10:21</strong></p>
<img src="https://secure.gravatar.com/avatar/dfcabe6e9dc22b3ccdbc2561b3af4834?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="A_Strandfelt&#39;s gravatar image" />
<p><span>A_Strandfelt</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="A_Strandfelt has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Feb '14, 10:22</strong> </span></p>
</div>
</div>
<div id="comments-container-30952" class="comments-container">
&#10;</div>
<div id="comment-tools-30952" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30952-form-container" class="comment-form-container">
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

<span id="30953"></span>

<div id="answer-container-30953" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30953-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="A_Strandfelt has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Read the <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#--tag-filter_.28--tf.29">Osmosis wiki page for the --tag-filter option</a> which explains the deadlock problem. You are not using --tag-filter but the issue is the same.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Feb '14, 11:00</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-30953" class="comments-container">
<span id="30955"></span>
<div id="comment-30955" class="comment">
<div id="post-30955-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks. I tried using the structure from the suggested example and replaced them with my code. However, I now get an exception: "The following named pipes (nodes, ways) and 0 default pipes have not been terminated with appropriate output sinks.". The setup can be seen here: <a href="http://pastebin.com/Gm4J20XB">http://pastebin.com/Gm4J20XB</a></p>
<p>Do I need to make it wait for the tasks to be completed before merging or something? If so, how?</p>
</div>
<div id="comment-30955-info" class="comment-info">
<span class="comment-age">(23 Feb '14, 11:42)</span> <span class="comment-user userinfo">A_Strandfelt</span>
</div>
</div>
<span id="30963"></span>
<div id="comment-30963" class="comment">
<div id="post-30963-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your command looks all right but I am not familiar with the caret character at the end of line; if this means "line continues" then the empty line (newline) just before --merge might be the problem since the shell believes that the command terminates there.</p>
</div>
<div id="comment-30963-info" class="comment-info">
<span class="comment-age">(23 Feb '14, 18:44)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30953" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30953-form-container" class="comment-form-container">
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

