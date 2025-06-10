+++
type = "question"
title = "Attributes Order in OSM XML"
description = '''In OSM XML, are the attributes of the elements (node, way, nd) always presented in the same order? For example is it always the case that the attributes of element node come in this order: id=&quot;..&quot; lat=&quot;..&quot; lon=&quot;..&quot;'''
date = "2013-02-04T19:08:00Z"
lastmod = "2013-02-04T19:49:00Z"
weight = 19577
keywords = [ "xml", "attributes", "osm" ]
aliases = [ "/questions/19577" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Attributes Order in OSM XML](/questions/19577/attributes-order-in-osm-xml)

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
<span id="post-19577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19577-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In OSM XML, are the attributes of the elements (node, way, nd) always presented in the same order?</p>
<p>For example is it always the case that the attributes of element node come in this order: id=".." lat=".." lon=".."</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-attributes" rel="tag" title="see questions tagged &#39;attributes&#39;">attributes</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '13, 19:08</strong></p>
<img src="https://secure.gravatar.com/avatar/361e0b98020ca3f3d7db7baa2ec6c590?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sadeer&#39;s gravatar image" />
<p><span>Sadeer</span><br />
<span class="score" title="176 reputation points">176</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sadeer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19577" class="comments-container">
<span id="19579"></span>
<div id="comment-19579" class="comment">
<div id="post-19579-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(just in case you haven't already seen it):</p>
<p><a href="http://wiki.openstreetmap.org/wiki/XML#Assumptions">http://wiki.openstreetmap.org/wiki/XML#Assumptions</a></p>
</div>
<div id="comment-19579-info" class="comment-info">
<span class="comment-age">(04 Feb '13, 19:27)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="19580"></span>
<div id="comment-19580" class="comment">
<div id="post-19580-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I saw the assumptions sections but it didn't mention anything on the attributes order of an element.</p>
</div>
<div id="comment-19580-info" class="comment-info">
<span class="comment-age">(04 Feb '13, 19:49)</span> <span class="comment-user userinfo">Sadeer</span>
</div>
</div>
</div>
<div id="comment-tools-19577" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19577-form-container" class="comment-form-container">
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

<span id="19578"></span>

<div id="answer-container-19578" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19578-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19578-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-19578-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No. The rails port issues the attributes in a specific order but that is an implementation detail and not guaranteed. The /map call, the /node /way /relation calls, and the planet file are all produced by different pieces of software and might differ.</p>
<p>If you're doing some sort of quick hack though, you can assume that the order you get your attributes in today will still be the order you get your attributes in tomorrow. That assumption is probably right 99.9% of the time ;)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '13, 19:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-19578" class="comments-container">
&#10;</div>
<div id="comment-tools-19578" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19578-form-container" class="comment-form-container">
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

