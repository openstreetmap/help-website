+++
type = "question"
title = "How to deal with &#x27;Way terminates on area&quot; errors?"
description = '''I&#x27;m fairly new to OSM editing so I&#x27;m asking this question to make sure I&#x27;m not mucking anything up. I&#x27;ve been using JOSM to edit the maps around my locality, but one thing I&#x27;ve noticed is that there are a LOT of validation errors about &quot;Way terminates on area&quot;. Basically I&#x27;d like to know how to rect...'''
date = "2012-02-22T13:15:00Z"
lastmod = "2012-02-22T14:11:00Z"
weight = 10723
keywords = [ "josm", "area", "terminates", "way", "on" ]
aliases = [ "/questions/10723" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to deal with 'Way terminates on area" errors?](/questions/10723/how-to-deal-with-way-terminates-on-area-errors)

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
<span id="post-10723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10723-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-10723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm fairly new to OSM editing so I'm asking this question to make sure I'm not mucking anything up. I've been using JOSM to edit the maps around my locality, but one thing I've noticed is that there are a LOT of validation errors about "Way terminates on area".</p>
<p>Basically I'd like to know how to rectify these, and how to prevent my own additions to the map(s) resulting in the same problem?</p>
<p>Any assistance would be greatly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span> <span class="post-tag tag-link-terminates" rel="tag" title="see questions tagged &#39;terminates&#39;">terminates</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-on" rel="tag" title="see questions tagged &#39;on&#39;">on</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Feb '12, 13:15</strong></p>
<img src="https://secure.gravatar.com/avatar/aead0057665a20dd19043461ff05789b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BinaryAxis&#39;s gravatar image" />
<p><span>BinaryAxis</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BinaryAxis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-10723" class="comments-container">
<span id="10728"></span>
<div id="comment-10728" class="comment">
<div id="post-10728-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>One thing that might be useful here would be a link to the area where you're seeing this. With that link, people may be able to advise whether JOSM's crying wolf, complaining correctly, or complaining about the wrong issue altogether.</p>
</div>
<div id="comment-10728-info" class="comment-info">
<span class="comment-age">(22 Feb '12, 13:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-10723" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10723-form-container" class="comment-form-container">
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

<span id="10724"></span>

<div id="answer-container-10724" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10724-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-10724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As a general rule, JOSM just tries to highlight things that might be a problem, and it is often fully ok to ignore them.</p>
<p>For example, a street terminating in a pedestrian area or a similar area is perfectly ok, as is a river terminating in a lake. What you should try and avoid is the connection of dissimilar object types - a footpath that leads up to the lake shore should perhaps not be connected to the lake. If you feel that JOSM is complaining too much, you can switch off certain checks via the preferences panel, or you can report it as a bug on <a href="http://josm.openstreetmap.de/.">http://josm.openstreetmap.de/.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '12, 13:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-10724" class="comments-container">
<span id="10726"></span>
<div id="comment-10726" class="comment">
<div id="post-10726-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ah right I see. The problem I've been having is that a lot of areas have been designated as 'Residential' by other users, but they are encapsulated between streets / ways. If you then try to connect a footpath (for example), to the street you end up getting this annoying error!</p>
<p>The only reason it concerned me is because I don't want footpaths essentially connecting to NOTHING, and effectively just being floating ways.</p>
</div>
<div id="comment-10726-info" class="comment-info">
<span class="comment-age">(22 Feb '12, 13:28)</span> <span class="comment-user userinfo">BinaryAxis</span>
</div>
</div>
<span id="10729"></span>
<div id="comment-10729" class="comment">
<div id="post-10729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have seen this at the junction of two highways but where the junction node is also shared by a residential or other landuse area. If it looks OK, I just ignore it (and hope someone fixes JOSM soon.)</p>
</div>
<div id="comment-10729-info" class="comment-info">
<span class="comment-age">(22 Feb '12, 14:11)</span> <span class="comment-user userinfo">srbrook</span>
</div>
</div>
</div>
<div id="comment-tools-10724" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10724-form-container" class="comment-form-container">
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

