+++
type = "question"
title = "Extracting country specific data."
description = '''Hi, Is there any way to extract nodes from only a certain country. I&#x27;ve used XAPI to do this but that uses a bounding box [bbox]. This is OK but suppose I only want nodes from the UK and not the Republic of Ireland. In this case the square bbox will inevitably rope in Republic of Ireland nodes when ...'''
date = "2011-03-09T09:57:00Z"
lastmod = "2011-03-09T15:31:00Z"
weight = 3646
keywords = [ "xapi", "extract", "bbox", "country" ]
aliases = [ "/questions/3646" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Extracting country specific data.](/questions/3646/extracting-country-specific-data)

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
<span id="post-3646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3646-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-3646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Is there any way to extract nodes from only a certain country.</p>
<p>I've used XAPI to do this but that uses a bounding box [bbox]. This is OK but suppose I only want nodes from the UK and not the Republic of Ireland. In this case the square bbox will inevitably rope in Republic of Ireland nodes when I only want UK nodes beacuse in order to get the whole of the UK the box will also cover Ireland.</p>
<p>I see that there is a download location where I can download country specific datasets: <a href="http://download.geofabrik.de/osm/europe/"></a><a href="http://download.geofabrik.de/osm/europe/"></a><a href="http://download.geofabrik.de/osm/europe/">http://download.geofabrik.de/osm/europe/</a></p>
<p>But I'm assuming that they have just collected the data using a bbox as well.</p>
<p>Thanks C</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span> <span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Mar '11, 09:57</strong></p>
<img src="https://secure.gravatar.com/avatar/1666f93738e1ffd71792709a8d206764?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="columboid&#39;s gravatar image" />
<p><span>columboid</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="columboid has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-3646" class="comments-container">
<span id="3647"></span>
<div id="comment-3647" class="comment">
<div id="post-3647-score" class="comment-score">
-2
</div>
<div class="comment-text">
<p>Always try before assuming :)</p>
</div>
<div id="comment-3647-info" class="comment-info">
<span class="comment-age">(09 Mar '11, 10:51)</span> <span class="comment-user userinfo">Breki</span>
</div>
</div>
</div>
<div id="comment-tools-3646" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3646-form-container" class="comment-form-container">
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

<span id="3649"></span>

<div id="answer-container-3649" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3649-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-3649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="columboid has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Geofabrik extracts do not use a simple rectangular bounding box. Instead they use a polygon, which follows the country borders fairly closely. So if for example you download the England extract, it will just contain England, and none of the surrounding bits of Scotland/Wales/Ireland etc.</p>
<p>Though you say you just want the UK, which it seems Geofabrik do not provide an extract for. They just have extracts for "Great Britain", "Ireland" and "British Isles". So to get all of the UK, you could download the British Isles extract, then use Osmosis to extract just the UK part using a polygon filter.</p>
<p>Or Cloudmade provide <a href="http://downloads.cloudmade.com/europe/united_kingdom">UK extracts</a>, though I'm not sure how closely they follow the Northern Ireland border.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '11, 15:15</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-3649" class="comments-container">
<span id="3650"></span>
<div id="comment-3650" class="comment">
<div id="post-3650-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Vclaw and gnurk, that is most useful. That's plenty for me to read up on and it sounds like the answer is in there. Thanks for your help.</p>
</div>
<div id="comment-3650-info" class="comment-info">
<span class="comment-age">(09 Mar '11, 15:31)</span> <span class="comment-user userinfo">columboid</span>
</div>
</div>
</div>
<div id="comment-tools-3649" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3649-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3648"></span>

<div id="answer-container-3648" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3648-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-3648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Smaller non-rectangular areas, like cities, can be extracted using the methods described in <a href="http://78.46.81.38/#chapter.use_cases">OSM Server Side Script</a>.</p>
<p>In order to extract big areas, like a whole country, you may download a <a href="https://wiki.openstreetmap.org/wiki/Planet">planet</a> file, or a part of a planet file, and then use Osmosis <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format">Polygon Filter File Format</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '11, 11:11</strong></p>
<img src="https://secure.gravatar.com/avatar/c2a980da3fdfa1ee2659ad70d1e21f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnurk&#39;s gravatar image" />
<p><span>gnurk</span><br />
<span class="score" title="6114 reputation points"><span>6.1k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="silver">●</span><span class="badgecount">60</span></span><span title="96 badges"><span class="bronze">●</span><span class="badgecount">96</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnurk has 18 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-3648" class="comments-container">
&#10;</div>
<div id="comment-tools-3648" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3648-form-container" class="comment-form-container">
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

