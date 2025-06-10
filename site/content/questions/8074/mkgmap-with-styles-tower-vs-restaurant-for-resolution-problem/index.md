+++
type = "question"
title = "Mkgmap with styles Tower vs restaurant for resolution problem"
description = '''Hello, Something that I don&#x27;t understand about styles in mkgmap : resolution For my style, I use levels : 0:24,1:22,2:20,3:18,4:16 I don&#x27;t use any TYP file In my points I have : man_made=tower [0x6411 resolution 16]  and  amenity=restaurant [0x2a00 resolution 16] When I zoom with a scale of 500m, I ...'''
date = "2011-09-21T22:56:00Z"
lastmod = "2011-09-22T16:17:00Z"
weight = 8074
keywords = [ "mkgmap", "style", "resolution" ]
aliases = [ "/questions/8074" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Mkgmap with styles Tower vs restaurant for resolution problem](/questions/8074/mkgmap-with-styles-tower-vs-restaurant-for-resolution-problem)

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
<span id="post-8074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8074-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>Something that I don't understand about styles in mkgmap : resolution</p>
<p>For my style, I use levels : 0:24,1:22,2:20,3:18,4:16 I don't use any TYP file</p>
<p>In my points I have :</p>
<p>man_made=tower [0x6411 resolution 16] and amenity=restaurant [0x2a00 resolution 16]</p>
<p>When I zoom with a scale of 500m, I just see towers and I need to zoom to 120m scale to see restaurants. If I change the icon of restaurants (0x..), the icon change in GPS. So, I'm pretty sure that the line is interpreted.</p>
<p>I try extrem values of resolution (10 and 24), but same thing !</p>
<p>If I put man_made=tower|amenity=restaurant [0x6411 resolution 16] it works, but with a tower icon for the restaurant !</p>
<p>Do I miss something ?</p>
<p>Thanks u all</p>
<p>Tested on garmin 60csx</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mkgmap" rel="tag" title="see questions tagged &#39;mkgmap&#39;">mkgmap</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-resolution" rel="tag" title="see questions tagged &#39;resolution&#39;">resolution</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Sep '11, 22:56</strong></p>
<img src="https://secure.gravatar.com/avatar/3e6d868fd890902785b2fc4cd31d49f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iero&#39;s gravatar image" />
<p><span>iero</span><br />
<span class="score" title="20 reputation points">20</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iero has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Sep '11, 14:07</strong> </span></p>
</div>
</div>
<div id="comments-container-8074" class="comments-container">
&#10;</div>
<div id="comment-tools-8074" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8074-form-container" class="comment-form-container">
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

<span id="8080"></span>

<div id="answer-container-8080" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8080-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="iero has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, you haven't missed anything. The resolution setting doesn't quite work as described - for info see <a href="http://www.mkgmap.org.uk/pipermail/mkgmap-dev/2011q3/011977.html">this</a> mkgmap list post.</p>
<p>In fact, <a href="http://www.google.co.uk/search?q=resolution+http%3A%2F%2Fwww.mkgmap.org.uk%2Fpipermail%2Fmkgmap-dev%2F&amp;ie=utf-8&amp;oe=utf-8&amp;aq=t&amp;rls=org.mozilla:en-GB:official&amp;client=firefox-a">searching that list</a> will often yield answers to this sort of question. Don't be put off that it's called <a href="http://www.mkgmap.org.uk/mailman/listinfo/mkgmap-dev">mkgmap-dev</a>, there's plenty of useful info for non-developers too. The rest of that thread's worth a read because I think that you said elsewhere you had a 60csx?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '11, 16:04</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-8080" class="comments-container">
<span id="8081"></span>
<div id="comment-8081" class="comment">
<div id="post-8081-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for this answer, it was a crasy thing, I spent hours on that !</p>
<p>So, I'll look for "under-used codes" with a custom TYP file to re-define importants points that need to show up at lower zoom.</p>
<p>I will look on the ml you pointed, it seems very interesting.</p>
<p>Thanks again</p>
</div>
<div id="comment-8081-info" class="comment-info">
<span class="comment-age">(22 Sep '11, 16:17)</span> <span class="comment-user userinfo">iero</span>
</div>
</div>
</div>
<div id="comment-tools-8080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8080-form-container" class="comment-form-container">
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

