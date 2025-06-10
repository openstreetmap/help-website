+++
type = "question"
title = "Do I create a separate entry (node) for a table under a shelter ?"
description = '''I have a freestanding shelter / gazebo tagged with: Amenity=Shelter Shelter_type=Picnic_shelter Bin=yes Power_supply=yes Table=yes The table is “in / under” the shelter, but the bin is “several meters away”. Not sure if I should  1: create separate nodes for the bin and table... and delete the tags ...'''
date = "2020-02-09T02:53:00Z"
lastmod = "2020-02-09T10:07:00Z"
weight = 72953
keywords = [ "amenity", "shelter_type" ]
aliases = [ "/questions/72953" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Do I create a separate entry (node) for a table under a shelter ?](/questions/72953/do-i-create-a-separate-entry-node-for-a-table-under-a-shelter)

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
<span id="post-72953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72953-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a freestanding shelter / gazebo tagged with:</p>
<p>Amenity=Shelter Shelter_type=Picnic_shelter Bin=yes Power_supply=yes Table=yes</p>
<p>The table is “in / under” the shelter, but the bin is “several meters away”.</p>
<p>Not sure if I should</p>
<p>1: create separate nodes for the bin and table... and delete the tags in the amenity...</p>
<p>OR</p>
<p>2: leave the bin and table as tags in the amenity only...</p>
<p>OR</p>
<p>3: add separate noes AND keep the tags in the shelter amenity...</p>
<p>Hope this makes sense...</p>
<p>Regards, - jd</p>
<p>I.e.</p>
<p>node = 753437011</p>
<p>Node = 7196475591</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-shelter_type" rel="tag" title="see questions tagged &#39;shelter_type&#39;">shelter_type</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '20, 02:53</strong></p>
<img src="https://secure.gravatar.com/avatar/973762f1b6cbc718adfd21f9b107df0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AussieJD&#39;s gravatar image" />
<p><span>AussieJD</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AussieJD has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72953" class="comments-container">
<span id="72959"></span>
<div id="comment-72959" class="comment">
<div id="post-72959-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As mentioned, you should remove generic names, or at least move them to <code>description=</code>. You can tag the electricity supply with <code>voltage=240</code>. <code>picnic_table=yes</code> is also a more common tag than <code>table=yes</code>.</p>
</div>
<div id="comment-72959-info" class="comment-info">
<span class="comment-age">(09 Feb '20, 10:07)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-72953" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72953-form-container" class="comment-form-container">
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

<span id="72956"></span>

<div id="answer-container-72956" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72956-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, I see you've already made some amendments.</p>
<p>I presume it's this area :- <a href="https://tinyurl.com/rjx7jmg">https://tinyurl.com/rjx7jmg</a></p>
<p>If there is only one table then there should be only one table mapped. IMHO from the size of the shelter I'd tag both table and shelter, I would say remove the table=yes (and bin=yes) tags from the shelter polygon leaving the table as a separate node.</p>
<p>I'd also question whether the fountain, shelter and table are formally named? If not then those name tags ought be removed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '20, 08:23</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-72956" class="comments-container">
<span id="72958"></span>
<div id="comment-72958" class="comment">
<div id="post-72958-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><code>*=yes</code> tags mean it has <code>*=</code> with it. It does not represent an instance of <code>*=</code>. Don't remove it.</p>
</div>
<div id="comment-72958-info" class="comment-info">
<span class="comment-age">(09 Feb '20, 09:53)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-72956" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72956-form-container" class="comment-form-container">
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

