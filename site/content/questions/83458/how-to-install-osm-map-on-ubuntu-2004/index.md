+++
type = "question"
title = "how to install osm map on ubuntu 20.04"
description = '''Hi i am new to maps i am struggling to install osm on a vps i tried a lot of tutorials its just one error after the other any good tutorial i can follow i need full world map coz the ones i am getting seem to be outdated. i am using Os ubuntu 20.04 , 60GB ram ,2TB storage'''
date = "2022-02-13T07:42:00Z"
lastmod = "2022-02-13T10:56:00Z"
weight = 83458
keywords = [ "osm", "newbie", "vps" ]
aliases = [ "/questions/83458" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to install osm map on ubuntu 20.04](/questions/83458/how-to-install-osm-map-on-ubuntu-2004)

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
<span id="post-83458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83458-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi i am new to maps i am struggling to install osm on a vps i tried a lot of tutorials its just one error after the other any good tutorial i can follow i need full world map coz the ones i am getting seem to be outdated. i am using Os ubuntu 20.04 , 60GB ram ,2TB storage</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-vps" rel="tag" title="see questions tagged &#39;vps&#39;">vps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '22, 07:42</strong></p>
<img src="https://secure.gravatar.com/avatar/c38fc20e7f4091bcacb7f428a3e974fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gramzrah&#39;s gravatar image" />
<p><span>gramzrah</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gramzrah has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83458" class="comments-container">
<span id="83459"></span>
<div id="comment-83459" class="comment">
<div id="post-83459-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It would be best if you follow one tutorial (I recommend <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/</a> ) and than ask with the specific errors you get.</p>
<p>Nonetheless I would not recommend to install a planet osm map on a vps, esp. not the one you seem to be using (you may try that for testing, but than you should got with a smaller extract, but those specs - which in case of the one you are using are better "on paper" than in real - won't get you anywhere for productive use for a full planet install).</p>
</div>
<div id="comment-83459-info" class="comment-info">
<span class="comment-age">(13 Feb '22, 10:12)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="83460"></span>
<div id="comment-83460" class="comment">
<div id="post-83460-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What would also help would be to explain what your end goal is - you say you want to "install osm on a vps", but presumably you're doing that because you want to do something with the data?</p>
<p>Maybe that something is "create a tile server that could be used instead of <a href="https://tile.openstreetmap.org/">https://tile.openstreetmap.org/</a> " in which case the "switch2osm" guide that <a href="https://help.openstreetmap.org/users/17439/spiekerooger">@Spiekerooger</a> linked to makes sense, but there are many other ways of accessing and using OSM data (for routing directions, for example).</p>
<p>It would really help to know what you are trying to achieve.</p>
</div>
<div id="comment-83460-info" class="comment-info">
<span class="comment-age">(13 Feb '22, 10:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="83461"></span>
<div id="comment-83461" class="comment">
<div id="post-83461-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i want to use Osrm and Nominatim basically running everything i dont want somebody to limit my requests i wanna use it for commercial use</p>
</div>
<div id="comment-83461-info" class="comment-info">
<span class="comment-age">(13 Feb '22, 10:52)</span> <span class="comment-user userinfo">gramzrah</span>
</div>
</div>
<span id="83462"></span>
<div id="comment-83462" class="comment">
<div id="post-83462-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>so which server should i use ???</p>
</div>
<div id="comment-83462-info" class="comment-info">
<span class="comment-age">(13 Feb '22, 10:53)</span> <span class="comment-user userinfo">gramzrah</span>
</div>
</div>
<span id="83463"></span>
<div id="comment-83463" class="comment">
<div id="post-83463-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OK, you're going to need to follow the installation guide for each of those projects, and I'd do them one at a time so as not to become confused.</p>
<p>For Nominatim, the instructions seem to be <a href="https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-20/">https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-20/</a> .</p>
</div>
<div id="comment-83463-info" class="comment-info">
<span class="comment-age">(13 Feb '22, 10:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-83458" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83458-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

