+++
type = "question"
title = "How to add the village for an address ?"
description = '''How can I add the village for an address? I did not found any tag for the &quot;village&quot; information. Should I complete only the &quot;addr:full&quot; tag ? Or should I use the &quot;is_in&quot; tag and specify as value the name of the village ?'''
date = "2011-08-04T10:24:00Z"
lastmod = "2011-08-04T12:30:00Z"
weight = 6866
keywords = [ "mapping", "address" ]
aliases = [ "/questions/6866" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to add the village for an address ?](/questions/6866/how-to-add-the-village-for-an-address)

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
<span id="post-6866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6866-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-6866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I add the village for an address? I did not found any tag for the "village" information. Should I complete only the "addr:full" tag ? Or should I use the "is_in" tag and specify as value the name of the village ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Aug '11, 10:24</strong></p>
<img src="https://secure.gravatar.com/avatar/069927bbc93795a141934dac42486fe3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jBeata&#39;s gravatar image" />
<p><span>jBeata</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jBeata has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-6866" class="comments-container">
&#10;</div>
<div id="comment-tools-6866" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6866-form-container" class="comment-form-container">
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

<span id="6871"></span>

<div id="answer-container-6871" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6871-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Addresses are provided by the <a href="https://wiki.openstreetmap.org/wiki/Addr">addr tag</a>. You can use <em>addr:city</em> to specify the city the address belongs to. When searching for an address, OSM's search function (currently provided by <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a>) also considers nearby <a href="https://wiki.openstreetmap.org/wiki/Place">place tag</a>s to determine in which city, suburb and so on an address is. The <a href="https://wiki.openstreetmap.org/wiki/Key:is_in">is_in tag</a> is usually only added to place tags and may support Nominatim and other search engines in their decisions. On the <a href="https://wiki.openstreetmap.org/wiki/Addr">addr tag</a> page there is also a tag called <em>addr:hamlet</em> but I don't know if Nominatim (or others) support it.</p>
<p>A strange thing I noticed about Nominatim is that it often adds addresses belonging to a city to small villages instead that are much further away than the place node of the city. This seems like a bug to me.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Aug '11, 11:53</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-6871" class="comments-container">
<span id="6872"></span>
<div id="comment-6872" class="comment">
<div id="post-6872-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Place tags can also be an area (relation or closed way) instead of a simple node. This is probably the best way to tag things (adding is_in or addr tags everywhere doesn't scale, and using a node is too approximate), although some tools might not take advantage of this (I do believe nominatim and mkgmap work correctly, at least).</p>
</div>
<div id="comment-6872-info" class="comment-info">
<span class="comment-age">(04 Aug '11, 12:21)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="6873"></span>
<div id="comment-6873" class="comment">
<div id="post-6873-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes thats correct, but adding a (not too rough) area for a village isn't as simple as adding a single node. Most places are still mapped as nodes.</p>
</div>
<div id="comment-6873-info" class="comment-info">
<span class="comment-age">(04 Aug '11, 12:30)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-6871" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6871-form-container" class="comment-form-container">
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

