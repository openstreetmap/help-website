+++
type = "question"
title = "Addresses for every nth house"
description = '''According to the wiki (https://wiki.openstreetmap.org/wiki/Key:addr:interpolation) you should be able to add a addr:interpolation tag to a line and make the value equal to a number. My understanding is that this number should then be used to increment the house values along that line based on the add...'''
date = "2014-09-01T00:17:00Z"
lastmod = "2014-09-01T23:49:00Z"
weight = 36466
keywords = [ "address", "interpolation" ]
aliases = [ "/questions/36466" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Addresses for every nth house](/questions/36466/addresses-for-every-nth-house)

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
<span id="post-36466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36466-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-36466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>According to the wiki (<a href="https://wiki.openstreetmap.org/wiki/Key:addr:interpolation">https://wiki.openstreetmap.org/wiki/Key:addr:interpolation</a>) you should be able to add a addr:interpolation tag to a line and make the value equal to a number. My understanding is that this number should then be used to increment the house values along that line based on the addr:housenumber values of the start and end nodes of the line. For example <a href="https://www.openstreetmap.org/way/301092844">this line</a> has a start point of 1047 and an end point of 1143. With the line set to have addr:interpolation = 4 I would expect to be able to find addresses 1051, 1055, 1059, 1063...1143, when searching for addresses. Edit-- I also would expect numbers like 1053, 1057, 1061, etc to not be found when searching for addresses.</p>
<p>Any ideas of why this isn't working? There seems to be some question of adding this type of feature back in 2009, but I can't seem to find any follow up as to if it was added or not. Am I miss reading the wiki or is it incorrect?</p>
<p>Edit: I found additional information at <a href="https://wiki.openstreetmap.org/wiki/Addresses#Using_interpolation">this wiki page</a> but it seems to confirm my understanding of how addr:interpolation=4 should work, but I'm still not seeing the skipped number results I expect.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span> <span class="post-tag tag-link-interpolation" rel="tag" title="see questions tagged &#39;interpolation&#39;">interpolation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Sep '14, 00:17</strong></p>
<img src="https://secure.gravatar.com/avatar/98d63deba6c6e14e73bfd65754098d09?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dbelcham&#39;s gravatar image" />
<p><span>dbelcham</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dbelcham has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Sep '14, 00:52</strong> </span></p>
</div>
</div>
<div id="comments-container-36466" class="comments-container">
&#10;</div>
<div id="comment-tools-36466" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36466-form-container" class="comment-form-container">
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

<span id="36487"></span>

<div id="answer-container-36487" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36487-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-36487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dbelcham has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The wiki and your mapping is ok. Nominatim (the search engine) simply only ever implemented the interpolation schema with <code>addr:interpolation=odd/even/all</code>. Interpolations with any other value are ignored. The interpolation with a numerical step value wouldn't be too hard to add. It simply does not seem to be <a href="http://taginfo.openstreetmap.org/keys/addr%3Ainterpolation#values">very popular</a>, so nobody has asked for the feature yet. <a href="https://trac.openstreetmap.org/">trac</a> is the right site to do that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '14, 23:32</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-36487" class="comments-container">
<span id="36488"></span>
<div id="comment-36488" class="comment">
<div id="post-36488-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the clarification. I'm wondering now if I will request it. I found out our county has an open data feed that has geo-location for all houses and their numbers. Am considering setting up an import to use that instead.</p>
</div>
<div id="comment-36488-info" class="comment-info">
<span class="comment-age">(01 Sep '14, 23:49)</span> <span class="comment-user userinfo">dbelcham</span>
</div>
</div>
</div>
<div id="comment-tools-36487" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36487-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36472"></span>

<div id="answer-container-36472" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36472-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-36472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>IMHO it actually works, wit:</p>
<p><a href="http://nominatim.openstreetmap.org/details.php?place_id=9206137285">http://nominatim.openstreetmap.org/details.php?place_id=9206137285</a></p>
<p><a href="http://nominatim.openstreetmap.org/details.php?place_id=9206137329">http://nominatim.openstreetmap.org/details.php?place_id=9206137329</a></p>
<p>In general if you are testing / debugging searches with Nominatim (you don't state what you are using BTW) it is best to use the interface here <a href="http://nominatim.openstreetmap.org/">http://nominatim.openstreetmap.org/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '14, 10:07</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-36472" class="comments-container">
<span id="36478"></span>
<div id="comment-36478" class="comment">
<div id="post-36478-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looks like there was a change in there that I hadn't intended and it was making almost every odd number address (i.e. 1141) searchable. I've deleted the nodes and way and re-created them and it looks like I'm seeing the behaviour I reported again. 1047 and 1143 are search able but no address between them is when the way has addr:interpolation=4.</p>
<p>I did my editing in iD and had been using the main page for debugging the search. I used Nominatim this time and am seeing the same missing results in both.</p>
</div>
<div id="comment-36478-info" class="comment-info">
<span class="comment-age">(01 Sep '14, 17:11)</span> <span class="comment-user userinfo">dbelcham</span>
</div>
</div>
</div>
<div id="comment-tools-36472" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36472-form-container" class="comment-form-container">
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

