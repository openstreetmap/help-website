+++
type = "question"
title = "Geometries from Python osmnx"
description = '''Hello everyone. I am interested in downloading all the toll_booth nodes from Italy regions. On Python Jupyter, I am using the osmnx library. Specifically, I am using tags = {&#x27;barrier&#x27;: &#x27;toll_booth&#x27;} toll = ox.geometries_from_polygon(italy_prj.geometry[reg_index], tags)  where italy_prj.geometry[reg_...'''
date = "2023-05-22T10:47:00Z"
lastmod = "2023-05-22T11:37:00Z"
weight = 87290
keywords = [ "toll_booths" ]
aliases = [ "/questions/87290" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Geometries from Python osmnx](/questions/87290/geometries-from-python-osmnx)

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
<span id="post-87290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87290-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone.</p>
<p>I am interested in downloading all the toll_booth nodes from Italy regions.</p>
<p>On Python Jupyter, I am using the osmnx library. Specifically, I am using</p>
<pre><code>tags = {&#39;barrier&#39;: &#39;toll_booth&#39;}
toll = ox.geometries_from_polygon(italy_prj.geometry[reg_index], tags)</code></pre>
<p>where <em>italy_prj.geometry[reg_index]</em> is the shapefile of the region of which I am downloading data.</p>
<p>Now, I added myself the tag barrier:toll_booth to the node 8933486721 (Name: Casello di Ceparana), because it was not present in the map.</p>
<p>If I use the before mentioned code, the node cannot be found among the barrier:tool_booth tagged elements. However, if i use</p>
<pre><code>tags = {&#39;name&#39;: &#39;Casello di Ceparana&#39;}</code></pre>
<p>then the node is found, with barrier:tool_booth among its tags!</p>
<p>Can someone tell me what am I doing wrong?</p>
<p>Thanks a lot,</p>
<p>Luca</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-toll_booths" rel="tag" title="see questions tagged &#39;toll_booths&#39;">toll_booths</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 May '23, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/90cd8d74b6a8e5aa73796594d279ad27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LucaMinzoni&#39;s gravatar image" />
<p><span>LucaMinzoni</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LucaMinzoni has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87290" class="comments-container">
<span id="87291"></span>
<div id="comment-87291" class="comment">
<div id="post-87291-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>On IRC, someone with the <em>exact same problem</em> said "If i download the node using its name, i can see the tag barrier:toll_booth as well! That's why i don't understand why that tag is not working to download the node...."</p>
<p>I said there "sounds like an issue with osmnx..."</p>
</div>
<div id="comment-87291-info" class="comment-info">
<span class="comment-age">(22 May '23, 11:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="87292"></span>
<div id="comment-87292" class="comment">
<div id="post-87292-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you check whether the shapefile actually contains your changes, i.e. is it recent enough? If so, please create a bug report for osmnx as suggested by <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>.</p>
</div>
<div id="comment-87292-info" class="comment-info">
<span class="comment-age">(22 May '23, 11:33)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="87293"></span>
<div id="comment-87293" class="comment">
<div id="post-87293-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> it was me indeed ahah <a href="https://help.openstreetmap.org/users/158/scai">@scai</a> the shapefiles are the official ones from Italian government, and using the same files I can retrieve the point by using it's name, and I fail to do that using the barrier tag</p>
</div>
<div id="comment-87293-info" class="comment-info">
<span class="comment-age">(22 May '23, 11:37)</span> <span class="comment-user userinfo">LucaMinzoni</span>
</div>
</div>
</div>
<div id="comment-tools-87290" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87290-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

