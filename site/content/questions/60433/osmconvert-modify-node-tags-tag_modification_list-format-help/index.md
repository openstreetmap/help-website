+++
type = "question"
title = "osmconvert modify-node-tags TAG_MODIFICATION_LIST format help"
description = '''Hello all, I have a problem when trying to modify the column headers of my osm.pbf file when using osmconvert. I am trying to change the &#x27;osm_id&#x27; to &#x27;FCODE&#x27;. I think I have the syntax correct, but am honestly unsure. All the documentation I find online keeps repeating the information in the wiki whi...'''
date = "2017-11-02T14:42:00Z"
lastmod = "2017-11-21T22:12:00Z"
weight = 60433
keywords = [ "osmconvert", "modify-node-tags" ]
aliases = [ "/questions/60433" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [osmconvert modify-node-tags TAG_MODIFICATION_LIST format help](/questions/60433/osmconvert-modify-node-tags-tag_modification_list-format-help)

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
<span id="post-60433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60433-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all,</p>
<p>I have a problem when trying to modify the column headers of my osm.pbf file when using osmconvert. I am trying to change the 'osm_id' to 'FCODE'. I think I have the syntax correct, but am honestly unsure. All the documentation I find online keeps repeating the information in the wiki which is not that helpful. This is the line of code where I try to accomplish that:</p>
<pre><code>osmconvert64.exe new_syria.osm.pbf --modify-node-tags=&quot;osm_id=536143307 to FCODE=536143307&quot; -o=new_syria_mapped.osm.pbf</code></pre>
<p>The example from the wiki is as follows:</p>
<pre><code>./osmconvert a.o5m --modify-node-tags=&quot;amenity=fire_hydrant to emergency=fire_hydrant&quot; -o=new_hydrant_syntax.o5m</code></pre>
<p>Any help would be greatly appreciated.</p>
<p>Thanks,</p>
<p>Zach</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-modify-node-tags" rel="tag" title="see questions tagged &#39;modify-node-tags&#39;">modify-node-tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Nov '17, 14:42</strong></p>
<img src="https://secure.gravatar.com/avatar/f0b26c2cf40adafb59cf431dc55df117?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zach%20Moose&#39;s gravatar image" />
<p><span>Zach Moose</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zach Moose has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60433" class="comments-container">
&#10;</div>
<div id="comment-tools-60433" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60433-form-container" class="comment-form-container">
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

<span id="60735"></span>

<div id="answer-container-60735" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60735-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Zach Moose has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello Zach,</p>
<p>the <em>--modify-tags</em> option is meant for tags only. Are you sure there are tags with the key "osm_id" in your data? It looks to me as you would try to rename the object ids of OSM datasets. However object ids do not have names, the are just numbers which identify objects within the OSM data world (nodes, ways, relations).</p>
<p>It usually does not make much sense to add an object id as tag. All what you get is redundant information. What do you need it for? What is the subsequent process?</p>
<p>Greetings, Markus</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '17, 21:08</strong></p>
<img src="https://secure.gravatar.com/avatar/3b5b4abfedd46928c7cd0d5cbf907ed3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marqqs&#39;s gravatar image" />
<p><span>Marqqs</span><br />
<span class="score" title="448 reputation points">448</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marqqs has 2 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-60735" class="comments-container">
<span id="60736"></span>
<div id="comment-60736" class="comment">
<div id="post-60736-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Markus,</p>
<p>Thank you for your response. I should have closed this answer as I figured out what I needed to do. I was in fact editing column names of the data. I accomplished this by loading the data into a Postgis database, manipulating the column names and attributes and then using the ogr2ogr tool to convert to shapefile.</p>
<p>Thank you for your input and clarification on tags.</p>
<p>Zach</p>
</div>
<div id="comment-60736-info" class="comment-info">
<span class="comment-age">(21 Nov '17, 22:12)</span> <span class="comment-user userinfo">Zach Moose</span>
</div>
</div>
</div>
<div id="comment-tools-60735" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60735-form-container" class="comment-form-container">
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

