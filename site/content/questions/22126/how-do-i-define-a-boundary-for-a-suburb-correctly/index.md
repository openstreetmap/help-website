+++
type = "question"
title = "How do I define a boundary for a suburb correctly?"
description = '''Hi everyone, I defined a boundary for the suburb I live in, because the current placement of suburb places in the map causes my street to be found in the wrong suburb. I did a multipolygon definition with the relevant ways in it and set the existing node for the suburb with the same name as label fo...'''
date = "2013-05-06T09:17:00Z"
lastmod = "2013-05-06T18:49:00Z"
weight = 22126
keywords = [ "suburb", "boundary", "definition" ]
aliases = [ "/questions/22126" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I define a boundary for a suburb correctly?](/questions/22126/how-do-i-define-a-boundary-for-a-suburb-correctly)

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
<span id="post-22126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22126-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>I defined a boundary for the suburb I live in, because the current placement of suburb places in the map causes my street to be found in the wrong suburb.</p>
<p>I did a multipolygon definition with the relevant ways in it and set the existing node for the suburb with the same name as label for the multipolygon.</p>
<p>However the multipolygon does not appear as the boundary for the suburb.</p>
<p>If I do a search for "Harleshausen" only the place-node is found not the boundary.</p>
<p>On the contrary if I do a search for "Prenzlauer Berg" there is a result for the place-node as well as for the boundary. I tried to do the definition of my suburb according to the settings used for the "Prenzlauer Berg".</p>
<p>Any hints how to get it right? What do I miss?</p>
<p>Regards, André</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-suburb" rel="tag" title="see questions tagged &#39;suburb&#39;">suburb</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-definition" rel="tag" title="see questions tagged &#39;definition&#39;">definition</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 May '13, 09:17</strong></p>
<img src="https://secure.gravatar.com/avatar/523637dce4fa7c1d5855d6c86bab14e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AnSc_de&#39;s gravatar image" />
<p><span>AnSc_de</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AnSc_de has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22126" class="comments-container">
&#10;</div>
<div id="comment-tools-22126" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22126-form-container" class="comment-form-container">
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

<span id="22137"></span>

<div id="answer-container-22137" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22137-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-22137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I assume that you are reffering to this boundary relation:</p>
<p><a href="http://www.openstreetmap.org/browse/relation/2911422">relation/2911422</a></p>
<p>In the moment when writing this answer, the geometry of the relation is broken. Click the link above to see it ... before someone other is repairing it ... you can see this if you are listed there as the last editor.</p>
<p>Solution: There are two positions where the minor suburb boundary ways meet the bigger boundaries. The bigger boundary ways have to be splitted at these points.</p>
<p>So all ways in the relation need to form a closed circle.</p>
<p>I really recommend to do that splitting and fixing of the relation in the offline editor JOSM, and not in the online editor Potlatch2 that you used so far. Search the OSM wiki for more details and help.</p>
<p>And be aware: the Nominatim database needs some days or hours to be synchronized with the main OSM database.</p>
<p>According to the tags of the relation: this is looking fine on the first view.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '13, 17:14</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-22137" class="comments-container">
<span id="22142"></span>
<div id="comment-22142" class="comment">
<div id="post-22142-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for pointing that out. I did not recognize the requirements for multipolygons from the wiki entry. I thought it enough that the path is closed not that the endpoints of two way must meet.</p>
</div>
<div id="comment-22142-info" class="comment-info">
<span class="comment-age">(06 May '13, 18:49)</span> <span class="comment-user userinfo">AnSc_de</span>
</div>
</div>
</div>
<div id="comment-tools-22137" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22137-form-container" class="comment-form-container">
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

