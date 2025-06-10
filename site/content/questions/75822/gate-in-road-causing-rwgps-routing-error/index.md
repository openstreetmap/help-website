+++
type = "question"
title = "Gate in road causing RWGPS routing error"
description = '''Hi, I&#x27;m a long time user of OSM, but this is my first time thinking about making edits. I do a lot of cycling around Devon, UK, and regularly use ridewithgps.com to plot routes, which I believe uses OSM data for routing. A few times now I&#x27;ve come across roads that it wouldn&#x27;t route me along, for no ...'''
date = "2020-07-21T10:29:00Z"
lastmod = "2020-07-21T16:24:00Z"
weight = 75822
keywords = [ "gate", "routing" ]
aliases = [ "/questions/75822" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Gate in road causing RWGPS routing error](/questions/75822/gate-in-road-causing-rwgps-routing-error)

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
<span id="post-75822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75822-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm a long time user of OSM, but this is my first time thinking about making edits. I do a lot of cycling around Devon, UK, and regularly use ridewithgps.com to plot routes, which I believe uses OSM data for routing. A few times now I've come across roads that it wouldn't route me along, for no obvious reason, and this time I decided to try and work out why.</p>
<p>The point in question is here: <a href="https://www.openstreetmap.org/node/6880810227.">https://www.openstreetmap.org/node/6880810227.</a> It looks like a gate has been placed in the middle of the road rather than, as I suspect it should be, at the edge of the road. I realise Google Streetview shouldn't be used as a data source, but looking on there does seem to confirm that the gate is at the side of the road. My question is: is this an error in the mapping and the gate should be moved; is it an error in how the gate is tagged; is the gate mapped and tagged correctly and it's the fault of the routing engine? My guess would be that it's the first option, as it just looks wrong with the gate in the middle of the road. I've tried the OSM directions tool (<a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_bike&amp;route=50.82136%2C-3.90860%3B50.81950%2C-3.90739)">https://www.openstreetmap.org/directions?engine=fossgis_osrm_bike&amp;route=50.82136%2C-3.90860%3B50.81950%2C-3.90739)</a> and it will happily route through that point with OSRM and sometimes with GraphHopper (although that's a bit hit and miss). I'd appreciate any thoughts on what the problem is here.</p>
<p>Obviously I can't do anything if it's the fault of RWGPS, but if it's a mapping or tagging error, can someone give me brief instructions on how to correct it? Is it as simple as clicking edit on OSM and dragging the gate to the side of the road or editing the tags on it? Is there any approval mechanism for any changes that I make?</p>
<p>Thanks for any help and advice you're able to offer :o)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gate" rel="tag" title="see questions tagged &#39;gate&#39;">gate</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '20, 10:29</strong></p>
<img src="https://secure.gravatar.com/avatar/29e3be44ee5712f4b560fde758013f16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kamoshika&#39;s gravatar image" />
<p><span>kamoshika</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kamoshika has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75822" class="comments-container">
&#10;</div>
<div id="comment-tools-75822" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75822-form-container" class="comment-form-container">
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

<span id="75823"></span>

<div id="answer-container-75823" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75823-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-75823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kamoshika has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes this is clearly an error, the gate should clearly be on the track and not on the road. While the UK doesn't really have any good aerial imagery (in some places it seems to have dramatically improved over the last weeks), you can see the situation fairly clearly with "Esri World Imagery (Clarity) Beta" (in iD use the layer button on the right hand side of the screen).</p>
<p>Thanks for doing the detective work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '20, 11:17</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jul '20, 16:53</strong> </span></p>
</div>
</div>
<div id="comments-container-75823" class="comments-container">
<span id="75827"></span>
<div id="comment-75827" class="comment">
<div id="post-75827-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the reply. I had a look at editing it, and it looks like the gate is a node (I hope I'm getting the terminology right) and that node is where the track joins the road, so something like this:</p>
<pre><code>=====G=====  
     |  
     |</code></pre>
<p>Where = is road, | is track and G is the gate. If I try and move the gate it just drags the adjacent sections of road and track around with the gate. I think what I need to do is to repalce the gate with a node that just joins sections of road / track, and re-add the gate as a node on the track. So, more like this:</p>
<pre><code>=====O=====
     |
     G
     |</code></pre>
<p>Am I understanding that correctly, and if so, how would I do that in the editor?</p>
<p>Thanks!</p>
</div>
<div id="comment-75827-info" class="comment-info">
<span class="comment-age">(21 Jul '20, 12:42)</span> <span class="comment-user userinfo">kamoshika</span>
</div>
</div>
<span id="75830"></span>
<div id="comment-75830" class="comment">
<div id="post-75830-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Right click on the gate -&gt; Extract.</p>
<p>Temporarily place the node somewhere convenient.</p>
<p>Drag the node onto the appropriate way. The way should highlight while you're dragging the node to indicate that the node will become part of it when you release.</p>
</div>
<div id="comment-75830-info" class="comment-info">
<span class="comment-age">(21 Jul '20, 13:13)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="75834"></span>
<div id="comment-75834" class="comment">
<div id="post-75834-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's great - many thanks for your help. First ever OSM edit done :o)</p>
</div>
<div id="comment-75834-info" class="comment-info">
<span class="comment-age">(21 Jul '20, 16:24)</span> <span class="comment-user userinfo">kamoshika</span>
</div>
</div>
</div>
<div id="comment-tools-75823" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75823-form-container" class="comment-form-container">
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

