+++
type = "question"
title = "[closed] What is the best way to render tiles and to bind them to my osm server?"
description = '''I have mapnik installed and successfully started to render the whole planet. But this is not what i want. I want to render only a country and then use those tiles with my private server. So my main questions are the following.   1. What to use to render tiles?   - * How to use it? Perhaps a link to ...'''
date = "2011-10-25T14:05:00Z"
lastmod = "2011-10-25T21:38:00Z"
weight = 8641
keywords = [ "rendering", "tiles" ]
aliases = [ "/questions/8641" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] What is the best way to render tiles and to bind them to my osm server?](/questions/8641/what-is-the-best-way-to-render-tiles-and-to-bind-them-to-my-osm-server)

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
<span id="post-8641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8641-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-8641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have mapnik installed and successfully started to render the whole planet. But this is not what i want. I want to render only a country and then use those tiles with my private server.</p>
<p>So my main questions are the following.<br />
1. What to use to render tiles?<br />
- * How to use it? Perhaps a link to a tutorial.<br />
- * how to get the coordinates of my country?<br />
2. How to make the binding between tiles and server?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '11, 14:05</strong></p>
<img src="https://secure.gravatar.com/avatar/dc9b01669c0702f230fa57c384b947a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexz&#39;s gravatar image" />
<p><span>alexz</span><br />
<span class="score" title="225 reputation points">225</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexz has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>25 Oct '11, 14:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></br></p>
</div>
</div>
<div id="comments-container-8641" class="comments-container">
&#10;</div>
<div id="comment-tools-8641" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8641-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question -- see https://help.openstreetmap.org/questions/136/how-do-i-render-my-own-maps-for-my-website" by Jonathan Bennett 25 Oct '11, 14:54

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8644"></span>

<div id="answer-container-8644" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8644-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="alexz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To render tiles for a particular area, you can use the <strong><a href="http://generate_tiles.py">generate_tiles.py</a></strong> script. This should be in your Mapnik directory. You have to edit section at the end of the script to specify the bounding boxes and zoom levels that you want. Then just run the script, and it will generate the tiles for those areas.</p>
<p>For getting the coordinates for your country, an easy way is to go to <a href="http://openstreetmap.org">openstreetmap.org</a>, and click on the tab for "Export". Choose the option for <em>Manually select a different area</em>, then draw a box for the area you want. That will give you the coordinates of the bounding box.</p>
<p>There is a useful tutorial here: <a href="http://weait.com/content/map-tiles-and-bounding-boxes">Map tiles and bounding boxes</a></p>
<p>For your second question, I'm not sure what you mean by "binding" the tiles. What sort of server? if just a webserver, you can just upload all of your tiles into the appropriate directory. If you mean viewing your tiles as a slippy map, you can do that by using OpenLayers. See this previous question and answer: <a href="/questions/8371/how-to-serve-tiles-from-my-own-server">How to serve tiles from my own server?</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '11, 15:00</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span> </br></p>
</div>
</div>
<div id="comments-container-8644" class="comments-container">
<span id="8650"></span>
<div id="comment-8650" class="comment">
<div id="post-8650-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you! That is what i was looking for! And yes, i want to serve my own tiles. Thanks thanks thanks!</p>
</div>
<div id="comment-8650-info" class="comment-info">
<span class="comment-age">(25 Oct '11, 21:38)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
</div>
<div id="comment-tools-8644" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8644-form-container" class="comment-form-container">
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

