+++
type = "question"
title = "how to  only get nodes on real roads way via overpass  api"
description = '''as the title shows, I want to get the OSM nodes data, which are on roads.  For roads, we can define it as the Way feature as highway tag. (I found this tip from a previous post).  How to do that?  EDIT; find the solution by myself:  way[highway](50.7460,7.170,50.7461,7.171);node(w); the above query ...'''
date = "2018-11-19T10:16:00Z"
lastmod = "2018-11-20T07:01:00Z"
weight = 66846
keywords = [ "roads", "overpass" ]
aliases = [ "/questions/66846" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to only get nodes on real roads way via overpass api](/questions/66846/how-to-only-get-nodes-on-real-roads-way-via-overpass-api)

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
<span id="post-66846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66846-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>as the title shows, I want to get the OSM nodes data, which are on roads.<br />
For roads, we can define it as the Way feature as <code>highway</code> tag. (I found this tip from a previous post).<br />
How to do that?</p>
<p>EDIT; find the solution by myself:<br />
<code>way[highway](50.7460,7.170,50.7461,7.171);node(w);</code></p>
<p>the above query will output the all the nodes on the ways tagged as highway and within the bounding box. The key part is <code>node(w)</code>. For more information, you can go to this osm wiki:<br />
<a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Nov '18, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/64c2be0cc81b8f9cb09fbba97b907938?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris%20Bao&#39;s gravatar image" />
<p><span>Chris Bao</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris Bao has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Nov '18, 02:55</strong> </span></p>
</div>
</div>
<div id="comments-container-66846" class="comments-container">
<span id="66861"></span>
<div id="comment-66861" class="comment">
<div id="post-66861-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you figured it out yourself then write it as an <em>answer</em> :)</p>
</div>
<div id="comment-66861-info" class="comment-info">
<span class="comment-age">(20 Nov '18, 07:01)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66846" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66846-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

