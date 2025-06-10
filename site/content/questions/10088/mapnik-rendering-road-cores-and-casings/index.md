+++
type = "question"
title = "[closed] Mapnik - Rendering - Road Cores and Casings"
description = '''Hi, In short I&#x27;m wondering if someone would be able to have a look at the mapnik rule sheet on road widths, in regards to what I shall elaborate on. I have done about as much as I am able to do myself. On the Mapnik renders there are a few differences in the road widths which I would like to propose...'''
date = "2012-01-20T08:09:00Z"
lastmod = "2012-01-20T09:12:00Z"
weight = 10088
keywords = [ "roads", "rendering", "road", "renderer", "mapnik" ]
aliases = [ "/questions/10088" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Mapnik - Rendering - Road Cores and Casings](/questions/10088/mapnik-rendering-road-cores-and-casings)

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
<span id="post-10088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10088-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-10088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>In short I'm wondering if someone would be able to have a look at the mapnik rule sheet on road widths, in regards to what I shall elaborate on. I have done about as much as I am able to do myself.</p>
<p>On the Mapnik renders there are a few differences in the road widths which I would like to propose getting a bit of a tweaking. I haven't looked at the rulesheet itself for a couple of reasons, so I started by making a test area for the different zoom levels for the road combinations. (excluding _link being down the central line).</p>
<p>(all these links are having the underscore dropped after the last - because it seems to be the italic shortcut)</p>
<p><a href="http://wiki.openstreetmap.org/w/images/1/14/Core-Casing_-">http://wiki.openstreetmap.org/w/images/1/14/Core-Casing_-</a><em>Z13.png</em></p>
<p><em><a href="http://wiki.openstreetmap.org/w/images/0/02/Core-Casing">http://wiki.openstreetmap.org/w/images/0/02/Core-Casing</a></em>-<em>Z14.png</em></p>
<p><em><a href="http://wiki.openstreetmap.org/w/images/2/21/Core-Casing">http://wiki.openstreetmap.org/w/images/2/21/Core-Casing</a></em>-<em>Z15.png</em></p>
<p><em><a href="http://wiki.openstreetmap.org/w/images/e/e5/Core-Casing">http://wiki.openstreetmap.org/w/images/e/e5/Core-Casing</a></em>-<em>Z16.png</em></p>
<p><em><a href="http://wiki.openstreetmap.org/w/images/5/55/Core-Casing">http://wiki.openstreetmap.org/w/images/5/55/Core-Casing</a></em>-<em>Z17.png</em></p>
<p><em><a href="http://wiki.openstreetmap.org/w/images/4/40/Core-Casing">http://wiki.openstreetmap.org/w/images/4/40/Core-Casing</a></em>-_Z18.png</p>
<p>From this I have extracted estimations the core-casing values and put them here:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/User:Ben./MapnikRoads">http://wiki.openstreetmap.org/wiki/User:Ben./MapnikRoads</a></p>
<p>(These are estimates, so may not always be correct, but it makes it clear where the differences are)</p>
<p>So then I stuck them into this table: <a href="http://wiki.openstreetmap.org/w/images/0/02/Difference_in_Core-Casing.PNG">http://wiki.openstreetmap.org/w/images/0/02/Difference_in_Core-Casing.PNG</a></p>
<p>To evaluate:</p>
<p>The "motorway" and "motorway_link_" are the strangest as they are smaller than all but a few roads of lower status than them. Then from trunk to Secondary the roads are a fraction bigger than others, but more noticeable the casing is thinner. Thirdly the way they increase over zoom levels isn't smooth at times. Finally the order in which they render has <em>links</em> render very early, rather than just before there similarly named road (i.e. motorway_link to motorway).</p>
<p>The main issue with this is in flyover junctions where roads don't flow nicely into one another; but there are other reasons also.</p>
<p>In conclusion: The answer to this is a bit opinionated so there isn't really one, but the suggestion I would make is that either all roads bar maybe residential and service should be the same size with the same casing, maybe oneday having lanes= taken into consideration. Another option is to have all roads under and including tertiary as the same along with all _link roads being the same. Then all roads at secondary and above levels being steped up bigger. This section would be good to discuss though for the better idea.</p>
<p>cheers, Ben</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-renderer" rel="tag" title="see questions tagged &#39;renderer&#39;">renderer</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jan '12, 08:09</strong></p>
<img src="https://secure.gravatar.com/avatar/56455f550da19b500ce9750cdb822395?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ben&#39;s gravatar image" />
<p><span>Ben</span><br />
<span class="score" title="30 reputation points">30</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ben has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>20 Jan '12, 08:18</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-10088" class="comments-container">
&#10;</div>
<div id="comment-tools-10088" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10088-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Not a question" by Frederik Ramm 20 Jan '12, 08:18

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10089"></span>

<div id="answer-container-10089" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10089-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you are writing is not a question. You would like to have a discussion about the standard rendering style we have on <a href="http://www.openstreetmap.org">www.openstreetmap.org</a>. This site is not suitable for discussions; mailing lists are. I have taken the liberty of copying your post to <a href="http://lists.openstreetmap.org/listinfo/talk">our "talk" mailing list.</a> Here's a <a href="http://lists.openstreetmap.org/pipermail/talk/2012-January/061699.html">direct link to the article.</a></p>
<p>For concrete change requests (but this doesn't seem to be one yet), one could also use our <a href="http://trac.openstreetmap.org/">bug tracker</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jan '12, 08:17</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-10089" class="comments-container">
<span id="10091"></span>
<div id="comment-10091" class="comment">
<div id="post-10091-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, my mistake, cheers.</p>
</div>
<div id="comment-10091-info" class="comment-info">
<span class="comment-age">(20 Jan '12, 09:12)</span> <span class="comment-user userinfo">Ben</span>
</div>
</div>
</div>
<div id="comment-tools-10089" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10089-form-container" class="comment-form-container">
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

