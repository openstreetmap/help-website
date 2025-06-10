+++
type = "question"
title = "Croatan National Forest - NC (help needed)"
description = '''Hi, I didn&#x27;t know where to ask that, but I&#x27;m trying to improve a part of North-Carolina which I think miss a lot of stuffs and is not really accurate. https://www.openstreetmap.org/edit#map=12/34.8309/-76.8074 I wanted to edit the Croatan National Park. I don&#x27;t know who or when it was created, but f...'''
date = "2018-08-16T03:53:00Z"
lastmod = "2018-08-16T12:11:00Z"
weight = 65378
keywords = [ "editing" ]
aliases = [ "/questions/65378" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Croatan National Forest - NC (help needed)](/questions/65378/croatan-national-forest-nc-help-needed)

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
<span id="post-65378-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65378-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65378-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I didn't know where to ask that, but I'm trying to improve a part of North-Carolina which I think miss a lot of stuffs and is not really accurate. <a href="https://www.openstreetmap.org/edit#map=12/34.8309/-76.8074">https://www.openstreetmap.org/edit#map=12/34.8309/-76.8074</a></p>
<p>I wanted to edit the Croatan National Park. I don't know who or when it was created, but for some reason the forest is weirdly made. For some reasons it was created with 2 layers of lines and shapes and I don't really know how it works. All the forest is done with 2 parallels lines and inside you can see the shape "Natural Reserve" and "Forest".</p>
<p>I really think I should re-do that with only one "Natural Reserve" shape.</p>
<p>Also in the attributes, there is a lot of things currently that I don't understand. Like source : <a href="http://data.nconemap.gov/downloads/vector/marea.zip">http://data.nconemap.gov/downloads/vector/marea.zip</a></p>
<p>and Wikidata/wikipedia.</p>
<p>I tried to look at the source on <a href="http://data.nconemap.gov/geoportal/catalog/main/home.page">http://data.nconemap.gov/geoportal/catalog/main/home.page</a> by typing merea. It was last updated in April 2018, but not sure how to upload datas to OSM or which file is going to be imported.</p>
<p>So do I need to create the new forest manually?</p>
<p>I know it's a long question, but thank you very much for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '18, 03:53</strong></p>
<img src="https://secure.gravatar.com/avatar/b4d5f5185c8510713a3099af71168ccf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nic727&#39;s gravatar image" />
<p><span>Nic727</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nic727 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65378" class="comments-container">
&#10;</div>
<div id="comment-tools-65378" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65378-form-container" class="comment-form-container">
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

<span id="65385"></span>

<div id="answer-container-65385" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65385-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no need to create a new national park; in fact there are already 2 entries for Croatan National Park.</p>
<p><a href="https://www.openstreetmap.org/relation/1431008/history">Croatan National Park 1</a></p>
<p><a href="https://www.openstreetmap.org/relation/8302338">Croatan National Park 2</a></p>
<p>The second one never should have been created. I believe some of the confusion comes from the fact that there is some consensus in OSM that national parks should not be landuse=forest or leisure=park, but instead boundary=protected_area. Since the protected area only shows a green outline but not solid green, people don't realize that it is already tagged and create it again.</p>
<p>To me, the proper action would be to remove the second one and make sure the first one has the most accepted use for US national parks. I confess to not being entirely sure what that is - for a history of national park tagging / rendering, see this <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/603">Github issue</a> about boundary=protected area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '18, 12:11</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-65385" class="comments-container">
&#10;</div>
<div id="comment-tools-65385" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65385-form-container" class="comment-form-container">
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

