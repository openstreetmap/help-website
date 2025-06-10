+++
type = "question"
title = "Adding Residential"
description = '''Hey Gang! I&#x27;m cleaning up addressing for E911 purposes, and have run into a couple of Residential sites that have no associated buildings reflected for the House? I can add a Point, but the only options are for Parks, Hospitals, etc.-is there a way that I can add the House with the accepted address?...'''
date = "2019-12-11T20:45:00Z"
lastmod = "2019-12-11T21:41:00Z"
weight = 72075
keywords = [ "adding", "residential" ]
aliases = [ "/questions/72075" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Adding Residential](/questions/72075/adding-residential)

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
<span id="post-72075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72075-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey Gang! I'm cleaning up addressing for E911 purposes, and have run into a couple of Residential sites that have no associated buildings reflected for the House? I can add a Point, but the only options are for Parks, Hospitals, etc.-is there a way that I can add the House with the accepted address? The sites that I'm working on have all been registered with both the County and E911 Dispatch.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-adding" rel="tag" title="see questions tagged &#39;adding&#39;">adding</span> <span class="post-tag tag-link-residential" rel="tag" title="see questions tagged &#39;residential&#39;">residential</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Dec '19, 20:45</strong></p>
<img src="https://secure.gravatar.com/avatar/8e265e4d159a2e5c4fa8e599d3198445?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bradley&#39;s gravatar image" />
<p><span>Bradley</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bradley has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72075" class="comments-container">
&#10;</div>
<div id="comment-tools-72075" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72075-form-container" class="comment-form-container">
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

<span id="72076"></span>

<div id="answer-container-72076" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72076-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-72076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Bradley -- It sounds like you're trying to add a residential building to the map using the browser-based map editor called "iD", which is the default editor that loads if you log into openstreetmap.org and press the "Edit" button.</p>
<p>If you want to add the building as a point (also known as a "node"):</p>
<ul>
<li>Click on the "Point" option at the top of the map (where it says Point/Line/Area)</li>
<li>Position the map and click where you want to add the node</li>
<li>In the sidebar on the left, instead of choosing any of the specific options, just click on "Point" (the first item in the list).</li>
<li>The sidebar will change to show the tags of the new node (but it currently doesn't have any tags so it shows an error!)</li>
<li>At the bottom of the left sidebar, under "All Tags", you'll see two empty boxes followed by a trash can icon and a lowercase i. Click in the left blank box and type "building", then hit tab.</li>
<li>The sidebar will change a little bit and boxes for the address info will appear, but don't go there yet. First you should finish the building tag you're adding under "All Tags". Tags in OSM have two parts: the key, in this case "building", and the value. In the second blank box to the right of "building", type the value for the building key that describes the kind of building you're adding. Some common building types are "residential", "detached", "apartments", "house". You can always just use "yes" for the building type if you don't know.</li>
<li>Now go back and fill in the address boxes that appeared above. (The state probably isn't required, because the state lines are already on the map.)</li>
</ul>
<p>You can repeat to add more addresses. When you're done, click the "Save" button (at the top right of the map, should show a number of changes you've made), type a description of your work under "Changeset Comment", and click the "Upload" button. It's also good practice to indicate where you're getting the information that you're adding -- you can use the changeset comment for that, or you can add a "Sources" field to your changeset and describe your sources there.</p>
<p>...Now, just FYI, most people these days prefer to actually draw the buildings on the map, rather than just using a node (point). It may not make a difference for E911 purposes, but if you want to do it that way, choose "Area" instead of "Point" and then click to draw the building shape. On the left you'll see a list called "Building features" that you can choose from, rather than manually typing in the building type.</p>
<p>Thanks for your work and good luck!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Dec '19, 21:41</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Dec '19, 04:55</strong> </span></p>
</div>
</div>
<div id="comments-container-72076" class="comments-container">
&#10;</div>
<div id="comment-tools-72076" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72076-form-container" class="comment-form-container">
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

