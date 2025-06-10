+++
type = "question"
title = "Running generate_image gives &quot;features only present in Mapnik version 0.7.1&quot; error"
description = '''I&#x27;m getting this error...  &quot;RuntimeError: This map uses features only present in Mapnik version 0.7.1 and newer (in node Map)&quot; What does it mean?  I&#x27;ve just run osm2pgsql and it seemed to do it&#x27;s thing (populate the database, though I&#x27;m not sure what the best way to check that is) The error occurs w...'''
date = "2010-12-08T02:24:00Z"
lastmod = "2010-12-08T07:12:00Z"
weight = 1746
keywords = [ "generate_image", "mapnik" ]
aliases = [ "/questions/1746" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Running generate_image gives "features only present in Mapnik version 0.7.1" error](/questions/1746/running-generate_image-gives-features-only-present-in-mapnik-version-071-error)

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
<span id="post-1746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1746-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm getting this error...</p>
<p><strong>"RuntimeError: This map uses features only present in Mapnik version 0.7.1 and newer (in node Map)"</strong></p>
<p>What does it mean?</p>
<p>I've just run osm2pgsql and it seemed to do it's thing (populate the database, though I'm not sure what the best way to check that is) The error occurs when I run ./generate_image.py By "this map" I presume it means the data which I've just loaded into the DB.</p>
<p>So maybe I have a an osm2pgsql&lt;-&gt;Mapnik version mismatch. I'm on Mapnik v0.7.0 and osm2pgsql0.66</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-generate_image" rel="tag" title="see questions tagged &#39;generate_image&#39;">generate_image</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Dec '10, 02:24</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jan '11, 09:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-1746" class="comments-container">
&#10;</div>
<div id="comment-tools-1746" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1746-form-container" class="comment-form-container">
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

<span id="1747"></span>

<div id="answer-container-1747" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1747-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-1747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Harry Wood has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It has nothing to do with osm2pgsql - this is purely related to the osm.xml stylesheet. Basically the stylesheet maintainers have started using new Mapnik features that are only available in &gt;= Mapnik 0.7.1, and this is an error they intended to be triggered since your Mapnik version is not the latest. If you are not able to upgrade to mapnik 0.7.1 then you can remove the 'minimum_version' item at the top of the &lt;map ...=""&gt; and go on your way - you just may run into other errors or bugs due to lacking functionality in Mapnik 0.7.0 (most likely you will need to add 'width' and 'height' back to all symbolizers that read in png symbols).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Dec '10, 07:12</strong></p>
<img src="https://secure.gravatar.com/avatar/306ad1795ede4b32b0d57ac69c40429a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="springmeyer&#39;s gravatar image" />
<p><span>springmeyer</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="springmeyer has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-1747" class="comments-container">
&#10;</div>
<div id="comment-tools-1747" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1747-form-container" class="comment-form-container">
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

