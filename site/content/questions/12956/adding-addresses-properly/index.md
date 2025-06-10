+++
type = "question"
title = "Adding Addresses Properly"
description = '''I&#x27;m new to OSM, but thought I would get started by contributing some small fixes to areas around where I live. I added some address components to the Mormon temples near my house to make searching for their locations easier. It seemed to work fine for the Jordan River Utah Temple (the address that i...'''
date = "2012-05-25T18:40:00Z"
lastmod = "2012-05-30T12:04:00Z"
weight = 12956
keywords = [ "address" ]
aliases = [ "/questions/12956" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Adding Addresses Properly](/questions/12956/adding-addresses-properly)

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
<span id="post-12956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12956-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to OSM, but thought I would get started by contributing some small fixes to areas around where I live. I added some address components to the Mormon temples near my house to make searching for their locations easier. It seemed to work fine for the Jordan River Utah Temple (the address that is returned by searching for it on OSM.org is the correct address), but searching for the Oquirrh Mountain Utah Temple returns an incorrect address. The address that is returned incorrectly indicates that the temple is off a street called Country Crossing Court, although the building number is correct.</p>
<p>I added the address components in the exact same way for both place (I think). Did I do something wrong here? What do I need to do to correct this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '12, 18:40</strong></p>
<img src="https://secure.gravatar.com/avatar/301d6ff1c2c557b2b90386286b29248a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sterlinggp&#39;s gravatar image" />
<p><span>sterlinggp</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sterlinggp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12956" class="comments-container">
&#10;</div>
<div id="comment-tools-12956" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12956-form-container" class="comment-form-container">
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

<span id="12967"></span>

<div id="answer-container-12967" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12967-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-12967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sterlinggp has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim has its own database, which is updated regularly from the OSM main DB. It may lag by a few days, so this is probably the reason.</p>
<p>The address information of Oquirrh Mountain Utah Temple looks correct (it says "11022 South 4000 West, South Jordan, Utah, 84095-5797, United States of America").</p>
<p>Looking at the history of Oquirrh Mountain Utah Temple, you can see that the address was only added on Fri, 25 May 2012. At <a href="http://nominatim.openstreetmap.org/">http://nominatim.openstreetmap.org/</a> you can see how current the Nominatim data is. As of this writing, it says "Data: 2012/05/25", so it may not yet have processed all changes from 25 May, which would explain the wrong result.</p>
<p>Check back in a few days, the problem should be resolved.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '12, 09:35</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-12967" class="comments-container">
<span id="13114"></span>
<div id="comment-13114" class="comment">
<div id="post-13114-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Update (May 29): Nominatim still reports the address incorrectly. This starts to look like a real bug in Nominatim. I'll try to keep an eye on it.</p>
</div>
<div id="comment-13114-info" class="comment-info">
<span class="comment-age">(30 May '12, 08:43)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
</div>
<div id="comment-tools-12967" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12967-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13102"></span>

<div id="answer-container-13102" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13102-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim works by linking addresses to their related street. In the case of 'Oquirrh Mountain Utah Temple' it is linked to a street of '4000 West' but there is no street with that name anywhere close to this temple.</p>
<p>If the street name is added to the appropriate unnamed road nearby the problem should resolve itself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '12, 23:57</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-13102" class="comments-container">
<span id="13110"></span>
<div id="comment-13110" class="comment">
<div id="post-13110-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As far as I can tell, the street '4000 West' is named properly (and is just a dozen or so meters away from the building itself). A Nominatim search for '4000 West' yields a point on the street many miles north of the temple. I'm not sure if this is the reason, but '4000 West' starts up in the north, vanishes for a little while, then reappears before it passes by the temple. I'm not sure what to do to correct this, though.</p>
</div>
<div id="comment-13110-info" class="comment-info">
<span class="comment-age">(30 May '12, 02:03)</span> <span class="comment-user userinfo">sterlinggp</span>
</div>
</div>
<span id="13120"></span>
<div id="comment-13120" class="comment">
<div id="post-13120-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You are right - I didn't look far enough up the road to see the label. I suspect you have found an issue with nominatim and very long roads. I'll investigate properly and see if I can find the cause.</p>
</div>
<div id="comment-13120-info" class="comment-info">
<span class="comment-age">(30 May '12, 12:04)</span> <span class="comment-user userinfo">twain</span>
</div>
</div>
</div>
<div id="comment-tools-13102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13102-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12957"></span>

<div id="answer-container-12957" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12957-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are using the Nominatim Search Engine, don't worry to much if results seems to be a bit wrong -&gt; maybe your OSM data is correct though.</p>
<p>Have a look at <a href="http://help.openstreetmap.org">http://help.openstreetmap.org</a> and do a search there for "nominatim" ... there are already several issues about Nominatim results.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '12, 19:21</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-12957" class="comments-container">
&#10;</div>
<div id="comment-tools-12957" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12957-form-container" class="comment-form-container">
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

