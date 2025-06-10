+++
type = "question"
title = "editing / deleting nodes in OSM.PBF file?"
description = '''Dear all, I am new to GIS. I am working with OSM.PBF files for a country, which I downloaded from geofabrik.de. I have a list of nodes, identified by their corresponding coordinates which I would like to remove from the file - basically these nodes correspond to roads and I want to measure travel ti...'''
date = "2019-01-29T13:54:00Z"
lastmod = "2019-01-30T06:57:00Z"
weight = 67783
keywords = [ "python", "nodes", "osm.pbf", "modify-node-tags" ]
aliases = [ "/questions/67783" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [editing / deleting nodes in OSM.PBF file?](/questions/67783/editing-deleting-nodes-in-osmpbf-file)

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
<span id="post-67783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67783-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear all,</p>
<p>I am new to GIS. I am working with OSM.PBF files for a country, which I downloaded from geofabrik.de. I have a list of nodes, identified by their corresponding coordinates which I would like to remove from the file - basically these nodes correspond to roads and I want to measure travel times for past periods, before these roads were build. If deleting nodes is too difficult, editing their tag to something like "avoid" should also do the trick. I would then like to save these edited files in OSM.PBF format (the program I am using in the next stage requires the files in this format).</p>
<p>Currently I am using Python to do this, but am a bit stuck. Would appreciate if somebody could point me to some samples of code editing tags of a node, or deleting nodes. Also, are there easier ways to do this than Python?</p>
<p>Thank you very much in advance! I can provide some more info if this is not very clear.</p>
<p>Ana</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-osm.pbf" rel="tag" title="see questions tagged &#39;osm.pbf&#39;">osm.pbf</span> <span class="post-tag tag-link-modify-node-tags" rel="tag" title="see questions tagged &#39;modify-node-tags&#39;">modify-node-tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jan '19, 13:54</strong></p>
<img src="https://secure.gravatar.com/avatar/a406e687bc2d2775701f124aff25369d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ana%20Moura&#39;s gravatar image" />
<p><span>Ana Moura</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ana Moura has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67783" class="comments-container">
&#10;</div>
<div id="comment-tools-67783" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67783-form-container" class="comment-form-container">
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

<span id="67784"></span>

<div id="answer-container-67784" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67784-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-67784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You cannot simply remove <em>nodes</em> as this would have undesirable consequences for the ways (roads) using these nodes. You will have to find the IDs of the <em>ways</em> you want to remove.</p>
<p>One possible option to remove certain ways from an .osm.pbf file is:</p>
<ul>
<li>use osmium-tool to convert the .osm.pbf into a .opl file which is a plain text file containing one line for each way</li>
<li>use a text editor to remove the lines corresponding to ways you do not want (or alternatively, you could also add something like maxspeed=1 or access=no to make your routing engine disregard these roads). The line corresponding to OSM way 1234 will beginn with "w1234"</li>
<li>again with osmium-tool, convert the modified .opl file back into .osm.pbf</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '19, 14:30</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jan '19, 14:36</strong> </span></p>
</div>
</div>
<div id="comments-container-67784" class="comments-container">
<span id="67788"></span>
<div id="comment-67788" class="comment">
<div id="post-67788-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much <a href="https://help.openstreetmap.org/users/104/frederik-ramm"></a><a href="https://help.openstreetmap.org/users/104/frederik-ramm">@Frederik Ramm</a>, that makes a lot of sense! I will try to implement it. Just one follow-up question: is there a smart way to go from node coordinates to way IDs? I collected all these nodes that I wanted to remove. I understand that instead I should remove the ways that they compose. These are identified by an OSM ID but it is not straightforward to me how to obtain the ID. Thanks again!</p>
</div>
<div id="comment-67788-info" class="comment-info">
<span class="comment-age">(29 Jan '19, 16:33)</span> <span class="comment-user userinfo">Ana Moura</span>
</div>
</div>
<span id="67789"></span>
<div id="comment-67789" class="comment">
<div id="post-67789-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In the .opl file, for each way there will be a list of all the nodes it uses. This list looks like so: <code>Nn1234,n2345,n3456</code> - so if you know you want to kick out the street that contains Node 12345, just use "grep" or your text editor's search function to identify the way that contains "n12345".</p>
</div>
<div id="comment-67789-info" class="comment-info">
<span class="comment-age">(29 Jan '19, 17:15)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="67806"></span>
<div id="comment-67806" class="comment">
<div id="post-67806-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Osmium also has the handy "osmium getparents" command which allows you, among other things, to find all ways referencing some nodes. Of course, if you know Python, you can also use PyOsmium to do these things. This example: <a href="https://github.com/osmcode/pyosmium/blob/master/examples/filter_coastlines.py">https://github.com/osmcode/pyosmium/blob/master/examples/filter_coastlines.py</a> should give you some hints.</p>
</div>
<div id="comment-67806-info" class="comment-info">
<span class="comment-age">(30 Jan '19, 06:57)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
</div>
<div id="comment-tools-67784" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67784-form-container" class="comment-form-container">
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

