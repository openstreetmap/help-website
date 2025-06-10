+++
type = "question"
title = "Taginfo planet import memory requirements"
description = '''Hello, After playing around with importing a country extract into taginfo, I wanted to test out a full planet import. After testing a few times, it seems like this would require a large ammount of ram. I tested this with a machine that has 64gb ram and it fails on the processing nodes step.  I&#x27;m cur...'''
date = "2016-08-22T18:57:00Z"
lastmod = "2016-08-23T13:11:00Z"
weight = 51651
keywords = [ "import", "taginfo", "memory" ]
aliases = [ "/questions/51651" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Taginfo planet import memory requirements](/questions/51651/taginfo-planet-import-memory-requirements)

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
<span id="post-51651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51651-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>After playing around with importing a country extract into taginfo, I wanted to test out a full planet import. After testing a few times, it seems like this would require a large ammount of ram. I tested this with a machine that has 64gb ram and it fails on the processing nodes step.</p>
<p>I'm curious if anyone knows how much ram is required when importing a full planet into taginfo?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-taginfo" rel="tag" title="see questions tagged &#39;taginfo&#39;">taginfo</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '16, 18:57</strong></p>
<img src="https://secure.gravatar.com/avatar/943c484e8c04680902357de8f080dcc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cellington&#39;s gravatar image" />
<p><span>Cellington</span><br />
<span class="score" title="216 reputation points">216</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cellington has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51651" class="comments-container">
&#10;</div>
<div id="comment-tools-51651" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51651-form-container" class="comment-form-container">
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

<span id="51673"></span>

<div id="answer-container-51673" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51673-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Taginfo works fine with 16 GB RAM on a planet file. Have a look in the config file right near the end and change the "geodistribution" setting according to the comments there. I also suggest you subscribe to the <a href="https://lists.openstreetmap.org/listinfo/taginfo-dev">taginfo mailing list</a>, that's where all the people running taginfo instances hang out and can help you best.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Aug '16, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-51673" class="comments-container">
<span id="51674"></span>
<div id="comment-51674" class="comment">
<div id="post-51674-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I modified the tagstats geodistribution value to DenseMmapArry and it worked fine on a 32gb machine.</p>
</div>
<div id="comment-51674-info" class="comment-info">
<span class="comment-age">(23 Aug '16, 13:11)</span> <span class="comment-user userinfo">Cellington</span>
</div>
</div>
</div>
<div id="comment-tools-51673" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51673-form-container" class="comment-form-container">
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

