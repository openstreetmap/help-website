+++
type = "question"
title = "Offline multi-modal routing on mobile"
description = '''I currently have a tileserver set up (so just a postgres database made with osm2pgsql), and I want to add support for routing. Is there any way that I can use a routing service that I can also use offline on mobile? Like the mobile device (iOS or Android) would cache some map data when it had a netw...'''
date = "2014-09-10T22:33:00Z"
lastmod = "2014-09-12T22:20:00Z"
weight = 36739
keywords = [ "mobile", "osrm", "routing", "gosmore" ]
aliases = [ "/questions/36739" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Offline multi-modal routing on mobile](/questions/36739/offline-multi-modal-routing-on-mobile)

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
<span id="post-36739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36739-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I currently have a tileserver set up (so just a postgres database made with osm2pgsql), and I want to add support for routing. Is there any way that I can use a routing service that I can also use offline on mobile? Like the mobile device (iOS or Android) would cache some map data when it had a network connection, and then later use the cached data to do routing locally. Is it actually possible to somehow compile OSRM, gosmore, OTP, etc. to work on those devices?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mobile" rel="tag" title="see questions tagged &#39;mobile&#39;">mobile</span> <span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-gosmore" rel="tag" title="see questions tagged &#39;gosmore&#39;">gosmore</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Sep '14, 22:33</strong></p>
<img src="https://secure.gravatar.com/avatar/11d268f0117b18e269e629611da12c39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rutgers_oss&#39;s gravatar image" />
<p><span>rutgers_oss</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rutgers_oss has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36739" class="comments-container">
&#10;</div>
<div id="comment-tools-36739" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36739-form-container" class="comment-form-container">
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

<span id="36744"></span>

<div id="answer-container-36744" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36744-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-36744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://graphhopper.com/">https://graphhopper.com/</a> is what comes to mind if you want to run the same engine both mobile and hosted. However the functionality that you are looking for (daynamically downloading data for routing) is unlikely to be found anywhere, nor do I believe that the use case exists in the form you are thinking of (the mobile device would have to predict when it is going to loose connectivity so that it could download data in advance).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '14, 06:53</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Sep '14, 06:56</strong> </span></p>
</div>
</div>
<div id="comments-container-36744" class="comments-container">
<span id="36803"></span>
<div id="comment-36803" class="comment">
<div id="post-36803-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I actually only have to download information once, since I'm working with a very small subset of the world (small enough that it's reasonable to download it all in one go).</p>
<p>That project looks cool, is there any way to get to work on iOS? If not, is there a way I could another multimodal router for iOS?</p>
</div>
<div id="comment-36803-info" class="comment-info">
<span class="comment-age">(12 Sep '14, 22:20)</span> <span class="comment-user userinfo">rutgers_oss</span>
</div>
</div>
</div>
<div id="comment-tools-36744" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36744-form-container" class="comment-form-container">
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

