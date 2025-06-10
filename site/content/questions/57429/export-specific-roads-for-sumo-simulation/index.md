+++
type = "question"
title = "Export specific roads for Sumo simulation"
description = '''Hello there, I am currently working on simulating DSRC vehicular communication on roads in my area. I am using Omnet/Sumo/Veins to perform the simulation. I am really happy with how easy it is to export road data from OSM and plug it into the simulation.  Now, I am having trouble setting up the simu...'''
date = "2017-08-02T23:16:00Z"
lastmod = "2017-08-07T17:31:00Z"
weight = 57429
keywords = [ "sumo", "veins", "omnet", "overpass" ]
aliases = [ "/questions/57429" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Export specific roads for Sumo simulation](/questions/57429/export-specific-roads-for-sumo-simulation)

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
<span id="post-57429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57429-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello there,</p>
<p>I am currently working on simulating DSRC vehicular communication on roads in my area. I am using Omnet/Sumo/Veins to perform the simulation. I am really happy with how easy it is to export road data from OSM and plug it into the simulation.</p>
<p>Now, I am having trouble setting up the simulation to narrow in on the roads we have specifically tested. I would like to export only the roads we have data for to run in Omnet. It seems like the Overpass API is a good way to go, but I may be off base here. Any other suggestions would be very helpful!</p>
<p>If Overpass is the way to go, I have two questions:</p>
<ol>
<li>How do I find the way(id) of the road I want. I found I can select specific roads with way(id), but I don't know how to find the road I specifically want. Once I export this data it will be plugged into the sim, so I am not concerned about this road ID changing after I export.</li>
<li>Does Overpass export to .osm files? This seems to be the only way to convert a map file to what I need for Sumo.</li>
</ol>
<p>I am very new with OSM, so any direction would be very helpful. Thank you so much!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sumo" rel="tag" title="see questions tagged &#39;sumo&#39;">sumo</span> <span class="post-tag tag-link-veins" rel="tag" title="see questions tagged &#39;veins&#39;">veins</span> <span class="post-tag tag-link-omnet" rel="tag" title="see questions tagged &#39;omnet&#39;">omnet</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '17, 23:16</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4fd7b854153d31a4fa8b9b90ce8a50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="le_sanglier&#39;s gravatar image" />
<p><span>le_sanglier</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="le_sanglier has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57429" class="comments-container">
&#10;</div>
<div id="comment-tools-57429" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57429-form-container" class="comment-form-container">
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

<span id="57430"></span>

<div id="answer-container-57430" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57430-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-57430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Output_Format_.28out:.29">xml</a> option on Overpass-API is what you would expect in a .osm file.</p>
<p>If you have locations associated with your testing you could use the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Relative_to_other_elements_.28around.29">around filter</a> with a suitable distance to find the highways of interest.</p>
<p>Otherwise you will probably have to resort to a manual process. One way to do it would be to download just the highways in the area of interest using Overpass-API and then pare that data down in JOSM (being careful not to upload damaging deletions). File-&gt;Save in JOSM will output the same osm xml.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '17, 00:06</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Aug '17, 02:24</strong> </span></p>
</div>
</div>
<div id="comments-container-57430" class="comments-container">
<span id="57493"></span>
<div id="comment-57493" class="comment">
<div id="post-57493-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks so much! To be honest, that is what I was afraid of, haha. I was trying that earlier, but the output was rather sloppy. I will just have to get better at it. Thanks again for the response!</p>
</div>
<div id="comment-57493-info" class="comment-info">
<span class="comment-age">(07 Aug '17, 17:31)</span> <span class="comment-user userinfo">le_sanglier</span>
</div>
</div>
</div>
<div id="comment-tools-57430" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57430-form-container" class="comment-form-container">
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

