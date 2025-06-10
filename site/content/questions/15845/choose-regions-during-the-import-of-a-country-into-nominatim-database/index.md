+++
type = "question"
title = "Choose regions during the import of a country into nominatim database."
description = '''Hi! Is there any possibility to have an overview during the import of an osm file (./utils/update.php --import-file germany.osm)? Which regions/nodes/relations are imported? What I want to do: to import only some regions from germany, which are near the border with the Netherlands. But I do not what...'''
date = "2012-09-06T14:03:00Z"
lastmod = "2012-09-07T10:03:00Z"
weight = 15845
keywords = [ "regions", "import", "nominatim" ]
aliases = [ "/questions/15845" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Choose regions during the import of a country into nominatim database.](/questions/15845/choose-regions-during-the-import-of-a-country-into-nominatim-database)

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
<span id="post-15845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15845-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>Is there any possibility to have an overview during the import of an osm file (./utils/update.php --import-file germany.osm)? Which regions/nodes/relations are imported?</p>
<p>What I want to do: to import only some regions from germany, which are near the border with the Netherlands. But I do not what to import every regions one after another (like bavaria.osm), because I know that are available to download like this. I have to use the hole germany.osm and from this file, during the import, to choose which regions I need and which not.</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-regions" rel="tag" title="see questions tagged &#39;regions&#39;">regions</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '12, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/2f496486f3d04cfe5b6d1d8ce9b660af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RoxanaO&#39;s gravatar image" />
<p><span>RoxanaO</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RoxanaO has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15845" class="comments-container">
&#10;</div>
<div id="comment-tools-15845" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15845-form-container" class="comment-form-container">
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

<span id="15878"></span>

<div id="answer-container-15878" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15878-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I found the solution. Using the JOSM program, I selected the needed bounding box (which included the wanted regions), got the minlon, minlat, maxlon, maxlat. With this in update.php I added to the command from line 226: --bbox minlon,minlat,maxlon,maxlat</p>
<p>Ex: <code>$sCMD = CONST_Osm2pgsql_Binary.' --bbox 5.5480957,50.6738352,9.140625,53.8265967 -klas -C 2000 -O gazetteer -d '.$aDSNInfo['database'].' '.$sTemporaryFile;</code></p>
<p>And then use the command: <code>./utils/update.php --import-file /media/9804A73C04A71BEE/OSMnominatim/pbf/germany.osm </code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '12, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/2f496486f3d04cfe5b6d1d8ce9b660af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RoxanaO&#39;s gravatar image" />
<p><span>RoxanaO</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RoxanaO has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Sep '12, 10:03</strong> </span></p>
</div>
</div>
<div id="comments-container-15878" class="comments-container">
&#10;</div>
<div id="comment-tools-15878" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15878-form-container" class="comment-form-container">
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

