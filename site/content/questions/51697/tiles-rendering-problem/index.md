+++
type = "question"
title = "Tiles rendering problem"
description = '''Like it was said in one of my question on stackexchange, I&#x27;m trying to configure my own tile server in CentOS 6 following this tutorial. I had some issues that have been solved, everything is working perfectly in my previous configured VM : I can render my tiles in a distant computer in QGIS, it&#x27;s v...'''
date = "2016-08-24T11:01:00Z"
lastmod = "2018-04-28T14:08:00Z"
weight = 51697
keywords = [ "qgis", "rendering", "time", "centos", "tileserver" ]
aliases = [ "/questions/51697" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tiles rendering problem](/questions/51697/tiles-rendering-problem)

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
<span id="post-51697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51697-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Like it was said in <a href="http://gis.stackexchange.com/questions/207824/open-postgis-datas-in-qgis">one of my question on stackexchange</a>, I'm trying to configure my own tile server in CentOS 6 following <a href="http://translate.googleusercontent.com/translate_c?depth=1&amp;hl=en&amp;rurl=translate.google.com&amp;sl=auto&amp;tl=en&amp;u=http://gis-lab.info/qa/mod_tile.html&amp;usg=ALkJrhis6odWAMEf7Pqotr85KI5V7G8f6w#.D0.A3.D1.81.D1.82.D0.B0.D0.BD.D0.BE.D0.B2.D0.BA.D0.B0_mod_tile.2C_renderd.2C_Mapnik.2C_osm2pgsql"><em>this</em></a> tutorial.</p>
<p>I had some issues that have been solved, everything is working perfectly in my previous configured VM : I can render my tiles in a distant computer in QGIS, it's very fast and no bugged.</p>
<p>I was thinking that it was going to be the same during the configuration on a "real" server, but I have some new problems...</p>
<p>In fact, <a href="http://myserveradress/osm_tiles/0/0/0.png">http://myserveradress/osm_tiles/0/0/0.png</a> is working. I can also get an access to my server from QGIS using QuickMapService like in my VM :</p>
<p><a href="http://help.openstreetmap.org/upfiles/before-zoom.PNG"><img src="http://help.openstreetmap.org/upfiles/before-zoom.PNG" alt="before zoom" /></a> <em>Coasts lines are present before a zoom</em></p>
<p><strong>BUT</strong> beyond a certain zoom level in a country (when it's supposed to render some streets/places/etc) I get this :</p>
<p><a href="http://i.stack.imgur.com/WF8AA.png"><img src="http://i.stack.imgur.com/WF8AA.png" alt="some errors" /></a> <a href="http://i.stack.imgur.com/vZrq9.png"><img src="http://i.stack.imgur.com/vZrq9.png" alt="some errors" /></a></p>
<p>And the screen is white...</p>
<p>Also, a strange fact from France rendering (country that I had tried to get into my database to finally stop the process) :</p>
<p><a href="http://help.openstreetmap.org/upfiles/francewut_NxKErNB.PNG"><img src="http://help.openstreetmap.org/upfiles/francewut_NxKErNB.PNG" alt="france" /></a> <em>Africa (that is uploaded in my DB) is supposed to be rendered...not France</em></p>
<p>I was wondering if it was coming from the server performances so I used the command</p>
<blockquote>
<p>render_list --all --socket=/var/run/renderd/renderd.sock -z 0 -Z 10</p>
</blockquote>
<p>in order to pre-render some tiles and decrease the rendering time but I also get an error like :</p>
<p><a href="http://i.stack.imgur.com/fDKQ4.png"><img src="http://i.stack.imgur.com/fDKQ4.png" alt="server terminal capture" /></a></p>
<p>I searched on the net in order to find some clues but most people do not find answers to this problem.</p>
<p>I uploaded all Africa continent during the last night and I swear I reused the same process as in my VM configuration...</p>
<p>Does someone have an idea ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span> <span class="post-tag tag-link-centos" rel="tag" title="see questions tagged &#39;centos&#39;">centos</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Aug '16, 11:01</strong></p>
<img src="https://secure.gravatar.com/avatar/e24bbbdda053f5691599e8a47c4e32c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="L%C3%A9o%20W&#39;s gravatar image" />
<p><span>Léo W</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Léo W has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Aug '16, 11:03</strong> </span></p>
</div>
</div>
<div id="comments-container-51697" class="comments-container">
&#10;</div>
<div id="comment-tools-51697" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51697-form-container" class="comment-form-container">
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

<span id="63200"></span>

<div id="answer-container-63200" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63200-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looks like you still have france either in your database or in your tile cache. For rendering issues, have you tried to run renderd with - f to look for errors?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '18, 09:43</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</img>
</div>
</div>
<div id="comments-container-63200" class="comments-container">
<span id="63203"></span>
<div id="comment-63203" class="comment">
<div id="post-63203-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry made a mistake and commented on this post from '16. Thus bringing it to the top. Please ignore.</p>
</div>
<div id="comment-63203-info" class="comment-info">
<span class="comment-age">(28 Apr '18, 14:08)</span> <span class="comment-user userinfo">gfitz</span>
</div>
</div>
</div>
<div id="comment-tools-63200" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63200-form-container" class="comment-form-container">
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

