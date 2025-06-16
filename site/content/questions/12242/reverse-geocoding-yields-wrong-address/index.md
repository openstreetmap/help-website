+++
type = "question"
title = "Reverse geocoding yields wrong address"
description = '''I&#x27;m really new at this and can&#x27;t seem to find the way to change some wrong information. Here is an example of an address: 204, Jasper Ave, Diego Martin, POINT LISAS INDUSTERIAL ESTATE, Trinidad and Tobago There is an error, &quot;POINT LISAS INDUSTERIAL ESTATE&quot; is not supposed to be there. that is a plac...'''
date = "2012-04-21T17:58:00Z"
lastmod = "2012-04-21T18:44:00Z"
weight = 12242
keywords = [ "corrections", "nominatim", "errors", "removal" ]
aliases = [ "/questions/12242" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reverse geocoding yields wrong address](/questions/12242/reverse-geocoding-yields-wrong-address)

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
<span id="post-12242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12242-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm really new at this and can't seem to find the way to change some wrong information.</p>
<p>Here is an example of an address:</p>
<p>204, Jasper Ave, Diego Martin, POINT LISAS INDUSTERIAL ESTATE, Trinidad and Tobago</p>
<p>There is an error, "POINT LISAS INDUSTERIAL ESTATE" is not supposed to be there. that is a place (POI) and not a boundary or town. Someone obviously made a mistake.</p>
<p>Basically the address should read:</p>
<p>204, Jasper Ave, Diamond Vale, Diego Martin, Trinidad and Tobago</p>
<p>So my question is how do I remove that area or boundary "POINT LISAS INDUSTERIAL ESTATE" and how can I import the correct towns, cities etc as polygons?</p>
<p>Jai</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-corrections" rel="tag" title="see questions tagged &#39;corrections&#39;">corrections</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span> <span class="post-tag tag-link-removal" rel="tag" title="see questions tagged &#39;removal&#39;">removal</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Apr '12, 17:58</strong></p>
<img src="https://secure.gravatar.com/avatar/3ae310b7b9c595a1f01a5fea0dfa1069?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dejaiman&#39;s gravatar image" />
<p><span>dejaiman</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dejaiman has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Apr '12, 18:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-12242" class="comments-container">
&#10;</div>
<div id="comment-tools-12242" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12242-form-container" class="comment-form-container">
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

<span id="12243"></span>

<div id="answer-container-12243" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12243-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem in this case is that at one point in the past, "Point Lisas Industrial Estate" was tagged as a "region" which it clearly isn't. This has been fixed (<a href="https://www.openstreetmap.org/browse/node/1327431650/history)">https://www.openstreetmap.org/browse/node/1327431650/history)</a> but the geocoder hasn't caught up with that yet.</p>
<p>The general method to investigate such problems is to go to nominatim.openstreetmap.org, enter the address, and then in the results click on "detail"; this lists all components that were used in making up the result.</p>
<p>To answer your second question, about importing correct polygons: If you have to ask, then importing data is not for you. It is difficult for many different reasons and you can create a lot of harm with imports. There's an article about <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">Import Guidelines</a> on the wiki.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '12, 18:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-12243" class="comments-container">
<span id="12244"></span>
<div id="comment-12244" class="comment">
<div id="post-12244-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok kewl, thanks...</p>
</div>
<div id="comment-12244-info" class="comment-info">
<span class="comment-age">(21 Apr '12, 18:44)</span> <span class="comment-user userinfo">dejaiman</span>
</div>
</div>
</div>
<div id="comment-tools-12243" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12243-form-container" class="comment-form-container">
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

