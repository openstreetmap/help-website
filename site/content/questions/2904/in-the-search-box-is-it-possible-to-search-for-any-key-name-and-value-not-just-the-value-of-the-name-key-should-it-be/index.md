+++
type = "question"
title = "In the Search box, is it possible to search for any key name and value, not just the value of the &quot;Name&quot; key? Should it be?"
description = '''Sort of like TagInfo, but limited to - and mapped to - the currently viewable box? I am aware of the XAPI + JOSM solution, but I want it easy. (I don&#x27;t currently use JOSM, and I am not crazy about composing the query string by hand, including the box coordinates.)'''
date = "2011-02-10T19:38:00Z"
lastmod = "2011-02-10T21:42:00Z"
weight = 2904
keywords = [ "search" ]
aliases = [ "/questions/2904" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [In the Search box, is it possible to search for any key name and value, not just the value of the "Name" key? Should it be?](/questions/2904/in-the-search-box-is-it-possible-to-search-for-any-key-name-and-value-not-just-the-value-of-the-name-key-should-it-be)

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
<span id="post-2904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2904-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Sort of like TagInfo, but limited to - and mapped to - the currently viewable box?</p>
<p>I am aware of the XAPI + JOSM solution, but I want it easy. (I don't currently use JOSM, and I am not crazy about composing the query string by hand, including the box coordinates.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '11, 19:38</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Feb '11, 19:38</strong> </span></p>
</div>
</div>
<div id="comments-container-2904" class="comments-container">
&#10;</div>
<div id="comment-tools-2904" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2904-form-container" class="comment-form-container">
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

<span id="2913"></span>

<div id="answer-container-2913" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2913-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ponzu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Simple answer: No, this is not possible. That is not really the purpose of the search box on the main page.</p>
<p>Though the search box does use some other tags as well as the name, eg to see what kind of object it is. And you can search for something like "pub in Glasgow", and it will find anything within Glasgow that is tagged as amenity=pub. For more details, see the wiki page for <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a>, which is the search tool.</p>
<p>If you do what to search for a particular key or value, then the best option is probably to use JOSM. You can just use JOSM to pick an area from the map, then download the osm data. Then use the "Find" tool to select the objects you want.</p>
<p>You don't necessarily have to use the XAPI for this, unless you want to search tags over a larger area (ie more than you can download in JOSM at once).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '11, 21:42</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-2913" class="comments-container">
&#10;</div>
<div id="comment-tools-2913" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2913-form-container" class="comment-form-container">
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

