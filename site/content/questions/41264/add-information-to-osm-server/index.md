+++
type = "question"
title = "add information to OSM server"
description = '''Hey guys, I actually new in OSM, but I have a problem. I have installed my own OSM server with OSRM, but I want to add some information to my OSM data. I would like to add information like hole information, traffic light information, can you guys help me how to solve this problem? '''
date = "2015-02-23T08:42:00Z"
lastmod = "2015-02-24T10:59:00Z"
weight = 41264
keywords = [ "information" ]
aliases = [ "/questions/41264" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [add information to OSM server](/questions/41264/add-information-to-osm-server)

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
<span id="post-41264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41264-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey guys, I actually new in OSM, but I have a problem. I have installed my own OSM server with OSRM, but I want to add some information to my OSM data. I would like to add information like hole information, traffic light information, can you guys help me how to solve this problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-information" rel="tag" title="see questions tagged &#39;information&#39;">information</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Feb '15, 08:42</strong></p>
<img src="https://secure.gravatar.com/avatar/4f0240d7bfc05f7087e8a1e084392d81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="louis_perdana&#39;s gravatar image" />
<p><span>louis_perdana</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="louis_perdana has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41264" class="comments-container">
<span id="41275"></span>
<div id="comment-41275" class="comment">
<div id="post-41275-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please Louis_Perdana specify your question "hole information", "traffic light information" import our your own data ? Import onto your own server or the OSM server ?</p>
</div>
<div id="comment-41275-info" class="comment-info">
<span class="comment-age">(23 Feb '15, 11:26)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-41264" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41264-form-container" class="comment-form-container">
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

<span id="41311"></span>

<div id="answer-container-41311" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41311-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While not totally impossible this is at least difficult.</p>
<p>You need to add the data to the osm data -before- you import it into OSRM. One way to do this is to edit the data with JOSM (this assumes that we are talking about a small to very small extract of OSM). Depending on how picky OSRM is you then might need to convert the resulting <a href="http://wiki.openstreetmap.org/wiki/JOSM_file_format">JOSM format OSM data</a> with negative ids, to regular OSM format (aka renumbering and throwing away some JOSM specific attributes).</p>
<p>The far simpler solution would be to add your data directly to OSM if it is useful, real and available on terms that allow it to be included in OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '15, 10:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '15, 11:05</strong> </span></p>
</div>
</div>
<div id="comments-container-41311" class="comments-container">
&#10;</div>
<div id="comment-tools-41311" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41311-form-container" class="comment-form-container">
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

