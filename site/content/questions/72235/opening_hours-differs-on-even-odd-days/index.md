+++
type = "question"
title = "opening_hours differs on even / odd days?"
description = '''It is very common in some countries that some amenities changes workhours on alternating days (so one day the work in the morning, the next in the evening).  So for example on even days (like 2.Jan or 18.Jun etc.) they will work only in the morning (for example 08:00-13:00), while on odd days (like ...'''
date = "2019-12-27T18:08:00Z"
lastmod = "2019-12-30T22:13:00Z"
weight = 72235
keywords = [ "opening_hours", "odd-even" ]
aliases = [ "/questions/72235" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [opening_hours differs on even / odd days?](/questions/72235/opening_hours-differs-on-even-odd-days)

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
<span id="post-72235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72235-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-72235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>It is very common in some countries that some amenities changes workhours on alternating days (so one day the work in the morning, the next in the evening).</p>
<p>So for example on even days (like 2.Jan or 18.Jun etc.) they will work only in the morning (for example 08:00-13:00), while on odd days (like 7.Mar or 31.Oct etc.) the will work only in the evening (for example 14:00-19:00).</p>
<p>While it is simple schedule in practice, looking at the <a href="https://wiki.openstreetmap.org/wiki/Key:opening_hours">https://wiki.openstreetmap.org/wiki/Key:opening_hours</a> I cannot seem to figure out how to map it. Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-opening_hours" rel="tag" title="see questions tagged &#39;opening_hours&#39;">opening_hours</span> <span class="post-tag tag-link-odd-even" rel="tag" title="see questions tagged &#39;odd-even&#39;">odd-even</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Dec '19, 18:08</strong></p>
<img src="https://secure.gravatar.com/avatar/666391973130e371bf8092f70c43df28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matija%20Nalis&#39;s gravatar image" />
<p><span>Matija Nalis</span><br />
<span class="score" title="750 reputation points">750</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matija Nalis has 2 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-72235" class="comments-container">
<span id="72237"></span>
<div id="comment-72237" class="comment">
<div id="post-72237-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I presume you are looking for a solution other than by brute force listing all the odd days there could be in a month?</p>
</div>
<div id="comment-72237-info" class="comment-info">
<span class="comment-age">(27 Dec '19, 20:20)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="72240"></span>
<div id="comment-72240" class="comment">
<div id="post-72240-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a> yes, that is correct assumption - listing half of days in a year one by one would be terrible (even if it actually worked, which I'm sceptical about due to extreme length of the field in such a case)... I was hoping for something like <code>week 2-53/2 10:00-20:00</code> but for even days instead of even weeks</p>
</div>
<div id="comment-72240-info" class="comment-info">
<span class="comment-age">(27 Dec '19, 22:12)</span> <span class="comment-user userinfo">Matija Nalis</span>
</div>
</div>
<span id="72253"></span>
<div id="comment-72253" class="comment">
<div id="post-72253-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>No expert on this , but you should be able to do something like 02-30/2 08:00-13:00; 01-31/2 14:00-19:00. I have no idea what happens to evaluation if you then introduce month or week ranges as well or, for that matter, days of the week. However, this does not seem to properly specified so there is probably no implementation (see <a href="https://github.com/opening-hours/opening_hours.js/issues/252)">https://github.com/opening-hours/opening_hours.js/issues/252)</a></p>
</div>
<div id="comment-72253-info" class="comment-info">
<span class="comment-age">(28 Dec '19, 10:15)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="72290"></span>
<div id="comment-72290" class="comment">
<div id="post-72290-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a> thanks for the reference! Unfortunately, as you say at this time it does not seem to be implemented in <a href="https://openingh.openstreetmap.de/evaluation_tool/">https://openingh.openstreetmap.de/evaluation_tool/</a> nor elsewhere I looked :(</p>
</div>
<div id="comment-72290-info" class="comment-info">
<span class="comment-age">(30 Dec '19, 22:13)</span> <span class="comment-user userinfo">Matija Nalis</span>
</div>
</div>
</div>
<div id="comment-tools-72235" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72235-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

