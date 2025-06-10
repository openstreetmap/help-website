+++
type = "question"
title = "How to count playgrounds in Germany?"
description = '''Hello Everybody,  I would like to use openstreetmaps to create some statistics about playgrounds. Specifically I would like to know how many playgrounds there are in Germany and in Berlin. But I would also love to understand how to generally count specific tags in a specific area. Thanks a lot and e...'''
date = "2017-10-29T19:23:00Z"
lastmod = "2017-10-29T22:19:00Z"
weight = 60347
keywords = [ "statistics", "germany" ]
aliases = [ "/questions/60347" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to count playgrounds in Germany?](/questions/60347/how-to-count-playgrounds-in-germany)

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
<span id="post-60347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60347-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello Everybody,</p>
<p>I would like to use openstreetmaps to create some statistics about playgrounds. Specifically I would like to know how many playgrounds there are in Germany and in Berlin.</p>
<p>But I would also love to understand how to generally count specific tags in a specific area.</p>
<p>Thanks a lot and excuse me, if there is an easy anser - I haven't done much with Openstreetmaps yet.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-germany" rel="tag" title="see questions tagged &#39;germany&#39;">germany</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Oct '17, 19:23</strong></p>
<img src="https://secure.gravatar.com/avatar/45595c1dc12c38e542fc5a3a78c4a606?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JannesPeters&#39;s gravatar image" />
<p><span>JannesPeters</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JannesPeters has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Oct '17, 06:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-60347" class="comments-container">
&#10;</div>
<div id="comment-tools-60347" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60347-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="60350"></span>

<div id="answer-container-60350" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60350-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-60350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JannesPeters has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One could use Overpass. This <a href="http://overpass-turbo.eu/s/sFJ">query</a> counts the number of playgrounds in Berlin. You could replace Berlin with Germany. Please note that because we export the count, the playgrounds are not displayed on the map. You have to look at the "data" tab after executing the query.</p>
<p>The <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Count_Pharmacies_per_County_.28updated_0.7.54.29">Overpass documentation</a> has an example to count the number of Pharmacies per county.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Oct '17, 19:40</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-60350" class="comments-container">
<span id="60354"></span>
<div id="comment-60354" class="comment">
<div id="post-60354-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>just a quick question. Here is the result for germany. What is the difference between "@count" and "@count:nodes"?</p>
<p>@count: 84743 @count:nodes: 28559 55812 @count:ways: 372 @count:relations</p>
</div>
<div id="comment-60354-info" class="comment-info">
<span class="comment-age">(29 Oct '17, 19:54)</span> <span class="comment-user userinfo">JannesPeters</span>
</div>
</div>
<span id="60356"></span>
<div id="comment-60356" class="comment">
<div id="post-60356-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Playgrounds can be represented as a point or area, "count" returns all the representations, "count:nodes" returns just the point features. More at <a href="http://wiki.openstreetmap.org/wiki/Elements">http://wiki.openstreetmap.org/wiki/Elements</a>.</p>
</div>
<div id="comment-60356-info" class="comment-info">
<span class="comment-age">(29 Oct '17, 20:43)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="60357"></span>
<div id="comment-60357" class="comment">
<div id="post-60357-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Naturally there could be some double counting (playgrounds mapped as an area and as a node), but I suspect (from spot checking the data) that this is likely to be minimal.</p>
</div>
<div id="comment-60357-info" class="comment-info">
<span class="comment-age">(29 Oct '17, 22:16)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="60358"></span>
<div id="comment-60358" class="comment">
<div id="post-60358-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The other thing to note, is that "kindergarten" is a fairly fuzzy concept (in general not just OSM). For example the Austrian variant would clearly include non-educational childcare on the other hand in Germany and Switzerland it would be more of a pre-school facility.</p>
</div>
<div id="comment-60358-info" class="comment-info">
<span class="comment-age">(29 Oct '17, 22:19)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-60350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60350-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60349"></span>

<div id="answer-container-60349" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60349-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Go to <a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a> start the wizard and enter "leisure=playground in Germany" (without the quotes), build the query and set the timeout to 240 up from the standard 25 (that allows the query to run for a maximum of 240 seconds).</p>
<p>Note the query is fairly slow and returns a lot of data, probably best to start with Berlin (leisure=playground in Berlin").</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Oct '17, 19:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Oct '17, 19:48</strong> </span></p>
</div>
</div>
<div id="comments-container-60349" class="comments-container">
&#10;</div>
<div id="comment-tools-60349" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60349-form-container" class="comment-form-container">
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

