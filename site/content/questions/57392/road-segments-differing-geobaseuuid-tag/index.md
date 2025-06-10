+++
type = "question"
title = "Road segments differing geobase:uuid tag"
description = '''In a town near where I live I&#x27;ve found that streets are individual lines that are not connected (eg 7 lines named 49th street that intersect) all with the exact same data except a differing geobase:uuid tag. Because of this I can&#x27;t merge the lines together into one line (some of their tags have conf...'''
date = "2017-08-01T07:18:00Z"
lastmod = "2017-08-01T15:54:00Z"
weight = 57392
keywords = [ "conflicts", "road", "tags" ]
aliases = [ "/questions/57392" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Road segments differing geobase:uuid tag](/questions/57392/road-segments-differing-geobaseuuid-tag)

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
<span id="post-57392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57392-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In a town near where I live I've found that streets are individual lines that are not connected (eg 7 lines named 49th street that intersect) all with the exact same data except a differing geobase:uuid tag. Because of this I can't merge the lines together into one line (some of their tags have conflicting values message). What is the best way to go about merging the lines into one line? Should I delete that tag or just leave them as is?</p>
<p>I'm using the iD editor.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-conflicts" rel="tag" title="see questions tagged &#39;conflicts&#39;">conflicts</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Aug '17, 07:18</strong></p>
<img src="https://secure.gravatar.com/avatar/8dea67e387a0c53d596d4d6a5d10cbec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JayKoh&#39;s gravatar image" />
<p><span>JayKoh</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JayKoh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Aug '17, 07:19</strong> </span></p>
</div>
</div>
<div id="comments-container-57392" class="comments-container">
&#10;</div>
<div id="comment-tools-57392" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57392-form-container" class="comment-form-container">
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

<span id="57402"></span>

<div id="answer-container-57402" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57402-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JayKoh has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is typically a good idea to provide a link to the area or objects under discussion.</p>
<p>In any case you can join the segments at their end nodes, which will enable routing a long the street. If there are no other differences on the segments you can delete the geobase tag (which is likely the indication of a import that should be investigated).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '17, 09:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-57402" class="comments-container">
<span id="57411"></span>
<div id="comment-57411" class="comment">
<div id="post-57411-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah the roads are joined together but it was making it a pain to add more information or update them as they had to be done individually. It appears to be part of this import <a href="http://wiki.openstreetmap.org/wiki/GeoBase_Import">http://wiki.openstreetmap.org/wiki/GeoBase_Import</a></p>
</div>
<div id="comment-57411-info" class="comment-info">
<span class="comment-age">(01 Aug '17, 15:54)</span> <span class="comment-user userinfo">JayKoh</span>
</div>
</div>
</div>
<div id="comment-tools-57402" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57402-form-container" class="comment-form-container">
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

