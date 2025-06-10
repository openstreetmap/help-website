+++
type = "question"
title = "Wrong postcodes for Sheffield (UK)"
description = '''We are using OSM for our app but many of the postcodes are incorrect when used to find a location. The house number and street names are correct but the postcodes are wrong. Could anyone offer some advice on how to fix this?  Many thanks'''
date = "2020-10-27T13:16:00Z"
lastmod = "2020-10-27T14:07:00Z"
weight = 77268
keywords = [ "postcode", "postcodes" ]
aliases = [ "/questions/77268" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wrong postcodes for Sheffield (UK)](/questions/77268/wrong-postcodes-for-sheffield-uk)

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
<span id="post-77268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77268-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We are using OSM for our app but many of the postcodes are incorrect when used to find a location. The house number and street names are correct but the postcodes are wrong. Could anyone offer some advice on how to fix this?</p>
<p>Many thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span> <span class="post-tag tag-link-postcodes" rel="tag" title="see questions tagged &#39;postcodes&#39;">postcodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Oct '20, 13:16</strong></p>
<img src="https://secure.gravatar.com/avatar/588702335b1b44ea8457df894c6becd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joshua&#39;s gravatar image" />
<p><span>Joshua</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joshua has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77268" class="comments-container">
<span id="77269"></span>
<div id="comment-77269" class="comment">
<div id="post-77269-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Are you using raw OSM data (e.g. from a planet file) or using some intermediate service to access the address information? Could you link to a place on www.openstreetmap.org which got a wrong postcode?</p>
</div>
<div id="comment-77269-info" class="comment-info">
<span class="comment-age">(27 Oct '20, 13:49)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-77268" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77268-form-container" class="comment-form-container">
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

<span id="77270"></span>

<div id="answer-container-77270" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77270-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've zoomed in on Sheffield and</p>
<ol>
<li>Not all addresses are mapped</li>
<li>Not all the addresses that are mapped have postcodes</li>
</ol>
<p>Adding postcodes to existing addresses I find is most easily done by using <a href="https://wiki.openstreetmap.org/wiki/Ordnance_Survey_OpenData#CodePoint_Tiles">chillly's postcode layer</a> in JOSM. Some guesswork is involved, especially where there is more than one postcode shown on a single side of a street, but with practice I suspect you'll get over 99% accuracy (with no figures to back this up).</p>
<p>For completely missing addresses you'll need to go and collect the house numbers first, then determine the postcodes in the same way as described above.</p>
<p>When you say you are getting the wrong postcode, if you are only using OSM data then whatever is giving you a postcode is probably returning the nearest one that is mapped to the co-ordinates you're specifying. <a href="http://overpass-turbo.eu/s/Zrj">This Overpass query</a> shows how uneven the addr:postcode tag usage is in the area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '20, 14:07</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Oct '20, 14:08</strong> </span></p>
</div>
</div>
<div id="comments-container-77270" class="comments-container">
&#10;</div>
<div id="comment-tools-77270" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77270-form-container" class="comment-form-container">
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

