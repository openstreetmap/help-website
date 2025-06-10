+++
type = "question"
title = "Remove a label from local OSM server map"
description = '''I am running a local OSM server I made with osm2pgsql. I would like to remove the &quot;Hudson Bay&quot; label from the map. I understand I would have to re render the tiles but that is okay. Can it just be removed in the postgres database? Could you guys point me in the right direction?  Thanks! :) '''
date = "2019-10-22T15:09:00Z"
lastmod = "2019-10-23T21:41:00Z"
weight = 71263
keywords = [ "local-tile-server", "labels", "postgresql", "osm2pgsql", "osm" ]
aliases = [ "/questions/71263" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Remove a label from local OSM server map](/questions/71263/remove-a-label-from-local-osm-server-map)

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
<span id="post-71263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71263-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am running a local OSM server I made with osm2pgsql. I would like to remove the "Hudson Bay" label from the map. I understand I would have to re render the tiles but that is okay. Can it just be removed in the postgres database? Could you guys point me in the right direction?</p>
<p>Thanks! :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-local-tile-server" rel="tag" title="see questions tagged &#39;local-tile-server&#39;">local-tile-server</span> <span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '19, 15:09</strong></p>
<img src="https://secure.gravatar.com/avatar/c586e65837086d3f4993593ef9d723fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LakesKeegan&#39;s gravatar image" />
<p><span>LakesKeegan</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LakesKeegan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71263" class="comments-container">
&#10;</div>
<div id="comment-tools-71263" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71263-form-container" class="comment-form-container">
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

<span id="71269"></span>

<div id="answer-container-71269" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71269-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="LakesKeegan has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are not updating the server automatically you can simply find the relevant object and null the name field.</p>
<p>Note that there seem to be multiple objects with the name and you will likely have to repeat this for all of them.</p>
<p>For the main multipolygon with id 9441240 you should be able to find entries in the planet_osm_polygon table, you will need to check for -9441240 too.</p>
<p>If you are updating your database, this can still be done, but you will need to add triggers to remove the name automatically if somebody edits the object (or you could simply do it manually if the name returns).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '19, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-71269" class="comments-container">
<span id="71278"></span>
<div id="comment-71278" class="comment">
<div id="post-71278-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can't seem to find where the label is coming from, is it just the "Name" column in the database? Would the Hstore data make any difference?</p>
</div>
<div id="comment-71278-info" class="comment-info">
<span class="comment-age">(23 Oct '19, 15:15)</span> <span class="comment-user userinfo">LakesKeegan</span>
</div>
</div>
<span id="71281"></span>
<div id="comment-71281" class="comment">
<div id="post-71281-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It is very well possible as I said that there multiple objects with the name. I don't believe that osm-carto uses hstore at all for names. I'll run a quick check on my database and report back.</p>
</div>
<div id="comment-71281-info" class="comment-info">
<span class="comment-age">(23 Oct '19, 16:03)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="71282"></span>
<div id="comment-71282" class="comment">
<div id="post-71282-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you!</p>
</div>
<div id="comment-71282-info" class="comment-info">
<span class="comment-age">(23 Oct '19, 16:33)</span> <span class="comment-user userinfo">LakesKeegan</span>
</div>
</div>
<span id="71283"></span>
<div id="comment-71283" class="comment">
<div id="post-71283-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>planet_osm_point 305640293 that doesn't seem to be rendered</p>
<p>planet_osm_ polygon -9441240 and maybe 518434801, 518425097 seems as there has just been some editing on the objects so YMMV</p>
</div>
<div id="comment-71283-info" class="comment-info">
<span class="comment-age">(23 Oct '19, 16:53)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="71284"></span>
<div id="comment-71284" class="comment not_top_scorer">
<div id="post-71284-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Am I able to just delete 305640293 or is that a bad idea?</p>
</div>
<div id="comment-71284-info" class="comment-info">
<span class="comment-age">(23 Oct '19, 16:57)</span> <span class="comment-user userinfo">LakesKeegan</span>
</div>
</div>
<span id="71286"></span>
<div id="comment-71286" class="comment not_top_scorer">
<div id="post-71286-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't think anybody uses it for anything, and as said it isn't rendered anyway.</p>
</div>
<div id="comment-71286-info" class="comment-info">
<span class="comment-age">(23 Oct '19, 17:14)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="71288"></span>
<div id="comment-71288" class="comment not_top_scorer">
<div id="post-71288-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I set the polygon names to null and deleted the point, the label is still showing up. Do you have any other ideas? Thanks again for your help.</p>
</div>
<div id="comment-71288-info" class="comment-info">
<span class="comment-age">(23 Oct '19, 18:01)</span> <span class="comment-user userinfo">LakesKeegan</span>
</div>
</div>
<span id="71289"></span>
<div id="comment-71289" class="comment not_top_scorer">
<div id="post-71289-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you sure that the tiles have been regenerated? the low zoom tiles typically are not dynamically rendered.</p>
</div>
<div id="comment-71289-info" class="comment-info">
<span class="comment-age">(23 Oct '19, 18:44)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="71291"></span>
<div id="comment-71291" class="comment">
<div id="post-71291-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Turns out they didn't finish rendering, the label is removed. Thanks for your help!</p>
</div>
<div id="comment-71291-info" class="comment-info">
<span class="comment-age">(23 Oct '19, 21:41)</span> <span class="comment-user userinfo">LakesKeegan</span>
</div>
</div>
</div>
<div id="comment-tools-71269" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-71269-form-container" class="comment-form-container">
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

