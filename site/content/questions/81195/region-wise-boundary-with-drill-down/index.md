+++
type = "question"
title = "Region wise boundary with drill down"
description = '''Hi, Hope all are doing well. Can someone please let me know following functionalities can be implemented using Openstreetmap ? 1- want to show only one state (suppose Maharastra in Inda), not complete map.  2- Show all districts of that state (Maharastra) with boundaries  3- Show regions (Blocks of ...'''
date = "2021-08-04T12:17:00Z"
lastmod = "2021-08-04T16:06:00Z"
weight = 81195
keywords = [ "drilldown" ]
aliases = [ "/questions/81195" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Region wise boundary with drill down](/questions/81195/region-wise-boundary-with-drill-down)

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
<span id="post-81195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81195-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Hope all are doing well. Can someone please let me know following functionalities can be implemented using Openstreetmap ?</p>
<p>1- want to show only one state (suppose Maharastra in Inda), not complete map. 2- Show all districts of that state (Maharastra) with boundaries 3- Show regions (Blocks of district) on click on specific district</p>
<p>If doable then please share any sample, API or help manual for implementation.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-drilldown" rel="tag" title="see questions tagged &#39;drilldown&#39;">drilldown</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Aug '21, 12:17</strong></p>
<img src="https://secure.gravatar.com/avatar/370407edaee250db11e4bead7a068425?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JaydevJangid&#39;s gravatar image" />
<p><span>JaydevJangid</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JaydevJangid has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81195" class="comments-container">
&#10;</div>
<div id="comment-tools-81195" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81195-form-container" class="comment-form-container">
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

<span id="81200"></span>

<div id="answer-container-81200" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81200-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>For 1, it's tricky, but <a href="https://wiki.openstreetmap.org/wiki/UMap">UMap</a> allows to restrict the map view to some bounding box. To really display only the state, and blank tiles otherwise, you'll have to create your own rendering stack AFAIK.</p>
<p>This <a href="http://overpass-turbo.eu/s/1a0Z">overpass query</a> will display all the districts (admin_level=5) of Maharastra, this resolves 2.</p>
<p>And you can load the result of overpass queries in UMap, to combine 1 and 2. Either dynamically, but the load on the server is high and the data should not change often, or statically, you export the data from overpass turbo, and import it as a layer in UMap.</p>
<p>But for 3, I don't see the regions in the <a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative#10_admin_level_values_for_specific_countries">list of admin_levels for India</a>, so I don't think they exists in OSM.</p>
<p>Hope this helps. Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Aug '21, 16:06</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-81200" class="comments-container">
&#10;</div>
<div id="comment-tools-81200" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81200-form-container" class="comment-form-container">
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

