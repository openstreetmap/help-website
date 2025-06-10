+++
type = "question"
title = "[closed] Build Nominatim service upon local-osm-tiles-server"
description = '''Hey, I have already a working instance of osm-tiles-server on Ubuntu (full planet already been imported and indexed). Is there a way that Nominatim will use this data? Or shall I re-import the same planet-osm using the Nominatim tool again? Thanks! Nir'''
date = "2015-03-22T12:58:00Z"
lastmod = "2015-03-22T13:22:00Z"
weight = 41844
keywords = [ "local-tile-server", "nominatim" ]
aliases = [ "/questions/41844" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] Build Nominatim service upon local-osm-tiles-server](/questions/41844/build-nominatim-service-upon-local-osm-tiles-server)

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
<span id="post-41844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41844-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey, I have already a working instance of osm-tiles-server on Ubuntu (full planet already been imported and indexed). Is there a way that Nominatim will use this data? Or shall I re-import the same planet-osm using the Nominatim tool again?</p>
<p>Thanks! Nir</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-local-tile-server" rel="tag" title="see questions tagged &#39;local-tile-server&#39;">local-tile-server</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Mar '15, 12:58</strong></p>
<img src="https://secure.gravatar.com/avatar/6baeac6eaec0495b46facbe28aafac46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arvivn&#39;s gravatar image" />
<p><span>arvivn</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arvivn has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>22 Mar '15, 14:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-41844" class="comments-container">
&#10;</div>
<div id="comment-tools-41844" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41844-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is answered, right answer was accepted" by SimonPoole 22 Mar '15, 14:29

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41845"></span>

<div id="answer-container-41845" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41845-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="arvivn has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unluckily the answer is: yes you need to import to the nominatim schema separately.</p>
<p>In the future there may be ways to share common tables and potentially do it all in one go, but currently this is not possible (except if you write the necessary code naturally).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '15, 13:22</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Mar '15, 13:22</strong> </span></p>
</div>
</div>
<div id="comments-container-41845" class="comments-container">
&#10;</div>
<div id="comment-tools-41845" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41845-form-container" class="comment-form-container">
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

