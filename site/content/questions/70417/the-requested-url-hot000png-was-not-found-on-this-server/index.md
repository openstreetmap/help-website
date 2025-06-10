+++
type = "question"
title = "The requested URL /hot/0/0/0.png was not found on this server"
description = '''Just installed OSM on Ubuntu 18.04 using the rather excellent guide published by the switch2osm folks. Everything works up to and including the initial manual test of renderd. When I try to go to the web page at http://yourserveripaddress/hot/0/0/0.png (yes, used the server&#x27;s IP address) I get the f...'''
date = "2019-08-19T02:45:00Z"
lastmod = "2019-08-20T22:07:00Z"
weight = 70417
keywords = [ "switch2osm" ]
aliases = [ "/questions/70417" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [The requested URL /hot/0/0/0.png was not found on this server](/questions/70417/the-requested-url-hot000png-was-not-found-on-this-server)

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
<span id="post-70417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70417-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Just installed OSM on Ubuntu 18.04 using the rather excellent guide published by the switch2osm folks.</p>
<p>Everything works up to and including the initial manual test of renderd.</p>
<p>When I try to go to the web page at <a href="http://yourserveripaddress/hot/0/0/0.png">http://yourserveripaddress/hot/0/0/0.png</a> (yes, used the server's IP address) I get the following error;</p>
<p>The requested URL /hot/0/0/0.png was not found on this server</p>
<p>I've reviewed all of the steps and confess I am a bit confused, not that that is particularly unusual. I tend to get grumpy when I follow a recipe and I burn the cake... so to speak.</p>
<p>Any help would be most helpful.</p>
<p>Chuck... WB6YOK</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Aug '19, 02:45</strong></p>
<img src="https://secure.gravatar.com/avatar/2948304e01d5d17fb1c1a0d26d2c6466?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chuck_Killian&#39;s gravatar image" />
<p><span>Chuck_Killian</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chuck_Killian has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70417" class="comments-container">
<span id="70418"></span>
<div id="comment-70418" class="comment">
<div id="post-70418-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As an addendum the URI /hot/ is configured in renderd.conf</p>
<p>Chuck... WB6YOK</p>
</div>
<div id="comment-70418-info" class="comment-info">
<span class="comment-age">(19 Aug '19, 02:54)</span> <span class="comment-user userinfo">Chuck_Killian</span>
</div>
</div>
<span id="70442"></span>
<div id="comment-70442" class="comment">
<div id="post-70442-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Anyone have an answer to this?</p>
</div>
<div id="comment-70442-info" class="comment-info">
<span class="comment-age">(20 Aug '19, 19:36)</span> <span class="comment-user userinfo">Chuck_Killian</span>
</div>
</div>
</div>
<div id="comment-tools-70417" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70417-form-container" class="comment-form-container">
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

<span id="70444"></span>

<div id="answer-container-70444" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70444-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70444-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70444-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello</p>
<p>Check few things: 1. ps -ef | grep renderd</p>
<p>if it is on the list, then: 2a. tail -n 10 /var/log/syslog or: 2b. grep "renderd" /var/log/syslog</p>
<p>You could also run renderd as regular application, as: renderd -f -c /usr/local/etc/renderd.conf and then check out the messages. If you see messages stating that there is no role "root" in postgres, then you have to set up: host + user name + password in the project.mml and regenerate styles.xml</p>
<p>And of course make sure that /hot/ is set in the renderd.conf as URI. If not, set it and reload apache.</p>
<p>Check also if the image got created. Sometimes it is taking a while to generate.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '19, 22:07</strong></p>
<img src="https://secure.gravatar.com/avatar/7b5775bcca69a6b6603f02a8255ef2f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="januzi&#39;s gravatar image" />
<p><span>januzi</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="januzi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Aug '19, 22:20</strong> </span></p>
</div>
</div>
<div id="comments-container-70444" class="comments-container">
&#10;</div>
<div id="comment-tools-70444" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70444-form-container" class="comment-form-container">
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

