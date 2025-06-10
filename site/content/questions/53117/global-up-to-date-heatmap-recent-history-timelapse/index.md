+++
type = "question"
title = "Global up-to-date heatmap (recent history timelapse)"
description = '''Is there a website where one could see (say relatively up-to-date) global heatmap history of OSM edits? I would like to see if there are any trends in the locations being edited - maybe that edits are &quot;moving&quot; from the developed world (where most of the at least basic mapping is done already) to the...'''
date = "2016-11-25T11:07:00Z"
lastmod = "2019-06-22T17:26:00Z"
weight = 53117
keywords = [ "world", "heatmap" ]
aliases = [ "/questions/53117" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Global up-to-date heatmap (recent history timelapse)](/questions/53117/global-up-to-date-heatmap-recent-history-timelapse)

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
<span id="post-53117-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53117-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53117-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a website where one could see (say relatively up-to-date) global heatmap history of OSM edits? I would like to see if there are any trends in the locations being edited - maybe that edits are "moving" from the developed world (where most of the at least basic mapping is done already) to the developing world (Asia, Africa etc.). It would be nice to be able to track these stats.</p>
<p>I know it certainly would be possible to build such heatmap myself from the diffs, but I want to avoid this at first.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-world" rel="tag" title="see questions tagged &#39;world&#39;">world</span> <span class="post-tag tag-link-heatmap" rel="tag" title="see questions tagged &#39;heatmap&#39;">heatmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Nov '16, 11:07</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '16, 11:08</strong> </span></p>
</div>
</div>
<div id="comments-container-53117" class="comments-container">
&#10;</div>
<div id="comment-tools-53117" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53117-form-container" class="comment-form-container">
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

<span id="53119"></span>

<div id="answer-container-53119" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53119-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-53119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While the map you describe is certainly fun to look at, it won't actually answer the questions you are interested in. It would basically shows population density, with an emphasis on a small number of changesets with huge amounts of small changes.</p>
<p>A simple useful approach is looking at a site like <a href="http://www.missingmaps.org/osmstats/">missing maps osm stats</a> or <a href="http://osm-analytics.org/">osm analytics</a> , and see if the speed of mapping roads is increasing in the developing world.</p>
<p>As far as I've seen when looking at the data, even as the road network becomes complete in Europe, people keep working on them, adding ever more detail. So if you want to know if "mapping attention" is shifting, I think you'd be better of with a map of simply the number of changesets or the number of different contributors. Some goodies in that direction are in this <a href="http://mapbox.github.io/osm-analysis-collab/">Mapbox osm analysis lab</a>. A thorough study would also take into account population and size of the economy to relate mapping activity to mapable objects.</p>
<p>[EDIT] I think <a href="http://mapbox.github.io/osm-analysis-collab/users-by-country?yearIdx=0&amp;minActiveDays=10&amp;maxActiveDays=365&amp;#3.36/44.35/-21.29">this one</a> goes closest to what you're looking for. It tries to tell too many things at once IMHO. I've opened it in Germany for you. The red dots show an explosion of number of daily active users as soon as 2008, and then it basically stays more or less the same. In the second graph, the red dots are the number of people yearly working on roads. Similar profile. The number for 2016 is quite low, probably because of some lag in getting the data. Then look at buildings: a much smoother rise. Interesting to compare this to the explosion in <a href="http://mapbox.github.io/osm-analysis-collab/users-by-country?yearIdx=0&amp;minActiveDays=10&amp;maxActiveDays=365&amp;#2.27/21.47/-84.47">DR Congo from 2014</a>, ups and downs in <a href="http://mapbox.github.io/osm-analysis-collab/users-by-country?yearIdx=0&amp;minActiveDays=10&amp;maxActiveDays=365&amp;#3.36/20.01/-107.09">Haiti</a> or the steady-as-she-goes in <a href="http://mapbox.github.io/osm-analysis-collab/users-by-country?yearIdx=0&amp;minActiveDays=10&amp;maxActiveDays=365&amp;#3.36/2.12/-99.51">Peru</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '16, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '16, 17:31</strong> </span></p>
</div>
</div>
<div id="comments-container-53119" class="comments-container">
&#10;</div>
<div id="comment-tools-53119" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53119-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53118"></span>

<div id="answer-container-53118" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53118-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Itoworld has <a href="http://product.itoworld.com/map/group/20">various nice heatmaps</a> including for example <a href="http://product.itoworld.com/map/129">recent edits for the last 90 days</a>. It's a snapshot with a good-but-not-great update frequency.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '16, 12:03</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-53118" class="comments-container">
<span id="69702"></span>
<div id="comment-69702" class="comment">
<div id="post-69702-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That product is not available anymore.</p>
</div>
<div id="comment-69702-info" class="comment-info">
<span class="comment-age">(22 Jun '19, 17:26)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
</div>
<div id="comment-tools-53118" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53118-form-container" class="comment-form-container">
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

