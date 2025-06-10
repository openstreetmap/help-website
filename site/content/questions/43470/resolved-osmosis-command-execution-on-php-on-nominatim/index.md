+++
type = "question"
title = "[RESOLVED] Osmosis command execution on PHP on Nominatim"
description = '''Hello. I&#x27;m trying to do a numeration address system for my Nominatim, since my country doenst have TIGER and the most commons numeration methods available. The system works fine, but when I include it in a plugins/ folder on Nominatim, he stops generating xml files with nodes from a PBF file. Everyt...'''
date = "2015-06-08T16:59:00Z"
lastmod = "2015-06-09T17:09:00Z"
weight = 43470
keywords = [ "apache", "nominatim", "pbf", "osmosis", "php" ]
aliases = [ "/questions/43470" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[RESOLVED\] Osmosis command execution on PHP on Nominatim](/questions/43470/resolved-osmosis-command-execution-on-php-on-nominatim)

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
<span id="post-43470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43470-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello.</p>
<p>I'm trying to do a numeration address system for my Nominatim, since my country doenst have TIGER and the most commons numeration methods available.</p>
<p>The system works fine, but when I include it in a plugins/ folder on Nominatim, he stops generating xml files with nodes from a PBF file. Everything works with in the command line. Only stops in the search.php request.</p>
<p>The output says it works: Jun 08, 2015 12:40:21 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Osmosis Version 0.43.1 Jun 08, 2015 12:40:21 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Preparing pipeline. Jun 08, 2015 12:40:22 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Launching pipeline execution. Jun 08, 2015 12:40:22 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Pipeline executing, waiting for completion. Jun 08, 2015 12:40:26 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Pipeline complete. Jun 08, 2015 12:40:26 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Total execution time: 4935 milliseconds.</p>
<p>The command I use is:</p>
<p>$cmd = CONST_Osmosis_Binary . " --read-pbf-fast " . <strong>PBFFILE</strong> . " --way-key keyList=name --way-key-value keyValueList=\"name." . trim($address[0]) . "\" --tag-filter reject-relations --used-node --write-xml " . <strong>DATA</strong> . "/data.xml 2&gt;&amp;1";</p>
<p>$output = shell_exec($cmd);</p>
<p>where <strong>PBFFILE</strong> is the absolute path to my pbf and <strong>DATA</strong> is the folder inside my plugin, also absolute and $address[0] is the streetname string.</p>
<p>I'm using apache as my server, on ubuntu 14.04, and all the folders and files are with the same permissions. (I've changed the default apache server user and group)</p>
<p>I know that this might be a apache or php problem, but i preferred to ask in here since i could receive a more specific awnser due to this be OSM projects.</p>
<p>Thank you very much.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '15, 16:59</strong></p>
<img src="https://secure.gravatar.com/avatar/55dc79063504ee084f40f4e6c0dd91a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yury%20Tinos&#39;s gravatar image" />
<p><span>Yury Tinos</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yury Tinos has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jun '15, 17:09</strong> </span></p>
</div>
</div>
<div id="comments-container-43470" class="comments-container">
&#10;</div>
<div id="comment-tools-43470" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43470-form-container" class="comment-form-container">
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

<span id="43494"></span>

<div id="answer-container-43494" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43494-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Resolved!!!!</p>
<p>My PHP was UTF-8, but the command line execution functions where in ANSI, so just had to add LANG=\"en_US.UTF8\" in front of my command and it worked.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jun '15, 17:09</strong></p>
<img src="https://secure.gravatar.com/avatar/55dc79063504ee084f40f4e6c0dd91a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yury%20Tinos&#39;s gravatar image" />
<p><span>Yury Tinos</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yury Tinos has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-43494" class="comments-container">
&#10;</div>
<div id="comment-tools-43494" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43494-form-container" class="comment-form-container">
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

