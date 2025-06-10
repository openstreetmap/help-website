+++
type = "question"
title = "umap popup does not show data from overpass-api"
description = '''Hi all, I have managed to create a map with umap based on data from the overpass-api showing the location of post boxes and atms. But for some reasons I&#x27;m not able to show data in the popups (name for atms or collection times for post boxes). The mouse over just shows me a crossed red circle. The da...'''
date = "2014-11-27T13:45:00Z"
lastmod = "2016-12-19T13:16:00Z"
weight = 38874
keywords = [ "umap", "popup", "overpass-api" ]
aliases = [ "/questions/38874" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [umap popup does not show data from overpass-api](/questions/38874/umap-popup-does-not-show-data-from-overpass-api)

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
<span id="post-38874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38874-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I have managed to create a map with umap based on data from the overpass-api showing the location of post boxes and atms. But for some reasons I'm not able to show data in the popups (name for atms or collection times for post boxes). The mouse over just shows me a crossed red circle. The data seems to be there as if I select to always show names the names of the atm show. But I'm not able to show any other data. Can anyone point me to my shortcoming?</p>
<p>Here is the map: <a href="http://umap.osm.ch/de/map/ein-paar-interessante-infos_82#18/47.37760/8.54019">http://umap.osm.ch/de/map/ein-paar-interessante-infos_82#18/47.37760/8.54019</a> It should be editable by anyone.</p>
<p>Help is highly appreciated!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-popup" rel="tag" title="see questions tagged &#39;popup&#39;">popup</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Nov '14, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/87c6ca48b84387b7902afdd8d711f3f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Mages&#39;s gravatar image" />
<p><span>Pascal Mages</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Mages has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38874" class="comments-container">
&#10;</div>
<div id="comment-tools-38874" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38874-form-container" class="comment-form-container">
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

<span id="38877"></span>

<div id="answer-container-38877" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38877-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-38877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Pascal Mages has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to change the popup template, to use the "table" one, which will loop over all properties and display them in table.</p>
<p>Here is a screencast that shows how to do that: <a href="http://i.imgur.com/Wo1pqnk.gif">http://i.imgur.com/Wo1pqnk.gif</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Nov '14, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/2b1724b5d0f3b2d1473819e36212fd61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ybon&#39;s gravatar image" />
<p><span>ybon</span><br />
<span class="score" title="626 reputation points">626</span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ybon has 6 accepted answers">42%</span></p>
</div>
</div>
<div id="comments-container-38877" class="comments-container">
<span id="38878"></span>
<div id="comment-38878" class="comment">
<div id="post-38878-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for your answer! That helped! I didn't realise that I had to cancel had close the edit mode in order for the popups to work. No I get the popups but they just show what ever data is on the node. Is there a way I can format what is shown? That's what I would actually expect from the Popup content template to do. But it doesn't. Any idea?</p>
</div>
<div id="comment-38878-info" class="comment-info">
<span class="comment-age">(27 Nov '14, 14:51)</span> <span class="comment-user userinfo">Pascal Mages</span>
</div>
</div>
<span id="38879"></span>
<div id="comment-38879" class="comment">
<div id="post-38879-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OK, I just got! It's all about closing the edit mode. Then the popup does what I wan't it to do!</p>
</div>
<div id="comment-38879-info" class="comment-info">
<span class="comment-age">(27 Nov '14, 14:59)</span> <span class="comment-user userinfo">Pascal Mages</span>
</div>
</div>
<span id="53608"></span>
<div id="comment-53608" class="comment">
<div id="post-53608-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The gif from <a href="http://help.openstreetmap.org/users/4961/ybon"></a><a href="http://help.openstreetmap.org/users/4961/ybon">@ybon</a> may be a bit hard to follow or go offline somewhen. Here are the steps to do it:</p>
<ul>
<li>Option A: Change the settings of one specifig layer.</li>
<li>Option B: Change the default settings for all layers.</li>
</ul>
<h1 id="detailed-steps-option-a">Detailed steps option A:</h1>
<p>Click "Manage layers" on the right -&gt; Choose your layer -&gt; Click its pencil symbol -&gt; Interaction options -&gt; Popup style: define -&gt; Table</p>
<p>(German: Auf der rechten Seite "Ebenen verwalten" klicken -&gt; Die richtige Ebene wählen -&gt; Das zugehörige Bleistiftsymbol klicken -&gt; Interaktionsoptionen -&gt; Popupstil: festlegen -&gt; Tabelle)</p>
<h1 id="detailed-steps-for-option-b">Detailed steps for option B:</h1>
<p>Click "Edit map settings" on the right (gearwheel symbol) -&gt; Default interaction options -&gt; Popup style: define -&gt; Table</p>
<p>(German: Auf der rechten Seite "Karteneinstellungen bearbeiten" klicken (Zahnradsymbol) -&gt; Standard-Interaktionsoptionen -&gt; Popupstil: festlegen -&gt; Tabelle</p>
</div>
<div id="comment-53608-info" class="comment-info">
<span class="comment-age">(19 Dec '16, 13:16)</span> <span class="comment-user userinfo">skorbut</span>
</div>
</div>
</div>
<div id="comment-tools-38877" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38877-form-container" class="comment-form-container">
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

