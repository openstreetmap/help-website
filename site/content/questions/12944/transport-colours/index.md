+++
type = "question"
title = "Transport colours"
description = '''Are there any renderers that will display the Transport relation colours as specified in the tag, instead of making all bus relations red, all subways another colour, etc. ? Are there are plans to implement and render the colours as specified in transport relations&#x27; tags in the OSM main Transport Ma...'''
date = "2012-05-25T02:03:00Z"
lastmod = "2014-01-02T23:44:00Z"
weight = 12944
keywords = [ "public-transport", "transport" ]
aliases = [ "/questions/12944" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Transport colours](/questions/12944/transport-colours)

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
<span id="post-12944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12944-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-12944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Are there any renderers that will display the Transport relation colours as specified in the tag, instead of making all bus relations red, all subways another colour, etc. ?</p>
<p>Are there are plans to implement and render the colours as specified in transport relations' tags in the OSM main Transport Map view on the homepage?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-transport" rel="tag" title="see questions tagged &#39;transport&#39;">transport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '12, 02:03</strong></p>
<img src="https://secure.gravatar.com/avatar/36cd6183f159eaf98709ea755e67ed50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brandon_macuser&#39;s gravatar image" />
<p><span>brandon_macuser</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brandon_macuser has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12944" class="comments-container">
&#10;</div>
<div id="comment-tools-12944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12944-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="29493"></span>

<div id="answer-container-29493" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29493-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-29493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'll answer the second part of the question, since I've been asked a few times about it.</p>
<p>There are three issues with supporting route colours:</p>
<ul>
<li>There's currently no support within mapnik for taking line colours from the database. This is the main reason that it's not done at the moment, since without this support I would need to write a separate rule for every possible colour! There is ongoing work on this in mapnik, so perhaps it will be possible in 2014. See <a href="https://github.com/mapnik/mapnik/issues/828">#828</a> and the expr-v2 branch in the code.</li>
<li>It's likely to make the map a complete mess of nasty colours! The people who design route diagrams work in isolation from one another, and even within one transport area often choose lurid and clashing colours for the routes.</li>
<li>I haven't figured out how to show the colours of overlapping routes in an automated fashion.</li>
</ul>
<p>Each issue has a solution, namely:</p>
<ul>
<li>Patience, since things seem to be progressing with mapnik!</li>
<li>I'm considering approaches to showing the colours beyond just changing the line colour, so that it's useful to viewers without overwhelming them, and also to providing different versions of the transport layer for different sites.</li>
<li>This still needs an automated approach figuring out! Yvecai currently creates <a href="http://www.opensnowmap.org/?zoom=14&amp;lat=46.80676&amp;lon=6.33372">good results</a> on opensnowmap, but that's by manually choosing the line offsets for every overlapping ski route. With things like buses - there are 14 different routes at my nearest stop - I don't think that this approach is yet a complete solution.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Dec '13, 13:52</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-29493" class="comments-container">
<span id="29558"></span>
<div id="comment-29558" class="comment">
<div id="post-29558-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<ul>
<li>With Opensnowmap, I also had useful results using markers (small colored rectangles along the ways). Having ways side by side as it is now on Opensnowmap needs manual adjustments. Even with this manual work, some cases are not entirely satisfactory given the ways geometry.</li>
<li>Also, I need to decrease the color 'luma' for a nice rendering. For instance, yellow pistes are barely noticeable on a white background without.</li>
</ul>
<p>Pistes coloring code for opensnowmap can be found here: <a href="https://github.com/yvecai/mapnik-opensnowmap.org/blob/master/offset-style/build-relations-style.py">https://github.com/yvecai/mapnik-opensnowmap.org/blob/master/offset-style/build-relations-style.py</a></p>
</div>
<div id="comment-29558-info" class="comment-info">
<span class="comment-age">(02 Jan '14, 23:44)</span> <span class="comment-user userinfo">yvecai</span>
</div>
</div>
</div>
<div id="comment-tools-29493" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29493-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12945"></span>

<div id="answer-container-12945" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12945-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-12945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is AIUI no plan for (Andy Allan's) Transport Map on the front page to do so. Other renderers which show transport information include <a href="http://www.öpnvkarte.de/">öpnvkarte</a> and <a href="http://www.openstreetbrowser.org/">OpenStreetBrowser</a> but I don't believe either of those do.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '12, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 May '12, 10:41</strong> </span></p>
</div>
</div>
<div id="comments-container-12945" class="comments-container">
&#10;</div>
<div id="comment-tools-12945" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12945-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29468"></span>

<div id="answer-container-29468" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29468-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I found OSMTransport (<a href="http://demo.3liz.com/osmtransport/)">http://demo.3liz.com/osmtransport/)</a> which displays route colors for a limited number of cities.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '13, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a2f19e3a960bbc861e85b69c9c13a8e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pbb&#39;s gravatar image" />
<p><span>pbb</span><br />
<span class="score" title="621 reputation points">621</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pbb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29468" class="comments-container">
&#10;</div>
<div id="comment-tools-29468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29468-form-container" class="comment-form-container">
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

