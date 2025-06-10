+++
type = "question"
title = "How to search golf features linked with golf course"
description = '''Hello everyone, just want to ask how to find a golf course that also with golf features linked (e.g golf holes, tee, green)? I used the following script to find the golf course in a list format in Overpass turbo: [out:csv(::id,::type,&quot;name&quot;)];  area[name=&quot;London&quot;]-&amp;gt;.a;  ( node(area.a)[leisure=gol...'''
date = "2018-08-14T04:48:00Z"
lastmod = "2018-08-14T16:49:00Z"
weight = 65315
keywords = [ "golf" ]
aliases = [ "/questions/65315" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to search golf features linked with golf course](/questions/65315/how-to-search-golf-features-linked-with-golf-course)

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
<span id="post-65315-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65315-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65315-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone, just want to ask how to find a golf course that also with golf features linked (e.g golf holes, tee, green)?</p>
<p>I used the following script to find the golf course in a list format in Overpass turbo:</p>
<p><strong>[out:csv(::id,::type,"name")]; area[name="London"]-&gt;.a; ( node(area.a)[leisure=golf_course]; way(area.a)[leisure=golf_course]; rel(area.a)[leisure=golf_course]; ); out;</strong></p>
<p>I can find out the list of golf course , but once i add golf=hole, i cannot find the golf hole , is it related to the unfinished mapping of the golf course or i am using the wrong script to query for a golf course details?</p>
<p>Thanks everyone!</p>
<p>8/14/2018 11:44PM edit</p>
<p>the script i use to query the golf course with golf features is as follow:</p>
<p><strong>[out:csv(::id,::type,"name")]; area[name="London"]-&gt;.a; ( node(area.a)[leisure=golf_course]; way(area.a)[leisure=golf_course]; rel(area.a)[leisure=golf_course]; node(area.a)[golf=hole]; way(area.a)[golf=hole]; rel(area.a)[golf=hole]; ); out;</strong></p>
<p>and i receive the follow result(just part of it): <strong>436469360 way 485708432 way South Norwood Pitch and Putt 498692711 way Hole 1 498955422 way Hole 2 498955430 way Hole 3 498960293 way Hole 4 498960312 way Hole 5 499153239 way Hole 6 499153253 way Hole 7 499153272 way Hole 8 499153283 way Hole 9 499157766 way Hole 10 499157773 way Hole 11 499996506 way Hole 13 499996508 way Hole 17 499996512 way Hole 12 499996513 way Hole 15 499996516 way Hole 18 499996519 way Hole 16 501679797 way 508221481 way 9 Hole Par 3 Golf Course 511273594 way Alexandra Palace Pitch &amp; Putt</strong></p>
<p>what i want to ask is whether i can use this script to query the golf course mapped with golf features already? thanks a lot !  </p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-golf" rel="tag" title="see questions tagged &#39;golf&#39;">golf</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '18, 04:48</strong></p>
<img src="https://secure.gravatar.com/avatar/e39d564e8c50f9fc137cb4273ee4659a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JohnLee65&#39;s gravatar image" />
<p><span>JohnLee65</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JohnLee65 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Aug '18, 16:48</strong> </span></p>
</div>
</div>
<div id="comments-container-65315" class="comments-container">
<span id="65341"></span>
<div id="comment-65341" class="comment">
<div id="post-65341-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are five golf courses with golf=hole in London, so you should get some results. Can you edit your question to add the query you're trying to use for getting the holes? There may just be a problem with the syntax.</p>
</div>
<div id="comment-65341-info" class="comment-info">
<span class="comment-age">(14 Aug '18, 16:40)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="65342"></span>
<div id="comment-65342" class="comment">
<div id="post-65342-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello Alester, i have edited the question, thanks for the suggest!</p>
</div>
<div id="comment-65342-info" class="comment-info">
<span class="comment-age">(14 Aug '18, 16:49)</span> <span class="comment-user userinfo">JohnLee65</span>
</div>
</div>
</div>
<div id="comment-tools-65315" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65315-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

