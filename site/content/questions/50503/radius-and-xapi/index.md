+++
type = "question"
title = "radius and xapi"
description = '''Hi, how can I use radius with xapi in overpass-api? thanks'''
date = "2016-06-28T13:33:00Z"
lastmod = "2016-06-28T13:40:00Z"
weight = 50503
keywords = [ "radius" ]
aliases = [ "/questions/50503" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [radius and xapi](/questions/50503/radius-and-xapi)

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
<span id="post-50503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50503-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>how can I use radius with xapi in overpass-api?</p>
<p>thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-radius" rel="tag" title="see questions tagged &#39;radius&#39;">radius</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '16, 13:33</strong></p>
<img src="https://secure.gravatar.com/avatar/122eea6c5b91fa9a90ad61ff6057049f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OuedraogoMichel&#39;s gravatar image" />
<p><span>OuedraogoMichel</span><br />
<span class="score" title="14 reputation points">14</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OuedraogoMichel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50503" class="comments-container">
&#10;</div>
<div id="comment-tools-50503" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50503-form-container" class="comment-form-container">
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

<span id="50504"></span>

<div id="answer-container-50504" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50504-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-50504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm afraid, XAPI doesn't support radius. XAPI is quite a dated query langugage and only covers a very small subset of what is otherwise possible with Overpass QL or XML.</p>
<p>For an example using <code>around</code> in Overpass QL ("Find all cinemas in Bonn which are at most 100m away from bus stops"), please take a look at the documentation on the OSM wiki: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Relative_to_other_elements_.28around.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Relative_to_other_elements_.28around.29</a></p>
<p>BTW: To migrate your old XAPI queries to current Overpass QL, you can leverage the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/XAPI_Compatibility_Layer#Migrating_from_XAPI_Compatibility_Layer_to_Overpass_XML_.2F_QL">migration guide</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jun '16, 13:40</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jun '16, 13:43</strong> </span></p>
</div>
</div>
<div id="comments-container-50504" class="comments-container">
&#10;</div>
<div id="comment-tools-50504" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50504-form-container" class="comment-form-container">
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

