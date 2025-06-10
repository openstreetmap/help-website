+++
type = "question"
title = "Trouble querying Overpass for footways in national parks"
description = '''I&#x27;m trying to query Overpass for trails and paths within nature reserves. My query seems to work fine in some nature reserves but not others. I have been querying in Maryland, USA. Specifically, I have noticed that it does not work in either of these national parks: Catoctin Mountain Park or Chesape...'''
date = "2023-04-24T00:36:00Z"
lastmod = "2023-04-24T15:11:00Z"
weight = 87159
keywords = [ "national_park", "overpass", "footway" ]
aliases = [ "/questions/87159" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Trouble querying Overpass for footways in national parks](/questions/87159/trouble-querying-overpass-for-footways-in-national-parks)

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
<span id="post-87159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87159-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to query Overpass for trails and paths within nature reserves. My query seems to work fine in some nature reserves but not others. I have been querying in Maryland, USA. Specifically, I have noticed that it does not work in either of these national parks: Catoctin Mountain Park or Chesapeake and Ohio Canal National Historical Park. Can anyone tell me what I am doing wrong? Here's my query:</p>
<p><a href="https://overpass-turbo.eu/s/1u8o">https://overpass-turbo.eu/s/1u8o</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-national_park" rel="tag" title="see questions tagged &#39;national_park&#39;">national_park</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-footway" rel="tag" title="see questions tagged &#39;footway&#39;">footway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '23, 00:36</strong></p>
<img src="https://secure.gravatar.com/avatar/b73071e1d4ffb0ca4883fb48dcb6b8e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sillyboy22&#39;s gravatar image" />
<p><span>sillyboy22</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sillyboy22 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87159" class="comments-container">
&#10;</div>
<div id="comment-tools-87159" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87159-form-container" class="comment-form-container">
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

<span id="87160"></span>

<div id="answer-container-87160" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87160-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87160-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87160-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sillyboy22 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>nature_reserve as ways are automatically converted to 'areas' in Overpass' database. Unsure if it's intentional, but relations aren't. Add map_to_area; to force a conversion</p>
<p><a href="https://overpass-turbo.eu/s/1ua9">https://overpass-turbo.eu/s/1ua9</a></p>
<pre><code>wr[leisure=nature_reserve]({{bbox}});
map_to_area;
wr[highway~&quot;^(footway|path|track)$&quot;](area);
out geom;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '23, 15:04</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '23, 15:25</strong> </span></p>
</div>
</div>
<div id="comments-container-87160" class="comments-container">
<span id="87161"></span>
<div id="comment-87161" class="comment">
<div id="post-87161-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Very helpful. Thanks!</p>
</div>
<div id="comment-87161-info" class="comment-info">
<span class="comment-age">(24 Apr '23, 15:11)</span> <span class="comment-user userinfo">sillyboy22</span>
</div>
</div>
</div>
<div id="comment-tools-87160" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87160-form-container" class="comment-form-container">
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

