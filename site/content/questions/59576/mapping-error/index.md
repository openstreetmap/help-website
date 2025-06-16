+++
type = "question"
title = "Mapping Error"
description = '''I currently lease and run a business/coffee shop (GiorgiPorgi) at 137 E. 3rd Street, Los Angeles, CA 90013. We are located on E. 3rd Street (northside of the street) between Main Street and Los Angeles Street. The map shows it between Los Angeles Street and Wall Street on the southside of E. 3rd Str...'''
date = "2017-09-12T21:15:00Z"
lastmod = "2017-09-13T09:00:00Z"
weight = 59576
keywords = [ "error" ]
aliases = [ "/questions/59576" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping Error](/questions/59576/mapping-error)

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
<span id="post-59576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59576-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I currently lease and run a business/coffee shop (GiorgiPorgi) at 137 E. 3rd Street, Los Angeles, CA 90013.</p>
<p>We are located on E. 3rd Street (northside of the street) between Main Street and Los Angeles Street.</p>
<p>The map shows it between Los Angeles Street and Wall Street on the southside of E. 3rd Street.</p>
<p>Other mapping services that use openstreetmap are sending customers into skidrow away from our coffee shop =(</p>
<p>I am not too tech savvy but am hoping someone here is kind of enough to help us and lost coffee tourists haha.</p>
<p>Much appreciated and to whomever can help free coffee for life at GiorgiPorgi...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Sep '17, 21:15</strong></p>
<img src="https://secure.gravatar.com/avatar/5363485b6b65add2f953b5f3203f8bd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GiorgiPorgi&#39;s gravatar image" />
<p><span>GiorgiPorgi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GiorgiPorgi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Sep '17, 21:16</strong> </span></p>
</div>
</div>
<div id="comments-container-59576" class="comments-container">
&#10;</div>
<div id="comment-tools-59576" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59576-form-container" class="comment-form-container">
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

<span id="59581"></span>

<div id="answer-container-59581" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59581-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-59581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Moving a node (POI) is really very easy with the in browser map editor, however there is a more fundamental issue with your question in that I don't seem to be able to actually locate your establishment where you say it currently, mistakenly, is.</p>
<p>OK, after checking your website, it seems as if the problem is actually not what I expected: that the node/point for your establishment is in the wrong place. I was assuming that your guests were looking it up by name. That can't be the case because there is clearly no such node in our database. Likely your guests are actually looking up the address. The problem is that in your area OSM data proper doesn't actually have any addresses that in turn implies that the apps are falling back on other data to roughly locate where the address is, which in your case is a "bit" off.</p>
<p>What should be done:</p>
<ul>
<li>add a POI for the cafe (good for you :-)) (done, thanks maxerickson)</li>
<li>add proper addresses for the buildings along the street (added from mapillary)</li>
</ul>
<p>It is 1am here now so I'm going to be doing something else for the next couple of hours :-). but we can work on this further tomorrow.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Sep '17, 21:27</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Sep '17, 08:57</strong> </span></p>
</div>
</div>
<div id="comments-container-59581" class="comments-container">
<span id="59583"></span>
<div id="comment-59583" class="comment">
<div id="post-59583-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried to move/create a POI, not sure if it worked.</p>
<p>If you go to the map on the bottom of our website www.giorgiporgi.com you can see the incorrect location still.</p>
<p>Not sure what happened eh... =/</p>
</div>
<div id="comment-59583-info" class="comment-info">
<span class="comment-age">(12 Sep '17, 23:56)</span> <span class="comment-user userinfo">GiorgiPorgi</span>
</div>
</div>
<span id="59584"></span>
<div id="comment-59584" class="comment">
<div id="post-59584-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You created a note, which is a way to give map feedback. I've created a POI: <a href="https://www.openstreetmap.org/node/5102160315">https://www.openstreetmap.org/node/5102160315</a></p>
<p>If you want to change it or move it or whatever, click the "Edit" button while looking at it. There is a short walk thru of the editor the first time you use it. Make sure to save after you have made any changes.</p>
</div>
<div id="comment-59584-info" class="comment-info">
<span class="comment-age">(13 Sep '17, 00:37)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="59589"></span>
<div id="comment-59589" class="comment">
<div id="post-59589-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It might take some time for MapBox to update their map with fresh OSM data.</p>
</div>
<div id="comment-59589-info" class="comment-info">
<span class="comment-age">(13 Sep '17, 07:56)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="59592"></span>
<div id="comment-59592" class="comment">
<div id="post-59592-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Et voilà: <a href="https://www.openstreetmap.org/search?query=GiorgiPorgi#map=19/34.04875/-118.24488">https://www.openstreetmap.org/search?query=GiorgiPorgi#map=19/34.04875/-118.24488</a></p>
<p>If you have time, adding any information on any missing or updated shops, restaurants in your vicinity is appreciated. Feel free just to add a note or edit directly.</p>
<p>The maillary imagery in the area seems to be from a Sunday as a result it is difficult to determine what actually exists and what not. See <a href="https://www.mapillary.com/map/im/XQMsKFCJ4Pj4Za_PSKPssQ">https://www.mapillary.com/map/im/XQMsKFCJ4Pj4Za_PSKPssQ</a></p>
</div>
<div id="comment-59592-info" class="comment-info">
<span class="comment-age">(13 Sep '17, 09:00)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-59581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59581-form-container" class="comment-form-container">
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

