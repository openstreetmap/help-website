+++
type = "question"
title = "How does OSM know an address that is not mapped?"
description = '''I want to add the address values for some houses I am adding in my neighborhood, but the addresses already show up when I search for them. How does OSM know where these unmapped places are? Also, how does it know where neighborhoods that are not explicitly marked are? When I add the tags for address...'''
date = "2014-09-04T02:46:00Z"
lastmod = "2014-09-04T03:55:00Z"
weight = 36571
keywords = [ "conflicts", "addressing", "search", "tagging", "address" ]
aliases = [ "/questions/36571" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How does OSM know an address that is not mapped?](/questions/36571/how-does-osm-know-an-address-that-is-not-mapped)

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
<span id="post-36571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36571-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to add the address values for some houses I am adding in my neighborhood, but the addresses already show up when I search for them. How does OSM know where these unmapped places are? Also, how does it know where neighborhoods that are not explicitly marked are?</p>
<p>When I add the tags for addresses, will OSM automatically recognize that the new address is better (it is), or do I need to do something to <code>help</code> it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-conflicts" rel="tag" title="see questions tagged &#39;conflicts&#39;">conflicts</span> <span class="post-tag tag-link-addressing" rel="tag" title="see questions tagged &#39;addressing&#39;">addressing</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '14, 02:46</strong></p>
<img src="https://secure.gravatar.com/avatar/eb91b1e453fe246b3781c55172f92df3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iansan5653&#39;s gravatar image" />
<p><span>iansan5653</span><br />
<span class="score" title="191 reputation points">191</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iansan5653 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36571" class="comments-container">
&#10;</div>
<div id="comment-tools-36571" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36571-form-container" class="comment-form-container">
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

<span id="36577"></span>

<div id="answer-container-36577" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36577-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-36577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The search function on the <a href="http://www.openstreetmap.org/">http://www.openstreetmap.org/</a> map page uses Nominatim. In addition the OSM data, Nominatim is loaded with information from other databases. If Nominatim does not find a result in the OSM data it looks at those other databases. So it is likely that your search is turning up data from another database.</p>
<p>If you add the address information to OSM it should show up first in the search function and, better yet from my point of view, will be available for "off line" searching with other software like OsmAnd.</p>
<p>So please add your locally gathered neighborhood address information to OSM, it will improve the data. And thanks for doing that!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '14, 03:55</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-36577" class="comments-container">
&#10;</div>
<div id="comment-tools-36577" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36577-form-container" class="comment-form-container">
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

