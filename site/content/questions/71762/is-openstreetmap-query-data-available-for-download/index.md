+++
type = "question"
title = "Is openstreetmap query data available for download?"
description = '''I am going to use openstreetmap data for my masters thesis, and would like some real query data into the dataset if possible. Is this available anywhere? I tried to ask this earlier but after verifying my email, it seems that the question has disappeared, otherwise sorry for dupilcate questions.'''
date = "2019-11-21T14:48:00Z"
lastmod = "2019-11-21T20:43:00Z"
weight = 71762
keywords = [ "query", "data" ]
aliases = [ "/questions/71762" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is openstreetmap query data available for download?](/questions/71762/is-openstreetmap-query-data-available-for-download)

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
<span id="post-71762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71762-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am going to use openstreetmap data for my masters thesis, and would like some real query data into the dataset if possible. Is this available anywhere?</p>
<p>I tried to ask this earlier but after verifying my email, it seems that the question has disappeared, otherwise sorry for dupilcate questions.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '19, 14:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0fe1384c3f0740bd27d1ca9ee09433b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frederik3214&#39;s gravatar image" />
<p><span>frederik3214</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frederik3214 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71762" class="comments-container">
<span id="71763"></span>
<div id="comment-71763" class="comment">
<div id="post-71763-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What do you mean with "some real query data into the dataset" - are you saying you would like to know what people have typed into the search box on openstreetmap.org?</p>
</div>
<div id="comment-71763-info" class="comment-info">
<span class="comment-age">(21 Nov '19, 14:57)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="71764"></span>
<div id="comment-71764" class="comment">
<div id="post-71764-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes exactly</p>
</div>
<div id="comment-71764-info" class="comment-info">
<span class="comment-age">(21 Nov '19, 14:59)</span> <span class="comment-user userinfo">frederik3214</span>
</div>
</div>
</div>
<div id="comment-tools-71762" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71762-form-container" class="comment-form-container">
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

<span id="71766"></span>

<div id="answer-container-71766" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71766-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap data is free for anyone to download, any anyone can run their own search web site with OSM data without OSM ever getting to see their search terms. Those search terms that people enter on www.openstreetmap.org <em>are</em> accessible to the server operators (i.e. the OSM Foundation). This information is not publicly released because there are privacy considerations. Even if we strip away the IP numbers, certain search terms or a certain sequence of searches could reveal personal information.</p>
<p>The OSMF has considered releasing such data for research purposes like yours, however that would be contingent on there being a tool/script/method for anonymizing these access logs to a point where they can be given to people without incurring the risk of a privacy breach.</p>
<p>If you are interested in developing such a tool that anonymizes Apache logs, you could get in touch with our licensing working group to find out what would be required, and then try to implement that; if you succeed, then your tould could later be used to generate an anonymised data set that you are allowed to see. It is, however, not a quick path, and would only work if your masters thesis has enough time left to be completed...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '19, 20:43</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-71766" class="comments-container">
&#10;</div>
<div id="comment-tools-71766" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71766-form-container" class="comment-form-container">
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

